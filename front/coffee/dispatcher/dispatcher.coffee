myApp = angular.module 'app', ['ngMaterial']
myApp.controller "DispatcherCtrl", ['GetDispatcherData', (GetData) ->
        vm = @ 
        vm.car = {
            marks:[]
            models:[]
        }
        vm.delCar = () ->
            GetData.delCar(vm.car.id).then ->
                vm.loadAuto()
                vm.car = {}
        vm.currentCar = (id) ->            
            vm.car = angular.copy(vm.cars[id])            
        vm.loadData = () ->
            GetData.getCars().then (response) ->
                vm.cars = response.data if response.data?           
        vm.loadModels = () ->
            models = []
            id=1
            GetData.getModels().then (response) ->
                if response.data?
                    angular.forEach response.data, (el)->
                            models.push(el) if el.marka.id is vm.car.marka
                            return
                vm.models = models
        vm.loadMarks = () ->        
            GetData.getMarks().then (response) ->
                vm.marks = response.data if response.data?           
                vm.car.models = [] 
        vm.saveCar = () ->
            GetData.saveCar(vm.car.id, vm.car).then (response)->
                vm.loadAuto()
                vm.car = response.data if response.data?
                return
        vm.loadData()

        return
    ]   
