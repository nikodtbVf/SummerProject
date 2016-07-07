var app = angular.module('fingerprint',[])
.constant('API_URL','http://localhost:8000/face_detection/');

app.controller('indexController', function($scope, $http, API_URL) {
  
   		$scope.showContent = true;
      
/*
        var url = API_URL + "employees";
        
        //append employee id to the URL if the form is in edit mode
        if (modalstate === 'edit'){
            url += "/" + id;
        }
        
        $http({
            method: 'POST',
            url: url,
            data: $.param($scope.employee),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(response) {
            console.log(response);
            location.reload();
        }).error(function(response) {
            console.log(response);
            alert('This is embarassing. An error has occured. Please check the log for details');
        });
   
*/
    $scope.showCredits = function(){
        $scope.showContent = false
    }
    $scope.backToPage = function(){
        $scope.showContent = true;
    }
});
app.directive('navbarSrc',function(){
    return{
        restrict:'E',
        templateUrl: 'source/navbar-src.html'
    }
});

app.directive('contentBody',function(){
    return{
        restrict:'E',
        templateUrl: 'source/content-body.html'
    }
});