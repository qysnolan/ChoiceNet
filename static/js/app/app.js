var serviceApp = angular.module('serviceApp', [
    'ngRoute',
    'ngCookies',
    'serviceControllers',
    'serviceFilters',
    'serviceServices',
    'filters'
]);

//serviceApp.run(['$http', '$cookies', function($http, $cookies) {
//    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
//    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
//}]);

serviceApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: '/static/js/app/views/service_list.html',
                controller: 'ServiceListCtrl'
            }).
            when('/detail/:serviceId', {
                templateUrl: '/static/js/app/views/service_detail.html',
                controller: 'ServiceDetailCtrl'
            }).
            otherwise({
                redirectTo: '/'
            });
    }],['$httpProvider',function($httpProvider) {
    var token = $('input[name=csrfmiddlewaretoken]').val();
    $httpProvider.defaults.headers.post['X-CSRFToken'] = token;
}]);