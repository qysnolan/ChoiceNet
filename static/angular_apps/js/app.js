'use strict';

/* App Module */

var serviceApp = angular.module('serviceApp', [
    'ngRoute',
    'serviceAnimations',

    'serviceControllers',
    'serviceFilters',
    'serviceServices'
]);

serviceApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
              when('/services', {
                templateUrl: 'templates/services/service-list.html',
                controller: 'ServiceAppListCtrl'
              }).
              when('/services/serviceID', {
                templateUrl: 'templates/services/service-detail.html',
                controller: 'ServiceDetailCtrl'
              }).
              otherwise({
                redirectTo: '/services'
              });
    }]);
