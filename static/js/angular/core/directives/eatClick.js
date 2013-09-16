'use strict';

angular.module('teacherEvaluator.core')
  .directive('eatClick', function () {
    return function(scope, element, attrs) {
        $(element).click(function(event) {
            event.stopPropagation();
        });
    };
  });
