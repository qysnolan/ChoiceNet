'use strict';

TeacherEvaluator.form
.controller('ElementModalCtrl', function ($scope, form) {

    //copies over the descriptors from the service to our local list for editing
    var refreshEditDescriptors = function () {
        var descriptors = form.descriptors()[$scope.standard][$scope.indicator][$scope.index];
        $scope.editDescriptors = descriptors;
    }

    // Takes a descriptors's index and integer upDown
    // if upDown == 1 we move it up (back) in the list, if -1 we move it down (forward)
    $scope.moveDescriptor = function (descriptor, upDown) {
        if (upDown === 1)
            var swappedDescriptor = descriptor - 1;
        else if (upDown === -1)
            var swappedDescriptor = descriptor + 1;

        if ((upDown === 1 && descriptor !== 0) || (upDown === -1 && descriptor !== $scope.editDescriptors.length-1)) {
            // check edge cases: can't go up if first, can't go down if last
            var temp = $scope.editDescriptors[swappedDescriptor];

            $scope.editDescriptors[swappedDescriptor] = $scope.editDescriptors[descriptor];
            $scope.editDescriptors[descriptor] = temp;

            form.swapOrder($scope.editDescriptors[descriptor], $scope.editDescriptors[swappedDescriptor]);

            form.splitDescriptors($scope.standard, $scope.indicator, $scope.index);
        }
    }



    // On the editElement broadcast from the main controller we assign proper variables
    $scope.$on('editElement', function(event, args) {
        $scope.index = args.idx;
        $scope.standard = args.std;
        $scope.indicator = args.ind;
        $scope.editDescriptors = form.descriptors()[$scope.standard][$scope.indicator][$scope.index]; // point to current descriptors
        $scope.open();
    });

    // Opens the model and copies over a temp copy of the element to be modified
    $scope.open = function () {
        var this_element = form.elements()[$scope.standard][$scope.indicator][$scope.index];
        var current_number = form.elements()[$scope.standard][$scope.indicator].length+1;
        $scope.editElement = {
            title: this_element.title,
            order: this_element.order,
            value: this_element.value,
            id: this_element.id
        };
        refreshEditDescriptors();
        $scope.shouldBeOpen = true;
    };

    $scope.close = function () {
        $scope.shouldBeOpen = false;
    };

    $scope.elementAlerts = [];

    // Pushes a given text alert so that it is displayed at the top of the model
    var addAlert = function (alert, list, timeout) {
        list.push(alert);
        setTimeout(function () {
            $scope.$apply(function () {
                list.splice(0,1);
            });
        }, timeout);
    };

    $scope.closeAlert = function(index) {
        $scope.elementAlerts.splice(index, 1);
    };

    $scope.addDescriptor = function () {
        form.addDescriptor($scope.indicator, $scope.index);
        refreshEditDescriptors();
    };

    $scope.deleteDescriptor = function (index) {
        form.deleteDescriptor(index, $scope.indicator, $scope.index);
        refreshEditDescriptors();
        var alert = {msg: "Descriptor deleted.", type: "info"};
        addAlert(alert, $scope.elementAlerts, 2000);
    };

    // Saves changes to element and descriptors if multiple is chosen otherwise saves and deletes descriptors
    $scope.saveElement = function () {
        reorderDescriptors();
        for (var i=0; i < $scope.editDescriptors.length; i++) {
            form.setDescriptor(i, $scope.standard, $scope.indicator, $scope.index, $scope.editDescriptors[i]);
        }
        form.setElement($scope.index, $scope.standard, $scope.indicator, $scope.editElement);
        $scope.close();
    };

    $scope.opts = {
        backdrop: false,
        backdropFade: true,
        dialogFade:true
    };

});
