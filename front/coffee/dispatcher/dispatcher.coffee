myApp = angular.module 'app', ['ngMaterial']
myApp.controller "DispatcherCtrl", ['GetDispatcherData', (GetData) ->
        vm = @        
        vm.newCar = () ->
            vm.car = {}                                        
        vm.delCar = () ->
            GetData.delCar(vm.car.id).then ->
                vm.loadAuto()
                vm.car = {}
        vm.currentCar = (id) ->            
            vm.car = angular.copy(vm.cars[id])            
        vm.loadData = () ->
            GetData.getCars().then (response) ->
                vm.cars = response.data if response.data?           
            GetData.getModels().then (response) ->
                vm.models = response.data if response.data?           
            GetData.getMarks().then (response) ->
                vm.marks = response.data if response.data?           
        vm.saveCar = () ->
            GetData.saveCar(vm.car.id, vm.car).then (response)->
                vm.loadAuto()
                vm.car = response.data if response.data?
                return
        vm.loadData()

        return
    ]   
