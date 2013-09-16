'use strict';

var TeacherEvaluator = {

    app: angular.module('teacherEvaluator', ['ui.bootstrap', 'ngResource',
        'ngCookies', 'teacherEvaluator.core', 'teacherEvaluator.formLibrary',
        'teacherEvaluator.permissionsEditor']),
    core: angular.module('teacherEvaluator.core', []),
    directory: angular.module('teacherEvaluator.directory', ['ui.bootstrap', 'ngResource', 'userCardDirective']),
    form: angular.module('teacherEvaluator.form', ['ngResource', 'ui.bootstrap', 'teacherEvaluator.core', 'teacherEvaluator', 'ngCookies']),
    permissionsEditor: angular.module('teacherEvaluator.permissionsEditor', []),
    evaluationList: angular.module('teacherEvaluator.evaluationList',['evaluationListService','ui.bootstrap','ngCookies']),
    formLibrary: angular.module('teacherEvaluator.formLibrary', []),
    userList:angular.module('teacherEvaluator.userList',['userListService', 'ui.bootstrap', 'ngCookies'])
};

TeacherEvaluator.app.run(['$http', '$cookies', function($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    //$http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
}]);

TeacherEvaluator.evaluationList.run(['$http', '$cookies', function($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
}]);

TeacherEvaluator.userList.run(['$http', '$cookies', function($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
}]);

TeacherEvaluator.directory
    .config(function ($routeProvider, $locationProvider) {
        $routeProvider
            .when('/', {
                    templateUrl: '/static/views/teacher_directory/directory.html',
                    controller: 'DirectoryCtrl'
            })
            .when('/test', {
                templateUrl: '/static/views/teacher_directory/test.html',
                controller: 'TestCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
        $locationProvider.html5Mode(true);
    });

TeacherEvaluator.form
.config(function ($routeProvider, $locationProvider) {
    $routeProvider
        .when('/:formId', {
            templateUrl: '/static/views/form_creator/form.html',
            controller: 'FormCtrl'
        })
        .otherwise({
            redirectTo: '/'
        });
    $locationProvider.html5Mode(true);
});

TeacherEvaluator.evaluationList
.config(function ($routeProvider, $locationProvider){
    $routeProvider
        .when('/', {
             templateUrl: '/static/views/evaluation_list/evaluation_list.html',
             controller: 'EvaluationListCtrl'
        });
    $locationProvider.html5Mode(true);
});

TeacherEvaluator.userList
.config(function ($routeProvider, $locationProvider){
    $routeProvider
        .when('/', {
            templateUrl: '/static/views/account_list/account_list.html',
            controller: 'UserListCtrl'
        });
    $locationProvider.html5Mode(true);
});

