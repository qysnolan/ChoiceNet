var serviceControllers = angular.module('serviceControllers', []);

serviceControllers.controller('ServiceListCtrl', function ($scope, $http) {
    var initiation = function() {
        $http.get(base_url).success(function(data) {
            $scope.services = data.results;
            $scope.count = data.count;
            $scope.previous = data.previous;
            $scope.next = data.next;
            $scope.totalPages = Math.ceil($scope.count/25);
            $scope.currentPage = 1;
            $scope.firstEntry = 25 * ($scope.currentPage - 1) + 1;
            $scope.lastEntry = $scope.firstEntry + 24 > $scope.count
                ? $scope.count : $scope.firstEntry + 24;
            var pages = [];
            for(var i=0; i<$scope.totalPages; i++)
                pages[i] = {"number": i+1};
            $scope.pages = pages;
            $scope.pageNumber = $scope.currentPage;
            $scope.base_url = base_url;
            $scope.searchTerm = searchValue.trim();
            checkDisable();
        });
        $scope.firstDisable = true;
        $scope.lastDisable = true;
        $scope.nextDisable = false;
        $scope.previousDisable = false;
        $scope.allDataLoaded = false;
        $scope.allDataLoading = false;
        $scope.orderProp = 'name';
        $scope.query = null;
    };

    initiation();
    $scope.pageView = false;

    var checkDisable = function() {
        $scope.previous==undefined
            ? $scope.previousDisable = true : $scope.previousDisable = false;
        $scope.next==undefined
            ? $scope.nextDisable = true : $scope.nextDisable = false;
        $scope.currentPage==1
            ? $scope.firstDisable = true : $scope.firstDisable = false;
        $scope.totalPages==$scope.currentPage
            ? $scope.lastDisable = true : $scope.lastDisable = false;
    };

    $scope.getServices = function(url, direction) {
        $http.get(url).success(function(data) {
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
            $scope.pageNumber = $scope.currentPage;
            $scope.firstEntry = 25 * ($scope.currentPage - 1) + 1;
            $scope.lastEntry = $scope.firstEntry + 24 > $scope.count
                ? $scope.count : $scope.firstEntry + 24;
            $scope.query = null;
            checkDisable();
        });
    };

    $scope.loadServices = function(url) {
        $http.get(url).success(function(data) {
            var data1 = $scope.services;
            var data2 = data.results;
            $scope.services = $.merge(data1, data2);
            $scope.previous = data.previous;
            $scope.next = data.next;
            $scope.currentPage ++;
            $scope.pageNumber = $scope.currentPage;
            $scope.firstEntry = 25 * ($scope.currentPage - 1) + 1;
            $scope.lastEntry = $scope.firstEntry + 24 > $scope.count
                ? $scope.count : $scope.firstEntry + 24;
            $scope.query = null;
            if(data.next==null)
                $scope.allDataLoaded = true;
        });
    };

    $scope.initiatePageView = function() {
        initiation();
        $scope.pageView=true;
    };

    $scope.initiateLoadView = function() {
        initiation();
        $scope.pageView=false;
    };

    $scope.loadAllServices = function() {
        $scope.allDataLoading = true;
        var page = 1;
        var totalData = [];
        var total = $scope.totalPages;
        while(page<=total){
            $http.get(base_url+'&page='+page).success(function(data) {
                var data1 = totalData;
                var data2 = data.results;
                totalData = $.merge(data1, data2);
            });
            page++;
        }
        $scope.services = totalData;
        $scope.currentPage = total;
        $scope.firstEntry = 1;
        $scope.lastEntry = $scope.count;
        $scope.next = null;
        $scope.allDataLoaded = true;
        $scope.allDataLoading = false;
        $scope.query = null;
    };

    $scope.goToPage = function(pageNumber) {
        $http.get(base_url+'&page='+pageNumber.number).success(function(data) {
            $scope.services = data.results;
            $scope.previous = data.previous;
            $scope.next = data.next;
            $scope.currentPage = pageNumber.number;
            $scope.pageNumber = $scope.currentPage;
            $scope.firstEntry = 25 * ($scope.currentPage - 1) + 1;
            $scope.lastEntry = $scope.firstEntry + 24 > $scope.count
                ? $scope.count : $scope.firstEntry + 24;
            $scope.query = null;
            checkDisable();
        });
    };
});

serviceControllers.controller('ServiceDetailCtrl',
    ['$scope', '$routeParams', '$http', 'Service',
    function($scope, $routeParams, $http, Service) {
        $scope.service = Service.get({serviceId: $routeParams.serviceId},
            function(service) {
                $scope.serviceName = service.name;
                $scope.csrf = csrf;
                $scope.date_created = Date.now()
            });

        var checkSalesNumber = function(serviceId) {
            $http.get('/sales/service/'+serviceId).success(function(data) {
                $scope.sales_number = data;
            });
        };
        checkSalesNumber($routeParams.serviceId);
}]);