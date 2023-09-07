from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from tickets_app.models import Ticket, EducationTicket
from tickets_app.serializers import TicketSerializer, EducationTicketSerializer


class TicketViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @action(detail=True, methods=['post'])
    def send_msg(self, request, pk=None):
        msg = EmailMessage(
            'Заявка на семинар',
            f'{request.data}',
            'info@coeverest.ru',
            [f'{User.objects.filter(username="everest_admin")[0].email}'],
        )

        msg.send()

        return HttpResponse('200 OK')

        # user = self.get_object()
        # serializer = PasswordSerializer(data=request.data)
        # if serializer.is_valid():
        #     user.set_password(serializer.validated_data['password'])
        #     user.save()
        #     return Response({'status': 'password set'})
        # else:
        #     return Response(serializer.errors,
        #                     status=status.HTTP_400_BAD_REQUEST)


class EducationTicketViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = EducationTicket.objects.all()
    serializer_class = EducationTicketSerializer

    @action(detail=True, methods=['post'])
    def send_msg(self, request, pk=None):
        msg = EmailMessage(
            'Заявка на корпоративное обучение',
            f'{request.data}',
            'info@coeverest.ru',
            [f'{User.objects.filter(username="everest_admin")[0].email}'],
        )

        msg.send()

        return HttpResponse('200 OK')
