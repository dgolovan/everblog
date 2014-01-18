'use strict';

angular.module('evernoteServices', ['ngResource'])
	.factory('Evernote', function($resource) {
		return 	$resource(
					'/api/evernote/:guid', 
					{}, 
					{
						query: {
							method: 'GET',
							params: { guid: '' },
							isArray: true
						},
						get: {
							method: 'GET',
							params: { guid: '' },
							isArray: false
						}
						
					}
				);
});


