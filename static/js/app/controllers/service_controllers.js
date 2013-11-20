var serviceControllers = angular.module('serviceControllers', []);

serviceControllers.controller('ServiceListCtrl', function ($scope, $http) {
    $http.get('api/services.json').success(function(data) {
        $scope.services = data.results;
        $scope.count = data.count;
        $scope.previous = data.previous;
        $scope.next = data.next;
    });
    $scope.firstDisable = false;
    $scope.lastDisable = false;
    $scope.nextDisable = true;
    $scope.previousDisable = false;
    $scope.orderProp = 'name';

    var checkDisable = function() {
        $scope.previous==null ? $scope.previousDisable = false : $scope.previousDisable = true;
        $scope.next==null ? $scope.nextDisable = false : $scope.nextDisable = true;
    };

    checkDisable();

    $scope.getServices = function(url) {
        $http.get(url).success(function(data) {
            $scope.services = data.results;
            $scope.count = data.count;
            $scope.previous = data.previous;
            $scope.next = data.next;
        });
        checkDisable();
    };

});
