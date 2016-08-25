myApp = angular.module('app', []);
myApp.controller "DispatcherCtrl", ['GetDispatcher',(GetData) ->
        vm = @        
        vm.status = [
                        { id:'used', name:'Используется'},
                        {id:'to',name:'ТО'},
                        {id:'rmnt',name:'Ремонт'},
                        {id:'dlt',name:'Удалено'}
                    ]
        vm.newCar = () ->
            vm.car = {}                                        
        vm.delCar = () ->
            GetData.delCar(vm.car.id).then ->
                vm.loadAuto()
                vm.car = {}
        vm.currentCar = (id) ->            
            vm.car = angular.copy(vm.cars[id])            
        vm.loadAuto = () ->
            GetData.getCars().then (response) ->
                vm.cars = response.data.results if response.data?           
        vm.saveCar = () ->
            GetData.saveCar(vm.car.id, vm.car).then (response)->
                vm.loadAuto()
                vm.car = response.data if response.data?
                return
        vm.loadAuto()
        # GetData.getRess().then (response) ->
        #     vm.ress = response.data.results if response.data?
        return
    ]   
