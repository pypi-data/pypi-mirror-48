(function() {
  angular.module('cradminLegacy.collapse', []).directive('cradminLegacyCollapse', [
    function() {
      /** A box that collapses/expands its content automatically when the header is clicked.
      
      Example
      =======
      
      ```html
      <div cradmin-legacy-collapse>
        <button ng-click="toggleContentVisible()" type="button">
          <span ng-if="contentHidden">Show</span>
          <span ng-if="!contentHidden">Hide</span>
        </button>
        <div ng-class="{'ng-hide': contentHidden}">
          Something here
        </div>
      </div>
      ```
      
      You can make it visible by default using ``initial-state="visible"``:
      
      ```html
      <div cradmin-legacy-collapse initial-state="visible">
        ...
      </div>
      ```
      
      If you want to avoid the initial flicker before the directive
      hides the content, add the ``ng-hide`` css class to the content div:
      
      ```html
      <div cradmin-legacy-collapse>
        <button ng-click="toggleContentVisible()" type="button">
          ...
        </button>
        <div ng-class="{'ng-hide': contentHidden}" ng-class="ng-hide">
          Something here
        </div>
      </div>
      ```
      */

      return {
        scope: true,
        controller: function($scope) {
          $scope.contentHidden = true;
          $scope.toggleContentVisible = function() {
            return $scope.contentHidden = !$scope.contentHidden;
          };
        },
        link: function($scope, $element, attrs) {
          return $scope.contentHidden = attrs.initialState !== 'visible';
        }
      };
    }
  ]);

}).call(this);
