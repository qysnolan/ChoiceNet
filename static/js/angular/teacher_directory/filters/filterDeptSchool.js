'use strict';

//filters a list of names by down, making sure that the teacher matches both dept and school chosen for search
angular.module('teacherEvaluator.directory')
  .filter('filterDeptSchool', function () {
    return function (names, args) {
    	var school = args.search.schools;
    	var department = args.search.department;
    	var teachers = args.teachers;
        var name = args.name;
    	var filteredNames = [];
    	for (var i=0; i < teachers.length; i++) {
    		var teacher = teachers[i];
            //check if either the school or department is undefined, if each one isn't then it must also be in the teacher's schools/departments
    		if (((school === undefined) || (school !== undefined && ($.inArray(school, teacher.schools) !== -1))) 
    		&& ((department === undefined) || (department !== undefined && teacher.department === department))) {
    			filteredNames.push(teacher[name]);
    		}
    	}
    	return filteredNames;
    };
  });
