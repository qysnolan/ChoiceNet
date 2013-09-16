angular.module('userListService', ['ngResource']).
    factory('User', function($resource){

    var users = [];
    var count;


    var userAPI = $resource('/api/users/', {});


    var getUsers = function(param){
        if(param.page === undefined)
           param.page = 1;
        userAPI.get(param, function(response){
           // on success
           count = response.count;
           users = response.results;
           return true;
        }, function(response){
            // on failure
            return false;
        });
    };


        return{
            getUsers: getUsers,

            users: function(){
                return users;
            },

            count: function(){
                return count;
            }
        }
    });



