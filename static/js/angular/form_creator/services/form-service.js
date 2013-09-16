'use strict';

TeacherEvaluator.form
.factory('form', function ($http, $cookies, $q, forms) {

    /////////////////////////////
    ////// LOCAL VARIABLES //////
    /////////////////////////////

    var form = {
        title: "Example Form Title",
    }
    var rubricByForm = true; // whether the rubric is applied by form or by standard
    var editFormModalIsOpen = false;
    var rubricModalIsOpen = false;
    var rubricModalPopupIsOpen = false;
    var currentStandard = 0; // index of current descriptor in standards.list
    var applyingRubric = false;

    /////////////////////////////
    ////// HELPER FUNCTIONS //////
    /////////////////////////////

    var sortByOrder = function (a, b) {
        if (a.order < b.order)
             return -1;
        if (a.order > b.order)
             return 1;
        // a must be equal to b
        return 0;
    }

    // swaps the order of two given parts of a form
    var swapOrder = function (item1, item2) {
        // swap order and patch the items
        var temp = item1.order;
        item1.order = item2.order;
        item2.order = temp;

        $http({method: 'PATCH', url: item1.url, data: {order: item1.order}});
        $http({method: 'PATCH', url: item2.url, data: {order: item2.order}});
    }

     // Swaps the content of two standards
    var swapForStandard = function (target, standard, swappedStandard) {
        var tempItems = target.list[swappedStandard];

        target.list[swappedStandard] = target.list[standard];
        target.list[standard] = tempItems;
    }

    // Update form when standard is added/edited
    var updateForm = function () {
        var patchForm = {};
        patchForm.standards = [];
        for (var i=0; i < standards.list.length; i++) {
            patchForm.standards[i] = standards.list[i].url;
        }
        $http({method: 'PATCH', url: form.url, data: patchForm});
    }

    // Update parent standard on server when indicator is added/edited
    var updateStandard = function (st) {
        var patchStandard = {};
        patchStandard.indicators = [];
        for (var i=0; i < indicators.list[st].length; i++) {
            patchStandard.indicators[i] = indicators.list[st][i].url; // assign list of urls for indicators attached to standard to conform to api
        }
        $http({method: 'PATCH', url: standards.list[st].url, data: patchStandard});
    };

    // Update parent indicator on server when an element is added/edited
    var updateIndicator = function (st, ind) {
        var deferred = $q.defer();

        var patchIndicator = {};
        patchIndicator.elements = [];
        for (var i=0; i < elements.list[st][ind].length; i++) {
            patchIndicator.elements[i] = elements.list[st][ind][i].url;
        }
        $http({method: 'PATCH', url: indicators.list[st][ind].url, data: patchIndicator}).then(function () {
            deferred.resolve();
        });

        return deferred.promise;
    };

    // Update parent element when descriptor is added/edited
    var updateElement = function (st, ind, elem) {
        var patchElement = {};
        patchElement.descriptors = [];
        for (var i=0; i < descriptors.list[st][ind][elem].length; i++) {
            patchElement.descriptors[i] = descriptors.list[st][ind][elem][i].url;
        }
        $http({method: 'PATCH', url: elements.list[st][ind][elem].url, data: patchElement});
    };

    /////////////////////////////
    ////// LOCAL OBJECTS //////
    /////////////////////////////

    //list of rubric descriptors
    var rubrics = {
        list: [],
        groups: [
            [],
            []
        ],
        length: function () {
            return this.list.length;
        },
        add: function () {
            var order = rubrics.length()+1;
            var rubric = {
                title: 'New Rubric Title',
                description: '',
                order: order,
                value: order
            };
            this.list.push(rubric);
        },
        delete: function (idx) {
            this.list.splice(idx,1);
        },
        //apply the rubric recursively to all descriptors
        applyRetroactive: function () {
            applyingRubric = true;
            $http({url: '/forms/apply_rubric/',
                method: 'POST',
                data: {
                    form: form.id,
                    standards:[],
                    rubrics: this.list
                },
                headers: {
                'X-CSRFToken': $cookies.csrftoken,
                        'Content-Type': 'application/json'
                }
            }).then(function (response) {
                location.reload();
            });
        }
    };

    // empty temp rubric used to store information from modal before a save command is issued
    var editRubric = {};

    // holds a set of descriptors for each standard that can be applied to elements
    var standardRubrics = {
        list: [
            [],
            []
        ],
        groups: [
            [],
            []
        ],
        isEmpty: function () {
            var empty = true;
            for (var st = 0; st < this.list.length; st++) {
                for (var i = 0; i < this.list[st].length; i++) {
                    empty = false;
                }
            }
            return empty;
        },
        add: function (st) {
            var rubric = {
                title: 'New Rubric Title',
                description: '',
                order: this.list[st].length+1,
                value: this.list[st].length+1
            };
            this.list[st].push(rubric);
        },
        delete: function (idx, st) {
            this.list[st].splice(idx,1);
        },
        //separates groups of standard rubrics into groups of length, length
        split: function (length) {
            for (var i=0; i < this.list.length; i++) {
                this.groups[i] = [];
                for (var j=0; j < Math.ceil(this.list[i].length/length); j++) {
                    this.groups[i][j] = [];
                    for (var k=0; k < length; k++) {
                        var entry = this.list[i][k + (j*length)];
                        if (this.list[i][k + (j*length)] !== undefined)
                            this.groups[i][j].push(this.list[i][k + (j*length)]);
                    }
                }
            }
        },
        // recursively applies the rubrics by standard by calling apply_rubric
        applyRetroactive: function () {
            // variables to keep track of when the rubric is done being applied
            var total = 0;
            var counter = 0;

            for (var st=0; st < this.list.length; st++) {
                if (this.list[st].length > 0) {
                    applyingRubric = true;
                    total++;
                    var standard = standards.list[st].id;
                    $http({url: '/forms/apply_rubric/',
                        method: 'POST',
                        data: {
                            form: form.id,
                            standards:[standard],
                            rubrics: this.list[st]
                        },
                        headers: {
                        'X-CSRFToken': $cookies.csrftoken,
                                'Content-Type': 'application/json'
                        }
                    }).then(function (response) {
                        counter++;
                        if (counter === total) {
                            location.reload();
                        }
                    });
                }
            }
        },
    }

    // local variable used to separate standardsRubrics into groups for use in button groups
    var standRubricsGroups = [];

    // object holding the local copy of standards as well as helper methods
    // the standards themselves are held at standards.list: 
    // >  standards.list[index]
    var standards = {
        loading: false, // bool to disable add standard buttons
        loaded: false, // used for loading indicator
        list: [
            {
                "title": "Standard 1",
                "order": 1,
                "short_name": "Standard 1",
                "description": "Hi I'm Standard 1"
            },
            {
                "title": "Standard 2",
                "order": 2,
                "short_name": "Standard 2",
                "description": "Hi I'm Standard 2"
            }
        ],
        groups: [], // list to separate standards into groups for buttons
        length: function () {
            return this.list.length;
        },
        add: function () {
            if (standards.loading) {
                return;
            }
            var currentNumber = this.length();
            var new_standard = {
                title: "Standard: New Standard",
                short_name: "New Standard",
                description: "This standard's description.",
                order: currentNumber+1
            };

            standards.loading = true;

            // POST new standard and then save the server's returned copy
            var url = form.url + '/standards/';
            $http.post(url, new_standard).success(function (savedStandard) {
                standards.list.push(savedStandard);
                standards.split(5);
                updateForm();
                standards.loading = false;
            });

            indicators.loaded[currentNumber] = true;

            indicators.list[currentNumber] = [];
            elements.list[currentNumber] = [];
            elements.loaded[currentNumber] = [];
            descriptors.list[currentNumber] = [];
            descriptors.loaded[currentNumber] = [];
            //rubrics.groups[currentNumber] = [];
            standardRubrics.list[currentNumber] = [];
        },
        clearGroups: function () {
            for (var i = 0; i < this.groups.length; i++) {
                this.groups[i] = [];
            }
        },
        delete: function (idx) {
            var url = '/forms/' + form.id + '/standards/' + this.list[idx].id + '/delete_recursive/';
            standards.list[idx].deleting = true;
            $http.get(url).then(function (response) {
                var standardsLeft = response.data;

                descriptors.list.splice(idx, 1);
                elements.list.splice(idx, 1);
                indicators.list.splice(idx, 1);
                standards.list.splice(idx, 1);
                standards.split(5);
                descriptors.split(5);

                standards.list = [];
                for (var i = 0; i < standardsLeft.length; i++) {
                    var standard = standardsLeft[i];
                    standards.list.push(standard);
                }
                standards.split(5);

                if (currentStandard === idx) // change currentStandard if it was our current one
                    currentStandard = 0;
                if (currentStandard === standards.list.length) // deleted a standard while selected last
                    currentStandard--;
            })
        },
        reorder: function () {
            for (var i=0; i < this.length(); i++) {
                var standard = this.list[i];
                var oldOrder = standard.order;
                if (oldOrder !== i+1) { // patch only if different to reduce overhead
                    standard.order = i+1;
                    $http({method: 'PATCH', url: standard.url, data: {order: standard.order}});
                }
            }
        },
        split: function (length) {
            this.clearGroups();
            for (var i=0; i < Math.ceil(this.length()/length); i++) {
                this.groups[i] = [];
                for (var j=0; j < length; j++) {
                    if (this.list[j + (i*length)] !== undefined)
                        this.groups[i].push(this.list[j + (i*length)])
                }
            }
        }
    }

    // object holding the local copy of indicators as well as helper methods
    // the indicators themselves are held at indicators.list
    // > indicators.list[standard][index]
    var indicators = {
        loading:  false, // boolean used to disable add indicator buttons
        loaded: [], // list of boolean variables used for loading sign
        list: [
            [],
            []
        ],
        add: function () {
            if (indicators.loading) {
                return;
            }
            var currentNumber = this.list[currentStandard].length;
            var new_indicator = {
                standard: currentStandard,
                title: "New Indicator Title",
                description: "New indicator description.",
                order: currentNumber+1,
                show: true
            }

            indicators.loading = true;

            var url = standards.list[currentStandard].url + '/indicators/';
            $http.post(url, new_indicator).then(function (response) {
                var savedIndicator = response.data;
                indicators.list[currentStandard].push(savedIndicator);
                updateStandard(currentStandard);

                indicators.loading = false;
            })

            //initialize elements(etc) list
            elements.list[currentStandard][currentNumber] = [];
            elements.loaded[currentStandard][currentNumber] = true;
            descriptors.list[currentStandard][currentNumber] = [];
            descriptors.loaded[currentStandard][currentNumber] = [];
        },
        delete: function (idx, update) {
            this.list[currentStandard][idx].deleting = true;

            var url = '/forms/' + form.id + '/standards/' + standards.list[currentStandard].id 
                + '/indicators/' + indicators.list[currentStandard][idx].id + '/delete_recursive/';
            var thisStandard = currentStandard; // catch this value just in case they change standards

            $http.get(url).then(function (response) {
                var indicatorsLeft = response.data;

                descriptors.list[thisStandard].splice(idx, 1);
                elements.list[thisStandard].splice(idx, 1);
                indicators.list[thisStandard].splice(idx, 1);
                descriptors.split(5);

                indicators.list[thisStandard] = [];
                for (var i = 0; i < indicatorsLeft.length; i++) {
                    var indicator = indicatorsLeft[i];
                    indicators.list[thisStandard].push(indicator);
                }
            });
        },
        reorder: function () {
            for (var i=0; i < this.list[currentStandard].length; i++) {
                var indicator = this.list[currentStandard][i];
                var oldOrder = indicator.order;
                if (oldOrder !== i+1) { // patch only if different to reduce overhead
                    indicator.order = i+1;
                    $http({method: 'PATCH', url: indicator.url, data: {order: indicator.order}});
                }
            }
        },
        // swaps indicators for given standards
        swapForStandard: function (standard, swappedStandard) {
            swapForStandard(this, standard, swappedStandard);
        }
    }

    // object holding the local copy of elements as well as helper methods
    // the elements themselves are held at elements.list
    // > elements.list[standard][indicator][index]
    var elements = {
        loading: [], // boolean to disable add element buttons when saving
        loaded: [], // matrix holding booleans for displaying whether elements are loading
        list: [
            [],
            []
        ],
        add: function (indicator) {
            if (elements.loading[indicator]) {
                return;
            }
            var st = currentStandard;
            var ind = indicator;
            var currentNumber = this.list[st][ind].length;
            var new_element = {
                title: "New Element",
                //assign order default to 1, this is changed when we reorder during the display function
                order: currentNumber+1,
                isMultple: true,
            };

            elements.loading[indicator] = true;

            var url = indicators.list[st][ind].url + '/elements/';
            $http.post(url, new_element).then(function (response) {
                var savedElement = response.data;
                elements.list[currentStandard][indicator].push(savedElement);

                elements.loaded[currentStandard][indicator][currentNumber] = true;
                descriptors.loaded[currentStandard][indicator][currentNumber] = true;

                updateIndicator(currentStandard, indicator);

                elements.loading[indicator] = false;

                descriptors.list[st][ind][currentNumber] = [];

                //if there's a rubric for the form and that's what was chosen, then initialize it
                if (rubricByForm && rubrics.length() > 0) {
                    descriptors.addListForElement(st, ind, currentNumber, rubrics.list);
                }
                //otherwise apply the rubrics by standard
                else if (!rubricByForm && standardRubrics.list[st].length > 0) {
                    descriptors.addListForElement(st, ind, currentNumber, standardRubrics.list[st]);
                }
                descriptors.split(5);
            })

        },
        delete: function (idx, indicator, update) {
            this.list[currentStandard][indicator][idx].deleting = true;

            var url = '/forms/' + form.id + '/standards/' + standards.list[currentStandard].id 
                + '/indicators/' + indicators.list[currentStandard][indicator].id + '/elements/' 
                + elements.list[currentStandard][indicator][idx].id + '/delete_recursive/';
            var thisStandard = currentStandard; // catch this value just in case they change standards

            $http.get(url).then(function (response) {
                var elementsLeft = response.data;

                descriptors.list[thisStandard][indicator].splice(idx, 1);
                elements.list[thisStandard][indicator].splice(idx, 1);
                descriptors.splitList(thisStandard, indicator, idx, 5);

                elements.list[thisStandard][indicator] = [];
                for (var i = 0; i < elementsLeft.length; i++) {
                    var element = elementsLeft[i];
                    elements.list[thisStandard][indicator].push(element);
                }
            });
        },
        reorder: function (indicator) {
            for (var i=0; i < this.list[currentStandard][indicator].length; i++) {
                var element = this.list[currentStandard][indicator][i];

                var oldOrder = element.order;
                if (oldOrder !== i+1) { // patch only if different to reduce overhead
                    element.order = i+1;
                    $http({method: 'PATCH', url: element.url, data: {order: element.order}});
                }
            }
        },
        // swaps elements for given indicators
        swapForIndicator: function (indicator, swappedIndicator) {
            var tempElements = this.list[currentStandard][swappedIndicator];

            this.list[currentStandard][swappedIndicator] = this.list[currentStandard][indicator];
            this.list[currentStandard][indicator] = tempElements;

            splitIndicator(currentStandard, indicator, 5);
            splitIndicator(currentStandard, swappedIndicator, 5);
        },
        // swaps elements for given standards
        swapForStandard: function (standard, swappedStandard) {
            swapForStandard(this, standard, swappedStandard);

            descriptors.split(5);
        },
        // returns the total number of elements across all standards
        total: function () {
            var total = 0;
            for (var st=0; st < this.list.length; st++) {
                for (var ind=0; ind < this.list[st].length; ind++) {
                    for (var elem=0; elem < this.list[st][ind].length; elem++) {
                        total++;
                    }
                }
            }
            return total;
        }
    }

    // object holding the local copy of descriptors as well as helper methods
    // the descriptors themselves are held at descriptors.list
    // > descriptors.list[standard][indicator][element][index]
    var descriptors = {
        loading: false, // bool to disable add descriptor buttons
        loaded: [], // matrix holding booleans for displaying whether descriptors are loading
        list: [
            [],
            []
        ],
        groups: [],
        length: function () {
            return this.list.length;
        },
        totalCount: function () {
            var total = 0;
            for (var st = 0; st < this.list.length; st++) {
                for (var ind = 0; ind < this.list[st].length; ind++) {
                    for (var elem = 0; elem < this.list[st][ind].length; elem++) {
                        for (var desc = 0; desc < this.list[st][ind][elem].length; desc++) {
                            total++;
                        }
                    }
                }
            }
            return total;
        },
        empty: function () {
            this.list = [];
        },
        add: function (indicator, element) {
            if (descriptors.loading) {
                return;
            }
            var st = currentStandard;
            var ind = indicator;
            var elem = element;
            var currentNumber = this.list[st][ind][elem].length;
            var new_descriptor = {
                title: "Descriptor Title",
                descriptor: "Descriptor description.",
                order: currentNumber+1,
                value: currentNumber+1,
            };

            descriptors.loading = true;

            var url = elements.list[st][ind][elem].url + '/descriptors/';
            $http.post(url, new_descriptor).then(function (response) {
                var savedDescriptor = response.data;
                console.log(savedDescriptor);
                descriptors.list[st][ind][elem].push(savedDescriptor);
                descriptors.reorder(st, ind, elem);
                updateElement(st, ind, elem);
                descriptors.splitList(st, ind, elem, 5);

                descriptors.loading = false;

            })

            //this.list[st][ind][elem].push(new_descriptor);
        },
        // makes sure order is maintained on front end (also validates .value field)
        reorder: function (st, ind, elem) {
            var descriptors = this.list[st][ind][elem];
            for (var i=0; i < descriptors.length; i++) {
                descriptors[i].order = i+1;
                descriptors[i].value = parseFloat(descriptors[i].value);
            }
        },
        // adds a list of descriptors for a given element
        addListForElement: function (st, ind, elem, list) {
            var deferred = $q.defer();
            var url = elements.list[st][ind][elem].url + '/descriptors';
            var descriptorsAdded = 0;
            for (var i=0; i < list.length; i++) {
                $http.post(url, list[i]).then(function (response) {
                    var savedDescriptor = response.data;
                    descriptors.list[st][ind][elem].push(savedDescriptor);

                    descriptorsAdded++;
                    if (descriptorsAdded === list.length) {
                        descriptors.list[st][ind][elem].sort(function (a, b) {
                            return a.order - b.order;
                        });
                        descriptors.splitList(st, ind, elem, 5);
                        updateElement(st, ind, elem);
                        deferred.resolve();
                    }
                })
            }

            return deferred.promise;
        },
        delete: function (idx, indicator, element) {
            var st = currentStandard;
            var ind = indicator;
            var elem = element;

            var url = descriptors.list[st][ind][elem][idx].url;
            $http.delete(url, {headers: {
                'X-CSRFToken': $cookies.csrftoken,
                'Content-Type': 'application/json'
            }}).then(function () {
                updateElement(currentStandard, ind, elem);
            });

            this.list[st][indicator][elem].splice(idx,1);
        },
        //splits list into a number of arrays of length, length
        //UNSAFE ASYNC
        split: function (length) {
            for (var st=0; st < this.length(); st++) {
                this.groups[st] = [];
                for (var ind=0; ind < this.list[st].length; ind++) {
                    this.groups[st][ind] = [];
                    var elemLength = this.list[st][ind].length;
                    for (var elem=0; elem < elemLength; elem++) {
                        this.groups[st][ind][elem] = [];
                        var thisDescriptors = this.list[st][ind][elem];
                        var thisGroup = this.groups[st][ind][elem]; //bug here
                        for (var i=0; i < Math.ceil(thisDescriptors.length/length); i++) {
                            thisGroup[i] = [];
                            for (var j=0; j < length; j++) {
                                if (thisDescriptors[j + (i*length)] !== undefined)
                                    thisGroup[i].push(thisDescriptors[j + (i * length)]);
                            }
                        }
                    }
                }
            }
        },
        // same as split except runs on all descriptors under indicator
        splitIndicator: function (st, ind, length) {
            for (var elem = 0; elem < elements.list[st][ind].length; elem++) {
                this.splitList(st, ind, elem, length);
            }
        },
        //same as split excepts works on descriptors for a single element
        splitList: function (st, ind, elem, length) {
            this.groups[st][ind][elem] = [];
            var thisDescriptors = this.list[st][ind][elem];
            if (thisDescriptors === undefined)
                return;
            var thisGroup = this.groups[st][ind][elem]; //bug here
            for (var i=0; i < Math.ceil(thisDescriptors.length/length); i++) {
                thisGroup[i] = [];
                for (var j=0; j < length; j++) {
                    if (thisDescriptors[j + (i*length)] !== undefined)
                        thisGroup[i].push(thisDescriptors[j + (i * length)]);
                }
            }
        },
        // swaps all descriptors between given elements
        swapForElement: function (indicator, element, swappedElement) {
            var tempDescriptors = this.list[currentStandard][indicator][swappedElement];

            this.list[currentStandard][indicator][swappedElement] = this.list[currentStandard][indicator][element];
            this.list[currentStandard][indicator][element] = tempDescriptors;

            this.splitList(currentStandard, indicator, element, 5);
            this.splitList(currentStandard, indicator, swappedElement, 5);
        },
        // swaps all descriptors for given indicators
        swapForIndicator: function (indicator, swappedIndicator) {
            var tempDescriptors = this.list[currentStandard][swappedIndicator];

            this.list[currentStandard][swappedIndicator] = this.list[currentStandard][indicator];
            this.list[currentStandard][indicator] = tempDescriptors;

            this.split(5);
        },
        // swaps all descriptors for given standards
        swapForStandard: function (standard, swappedStandard) {
            swapForStandard(this, standard, swappedStandard);
        }
    }
    /////////////////////////////
    ////// Public API here //////
    /////////////////////////////
    return {
        // Takes the id of the form, requests data from the server and then unpacks it into local data structures
        startup: function (id) {
            forms.getFormById(id).$then(function (response) {
                // Successful form GET
                form = response.data;
                if (form.has_been_used) // Redirect for form integrity
                    window.location = '/404';

                var url = form.url + '/data/';

                $http.get(url).then(function (response) {
                    var formData = response.data;
                    standards.list = formData;

                    standards.loaded = true;
                    standards.split(5);
                    standardRubrics.split(5);

                    for (var i=0; i < standards.list.length; i++) {
                        standardRubrics.list[i] = [];

                        indicators.list[i] = [];
                        elements.list[i] = [];
                        descriptors.list[i] = [];
                        descriptors.groups[i] = [];

                        indicators.loaded[i] = false;
                        elements.loaded[i] = [];
                        descriptors.loaded[i] = [];

                        var getIndicators = function (i) {
                            var loadedIndicators = standards.list[i].indicators;
                            indicators.list[i] = loadedIndicators;
                            indicators.loaded[i] = true;

                            for (var j=0; j < indicators.list[i].length; j++) {

                                elements.list[i][j] = [];
                                descriptors.list[i][j] = [];
                                descriptors.groups[i][j] = [];

                                elements.loaded[i][j] = false;
                                descriptors.loaded[i][j] = [];

                                var getElements = function (j) {
                                    var loadedElements = indicators.list[i][j].elements;
                                    elements.list[i][j] = loadedElements;
                                    elements.loaded[i][j] = true;

                                    for (var k=0; k < elements.list[i][j].length; k++) {
                                        descriptors.list[i][j][k] = [];
                                        descriptors.loaded[i][j][k] = false;
                                        descriptors.groups[i][j][k] = [];

                                        var getDescriptors = function (k) {
                                            var loadedDescriptors = elements.list[i][j][k].descriptors;
                                            descriptors.list[i][j][k] = loadedDescriptors;
                                            descriptors.splitList(i, j, k, 5);
                                            descriptors.loaded[i][j][k] = true;
                                        }
                                        getDescriptors(k);
                                    }
                                }
                                getElements(j);
                            }
                        };
                        getIndicators(i);
                    }
                });
            }, function (response) {
                // error @ form GET
                window.location = '/404';
            });
        },

        form: function () {
            return form;
        },

        // PATCH method for changing attributes of form
        setForm: function (newForm) {
            newForm.name = newForm.name.substring(0,100); //truncate so it's max length
            form = newForm;
            $http({method: 'PATCH', url: form.url, data: form});
        },

        swapOrder: swapOrder,

        applyingRubric: function () {
            return applyingRubric;
        },

        rubricModalIsOpen: function () {
            return rubricModalIsOpen;
        },

        rubricModalOpen: function () {
            rubricModalIsOpen = true;
        },

        rubricModalClose: function () {
            rubricModalIsOpen = false;
        },

        editFormModalOpen: function () {
            editFormModalIsOpen = true;
        },

        editFormModalClose: function () {
            editFormModalIsOpen = false;
        },

        editFormModalIsOpen: function () {
            return editFormModalIsOpen;
        },

        rubricModalPopupIsOpen: function () {
            return rubricModalPopupIsOpen;
        },

        rubricModalPopupOpen: function (rubric) {
            editRubric = rubric;
            rubricModalPopupIsOpen = true;
        },

        rubricModalPopupClose: function () {
            rubricModalPopupIsOpen = false;
        },

        setRubricByForm: function (bool) {
            rubricByForm = bool;
        },

        // Using the temp rubric, editRubric, from the rubric modal, we receive a save command with a bool retroactive from rubric popup
        // if retroactive is true: we recurse through all descriptors and set rubric, otherwise just set rubric
        saveRubric: function (retroactive) {
            if (rubricByForm){
                for (var i = 0; i < editRubric.list.length; i++) {
                    rubrics.list[i] = editRubric.list[i];
                };
            }
            if (retroactive) {
                if (rubricByForm)
                    rubrics.applyRetroactive();
                else
                    standardRubrics.applyRetroactive();
            }
        },

        standards: function () {
            return standards.list;
        },

        standardsLoaded: function () {
            return standards.loaded;
        },

        standardLoading: function () {
            return standards.loading;
        },

        standardGroups: function () {
            return standards.groups;
        },

        indicators: function () {
            return indicators.list;
        },

        indicatorsLoaded: function () {
            return indicators.loaded;
        },

        indicatorLoading: function () {
            return indicators.loading;
        },

        elements: function () {
            return elements.list;
        },

        elementsLoaded: function () {
            return elements.loaded;
        },

        elementLoading: function () {
            return elements.loading;
        },

        descriptors: function () {
            return descriptors.list;
        },

        descriptorsLoaded: function () {
            return descriptors.loaded;
        },

        descriptorLoading: function () {
            return descriptors.loading;
        },

        descriptorGroups: function () {
            return descriptors.groups;
        },

        splitDescriptors: function (standard, indicator, element) {
            descriptors.splitList(standard, indicator, element, 5);
        },

        rubrics: function () {
            return rubrics.list;
        },

        standardRubrics: function () {
            return standardRubrics.list;
        },

        standardRubricsGroups: function () {
            return standardRubrics.groups;
        },

        formTitle: function () {
            return form.title;
        },

        setFormTitle: function (title) {
            form.title = title;
        },

        currentStandard: function () {
            return currentStandard;
        },
        setCurrentStandard: function (standard) {
            currentStandard = standard;
        },

        addStandard: function () {
            standards.add();
            standards.split(5);
        },

        deleteStandard: function (idx) {
            standards.delete(idx);
        },

        // takes reference index (idx) for the standard and a new standard (standard) to update it with
        // changes standard at position: standards.list[idx]
        setStandard: function (idx, standard) {
            var url = standards.list[idx].url;
            $http({method: 'PATCH', url: url, data: standard}).then(function (response) {
                var savedStandard = response.data;
                 standards.list[idx] = savedStandard;
                 standards.split(5);
            });
        },

        // Takes a standard's index and integer upDown
        // if upDown == 1 we move it up (back) in the list, if -1 we move it down (forward)
        moveStandard: function (standard, upDown) {
            if (upDown === 1)
                var swappedStandard = standard - 1;
            else if (upDown === -1)
                var swappedStandard = standard + 1;

            if ((upDown === 1 && standard !== 0) || (upDown === -1 && standard !== standards.list.length-1)) {
                // check edge cases: can't go up if first, can't go down if last
                var temp = standards.list[swappedStandard];

                standards.list[swappedStandard] = standards.list[standard];
                standards.list[standard] = temp;

                swapOrder(standards.list[standard], standards.list[swappedStandard])

                indicators.swapForStandard(standard, swappedStandard);
                elements.swapForStandard(standard, swappedStandard);
                descriptors.swapForStandard(standard, swappedStandard);

                standards.split(5);
                descriptors.split(5);
            }
        },

        addIndicator: function () {
            indicators.add();
        },

        deleteIndicator: function (idx) {
            indicators.delete(idx);
        },

        // takes reference indexes (idx, standard) for the indicator and a new indicator (indicator) to update it with
        // changes indicator at position: indicators.list[standard][idx]
        setIndicator: function (idx, standard, indicator) {
            var url = indicators.list[standard][idx].url;
            $http({method: 'PATCH', url: url, data: indicator}).then(function (response) {
                var savedIndicator = response.data;
                indicators.list[standard][idx] = savedIndicator;
            });
        },

        // Takes a indicators's index and integer upDown
        // if upDown == 1 we move it up (back) in the list, if -1 we move it down (forward)
        moveIndicator: function (indicator, upDown) {
            if (upDown === 1)
                var swappedIndicator = indicator - 1;
            else if (upDown === -1)
                var swappedIndicator = indicator + 1;

            if ((upDown === 1 && indicator !== 0) || (upDown === -1 && indicator !== indicators.list[currentStandard].length-1)) {
                // check edge cases: can't go up if first, can't go down if last
                var temp = indicators.list[currentStandard][swappedIndicator];

                indicators.list[currentStandard][swappedIndicator] = indicators.list[currentStandard][indicator];
                indicators.list[currentStandard][indicator] = temp;

                swapOrder(indicators.list[currentStandard][indicator], indicators.list[currentStandard][swappedIndicator])

                elements.swapForIndicator(indicator, swappedIndicator);
                descriptors.swapForIndicator(indicator, swappedIndicator);
            }
        },

        addElement: function (indicator) {
            elements.add(indicator);
        },

        deleteElement: function (idx, indicator) {
            elements.delete(idx, indicator);
        },

        // takes reference indexes (idx, standard, indicator) for the element and a new element (element) to update it with
        // changes element at position: elements.list[standard][indicator][idx]
        setElement: function (idx, standard, indicator, element) {
            var url = elements.list[standard][indicator][idx].url;
            $http({method: 'PATCH', url: url, data: element}).then(function (response) {
                var savedElement = response.data;
                elements.list[standard][indicator][idx] = savedElement;
                descriptors.splitList(standard, indicator, idx, 5);
            });
        },

        // Takes an element's index and integer upDown
        // if upDown == 1 we move it up (back) in the list, if -1 we move it down (forward)
        moveElement: function (indicator, element, upDown) {
            // takes indexes for indicator and element and then upDown: 1 = up, -1 = down

            if (upDown === 1)
                var swappedElement = element - 1;
            else if (upDown === -1)
                var swappedElement = element + 1;

            if ((upDown === 1 && element !== 0) || (upDown === -1 && element !== elements.list[currentStandard][indicator].length-1)) {
                // check edge cases: can't go up if first, can't go down if last
                var temp = elements.list[currentStandard][indicator][swappedElement];

                elements.list[currentStandard][indicator][swappedElement] = elements.list[currentStandard][indicator][element];
                elements.list[currentStandard][indicator][element] = temp;

                swapOrder(elements.list[currentStandard][indicator][element], elements.list[currentStandard][indicator][swappedElement]);

                descriptors.swapForElement(indicator, element, swappedElement);
            }
        },

        addDescriptor: function (indicator, element) {
            descriptors.add(indicator, element);
            descriptors.split(5);
        },

        deleteDescriptor: function (idx, indicator, element) {
            descriptors.delete(idx, indicator, element);
            descriptors.split(5);
        },

        //deletes all descriptors for a given element
        deleteAllDescriptors: function (indicator, element) {
            var st = currentStandard;
            var ind = indicator;
            var elem = element;
            descriptors.list[st][ind][elem] = [];
            //rubrics.groups[st][ind][elem] = [];
        },

        // takes reference indexes (idx, standard, indicator, element) for the descriptor and a new descritpor (descriptor) to update it with
        // changes descriptor at position: descriptors.list[standard][indicator][element][idx]
        setDescriptor: function (idx, standard, indicator, element, descriptor) {
            var url = descriptors.list[standard][indicator][element][idx].url;
            $http({method: 'PATCH', url: url, data: descriptor}).then(function (response) {
                var savedDescriptor = response.data;
                descriptors.list[standard][indicator][element][idx] = savedDescriptor;
            });
        },

        addRubric: function () {
            rubrics.add();
        },

        deleteRubric: function (idx) {
            rubrics.delete(idx);
        },

        setRubric: function (idx, rubric) {
            rubrics.list[idx] = rubric;
        },

        addStandardRubric: function (st) {
            standardRubrics.add(st);
            standardRubrics.split(5);
        },

        //deletes a single entry in a standard's rubric i.e. standardRubrics[i][j]
        deleteStandardRubric: function (idx, st) {
            standardRubrics.delete(idx, st);
            standardRubrics.split(5);
        },

        //takes a list of descriptors as a rubric and assigns it to the standardRubrics list
        setStandardRubric: function (idx, rubric) {
            standardRubrics.list[idx] = rubric;
        },
    };
});