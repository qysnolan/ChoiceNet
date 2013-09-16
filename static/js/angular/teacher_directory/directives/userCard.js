/*
You'll need these...
<script type="text/javascript" src="/static/js/angular/angular.js"></script>
<script type="text/javascript" src="/static/js/angular/ui-bootstrap-tpls-0.4.0.js"></script>
<script src="http://code.angularjs.org/1.1.5/angular-resource.js"></script>
<script type="text/javascript" src="/static/js/angular/core/directives/userCard.js"></script>
<script type="text/javascript" src="/static/js/angular/core/filters/ratingColor.js"></script>
*/
angular.module('userCardDirective', ['ngResource', 'ui.bootstrap'])
  .directive('userCard', function($resource, $http) {
    // return the directive link function. (compile function not needed)
    return {
      restrict: 'E',
      scope: {
        userObject: '=userObject',
        userId: '@userId' //takes a user id
      },
      templateUrl: '/static/views/teacher_directory/userCard.html',
      link: function(scope, element, attrs) {
        var usersAPI = $resource('/api/users/:id/.json', {page: 1});

        //get the user using the id or an object
        var updateUser = function () {
          if (scope.userId) {
            scope.user = usersAPI.get({id:scope.userId}, function (data) {
              console.log(data);
            });
          }
          else if (scope.userObject) {
            scope.user = scope.userObject;
          };
        }

        var getRandomInt = function (min, max) {
          return Math.floor(Math.random() * (max - min + 1)) + min;
        }

        //fetch and return the evaluations for the given user
        var getEvaluations = function (user) {
          return $http.get('/api/evaluations/.json?teacher='+user.id).then(function (response) {
            var evaluations = response.data.results;
            for (var i = 0; i < evaluations.length; i++) {
              evaluations[i].score = getRandomInt(0, 100)
            }
            return evaluations;
          })
        }

        scope.showTeacherInfo = function (user) {
          user.shown = !user.shown;
          //only load the data the first time we show it
          if (!user.loadedData)
            user.evaluations = getEvaluations(user);
          user.loadedData = true;
        };

        scope.$watch(scope.userObject, function () {
          updateUser();
        }) 
      }
    }
  });