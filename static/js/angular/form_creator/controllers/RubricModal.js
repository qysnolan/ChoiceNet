'use strict';

TeacherEvaluator.form
.controller('RubricModalCtrl', function ($scope, form) {

    $scope.$watch(function () {
        return form.rubricModalIsOpen();
    }, function () {
            if (form.rubricModalIsOpen())
                $scope.open();
    });

    $scope.open = function () {
        $scope.editRubrics.refresh();
        $scope.shouldBeOpen = true;
    };

    $scope.close = function () {
        $scope.shouldBeOpen = false;
        form.rubricModalClose();
    };

    $scope.editRubrics = {
        list: [],
        split: function (length) {
            length = 5;
            var groups = [];
            for (var i=0; i < Math.ceil(this.list.length/length); i++) {
                groups[i] = [];
                for (var j=0; j < 5; j++) {
                    var entry = this.list[j + (i*5)];
                    if (entry !== undefined)
                        groups[i].push(entry);
                }
            }
            $scope.rubricsGroups = groups;
        },
        refresh: function () {
            this.list = [];
            for (var i=0; i < $scope.rubrics.length; i++) {
                this.list[i] = {
                    title: $scope.rubrics[i].title,
                    description: $scope.rubrics[i].description,
                    order: $scope.rubrics[i].order,
                    value: $scope.rubrics[i].value
                };
            }
            this.split(5);
        }
    };
    
    $scope.rubrics = form.rubrics();
    //whether the rubric applies to the whole form (true) or by standard (false)
    $scope.byForm = true;

    $scope.standards = form.standards();
    $scope.radioStandard = {
        val: 0
    };
    $scope.standardRubrics = form.standardRubrics();
    $scope.standardRubricsGroups = form.standardRubricsGroups();

    $scope.addStandardRubric = function (st) {
        form.addStandardRubric(st);
    };

    $scope.deleteStandardRubric = function (idx, st) {
        form.deleteStandardRubric(idx, st);
    };

    $scope.addRubric = function () {
        form.addRubric();
        $scope.editRubrics.refresh();
    };

    $scope.deleteRubric = function (idx) {
        form.deleteRubric(idx);
        $scope.editRubrics.refresh();
    };

    $scope.saveRubric = function () {
        if ($scope.byForm)
            form.setRubricByForm(true);
        else
            form.setRubricByForm(false);
        $scope.close();
        form.rubricModalPopupOpen($scope.editRubrics);
    };

    $scope.opts = {
        backdrop: false,
        backdropFade: true,
        dialogFade:true
    }
});
