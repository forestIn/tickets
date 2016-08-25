from django.test import TestCase
from users.models import CustomUser, BE
from dispatcher.models import Cars, AutoModels, AutoMarks

class BaseTestCars(TestCase):

    @classmethod
    def setUpTestData(cls):
        marka = AutoMarks(name='Lexus')
        marka.save()
        model = AutoModels(marka=marka,name='470')
        model.save()
        be = BE(name='Исполнительная дирекция')    
        be.save()
        car = Cars(marka_model_car=model, fedNumber='E220 КМ',be=be)
        car.save()
        disp = CustomUser(username='dispatcher', is_active=True, type_user='DP')
        disp.set_password('123')
        disp.save()
        custom_user = CustomUser(username='custom', is_active=True)
        custom_user.set_password('123')
        custom_user.save()
        
