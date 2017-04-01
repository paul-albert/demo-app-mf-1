'use strict';

demoApp.controller('employeesController', ['$rootScope', '$scope', 'config',
    function employeesController ($rootScope, $scope, config) {
        $scope.msg = 'Employees Message';
        $rootScope.pageTitle = config.appName + ' - Employees';
    }
]);
