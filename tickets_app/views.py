import requests
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from tickets_app.models import Ticket, EducationTicket
from tickets_app.serializers import TicketSerializer, EducationTicketSerializer


class TicketViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        body = self.request.data

        alert = EmailMessage(
            'Заявка на семинар',
            f'{body}',
            'coeverest <info@mail.coeverest.ru>',
            [f'{User.objects.filter(username="everest_dogovor")[0].email}'],
        )
        alert.send()

        if body["email"]:
            req = requests.get(f'https://api.unisender.com/ru/api/subscribe?format=json&api_key=6zijh7kdf7jwmgixh5ib8xf7rtkedig8ow7oubto&list_ids=3,2&fields[email]={body["email"]}&double_optin=0&overwrite=1')

        serializer.save()


class EducationTicketViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = EducationTicket.objects.all()
    serializer_class = EducationTicketSerializer

    def perform_create(self, serializer):
        body = self.request.data

        alert = EmailMessage(
            'Заявка на корпоративное обучение',
            f'{body}',
            'coeverest <info@mail.coeverest.ru>',
            [f'{User.objects.filter(username="everest_dogovor")[0].email}'],
        )
        alert.send()

        if body["email"]:
            req = requests.get(f'https://api.unisender.com/ru/api/subscribe?format=json&api_key=6zijh7kdf7jwmgixh5ib8xf7rtkedig8ow7oubto&list_ids=3,2&fields[email]={body["email"]}&double_optin=0&overwrite=1')

        serializer.save()


# requests.post('https://api.unisender.com/ru/api/subscribe', data={
#     'format': 'json',
#     'api_key': '6zijh7kdf7jwmgixh5ib8xf7rtkedig8ow7oubto',
#     'list_ids': 2,
#     'fields[email]': request.data.get('email'),
#     'double_optin': 0,
#     'overwrite': 0
# })
