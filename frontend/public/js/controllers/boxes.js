'use strict';

demoApp.controller('boxesController', ['$rootScope', '$scope', 'config',
    function boxesController ($rootScope, $scope, config) {
        $scope.msg = 'Boxes Message';
        $rootScope.pageTitle = config.appName + ' - Boxes';
    }
]);
