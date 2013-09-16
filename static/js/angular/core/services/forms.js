TeacherEvaluator.core
.factory('forms', function($resource){
    var api = $resource('/api/forms/:id?format=json', {page: 1});

    var forms = [];

    var getByPage = function (page) {
        api.get({page: page}, function (data) {
            evaluations = data.results;
            total = data.count;

            return true;
        }, function (data) {
            return false;
        });
    };

    var getForms = function() {
        api.get(function (data) {
            forms = data.results;
        })
    };

    var getFormById = function (id) {
        return api.get({id:id}, function (data) {
            return data;
        })
    }

    return {
        getByPage: getByPage,
        getFormById: getFormById,
        getForms: getForms,
        forms: function () {
            return forms;
        }
    }
});
