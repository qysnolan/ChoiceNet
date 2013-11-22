'use strict';

/* Services */

var serviceServices = angular.module('serviceServices', ['ngResource']);

serviceServices.factory('Service', ['$resource',
    function($resource){
        return $resource('api/services/:serviceId', {}, {
            query: {method:'GET', params:{serviceId:'services'}, isArray:true}
        });
    }]);

angular.module('filters', []).
    filter('truncate', function () {
        return function (text, length) {
            if(text==undefined)
                return text;
            var end = "...";
            if (text.length <= length || text.length - end.length <= length) {
                return text;
            }
            else {
                return String(text).substring(0, length-end.length) + end;
            }
        };
    });
