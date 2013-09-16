'use strict';

angular.module('teacherEvaluator.directory')
  .controller('DirectoryCtrl', function ($scope, $http, $resource, service, limitToFilter) {
    $scope.extraSearch = false;

    //fetches a typeahead from the API a specific fieldName of model
    $scope.getTypeahead = function (model, fieldName, term) {
      return $http.get('/api/'+ model +'/.json?'+ fieldName +'='+term).then(function(response){
        var objects = response.data.results;
        var list = []
        for (var i = 0; i < objects.length; i++) {
          list.push(objects[i][fieldName]);
        }
        return limitToFilter(list, 15);
      });
    }

    //given a name (term) fetches a typeahead list from the API
    $scope.nameTypeahead = function (term) {
      return $http.get('/api/users.json?search='+term).then(function(response){
        var objects = response.data.results;
        var list = [];
        for (var i = 0; i < objects.length; i++) {
          list.push(objects[i].first_name + ' ' + objects[i].last_name);
        }
        return limitToFilter(list, 15);
      });
    }

    var paginationButtons = {
      first: '<i class="icon-double-angle-left"></i>',
      previous: '<i class="icon-angle-left"></i>',
      next: '<i class="icon-angle-right"></i>',
      last: '<i class="icon-double-angle-right"></i>'
    };  
    var setPaginationButtons = function () {
      $('div.pagination a:contains("First")').html(paginationButtons.first); 
      $('div.pagination a:contains("Previous")').html(paginationButtons.previous); 
      $('div.pagination a:contains("Next")').html(paginationButtons.next); 
      $('div.pagination a:contains("Last")').html(paginationButtons.last);
    }

    //watch the service for updates to the teachers list, apply changes to relevant vars
    $scope.$watch(function () {
      $scope.teachers = service.teachers();
      $scope.count = service.count();
      $scope.totalPages = Math.ceil($scope.count/25);
      //fix to add links to pagination buttons
      $('div.pagination a').attr('href', 'javascript:void(0)');
      setPaginationButtons();
    });

    //when the page changes, update the teachers
    $scope.$watch('currentPage', function () {
      //keep trying to fetch teachers until a success
      service.getTeachers({page: $scope.currentPage});
    });
    
    $scope.isLoading = true;
    $scope.currentPage = 1;
    $scope.maxSize = 10; 
    $scope.search = {
    };

    $scope.searchTeachers = function () {
      $scope.currentPage = 1;
      var params = {
        username: $scope.search.username,
        department: $scope.search.department,
        school: $scope.search.school,
        //we have to search for the name because it's arbitrary input
        search: $scope.search.name,
        page: $scope.currentPage
      };
      $scope.isLoading = true;
      $scope.isLoading = service.getTeachers(params);
    };

    $scope.$evalAsync(function () {
      service.getTeachers({});
      $scope.isLoading = false;
    });
  
    $scope.red = 0;
    $scope.green = 256;

    $scope.$watch(function () {
      $('a[data-toggle="tooltip"]').tooltip();
    })
  });
