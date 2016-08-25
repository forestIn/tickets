from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from dispatcher.views import CarsViewSet, AutoModelsViewSet, AutoMarksViewSet

router = DefaultRouter()
router.register(r'automarks', AutoMarksViewSet)
router.register(r'automodels', AutoModelsViewSet)
router.register(r'cars', CarsViewSet)



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^api/v1/', include(router.urls)), 
    url(r'^dispatcher/', include('dispatcher.urls', namespace="dispatcher")),
    url(r'^admin/', admin.site.urls),   
]
