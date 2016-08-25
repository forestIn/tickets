angular.module 'app'   
    .factory 'GetDispatcher', [ '$http', ($http) ->        
        api = "/api/v1/cars/"
        getCars: () -> 
            $http.get api+"?format=json"
        saveCar: (idcars, car) ->
            if idcars? then $http.put 'api/v1/cars/'+idcars+'/',car
            else $http.post api,car
        delCar: (idCar) ->
            if idCar? then $http.delete api+idCar+'/' 
    ] 
    .config ['$httpProvider','$locationProvider', ($httpProvider,$locationProvider) ->
        #сконфигурим CSRF
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $locationProvider.html5Mode(true).hashPrefix('!');
    ]