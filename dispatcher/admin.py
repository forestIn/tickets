from django.contrib import admin

from .models import Cars, AutoModels, AutoMarks

admin.site.register(Cars)
admin.site.register(AutoModels)
admin.site.register(AutoMarks)