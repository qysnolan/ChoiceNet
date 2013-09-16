'use strict';

angular.module('teacherEvaluator.directory')
  .controller('TestCtrl', function ($scope, $resource) {
  	$scope.format = 'M/d/yy h:mm:ss a';
  	$scope.inputId = 0;
  	var usersAPI = $resource('/api/users/:id.json', {page: 1});

  	$scope.teacher = usersAPI.get({id:2109}, function (data) {
		console.log(data);
	});
  });
