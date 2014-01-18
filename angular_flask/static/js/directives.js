'use strict';

/* Directives */


angular.module('directive.newlinesConvert', []).
directive('newlinesConvert', function () {
  
  return {
    restrict: 'A',
    link: function(scope, el, attrs){
      scope.$watch('post.body', function(newValue, oldValue){        
        if(scope.post.body){
          scope.post.body = scope.post.body.replace(/<br\s*\/?>/mg,"\n");
        }       
      });
      
    }
  };
});
