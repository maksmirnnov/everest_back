from rest_framework.serializers import ModelSerializer, DateField, TimeField, DateTimeField
from everest_app.models import Seminar, Lector, SeminarPriceItem


class SeminarSerializer(ModelSerializer):
    date_start = DateField(format='%d.%m.%Y')
    date_end = DateField(format='%d.%m.%Y')
    time_start = TimeField(format='%H:%M')
    time_end = TimeField(format='%H:%M')
    time_create = DateTimeField(format='%d.%m.%Y %H:%M')
    time_update = DateTimeField(format='%d.%m.%Y %H:%M')

    class Meta:
        model = Seminar
        fields = '__all__'
        depth = 2


class LectorSerializer(ModelSerializer):
    class Meta:
        model = Lector
        fields = '__all__'


class SeminarPriceItemSerializer(ModelSerializer):
    class Meta:
        model = SeminarPriceItem
        fields = '__all__'
