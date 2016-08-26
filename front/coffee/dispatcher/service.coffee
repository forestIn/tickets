angular.module 'app'  
    .factory 'GetDispatcherData', [ '$http', ($http) ->        
        urlCars = "/api/v1/cars/"
        urlModels = "/api/v1/automodels/"
        urlMarks = "/api/v1/automarks/"

        getCars: () -> 
            $http.get urlCars+"?format=json"              
        saveCar: (idcars, car) ->
            if idcars? then $http.put urlCars+idcars+'/',car
            else $http.post urlCars,car
        delCar: (idCar) ->
            if idCar? then $http.delete urlCars+idCar+'/' 
        getModels: () -> 
            $http.get urlModels+"?format=json"           
        getMarks: () -> 
            $http.get urlMarks+"?format=json"              

    ] 
    .config ['$httpProvider','$locationProvider', ($httpProvider,$locationProvider) ->
        #сконфигурим CSRF
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        # $locationProvider.html5Mode(true).hashPrefix('!');
    ]

