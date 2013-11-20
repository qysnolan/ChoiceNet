'use strict';

/* Controllers */

var serviceControllers = angular.module('serviceControllers', []);

serviceControllers.controller('ServiceListCtrl', function ($scope, $http) {
  $http.get('api/services.json').success(function(data) {
    $scope.services = data.results;
  });
  $scope.orderProp = 'name';
});

//phonecatControllers.controller('PhoneDetailCtrl', ['$scope', '$routeParams', 'Phone',
//  function($scope, $routeParams, Phone) {
//    $scope.phone = Phone.get({phoneId: $routeParams.phoneId}, function(phone) {
//      $scope.mainImageUrl = phone.images[0];
//    });
//
//    $scope.setImage = function(imageUrl) {
//      $scope.mainImageUrl = imageUrl;
//    }
//  }]);