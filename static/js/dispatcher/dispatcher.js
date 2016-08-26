(function() {
  var myApp;

  myApp = angular.module('app', ['ngMaterial']);

  myApp.controller("DispatcherCtrl", [
    'GetDispatcherData', function(GetData) {
      var vm;
      vm = this;
      vm.newCar = function() {
        return vm.car = {};
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
        GetData.getCars().then(function(response) {
          if (response.data != null) {
            return vm.cars = response.data;
          }
        });
        GetData.getModels().then(function(response) {
          if (response.data != null) {
            return vm.models = response.data;
          }
        });
        return GetData.getMarks().then(function(response) {
          if (response.data != null) {
            return vm.marks = response.data;
          }
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
