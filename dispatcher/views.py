from django.views.generic import TemplateView
from braces.views import LoginRequiredMixin


from users.mixins import DispatcherMixin

class DispatcherView(LoginRequiredMixin, DispatcherMixin, TemplateView):
    template_name = "dispatcher/dispatcher.html"


from .models import Cars, AutoModels, AutoMarks
from .serializers import CarSerializer, AutoModelSerializer, AutoMarksSerializer
from rest_framework import viewsets, mixins, permissions
from users.permissions import IsDispatcher


class AutoMarksViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, IsDispatcher,)
    
    queryset = AutoMarks.objects.all()
    serializer_class = AutoMarksSerializer



class AutoModelsViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, IsDispatcher,)
    
    queryset = AutoModels.objects.all()
    serializer_class = AutoModelSerializer


class CarsViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated, IsDispatcher,)
    
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


