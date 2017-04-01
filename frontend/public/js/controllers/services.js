'use strict';

demoApp.filter('serviceActive', function () {
	return function (input) {
	    return input == 1;
	};
});

demoApp.controller('servicesController', ['$rootScope', '$scope', '$http', 'config',
    function servicesController ($rootScope, $scope, $http, config) {

        $scope.msg = 'Services Message';
        $rootScope.pageTitle = config.appName + ' - Services';

        var urlPrefix = config.baseApiServerPrefix + 'services/';

        $scope.getData = function () {
            $http.get(urlPrefix).then(
                function successCallback(response) {
                    $scope.servicesTable = {};  // important hack!
                    $scope.services = response.data.services;
                },
                function errorCallback(response) {
                    console.log(response);
                }
            );
        }

        $scope.deleteService = function (id) {
            $http.delete(urlPrefix + id).then(
                function successCallback(response) {
                    $scope.getData();
                },
                function errorCallback(response) {
                    console.log(response);
                    $scope.getData();
                }
            );
        };

        $scope.getData();

    }
]);
