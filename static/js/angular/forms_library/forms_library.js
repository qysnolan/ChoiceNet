TeacherEvaluator.formLibrary.factory('service', function ($resource) {
    var forms = [];

    var formsApi = $resource('/api/library.json');

    var getForms = function (param) {
        formsApi.get(param, function (data){
            forms = data.results;
            count = data.count;
        });
    };

    return {
        forms: function () {
            return forms;
        },
        getForms: getForms,

        count: function () {
            return count;
        }
    }

});

var RatingControl = function ($scope) {
    $scope.rate = 0;
    $scope.isReadonly = false;
};

TeacherEvaluator.formLibrary.filter('truncate', function () {
    return function (text, length, end) {
        if (isNaN(length))
            length = 10;

        if (end === undefined)
            end = "...";

        if (text.length <= length || text.length - end.length <= length) {
            return text;
        }
        else {
            return String(text).substring(0, length-end.length) + end;
        }

    };
});
    
TeacherEvaluator.formLibrary.controller("LibraryCtrl",
    function($scope, $dialog, $timeout ,service) {
    var timer = false;

    $scope.searchByDescription ="";
    $scope.searchByForm = "";

    $scope.currentPage = 1;
    $scope.firstEntryOnCurrentPage = 0;
    $scope.lastEntryOnCurrentPage = 0;
    $scope.maxSize = 6;

    $scope.$watch(function () {
        $scope.forms = service.forms();
        $scope.count = service.count();
        $scope.totalPages = Math.ceil($scope.count/25);
        $scope.firstEntryOnCurrentPage = $scope.count>0 ?
            25 * ($scope.currentPage - 1) + 1 : 0;
        $scope.lastEntryOnCurrentPage = $scope.firstEntryOnCurrentPage + 24 >
            $scope.count ? $scope.count : $scope.firstEntryOnCurrentPage + 24
    });

    $scope.view = function (form) {
        $scope.showView = true;
        $scope.form = form;
    };

    $scope.close = function () {
        $scope.showView = false;
    };

    $scope.$watch('currentPage + searchByDescription + searchByForm',function (){
      // retrieve data from api when things change
      if(timer){
         $timeout.cancel(timer);
      }
      timer = $timeout(function(){
         service.getForms({page: $scope.currentPage, name: $scope.searchByForm,
             description: $scope.searchByDescription});
      }, 500);
    });

});
