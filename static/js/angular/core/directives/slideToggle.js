'use strict';

angular.module('teacherEvaluator.core')
  .directive('slideToggle', function () {
    return function(scope, element, attrs) {
		$(element).click(function(event) {
			//event.stopPropagation();
			$(element).slideToggle("slow");
		});
	};
  });
