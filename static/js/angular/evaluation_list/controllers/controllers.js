 function EvaluationListCtrl($scope, $timeout, $http, Evaluation) {

  var timer = false;
  var ordering = "";
  $scope.currentPage = 1;
  $scope.maxSize = 6;
  $scope.search = "";
  $scope.firstEntryOnCurrentPage = 0;
  $scope.lastEntryOnCurrentPage = 0;

  $scope.$evalAsync(function () {
      Evaluation.getUserUrl();
   });

  $scope.canEdit = function (evaluation) {
    if (evaluation.is_submitted) {
      return false;
    }

    if (evaluation.evaluator == Evaluation.userUrl()) {
      return true;
    }

    if (evaluation.teacher != Evaluation.userUrl()) {
      return true;
    }

    return false;
  }

  $scope.column_head = {
       1: "Modified",
       2: "Teacher",
       3: "Form",
       4: "Evaluator",
       5: "Submitted"
  };

  $scope.sort = {
      column: '1',
      descending: true
  };

  $scope.changeSorting = function(column) {
        var sort = $scope.sort;
        if (sort.column == column) {
            sort.descending = !sort.descending;
        }
        else {
            sort.column = column;
            if(column == '1' || column == '5'){
                sort.descending = true;
            }
            else{
                sort.descending = false;
            }
        }



        switch(column)
        {
            case '1':
                ordering = sort.descending ? "-time_modified": "time_modified";
                break;
            case '2':
                ordering = sort.descending ? "-teacher_name": "teacher_name";
                break;
            case '3':
                ordering = sort.descending ? "-form" : "form";
                break;
            case '4':
                ordering = sort.descending ? "-evaluator_name" : "evaluator_name";
                break;
            case '5':
                ordering = sort.descending ? "-is_submitted" : "is_submitted";
                break;
            default:
                ordering = "";
        }

        Evaluation.getEvaluations({page: 1, search: $scope.search, ordering: ordering});
        $scope.currentPage = 1;

        };


  $scope.deleteEvaluation = function(evaluationId){
     $http.post("/deleteEvaluation/", "evaluation=" + evaluationId)
     .success(function() {
         if ($scope.count%25 == 1 && $scope.currentPage >= 2){
             //delete the only record in current page, return the previous page
             $scope.currentPage = $scope.currentPage-1;
         }
         else {
             //otherwise, update current page
             Evaluation.getEvaluations({page: $scope.currentPage, search: $scope.search, ordering:ordering});
         }
     }).error(function(data, status) {
           $scope.status = status;
     });
  };


  $scope.$watch(function(){
      // update evaluation list
      $scope.userUrl = Evaluation.userUrl();
      $scope.evaluations = Evaluation.evaluations();
      $scope.count = Evaluation.count();
      $scope.totalPages = Math.ceil($scope.count/25);
      $scope.firstEntryOnCurrentPage = 25 * ($scope.currentPage - 1) + 1;
      $scope.lastEntryOnCurrentPage = $scope.firstEntryOnCurrentPage + 24 > $scope.count ? $scope.count : $scope.firstEntryOnCurrentPage + 24
  });

  $scope.$watch('currentPage', function () {
      // retrieve data from api when a different page is requested
     Evaluation.getEvaluations({page: $scope.currentPage, search: $scope.search, ordering: ordering});
  });

  $scope.$watch('search', function () {
      // fetch results containing the search words
      if(timer){
          $timeout.cancel(timer);
      }
      timer = $timeout(function(){
         Evaluation.getEvaluations({page: 1, search: $scope.search, ordering: ordering});
         $scope.currentPage = 1;
      }, 500);
  });
}
