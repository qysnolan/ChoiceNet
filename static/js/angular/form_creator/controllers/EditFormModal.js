'use strict';

TeacherEvaluator.form
.controller('EditFormModalCtrl', function ($scope, form) {

    $scope.$watch(function () {
        return form.editFormModalIsOpen();
    }, function () {
        if (form.editFormModalIsOpen())
            $scope.open();
    });

    $scope.open = function () {
        $scope.shouldBeOpen = true;

        $scope.formTitle = form.form().name;
        $scope.formDescription = form.form().description;
    };

    $scope.close = function () {
        $scope.shouldBeOpen = false;
        form.editFormModalClose();
    };

    $scope.saveForm = function () {
        var updatedForm = form.form();
        updatedForm.name = $scope.formTitle;
        updatedForm.description = $scope.formDescription;

        form.setForm(updatedForm);

        $scope.close();
    };

    $scope.opts = {
        backdrop: false,
        backdropFade: true,
        dialogFade:true
    }
});
