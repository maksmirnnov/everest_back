from rest_framework.serializers import ModelSerializer, DateTimeField
from tickets_app.models import Ticket, EducationTicket


class TicketSerializer(ModelSerializer):
    time_create = DateTimeField(format='%d.%m.%Y %H:%M', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class EducationTicketSerializer(ModelSerializer):
    time_create = DateTimeField(format='%d.%m.%Y %H:%M', read_only=True)

    class Meta:
        model = EducationTicket
        fields = '__all__'
