TeacherEvaluator.core.factory("Schools", ["$resource", function($resource)
{
    var api = $resource('/api/schools.json', {page: 1});

    var schools = [];
    var total = 0;

    var getByPage = function (page)
    {
        api.get({page: page}, function (data)
        {
            schools = data.results;
            total = data.count;

            return true;
        }, function (data)
        {
            return false;
        });
    };

    var getSchools = function()
    {
        return schools;
    };

    var getTotal = function()
    {
        return total;
    };

    return {
        getByPage: getByPage,
        getTotal: getTotal,
        schools: getSchools
    }
}]);
