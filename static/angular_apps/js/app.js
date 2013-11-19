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
              when('/', {
                templateUrl: '/static/angular_apps/templates/service-list.html',
                controller: 'ServiceAppListCtrl'
              }).
              when('/serviceID', {
                templateUrl: '/static/angular_apps/templates/service-detail.html',
                controller: 'ServiceDetailCtrl'
              }).
              otherwise({
                redirectTo: '/services'
              });
    }]);
