(function() {
  var myApp;

  myApp = angular.module('app', ['ngMaterial']);

  myApp.controller("DispatcherCtrl", [
    'GetDispatcherData', function(GetData) {
      var vm;
      vm = this;
      vm.car = {
        marks: [],
        models: []
      };
      vm.delCar = function() {
        return GetData.delCar(vm.car.id).then(function() {
          vm.loadAuto();
          return vm.car = {};
        });
      };
      vm.currentCar = function(id) {
        return vm.car = angular.copy(vm.cars[id]);
      };
      vm.loadData = function() {
        return GetData.getCars().then(function(response) {
          if (response.data != null) {
            return vm.cars = response.data;
          }
        });
      };
      vm.loadModels = function() {
        var id, models;
        models = [];
        id = 1;
        return GetData.getModels().then(function(response) {
          if (response.data != null) {
            angular.forEach(response.data, function(el) {
              if (el.marka.id === vm.car.marka) {
                models.push(el);
              }
            });
          }
          return vm.models = models;
        });
      };
      vm.loadMarks = function() {
        return GetData.getMarks().then(function(response) {
          if (response.data != null) {
            vm.marks = response.data;
          }
          return vm.car.models = [];
        });
      };
      vm.saveCar = function() {
        return GetData.saveCar(vm.car.id, vm.car).then(function(response) {
          vm.loadAuto();
          if (response.data != null) {
            vm.car = response.data;
          }
        });
      };
      vm.loadData();
    }
  ]);

}).call(this);
