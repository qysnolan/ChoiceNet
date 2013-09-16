'use strict';
//splits an array into a series of arrays of length 'length'
angular.module('teacherEvaluator.core')
  .filter('splitToGroups', function () {
    return function (array, length) {
    	var groups = [];
		for (var i=0; i < Math.ceil(array.length/length); i++) {
			groups[i] = [];
			for (var j=0; j < length; j++) {
		  		if (array[j + (i*length)] !== undefined)
		      		groups[i].push(array[j + (i * length)]);
		  	}
		}
		return groups; 
    };
  });

