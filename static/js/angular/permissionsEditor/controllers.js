TeacherEvaluator.permissionsEditor.controller("PermissionsCtrl", ["$scope", "$http", "$location", "Schools", "Groups", function($scope, $http, $location, Schools, Groups) {
    var formId = $location.absUrl().split("/")[4];

    $scope.permissions = [
        {
            name: "Can not view"
        },
        {
            id: 2,
            name: "Can create self evaluations"
        },
        {
            id: 3,
            name: "Can create evaluations"
        },
        {
            id: 4,
            name: "Can edit"
        }
    ];

    Schools.getByPage(1);
    Groups.getByPage(1);

    $scope.$watch(function() {
        $scope.schools = Schools.schools();
        $scope.groups = Groups.groups();
    });

    /*
    $scope.users = [
        {
            id: 1,
            first_name: "First",
            last_name: "Last",
            schools: [
                $scope.schools[0]
            ],
            groups: [
                $scope.groups[1]
            ],
            permission: $scope.permissions[0]
        },
        {
            id: 2,
            first_name: "Blah",
            last_name: "Last",
            schools: [
                $scope.schools[1]
            ],
            groups: [
                $scope.groups[0]
            ],
            permission: $scope.permissions[0]
        },
        {
            id: 3,
            first_name: "First",
            last_name: "That",
            schools: [
                $scope.schools[0],
                $scope.schools[1]
            ],
            groups: [
                $scope.groups[0],
                $scope.groups[1]
            ],
            permission: $scope.permissions[0]
        }
    ];*/

    $scope.selections = {
        school: null,
        group: null
    };

    $scope.filterUsersByGroup = function(user) {
        if ($scope.selections.group === null) {
            return true;
        }

        if ($.inArray($scope.selections.group, user.groups)) {
            return true;
        }

        return false;
    };

    $scope.filterUsersBySchool = function(user) {
        if ($scope.selections.school === null) {
            return true;
        }

        if ($.inArray($scope.selections.school, user.schools)) {
            return true;
        }

        return false;
    };

    $scope.saveSchoolPermissions = function (school) {
        permission = school.permission;

        if (!permission) {
            permission = 1;
        }

        $http.post("/forms/" + formId + "/permissions/", "school=" + school.id + "&permission=" + permission);
    };
}]);
