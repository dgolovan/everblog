'use strict';

function MenuController($scope, $location) 
{ 
    $scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };
}

function IndexController($scope) {
	
}

function EverblogController($scope, Evernote){
  $scope.notes = Evernote.query();
}

function EverblogPostController($scope, $routeParams, Evernote){
  var guid = $routeParams.guid;
  $scope.note = Evernote.get({ guid: guid });
}
