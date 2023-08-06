
$(document).ready(function() {
    TestList.getTests(Global.project);
    $('#treeRoot').treed();
});


const TestList = new function(){

    this.getTests = function(projectName){
        $.ajax({
            url: "/api/project/test-tree",
            data: {
                "project": projectName
            },
            dataType: 'json',
            type: 'GET',
            success: function(tests) {
                let treeRoot = $("#treeRoot");
                Project.loadTreeElements(treeRoot, tests.sub_elements, 'test');
                TestList.getTestsTags(tests);
            },
        });
    }

    this.getTestsTags = function(tests){
        $.ajax({
            url: "/api/project/test-tags",
            data: {
                "project": Global.project
            },
            dataType: 'json',
            type: 'GET',
            success: function(testsTags) {
                TestList.displayTags(testsTags)
            },
        });
    }

    this.displayTags = function(testsTags){
        Object.keys(testsTags).forEach(test => {
            TestList.displayTestTags(test, testsTags[test])
        });
    }

    this.displayTestTags = function(testName, tags){
        let timeout = 0;
        setTimeout(function(){
            let testElement = $(`li.tree-element[type='test'][fullpath='${testName}']`);
            let tagContainer = $(`<div class="tag-container"></div>`);
            tags.forEach(function(tag){
                let tagElement = $(`<span class="tag">${tag}</span>`);
                tagContainer.append(tagElement)
            })
            testElement.find('.tree-element-buttons').before(tagContainer);
            }, timeout, tags)
    }

    this.getDisplayedTestTags = function(testName){
        let tags = []
        let testElement = $(`li.tree-element[type='test'][fullpath='${testName}']`);
        let testTags = testElement.find('div.tag-container>span.tag');
        testTags.each(function(i){
            tags.push($(this).html())
        })
        return tags
    }
}
