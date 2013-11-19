'use strict';

/* Controllers */

var serviceControllers = angular.module('serviceControllers', []);

serviceControllers.controller('ServiceListCtrl', ['$scope', 'Service',
  function($scope, Service) {
    $scope.phones = Service.query();
    $scope.orderProp = 'date';
  }]);

serviceControllers.controller('ServiceDetailCtrl', ['$scope', '$routeParams', 'Service',
  function($scope, $routeParams, Service) {
    $scope.phone = Service.get({phoneId: $routeParams.phoneId}, function(service) {
      $scope.mainImageUrl = service.images[0];
    });

    $scope.setImage = function(imageUrl) {
      $scope.mainImageUrl = imageUrl;
    }
  }]);
