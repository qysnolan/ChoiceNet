function UserListCtrl($scope, $timeout, $http, User) {
  var timer = false;
  $scope.currentPage = 1;
  $scope.maxSize = 5;
  $scope.search = "";
  $scope.ordering="";
  $scope.firstEntryOnCurrentPage = 0;
  $scope.lastEntryOnCurrentPage = 0;


  $scope.column_head = {
       1: "Name",
       2: "Group",
       3: "Last Login"
  };

  $scope.sort = {
      column: '1',
      descending: false
  };

  $scope.changeSorting = function(column) {
        var sort = $scope.sort;
        if (sort.column == column) {
            sort.descending = !sort.descending;
        }
        else {
            sort.column = column;
            sort.descending = false;
        }

        switch(column)
        {
            case '1':
                $scope.ordering = sort.descending ? "-name": "name";
                break;
            case '2':
                $scope.ordering = sort.descending ? "-department_name": "department_name";
                break;
            case '3':
                $scope.ordering = sort.descending ? "-last_login": "last_login";
                break;
            default:
                $scope.ordering = "";
        }

        User.getUsers({page: 1, search: $scope.search, ordering: $scope.ordering});
        $scope.currentPage = 1;
        };

  $scope.isFirstLogin = function(lastLogin, dateJoined){
    var lastLoginTime = Date.parse(lastLogin);
    var dateJoinedTime = Date.parse(dateJoined);
    return lastLoginTime <= dateJoinedTime;
  };

  $scope.deactivate = function(userId){
     $http.post("/deactivateAccount/", "user=" + userId)
     .success(function() {
           User.getUsers({page: $scope.currentPage, search: $scope.search, ordering: $scope.ordering});
     }).error(function(data, status) {
           $scope.status = status;
     });
  };

  $scope.activate = function(userId){
      $http.post("/activateAccount/", "activateID=" + userId)
      .success(function(){
            User.getUsers({page: $scope.currentPage, search: $scope.search, ordering: $scope.ordering});
          }).error(function(data, status){
              $scope.status = status;
          })
  };

  $scope.$watch(function(){
      // update evaluation list
      $scope.users = User.users();
      $scope.count = User.count();
      $scope.totalPages = Math.ceil($scope.count/25);
      $scope.firstEntryOnCurrentPage = 25 * ($scope.currentPage - 1) + 1;
      $scope.lastEntryOnCurrentPage = $scope.firstEntryOnCurrentPage + 24 > $scope.count ? $scope.count : $scope.firstEntryOnCurrentPage + 24
  });

  $scope.$watch('currentPage', function () {
      // retrieve data from api when a different page is requested
     User.getUsers({page: $scope.currentPage, search: $scope.search, ordering: $scope.ordering});
  });

  $scope.$watch('search', function () {
      // fetch results containing the search words
      if(timer){
          $timeout.cancel(timer);
      }
      timer = $timeout(function(){
         User.getUsers({page: 1, search: $scope.search, ordering: $scope.ordering});
         $scope.currentPage = 1;
      }, 500);
  });
}
