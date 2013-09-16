'use strict';

TeacherEvaluator.form
.controller('IndicatorModalCtrl', function ($scope, form) {
    $scope.$on('editIndicator', function(event, args) {
        $scope.index = args.idx;
        $scope.standard = args.std;
        $scope.open();
    });

    $scope.saveIndicator = function() {
        form.setIndicator($scope.index, $scope.standard, $scope.editIndicator);
        $scope.close();
    };

    $scope.open = function () {
        var this_indicator = $scope.indicators[$scope.standard][$scope.index];
        var current_number = $scope.indicators[$scope.standard].length+1;
        $scope.editIndicator = {
            title: this_indicator.title,
            description: this_indicator.description,
            order: this_indicator.order,
            id: this_indicator.id
        };
        $scope.shouldBeOpen = true;
    };

    $scope.close = function () {
        $scope.shouldBeOpen = false;
    };

    $scope.opts = {
        backdrop: false,
        backdropFade: true,
        dialogFade:true
    };
});
