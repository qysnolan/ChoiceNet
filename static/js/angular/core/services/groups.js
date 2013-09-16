TeacherEvaluator.core.factory("Groups", ["$resource", function($resource)
{
    var api = $resource('/api/departments.json', {page: 1});

    var groups = [];
    var total = 0;

    var getByPage = function (page)
    {
        api.get({page: page}, function (data)
        {
            groups = data.results;
            total = data.count;

            return true;
        }, function (data)
        {
            return false;
        });
    };

    var getGroups = function()
    {
        return groups;
    };

    var getTotal = function()
    {
        return total;
    };

    return {
        getByPage: getByPage,
        getTotal: getTotal,
        groups: getGroups
    }
}]);
