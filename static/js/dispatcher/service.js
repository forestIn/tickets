(function() {
  angular.module('app').factory('GetDispatcher', [
    '$http', function($http) {
      var api;
      api = "/api/v1/cars/";
      return {
        getCars: function() {
          return $http.get(api + "?format=json");
        },
        saveCar: function(idcars, car) {
          if (idcars != null) {
            return $http.put('api/v1/cars/' + idcars + '/', car);
          } else {
            return $http.post(api, car);
          }
        },
        delCar: function(idCar) {
          if (idCar != null) {
            return $http["delete"]('api/v1/cars/' + idCar + '/');
          }
        }
      };
    }
  ]).config([
    '$httpProvider', '$locationProvider', function($httpProvider, $locationProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
      return $locationProvider.html5Mode(true).hashPrefix('!');
    }
  ]);

}).call(this);
