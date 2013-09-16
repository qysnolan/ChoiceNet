TeacherEvaluator.form
.controller('RubricModalPopupCtrl', function ($scope, form) {
    $scope.$watch(function () {
        return form.rubricModalPopupIsOpen();
    }, function () {
        if (form.rubricModalPopupIsOpen())
            $scope.open();
    });

    //Check box whether changes to rubric apply retroactively to previously added descriptors
    $scope.retroactive = false;

    $scope.open = function () {
        $scope.shouldBeOpen = true;
    };

    $scope.close = function () {
        $scope.shouldBeOpen = false;
        form.rubricModalPopupClose();
    };

    $scope.save = function (retroactive) {
        form.saveRubric(retroactive);
        $scope.close();
    };
    
    $scope.opts = {
        backdrop: false,
        backdropFade: true,
        dialogFade:true,
        keyboard: true
    }

});