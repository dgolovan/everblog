'use strict';

/* Filters */

angular.module('angularFlaskFilters', [])
.filter('uppercase', function() {
	return function(input) {
		return input.toUpperCase();
	}
})
.filter('splittag', function() {
    return function(input) {
      var delimiter = ',';
      
      return input.split(delimiter);
    } 
});