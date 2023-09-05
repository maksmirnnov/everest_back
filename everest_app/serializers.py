from rest_framework.serializers import ModelSerializer, DateTimeField
from everest_app.models import Seminar, Lector, Ticket


class SeminarSerializer(ModelSerializer):
    date_start = DateTimeField(format='%d.%m.%Y %H:%M')
    date_end = DateTimeField(format='%d.%m.%Y %H:%M')
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


class TicketSerializer(ModelSerializer):
    time_create = DateTimeField(format='%d.%m.%Y %H:%M', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
