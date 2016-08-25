(function() {
  var myApp;

  myApp = angular.module('app', []);

  myApp.controller("DispatcherCtrl", [
    'GetDispatcher', function(GetData) {
      var vm;
      vm = this;
      vm.status = [
        {
          id: 'used',
          name: 'Используется'
        }, {
          id: 'to',
          name: 'ТО'
        }, {
          id: 'rmnt',
          name: 'Ремонт'
        }, {
          id: 'dlt',
          name: 'Удалено'
        }
      ];
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
      vm.loadAuto = function() {
        return GetData.getCars().then(function(response) {
          if (response.data != null) {
            return vm.cars = response.data.results;
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
      vm.loadAuto();
    }
  ]);

}).call(this);
