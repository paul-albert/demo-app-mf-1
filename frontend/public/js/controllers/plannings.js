'use strict';

demoApp.controller('planningsController', ['$rootScope', '$scope', 'config',
    function planningsController ($rootScope, $scope, config) {
        $scope.msg = 'Plannings Message';
        $rootScope.pageTitle = config.appName + ' - Plannings';
    }
]);
