'use strict';

demoApp.controller('suppliersController', ['$rootScope', '$scope', 'config',
    function suppliersController ($rootScope, $scope, config) {
        $scope.msg = 'Suppliers Message';
        $rootScope.pageTitle = config.appName + ' - Suppliers';
    }
]);
