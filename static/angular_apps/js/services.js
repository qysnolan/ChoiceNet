'use strict';

/* Services */

var serviceServices = angular.module('serviceServices', ['ngResource']);

serviceServices.factory('Service', ['$resource',
  function($resource){
    return $resource('/api/services.json', {});
  }]);
