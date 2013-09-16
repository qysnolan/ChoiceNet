'use strict';

TeacherEvaluator.core
.filter('float', function () {
    return function (input) {
        return parseFloat(input);
    };
});
