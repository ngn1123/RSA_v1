var registrationApp = angular.module("registrationApp", []);

registrationApp.factory('onlineRegFactory', function ($http) {
    return {
        addOnlineRegistrations: function (onlineReg, callback) {
            debugger

            function getCookie(name) {
                debugger;
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            
            var csrftoken = getCookie('csrftoken');

            return $http({
			    method: 'POST',
			    url: 'api/register/',
			    data: onlineReg,
			    headers: {
                  'X-CSRFToken': csrftoken
               }
			}).success(callback);
        }
    }
});

registrationApp.controller('OnlineRegistrationController', function ($scope, onlineRegFactory, $location, $anchorScroll) {
    $scope.parent = {};
    $scope.students = [];
    $scope.onlineReg = {};
    $scope.childIndex;
    $scope.capReached = false;
    $scope.registering = false;
    $scope.submitted = false;
    $scope.currentGrade = ['None', 'PK3', 'PK4', 'KG', '1st', '2nd', '3rd', '4th', '5th'];
    $scope.gradeList = ['PK3', 'PK4', 'KG', '1st', '2nd', '3rd', '4th', '5th'];

    $scope.addChild = function () {
        $scope.students.push(
                { first_name: '', middle_name: '', last_name: '', dob: '', gender: '', grade_applying_for: '',
                ethnicity: '', race: '', ethnicRace: '', amerInd: '', asian: '', black: '', hawPacIsl: '', white: '',
                prev_school_name: '', current_grade: '', prev_school_address: '', prev_school_city: '', prev_school_state: '',
                prev_school_zip: '', prev_school_phone: '', prev_school_email: '' }
            )
    }

    if($scope.students.length == 0) {
        $scope.addChild();
    }

    $scope.assignIndex = function (index) {
        $scope.childIndex = index;
    }   

    $scope.removeChild = function () {
        $scope.students.splice($scope.childIndex, 1)
    }

    $scope.addOnlineRegistration = function (isValid) {
        debugger;
        $scope.submitted = true;
        if (isValid) {
            debugger;
            $scope.registering = true;

            angular.forEach($scope.students, function(student) {
                debugger;
                student.race = student.amerInd + student.asian + student.black + student.hawPacIsl + student.white;
                
                if(student.ethnicity == 'H') {
                    student.ethnicRace = student.ethnicity;
                }
                else {
                    student.ethnicRace = student.race;
                }
            });

            $scope.parent.students = $scope.students;
            onlineRegFactory.addOnlineRegistrations($scope.parent, function (data) {
                debugger
                if (data == "true") {
                   window.open('/register/confirm', '_self')
                }
                else {
                   $scope.registering = false;
                   toastr.error("If this error continues, please contact Radiant Stem for assistance.", "Error: Unable to register student")
                }
            });
        }
        else {
            $location.hash('errorMessage');
            $anchorScroll();
        }
    }
});
