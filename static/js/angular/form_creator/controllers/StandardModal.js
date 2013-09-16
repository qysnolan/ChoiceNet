'use strict';

TeacherEvaluator.form
.controller('StandardModalCtrl', function ($scope, form) {
    $scope.$on('editStandard', function(event, args) {
        $scope.index = args.idx;
        $scope.open();
    });

    $scope.saveStandard = function() {
        form.setStandard($scope.index, $scope.editStandard);
        $scope.close();
    };

    $scope.open = function () {
        var this_standard = form.standards()[$scope.index];
        var current_number = form.standards().length+1;
        $scope.editStandard = {
            title: this_standard.title,
            short_name: this_standard.short_name,
            description: this_standard.description,
            order: this_standard.order,
            id: this_standard.id
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
