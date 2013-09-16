'use strict';

angular.module('teacherEvaluator.core')
  .filter('roundUp', function () {
    return function (value) {
        return Math.ceil(value);
    };
  });
