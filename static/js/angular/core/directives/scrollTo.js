'use strict';

TeacherEvaluator.core
  .directive('scrollTo', function ($location, $anchorScroll) {
    return function(scope, element, attrs) {
        element.bind('click', function(event) {
            event.stopPropagation();
            scope.$on('$locationChangeStart', function(ev) {
              ev.preventDefault();
            });
            var target = attrs.scrollTo;
            $location.hash(target);
            $anchorScroll();
            var targetId = '#' + target;
            // highlight it with color
            $(targetId).animate({
                backgroundColor: '#fff684'
            }, 1000, function () {
                $(targetId).animate({
                    backgroundColor: "#FFFFFF"
                }, 1000);
            });
        });
    };
  });
