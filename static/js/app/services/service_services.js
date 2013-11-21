'use strict';

/* Services */

var serviceServices = angular.module('serviceServices', ['ngResource']);

serviceServices.factory('Service', ['$resource',
  function($resource){
    return $resource('services/serviceId.json', {}, {
      query: {method:'GET', params:{serviceId:'services'}, isArray:true}
    });
  }]);
