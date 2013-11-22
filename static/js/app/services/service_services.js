'use strict';

/* Services */

var serviceServices = angular.module('serviceServices', ['ngResource']);

serviceServices.factory('Service', ['$resource',
  function($resource){
      console.log(1);
    return $resource('api/services/:serviceId', {}, {
      query: {method:'GET', params:{serviceId:'services'}, isArray:true}
    });
  }]);
