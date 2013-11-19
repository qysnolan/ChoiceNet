'use strict';

/* Controllers */

var serviceApp = angular.module('serviceApp', []);

serviceApp.controller('ServiceListCtrl', function ($scope, $http) {
  $http.get('api/services.json').success(function(data) {
    $scope.services = data.results;
  });

  $scope.orderProp = 'date_modified';
});
