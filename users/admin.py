from django.contrib import admin

# Register your models here.
from .models import CustomUser, BE
# Register your models here.
# class UserModelAdmin(admin.ModelAdmin):
#     list_display=["__str__","first_name","last_name","department","chief"]
#     list_editable=["chief","department"]
#     class Meta:
#         model = User
# admin.site.register(User,UserModelAdmin)
admin.site.register(CustomUser)
admin.site.register(BE)
