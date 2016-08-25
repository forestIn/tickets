from rest_framework import serializers
from .models import Cars, AutoModels, AutoMarks
from users.models import BE, CustomUser

class AutoMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoMarks
        fields = ('__all__')


class AutoModelSerializer(serializers.ModelSerializer):
    marka = AutoMarksSerializer()
    class Meta:
        model = AutoModels
        fields = ('name','marka')


class CarSerializer(serializers.ModelSerializer):
    be = serializers.StringRelatedField()
    marka_model_car = AutoModelSerializer()    
    user = serializers.StringRelatedField()
    class Meta:
        model = Cars
        fields = ('id', 'marka_model_car', 'fedNumber','updated','timestamp','is_active','be','user')
        read_only_fields = ('updated','timestamp',)

