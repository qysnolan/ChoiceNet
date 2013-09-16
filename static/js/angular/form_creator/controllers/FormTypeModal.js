'use strict';

TeacherEvaluator.form
.controller('FormTypeModalCtrl', function ($scope, form) {
    $scope.$on('changeFormType', function(event) {
        $scope.threeLevel = form.threeLevel();
        $scope.shouldBeOpen = true;
    });

    $scope.close = function () {
        $scope.shouldBeOpen = false;
    };

    $scope.threeLevel = false;

    $scope.save = function () {
        form.setThreeLevel($scope.threeLevel);
        $scope.close();
    };

    $scope.opts = {
        backdrop: false,
        backdropFade: true,
        dialogFade:true
    };
});
