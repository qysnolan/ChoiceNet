var serviceControllers = angular.module('serviceControllers', []);

serviceControllers.controller('ServiceListCtrl', function ($scope, $http) {
    $http.get('api/services.json').success(function(data) {
        $scope.services = data.results;
        $scope.count = data.count;
        $scope.previous = data.previous;
        $scope.next = data.next;
        $scope.totalPages = Math.ceil($scope.count/25);
        $scope.currentPage = 1;
        $scope.firstEntry = 25 * ($scope.currentPage - 1) + 1;
        $scope.lastEntry = $scope.firstEntry + 24 > $scope.count ? $scope.count : $scope.firstEntry + 24;
        checkDisable();
    });
    $scope.firstDisable = true;
    $scope.lastDisable = true;
    $scope.nextDisable = false;
    $scope.previousDisable = false;
    $scope.orderProp = 'name';

    var checkDisable = function() {
        $scope.previous==undefined ? $scope.previousDisable = true : $scope.previousDisable = false;
        $scope.next==undefined ? $scope.nextDisable = true : $scope.nextDisable = false;
        $scope.currentPage==1 ? $scope.firstDisable = true : $scope.firstDisable = false;
        $scope.totalPages==$scope.currentPage ? $scope.lastDisable = true : $scope.lastDisable = false;
    };

    $scope.getServices = function(url, direction) {
        $http.get(url).success(function(data) {
//            var data1 = $scope.services;
//            var data2 = data.results;
//            $scope.services = $.concat(data1, data2);
            $scope.services = data.results;
            $scope.previous = data.previous;
            $scope.next = data.next;
            if(direction==1)
                $scope.currentPage = 1;
            if(direction==2)
                $scope.currentPage --;
            if(direction==3)
                $scope.currentPage ++;
            if(direction==4)
                $scope.currentPage = $scope.totalPages;
            $scope.firstEntry = 25 * ($scope.currentPage - 1) + 1;
            $scope.lastEntry = $scope.firstEntry + 24 > $scope.count ? $scope.count : $scope.firstEntry + 24;
            checkDisable();
        });
    };

});
