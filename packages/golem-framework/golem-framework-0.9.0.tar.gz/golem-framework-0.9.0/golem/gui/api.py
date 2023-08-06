"""Golem GUI API blueprint"""
import os
from copy import deepcopy
from functools import wraps

from flask import jsonify, request, current_app, abort
from flask.blueprints import Blueprint
from flask_login import current_user
from itsdangerous import BadSignature, SignatureExpired

from golem.core import (environment_manager, settings_manager, test as test_module,
                        session, utils, tags_manager, test_directory)
from golem.core.page import Page
from golem.core import page as page_module
from golem.core import suite as suite_module
from golem.core.project import Project, create_project
from golem.gui import gui_utils, report_parser
from golem.gui.user_management import Users, Permissions


api_bp = Blueprint('api', __name__, url_prefix='/api')


def auth_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:
            token = request.headers.get('token', None)
            if token:
                try:
                    user = Users.verify_auth_token(current_app.secret_key, token)
                    request.api_user = user
                except BadSignature:
                    abort(401, 'Token did not match')
                except SignatureExpired:
                    abort(401, 'Signature Expired')
                except Exception:
                    abort(401, 'Unknown error')
            else:
                abort(400, 'Missing token')
        return func(*args, **kwargs)
    return decorated_view


@api_bp.route('/auth/token', methods=['POST'])
def auth_token():
    username = request.json['username']
    password = request.json['password']
    user = Users.get_user_by_username(username=username)
    if user is None:
        abort(401, 'User does not exist')
    elif not user.verify_password(password):
        abort(401, 'Incorrect password')
    else:
        token = user.generate_auth_token(current_app.secret_key)
        return jsonify(token.decode())


@api_bp.route('/golem/actions')
@auth_required
def golem_actions():
    project = request.args.get('project', None)
    response = jsonify(gui_utils.GolemActionParser().get_actions(project))
    response.cache_control.max_age = 604800
    response.cache_control.public = True
    return response


@api_bp.route('/golem/default-browser')
@auth_required
def golem_default_browser():
    return jsonify(session.settings['default_browser'])


@api_bp.route('/golem/project-permissions')
@auth_required
def golem_permissions_project():
    return jsonify(Permissions.project_permissions)


@api_bp.route('/page/code/save', methods=['PUT'])
@auth_required
def page_code_save():
    project = request.json['project']
    page_name = request.json['pageName']
    content = request.json['content']
    _verify_permissions(Permissions.STANDARD, project)
    path = Page(project, page_name).path
    page_module.edit_page_code(project, page_name, content)
    _, error = utils.import_module(path)
    return jsonify({'error': error})


@api_bp.route('/page/delete', methods=['DELETE'])
@auth_required
def page_delete():
    project = request.json['project']
    page_name = request.json['fullPath']
    _verify_permissions(Permissions.ADMIN, project)
    errors = page_module.delete_page(project, page_name)
    return jsonify(errors)


@api_bp.route('/page/duplicate', methods=['POST'])
@auth_required
def page_duplicate():
    project = request.json['project']
    page_name = request.json['fullPath']
    new_page_name = request.json['newFileFullPath']
    _verify_permissions(Permissions.STANDARD, project)
    errors = page_module.duplicate_page(project, page_name, new_page_name)
    return jsonify(errors)


@api_bp.route('/page/components')
@auth_required
def page_components():
    project = request.args['project']
    page_name = request.args['page']
    _verify_permissions(Permissions.READ_ONLY, project)
    result = {
        'error': '',
        'contents': []
    }
    page = Page(project, page_name)
    if not page.exists:
        result['error'] = 'page does not exist'
    else:
        result['components'] = page.components
    return jsonify(result)


@api_bp.route('/page/rename', methods=['POST'])
@auth_required
def page_rename():
    project = request.json['project']
    page_name = request.json['fullFilename']
    new_page_name = request.json['newFullFilename']
    _verify_permissions(Permissions.STANDARD, project)
    errors = page_module.rename_page(project, page_name, new_page_name)
    return jsonify({'errors': errors})


@api_bp.route('/page/save', methods=['PUT'])
@auth_required
def page_save():
    project = request.json['project']
    page_name = request.json['pageName']
    elements = request.json['elements']
    functions = request.json['functions']
    import_lines = request.json['importLines']
    _verify_permissions(Permissions.STANDARD, project)
    page_module.edit_page(project, page_name, elements, functions, import_lines)
    return jsonify('page-saved')


@api_bp.route('/project', methods=['POST'])
@auth_required
def project_create():
    project_name = request.json['project']
    project_name = project_name.strip().replace(' ', '_')
    _verify_permissions(Permissions.SUPER_USER)
    errors = []
    if len(project_name) < 3:
        errors.append('Project name is too short')
    elif len(project_name) > 50:
        errors.append('Project name is too long')
    elif test_directory.project_exists(project_name):
        errors.append('A project with that name already exists')
    else:
        create_project(project_name)
    return jsonify({'errors': errors, 'project_name': project_name})


@api_bp.route('/project/environments')
@auth_required
def project_environments():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    return jsonify(environment_manager.get_envs(project))


@api_bp.route('/project/environments/save', methods=['PUT'])
@auth_required
def project_environments_save():
    project = request.json['project']
    env_data = request.json['environmentData']
    _verify_permissions(Permissions.ADMIN, project)
    error = environment_manager.save_environments(project, env_data)
    return jsonify({'error': error})


@api_bp.route('/project-exists')
@auth_required
def project_exists():
    project = request.json['project']
    return jsonify(test_directory.project_exists(project))


@api_bp.route('/project/has-tests')
@auth_required
def project_has_tests():
    project = request.args['project']
    has_tests = Project(project).has_tests
    response = jsonify(has_tests)
    if has_tests:
        response.cache_control.max_age = 604800
        response.cache_control.public = True
    return response


@api_bp.route('/project/health')
@auth_required
def project_health():
    project = request.args['project']
    _verify_permissions(Permissions.REPORTS_ONLY, project)
    project_data = report_parser.get_last_executions(projects=[project], suite=None,
                                                     limit=1)
    health_data = {}
    for suite, executions in project_data[project].items():
        execution_data = report_parser.get_execution_data(project=project,
                                                          suite=suite,
                                                          execution=executions[0])
        health_data[suite] = {
            'execution': executions[0],
            'total': execution_data['total_tests'],
            'totals_by_result': execution_data['totals_by_result']
        }
    return jsonify(health_data)


@api_bp.route('/project/page', methods=['POST'])
@auth_required
def project_page_create():
    project = request.json['project']
    page_name = request.json['fullPath']
    _verify_permissions(Permissions.STANDARD, project)
    element, errors = _create_project_element(project, page_name, 'page')
    return jsonify({'errors': errors, 'element': element})


@api_bp.route('/project/page/directory', methods=['POST'])
@auth_required
def project_page_directory_create():
    project = request.json['project']
    dir_name = request.json['fullPath']
    _verify_permissions(Permissions.STANDARD, project)
    errors = Project(project).create_directories(dir_name, 'page')
    element = {'name': dir_name.split('.')[-1], 'full_name': dir_name}
    return jsonify({'errors': errors, 'element': element})


@api_bp.route('/project/page-exists')
@auth_required
def project_page_exists():
    project = request.args['project']
    page_name = request.args['page']
    _verify_permissions(Permissions.READ_ONLY, project)
    return jsonify(Page(project, page_name).exists)


@api_bp.route('/project/page-tree')
@auth_required
def project_page_tree():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    return jsonify(Project(project).page_tree)


@api_bp.route('/project/pages')
@auth_required
def project_pages():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    pages = Project(project).pages()
    return jsonify(pages)


@api_bp.route('/project/suite', methods=['POST'])
@auth_required
def project_suite_create():
    project = request.json['project']
    suite_name = request.json['fullPath']
    _verify_permissions(Permissions.STANDARD, project)
    element, errors = _create_project_element(project, suite_name, 'suite')
    return jsonify({'errors': errors, 'element': element})


@api_bp.route('/project/suite/directory', methods=['POST'])
@auth_required
def project_suite_directory_create():
    project = request.json['project']
    dir_name = request.json['fullPath']
    _verify_permissions(Permissions.STANDARD, project)
    errors = Project(project).create_directories(dir_name, 'suite')
    element = {'name': dir_name.split('.')[-1], 'full_name': dir_name}
    return jsonify({'errors': errors, 'element': element})


@api_bp.route('/project/suite-tree')
@auth_required
def project_suite_tree():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    return jsonify(Project(project).suite_tree)


@api_bp.route('/project/supported-browsers')
@auth_required
def project_supported_browsers():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    settings = settings_manager.get_project_settings(project)
    remote_browsers = settings_manager.get_remote_browser_list(settings)
    default_browsers = gui_utils.get_supported_browsers_suggestions()
    return jsonify(remote_browsers + default_browsers)


@api_bp.route('/project/tags')
@auth_required
def project_tags():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    return jsonify(tags_manager.get_project_unique_tags(project))


@api_bp.route('/project/test', methods=['POST'])
@auth_required
def project_test_create():
    project = request.json['project']
    test_name = request.json['fullPath']
    _verify_permissions(Permissions.STANDARD, project)
    element, errors = _create_project_element(project, test_name, 'test')
    return jsonify({'errors': errors, 'element': element})


@api_bp.route('/project/test/directory', methods=['POST'])
@auth_required
def project_test_directory_create():
    project = request.json['project']
    dir_name = request.json['fullPath']
    _verify_permissions(Permissions.STANDARD, project)
    errors = Project(project).create_directories(dir_name, 'test')
    element = {'name': dir_name.split('.')[-1], 'full_name': dir_name}
    return jsonify({'errors': errors, 'element': element})


@api_bp.route('/project/test-tags')
@auth_required
def project_test_tags():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    return jsonify(tags_manager.get_all_project_tests_tags(project))


@api_bp.route('/project/test-tree')
@auth_required
def project_test_tree():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    return jsonify(Project(project).test_tree)


@api_bp.route('/projects')
@auth_required
def projects():
    return jsonify(test_directory.get_projects())


@api_bp.route('/report/suite/execution')
@auth_required
def report_suite_execution():
    project = request.args['project']
    suite = request.args['suite']
    execution = request.args['execution']
    _verify_permissions(Permissions.REPORTS_ONLY, project)
    execution_data = report_parser.get_execution_data(project=project, suite=suite,
                                                      execution=execution)
    response = jsonify(execution_data)
    if execution_data['has_finished']:
        response.cache_control.max_age = 60 * 60 * 24 * 7
        response.cache_control.public = True
    return response


@api_bp.route('/report/last-executions')
@auth_required
def report_last_executions():
    user = _get_user_api_or_session()
    project_list = user.project_list
    project_data = report_parser.get_last_executions(project_list, limit=5)
    return jsonify(projects=project_data)


@api_bp.route('/report/project/last-executions')
@auth_required
def report_project_last_executions():
    project = request.args['project']
    _verify_permissions(Permissions.REPORTS_ONLY, project)
    project_data = report_parser.get_last_executions([project], limit=10)
    return jsonify(projects=project_data)


@api_bp.route('/report/suite/last-executions')
@auth_required
def report_suite_last_executions():
    project = request.args['project']
    suite = request.args['suite']
    _verify_permissions(Permissions.REPORTS_ONLY, project)
    project_data = report_parser.get_last_executions([project], suite=suite, limit=50)
    return jsonify(projects=project_data)


@api_bp.route('/report/test-set')
@auth_required
def report_test_set():
    project = request.args['project']
    suite = request.args['suite']
    execution = request.args['execution']
    test_full_name = request.args['testName']
    test_set = request.args['testSet']
    _verify_permissions(Permissions.REPORTS_ONLY, project)
    test_detail = report_parser.get_test_case_data(project, test_full_name,
                                                   suite=suite, execution=execution,
                                                   test_set=test_set, is_single=False,
                                                   encode_screenshots=True)
    response = jsonify(test_detail)
    if test_detail['has_finished']:
        response.cache_control.max_age = 604800
        response.cache_control.public = True
    return response


@api_bp.route('/report/test/status')
@auth_required
def report_test_status():
    project = request.args['project']
    test_name = request.args['test']
    timestamp = request.args['timestamp']
    _verify_permissions(Permissions.REPORTS_ONLY, project)
    path = os.path.join(session.testdir, 'projects', project, 'reports',
                        'single_tests', test_name, timestamp)
    result = {
        'sets': {},
        'is_finished': False
    }
    sets = {}
    if os.path.isdir(path):
        for elem in os.listdir(path):
            if os.path.isdir(os.path.join(path, elem)):
                sets[elem] = {
                    'log': [],
                    'report': None
                }
    result['is_finished'] = report_parser.is_execution_finished(path, sets)
    for set_name in sets:
        report_path = os.path.join(path, set_name, 'report.json')
        if os.path.exists(report_path):
            test_data = report_parser.get_test_case_data(project, test_name,
                                                         execution=timestamp,
                                                         test_set=set_name,
                                                         is_single=True)
            sets[set_name]['report'] = test_data
        log_path = os.path.join(path, set_name, 'execution_info.log')
        if os.path.exists(log_path):
            with open(log_path) as log_file:
                sets[set_name]['log'] = log_file.readlines()
    result['sets'] = sets
    return jsonify(result)


@api_bp.route('/settings/global/save', methods=['PUT'])
@auth_required
def settings_global_save():
    settings = request.json['settings']
    _verify_permissions(Permissions.SUPER_USER)
    settings_manager.save_global_settings(settings)
    session.settings = settings_manager.get_global_settings()
    return jsonify('settings-saved')


@api_bp.route('/settings/global')
@auth_required
def settings_global_get():
    _verify_permissions(Permissions.SUPER_USER)
    return jsonify(settings_manager.get_global_settings())


@api_bp.route('/settings/project/save', methods=['PUT'])
@auth_required
def settings_project_save():
    project = request.json['project']
    settings = request.json['settings']
    _verify_permissions(Permissions.ADMIN, project)
    settings_manager.save_project_settings(project, settings)
    return jsonify('settings-saved')


@api_bp.route('/settings/project')
@auth_required
def settings_project_get():
    project = request.args['project']
    _verify_permissions(Permissions.READ_ONLY, project)
    return jsonify(settings_manager.get_project_settings_only(project))


@api_bp.route('/suite/delete', methods=['DELETE'])
@auth_required
def suite_delete():
    project = request.json['project']
    page_name = request.json['fullPath']
    _verify_permissions(Permissions.ADMIN, project)
    errors = suite_module.delete_suite(project, page_name)
    return jsonify(errors)


@api_bp.route('/suite/duplicate', methods=['POST'])
@auth_required
def suite_duplicate():
    project = request.json['project']
    page_name = request.json['fullPath']
    new_page_name = request.json['newFileFullPath']
    _verify_permissions(Permissions.STANDARD, project)
    errors = suite_module.duplicate_suite(project, page_name, new_page_name)
    return jsonify(errors)


@api_bp.route('/suite/rename', methods=['POST'])
@auth_required
def suite_rename():
    project = request.json['project']
    page_name = request.json['fullFilename']
    new_page_name = request.json['newFullFilename']
    _verify_permissions(Permissions.STANDARD, project)
    errors = suite_module.rename_suite(project, page_name, new_page_name)
    return jsonify({'errors': errors})


@api_bp.route('/suite/run', methods=['POST'])
@auth_required
def suite_run():
    project = request.json['project']
    suite_name = request.json['suite']
    _verify_permissions(Permissions.STANDARD, project)
    timestamp = gui_utils.run_suite(project, suite_name)
    return jsonify(timestamp)


@api_bp.route('/suite/save', methods=['PUT'])
@auth_required
def suite_save():
    project = request.json['project']
    suite_name = request.json['suite']
    tests = request.json['tests']
    processes = request.json['processes']
    tags = request.json['tags']
    browsers = request.json['browsers']
    environments = request.json['environments']
    _verify_permissions(Permissions.STANDARD, project)
    suite_module.edit_suite(project, suite_name, tests, processes, browsers,
                            environments, tags)
    return jsonify('suite-saved')


@api_bp.route('/test/code/save', methods=['PUT'])
@auth_required
def test_code_save():
    project = request.json['project']
    test_name = request.json['testName']
    table_test_data = request.json['testData']
    content = request.json['content']
    _verify_permissions(Permissions.STANDARD, project)
    test_module.edit_test_code(project, test_name, content, table_test_data)
    path = test_module.Test(project, test_name).path
    _, error = utils.import_module(path)
    return jsonify({'error': error})


@api_bp.route('/test/delete', methods=['DELETE'])
@auth_required
def test_delete():
    project = request.json['project']
    test_name = request.json['fullPath']
    _verify_permissions(Permissions.ADMIN, project)
    errors = test_module.delete_test(project, test_name)
    return jsonify(errors)


@api_bp.route('/test/duplicate', methods=['POST'])
@auth_required
def test_duplicate():
    project = request.json['project']
    test_name = request.json['fullPath']
    new_test_name = request.json['newFileFullPath']
    _verify_permissions(Permissions.STANDARD, project)
    errors = test_module.duplicate_test(project, test_name, new_test_name)
    return jsonify(errors)


@api_bp.route('/test/rename', methods=['POST'])
@auth_required
def test_rename():
    project = request.json['project']
    test_name = request.json['fullFilename']
    new_test_name = request.json['newFullFilename']
    _verify_permissions(Permissions.STANDARD, project)
    errors = test_module.rename_test(project, test_name, new_test_name)
    return jsonify({'errors': errors})


@api_bp.route('/test/run', methods=['POST'])
@auth_required
def test_run():
    project = request.json['project']
    test_name = request.json['testName']
    browsers = request.json['browsers']
    environments = request.json['environments']
    processes = request.json['processes']
    _verify_permissions(Permissions.STANDARD, project)
    timestamp = gui_utils.run_test(project, test_name, browsers, environments, processes)
    return jsonify(timestamp)


@api_bp.route('/test/save', methods=['PUT'])
@auth_required
def test_save():
    project = request.json['project']
    test_name = request.json['testName']
    description = request.json['description']
    pages = request.json['pages']
    test_data_content = request.json['testData']
    test_steps = request.json['steps']
    tags = request.json['tags']
    _verify_permissions(Permissions.STANDARD, project)
    test_module.edit_test(project, test_name, description, pages, test_steps,
                          test_data_content, tags)
    return jsonify('test-saved')


@api_bp.route('/users')
@auth_required
def users_get():
    _verify_permissions(Permissions.SUPER_USER)
    users = deepcopy(Users.users())
    for user in users:
        del user['password']
    return jsonify(users)


@api_bp.route('/users/user')
@auth_required
def user_get():
    _verify_permissions(Permissions.SUPER_USER)
    username = request.args['username']
    user = Users.get_user_dictionary(username)
    if user:
        del user['password']
    return jsonify(user)


@api_bp.route('/users/new', methods=['PUT'])
@auth_required
def users_new():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    is_superuser = request.json['isSuperuser']
    _verify_permissions(Permissions.SUPER_USER)
    project_permissions_raw = request.json['projectPermissions']
    project_permissions = {}
    for project_permission in project_permissions_raw:
        project_permissions[project_permission['project']] = project_permission['permission']
    errors = Users.create_user(username, password, email, is_superuser, project_permissions)
    return jsonify(errors)


@api_bp.route('/users/edit', methods=['POST'])
@auth_required
def users_edit():
    old_username = request.json['oldUsername']
    new_username = request.json['newUsername']
    email = request.json['email']
    is_superuser = request.json['isSuperuser']
    project_permissions_raw = request.json['projectPermissions']
    _verify_permissions(Permissions.SUPER_USER)
    project_permissions = {}
    if project_permissions_raw is not None:
        for p in project_permissions_raw:
            project_permissions[p['project']] = p['permission']
    errors = Users.edit_user(old_username, new_username, email, is_superuser, project_permissions)
    return jsonify(errors)


@api_bp.route('/users/delete', methods=['DELETE'])
@auth_required
def users_delete():
    _verify_permissions(Permissions.SUPER_USER)
    username = request.json['username']
    errors = Users.delete_user(username)
    return jsonify({'errors': errors})


@api_bp.route('/users/reset-password', methods=['POST'])
@auth_required
def users_reset_user_password():
    _verify_permissions(Permissions.SUPER_USER)
    username = request.json['username']
    new_password = request.json['newPassword']
    errors = Users.reset_user_password(username, new_password)
    return jsonify({'errors': errors})


@api_bp.route('/user/reset-password', methods=['POST'])
@auth_required
def user_reset_user_password():
    username = request.json['username']
    if username == current_user.username:
        new_password = request.json['newPassword']
        errors = Users.reset_user_password(username, new_password)
    else:
        errors = ['Cannot change current user password']
    return jsonify({'errors': errors})


def _create_project_element(project, element_name, element_type):
    errors = []
    if element_type == 'test':
        errors = test_module.create_test(project, element_name)
    elif element_type == 'page':
        errors = page_module.create_page(project, element_name)
    elif element_type == 'suite':
        errors = suite_module.create_suite(project, element_name)
    else:
        errors.append('Invalid element type {}'.format(element_type))
    element = {
        'name': element_name.split('.')[-1],
        'full_name': element_name
    }
    return element, errors


def _get_user_api_or_session():
    """Get current_user if user is authenticated (Flask Login)
    or request.api_user if present
    """
    user = None
    if current_user and current_user.is_authenticated:
        user = current_user
    elif request.api_user:
        user = request.api_user
    return user


def _verify_permissions(permission, project=None):
    """Verify session user or api user has the required permissions.
    For permission=superuser, project is optional.
    When permission weight is not reached it will raise HTTP 401.
    """
    user = _get_user_api_or_session()
    if user is None:
        abort(401)
    required_permission_weight = Permissions.get_weight(permission)
    user_weight = 0
    if user.is_superuser:
        user_weight = Permissions.get_weight(Permissions.SUPER_USER)
    elif project:
        user_weight = user.project_weight(project)
    if required_permission_weight > user_weight:
        abort(401)
