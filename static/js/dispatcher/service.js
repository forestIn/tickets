(function() {
  angular.module('app').factory('GetDispatcherData', [
    '$http', function($http) {
      var urlCars, urlMarks, urlModels;
      urlCars = "/api/v1/cars/";
      urlModels = "/api/v1/automodels/";
      urlMarks = "/api/v1/automarks/";
      return {
        getCars: function() {
          return $http.get(urlCars + "?format=json");
        },
        saveCar: function(idcars, car) {
          if (idcars != null) {
            return $http.put(urlCars + idcars + '/', car);
          } else {
            return $http.post(urlCars, car);
          }
        },
        delCar: function(idCar) {
          if (idCar != null) {
            return $http["delete"](urlCars + idCar + '/');
          }
        },
        getModels: function() {
          return $http.get(urlModels + "?format=json");
        },
        getMarks: function() {
          return $http.get(urlMarks + "?format=json");
        }
      };
    }
  ]).config([
    '$httpProvider', '$locationProvider', '$mdThemingProvider', function($httpProvider, $locationProvider, $mdThemingProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      return $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
  ]);

}).call(this);
