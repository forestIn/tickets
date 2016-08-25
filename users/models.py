from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser


class BE(models.Model):
    name = models.CharField("Расположение", max_length=120)
    
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):    
    USER = 'US'
    DISPATCHER = 'DP'

    TYPE_USER = (
        (USER, 'Пользователь'),
        (DISPATCHER, 'Диспетчер'),
    )
    curator= models.BooleanField("заведующий", default=False)
    department= models.CharField("подразделение", blank=True, max_length=255)
    position= models.CharField("должность", blank=True, max_length=255)
    phone= models.CharField("телефон", blank=True, max_length=40)
    chief = models.ForeignKey('self',verbose_name = "Руководитель", null=True, on_delete=models.SET_NULL, related_name='+', blank=True)
    type_user = models.CharField(max_length=2, choices=TYPE_USER, default=USER)
    be = models.ForeignKey(BE, verbose_name='Расположение', null=True)


    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})