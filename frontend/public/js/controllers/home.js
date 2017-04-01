'use strict';

demoApp.controller('homeController', ['$rootScope', '$scope', 'config',
    function homeController ($rootScope, $scope, config) {
        //console.log(config);
        //console.log('App Name', config.appName);
        //console.log('App Name', config.appVersion);
        $scope.msg = 'Home Message';
        $rootScope.pageTitle = config.appName + ' - Home';
    }
]);
