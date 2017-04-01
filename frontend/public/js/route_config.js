'use strict';

demoApp
    .config(['$routeProvider', function ($routeProvider) {
        var partialsPath = 'templates/partials/';
        $routeProvider.
            when('/', {
                controller: 'homeController',
                templateUrl: partialsPath + 'home.html',
            }).
            when('/clients/', {
                controller: 'clientsController',
                templateUrl: partialsPath + 'clients.html',
            }).
            when('/suppliers/', {
                controller: 'suppliersController',
                templateUrl: partialsPath + 'suppliers.html',
            }).
            when('/employees/', {
                controller: 'employeesController',
                templateUrl: partialsPath + 'employees.html',
            }).
            when('/plannings/', {
                controller: 'planningsController',
                templateUrl: partialsPath + 'plannings.html',
            }).
            when('/services/', {
                controller: 'servicesController',
                templateUrl: partialsPath + 'services.html',
            }).
            when('/boxes/', {
                controller: 'boxesController',
                templateUrl: partialsPath + 'boxes.html',
            }).
            otherwise({
                redirectTo: '/',
            });
    }])
;
