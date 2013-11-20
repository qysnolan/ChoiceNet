
var serviceApp = angular.module('serviceApp', [
  'ngRoute',
  'serviceAnimations',
  'serviceControllers',
  'serviceFilters',
  'serviceServices'
]);

serviceApp.config
    (['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: '/static/js/app/views/service_list.html',
        controller: 'ServiceListCtrl'
      }).
//      when('/serviceId', {
//        templateUrl: '/static/js/app/views/service_detail.html',
//        controller: 'ServiceDetailCtrl'
//      }).
      otherwise({
        redirectTo: '/'
      });

  }]);