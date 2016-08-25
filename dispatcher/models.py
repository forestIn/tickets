from django.db import models
from django.conf import settings

from users.models import BE

class AutoMarks(models.Model):
    name = models.CharField("Марка автомобиля", max_length=50)

    def __str__(self):
        return self.name


class AutoModels(models.Model):
    name = models.CharField("Модель автомобиля", max_length=50)
    marka = models.ForeignKey(AutoMarks)

    def __str__(self):
        return self.marka.name + ' ' +self.name


class Cars(models.Model):
    be = models.ForeignKey(BE, verbose_name='Расположение', null=True, related_name='res')
    marka_model_car = models.ForeignKey(AutoModels,verbose_name='марка-модель')
    fedNumber = models.CharField("Гос.номер автомобиля", max_length=50)    
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,verbose_name = "Ответственный за авто", null=True,blank=True, on_delete=models.SET_NULL, related_name='owner') 
    is_active = models.BooleanField("Активный", default=True)
    
    def __str__(self):
        return self.marka_model_car.__str__()+" "+self.fedNumber

