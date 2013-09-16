angular.module('evaluationListService', ['ngResource']).
    factory('Evaluation', function($resource){

    var evaluations = [];
    var count;
    var userUrl;

    var evaluationAPI = $resource('/api/evaluations/', {});
    var userAPI = $resource('/api/me/', {});


    var getUserUrl = function(){
        userAPI.get(function(response){
            userUrl = response.url;
            return true;
        }, function(response){
            return false;
        });
    };

    var getEvaluations = function(param){
        if(param.page === undefined)
           param.page = 1;
        evaluationAPI.get(param, function(response){
           // on success
           count = response.count;
           evaluations = response.results;
           return true;
        }, function(response){
            // on failure
            return false;
        });
    };

    var reset = function(){
        evaluations=[];
        count= undefined;
    };

        return{
            getEvaluations: getEvaluations,

            reset: reset,

            getUserUrl: getUserUrl,

            evaluations: function(){
                return evaluations;
            },

            count: function(){
                return count;
            },

            userUrl: function(){
                return userUrl;
            }

        }


});
