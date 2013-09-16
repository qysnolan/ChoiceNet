angular.module('teacherEvaluator.directory')
.factory('service', function ($http, $resource) {
	var teachers = [];
    var count = undefined;
	
    var teachersAPI = $resource('/api/users/.json',
        {page: 1});

    //Fetch a list of teachers from the API.
    //Optionally accepts an object of filtering params.
    //Returns true if success, false if failure.
    var getTeachers = function (params) {
        if (params.page === undefined)
            params.page = 1;
        teachersAPI.get(params, function (data) {
            console.log("sucess");
            //on success
            count = data.count;
            teachers = data.results;
            for (var i=0; i < teachers.length; i++) {
                teachers[i].shown = false;
            }
            return true;
        }, function (data) {
            console.log("fail");
            //on failure
            return false;
        })
    };

	//public api
	return {
		getTeachers: getTeachers,
        teachers: function () {
            return teachers
        },
        count: function () {
            return count;
        },

	}
});