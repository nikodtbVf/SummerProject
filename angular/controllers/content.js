app.controller('contentController', function($scope, $http, API_URL) {
	
    $scope.giveUrl = true;
    $scope.formPerson = false;
	$scope.image = {};
    $scope.person = {};
	$scope.lastUrl = "nothing"
    $scope.showInfo = false
    $scope.showMessage = false;
    $scope.infoPerson = false
    
    $scope.saveFake = function() {
        $scope.infoPerson = false;
        $scope.person = {}
        $scope.lastUrl = $scope.image.name
        var url = API_URL + "detect/" 
 		$http({
            method: 'POST',
            url: url,
            data:$.param({ url : $scope.image.name }),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(response) {
          
        }).error(function(response) {
            console.log(response)
        });  
	}

    $scope.saveImage = function() {
        $scope.infoPerson = false;
        $scope.person = {}
        $scope.lastUrl = $scope.image.name
        console.log($scope.image.name)
        var url = API_URL + "image/" 
        $http({
            method: 'POST',
            url: url,
            data:$.param({ url : $scope.image.name}),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(response) {
             
             if(response.success)
                if(response["matching"]){
                    var id = parseInt(response.id)
                    $scope.showData(id);
                }   
                else{
                    $scope.formPerson = true;
                    $scope.giveUrl = false;
                }
        }).error(function(response) {
            console.log(response)
        });  
    }            
   
    $scope.showData = function(idP){
        $scope.showInfo = true  
        var url = API_URL + "getInfo/"
        $http({
            method: 'POST',
            url: url,
            data:$.param({ id : idP}),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(response) {
            console.log(response)
            $scope.putData(response);
            $scope.infoPerson = true;
        }).error(function(response) {
           
        });  
    }

    this.savePerson = function() {
        
        var url = API_URL + "addPerson/"

        $http({
            method: 'POST',
            url: url,
            data: $.param({ 
                           name:  $scope.person.name,
                           last_name: $scope.person.last_name,
                           work: $scope.person.work,    
                           cellphone: $scope.person.cellphone,
                           street: $scope.person.street,
                           number_house: $scope.person.number_house,
                           colony: $scope.person.colony,
                           postalcode: $scope.person.postalcode,
                           municipality: $scope.person.municipality,
                           state: $scope.person.state,
                           urlimage : $scope.lastUrl 
                        }),
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        }).success(function(response) { 
           $scope.showMessage = true;
           $scope.message = response.message;
           $scope.formPerson = false;
        }).error(function(response) {
            console.log(response)
        }); 
    }

    $scope.putData = function(response){
        $scope.person.name = response.name
        $scope.person.last_name = response.last_name
        $scope.person.work = response.work
        $scope.person.cellphone = response.cellphone
        $scope.person.street = response.street
        $scope.person.number_house = response.number_house
        $scope.person.colony = response.colony
        $scope.person.postalcode = response.postalcode
        $scope.person.municipality = response.municipality
        $scope.person.state = response.state
    }

    $scope.changeStateAlert = function(){
        $scope.showMessage = !($scope.showMessage)
        $scope.giveUrl = true;
    }

});

app.directive('formUrl',function(){
	return{
		restrict: 'E',
		templateUrl: 'source/form-url.html'
	}
});

app.directive('formPerson',function(){
    return{
        restrict: 'E',
        templateUrl: 'source/form-person.html'
    }
});