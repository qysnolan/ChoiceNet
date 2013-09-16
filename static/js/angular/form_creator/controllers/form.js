'use strict';

TeacherEvaluator.form
.controller('FormCtrl', function ($scope, $http, $cookies, $routeParams, $dialog, $anchorScroll, form, forms) {

    $scope.formId = $routeParams.formId;
    $scope.form = form;

    // Checks if the page was accessed with an id, then bootstraps form.startup()
    $scope.$evalAsync(function () {
        if ($scope.formId)
            form.startup($routeParams.formId);
        else
            window.location = '/404';
    });

    $scope.elementInfoShow = []; // List used to store booleans to show element-descriptor table
    $scope.showTitle = true;
    $scope.indicators = form.indicators();
    $scope.showIndicatorInfo = true;
    $scope.elements = form.elements();
    $scope.descriptors = form.descriptors();
    $scope.descriptorGroups = form.descriptorGroups();
    $scope.radioStandard = {val: form.currentStandard()};

    // Functions to switch between main and help pages
    $scope.help = function () {
        $scope.selection = '/static/views/form_creator/partials/help.html';
    };
    $scope.goBack = function () {
        $scope.selection = '/static/views/form_creator/partials/formBody.html';
    }

    $scope.alert = {}; // object for carrying alert information to share with the alert modal
    $scope.alertOptions = {
        backdrop: false,
        backdropFade: true,
        dialogFade:true
    };
    $scope.openAlert = function (type, title, children, func, args) {
    /*
    Opens an alert when a part of a form is selected to be deleted.
    PARAMS:
        type: String - The type of form element being deleted 
        title: String - The actual variable title of the thing being deleted
        children: Object of form {type: 'elements', count: form.elements()[form.currentStandard()][$index].length}
        func: String - function to carry out the delete as a string i.e. 'deleteIndicator'
        args: Array - array of arguments that will be handed off to the func i.e. [$index, element]
                NOTE: Remember these are evaluated in the given scope before they're handed off!
    */
        var argsList = '';
        for (var i=0; i < args.length; i++) {
            if (i === args.length-1)
                var temp = args[i];
            else
                var temp = args[i] + ',';
            argsList = argsList.concat(temp);
        }
        func = func.concat('(' + argsList + ')');
        func = '$scope.'+func;
        $scope.alert.func = func;
        $scope.alert.type = type;
        $scope.alert.title = title;
        $scope.alert.children = children;
        $scope.alertIsOpen = true;
    };
    $scope.closeAlert = function (del) {
        $scope.alertIsOpen = false;
        if (del)
            eval($scope.alert.func);
    };

    $scope.$watch(function () {
        $scope.rubricModalIsOpen = form.rubricModalIsOpen()
    });

    $scope.selectStandard = function(idx) {
        form.setCurrentStandard(idx);
    };

    $scope.editRubric = function () {
        form.rubricModalOpen();
    };

    $scope.editForm = function () {
        form.editFormModalOpen();
    };

    $scope.changeFormType = function () {
        $scope.$broadcast('changeFormType');
    }

    // STANDARDS STUFF 
    //Broadcast an event so that the StandardModalCtrl can take control
    $scope.editStandard = function(idx) {
        var args = {"idx":idx};
        $scope.$broadcast('editStandard', args);
    }
    $scope.deleteStandard = function (idx) {
        var standardsLength = form.standards().length;
        form.deleteStandard(idx);
        if (idx === form.currentStandard())
            $scope.radioStandard.val = 0;
        if ($scope.radioStandard.val === standardsLength-1)
            $scope.radioStandard.val--;
    }

    // INDICATORS STUFF
    $scope.editIndicator = function(idx) {
        var args = {
            'idx': idx,
            'std': form.currentStandard()
        };
        $scope.$broadcast('editIndicator', args);
    }

    $scope.deleteIndicator = function (idx) {
        form.deleteIndicator(idx);
    }

    // ELEMENTS STUFF
    $scope.editElement = function(idx, indicator) {
        var args = {
            'idx': idx,
            'std': form.currentStandard(),
            'ind': indicator
        };
        $scope.$broadcast('editElement', args);
    }

    $scope.deleteElement = function(idx, indicator) {
        form.deleteElement(idx, indicator);
    }

    // DESCRIPTORS STUFF
    $scope.deleteDescriptor = function (idx, indicator, element) {
        form.deleteDescriptor(idx, indicator, element);
    }

});     
