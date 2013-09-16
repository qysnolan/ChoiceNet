TeacherEvaluator.core.factory("Evaluations", ["$resource", function($resource)
{
    var api = $resource('/api/evaluations.json', {page: 1});

    var evaluations = [];
    var total = 0;

    var getByPage = function (page)
    {
        api.get({page: page}, function (data)
        {
            evaluations = data.results;
            total = data.count;

            return true;
        }, function (data)
        {
            return false;
        });
    };

    var getEvaluations = function()
    {
        return evaluations;
    };

    var getTotal = function()
    {
        return total;
    };

    return {
        getByPage: getByPage,
        getTotal: getTotal,
        schools: getEvaluations
    }
}]);
