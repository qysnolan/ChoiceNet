TeacherEvaluator.core.factory("Users", ["$resource", function($resource)
{
    var api = $resource('/api/users.json', {page: 1});

    var users = [];
    var total = 0;

    var getByPage = function (page)
    {
        api.get({page: page}, function (data)
        {
            users = data.results;
            total = data.count;

            return true;
        }, function (data)
        {
            return false;
        });
    };

    var getByUsername = function(username)
    {
        api.get({username: username}, function (data)
        {
            users = data.results;
            total = data.count;

            return true;
        }, function (data)
        {
            return false;
        });
    };

    var getUsers = function()
    {
        return users;
    };

    var getTotal = function()
    {
        return total;
    };

    return {
        getByUsername: getByUsername,
        getByPage: getByPage,
        getTotal: getTotal,
        users: getUsers
    }
}]);
