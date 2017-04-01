'use strict';

demoApp
    .config(['$locationProvider', function ($locationProvider) {
        $locationProvider
            // for suppress hash prefixes in urls
            .hashPrefix('')
            // not use the HTML5 History API
            .html5Mode(false)
        ;
    }])
;
