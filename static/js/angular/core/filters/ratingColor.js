'use strict';

angular.module('userCardDirective')
  .filter('ratingColor', function () {
    return function (rating) {
        if (rating < 20)
            return 'FF0000';
        else if (rating < 40)
            return 'FFA500';
        else if (rating < 60)
            return 'FFFF00';
        else if (rating < 80)
            return 'B1FB17';
        else
            return '57E964';

    };
});