'use strict';

angular.element(document).ready(function() {
   angular.module('AngularFlask', ['angularFlaskFilters', 'evernoteServices', 'ngSanitize', 'directive.newlinesConvert'])
   	.config(['$routeProvider', '$locationProvider',
			function($routeProvider, $locationProvider) {
				$routeProvider
				.when('/', {
					templateUrl: '/static/partials/landing.html',
					controller: IndexController
				})

				.when('/everblog', {
					templateUrl: '/static/partials/everblog.html',
					controller: EverblogController
				})
				.when('/everpost/:guid', {
					templateUrl: '/static/partials/everpost.html',
					controller: EverblogPostController
				})
				.otherwise({
					redirectTo: '/'
				});

				$locationProvider.html5Mode(true);
			}
	]);
  //Manual bootstrap 	
  angular.bootstrap(document, ['AngularFlask']);
});