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
    permission_classes = []
    authentication_classes = []

    def perform_create(self, serializer):
        # body = self.request.data

        # alert = EmailMessage(
        #     f'Новая заявка на {body.get("price").split("-")[1]} (с сайта)',
        #     f'Семинар: {body.get("seminar")}\n \
        #     Цена, формат: {body.get("price")}\n \
        #     Название организации: {body.get("org_name")}\n \
        #     Юр. адрес: {body.get("ur_address")}\n \
        #     Почтовый адрес: {body.get("mail_address")}\n \
        #     Email: {body.get("email")}\n \
        #     Телефон: {body.get("phone_number")}\n \
        #     ФИО руководителя: {body.get("job_and_supervisor_name")}\n \
        #     Инн: {body.get("inn")}\n \
        #     Кпп: {body.get("kpp")}\n \
        #     Бик: {body.get("bik")}\n \
        #     Расчетный счет: {body.get("check_acc")}\n \
        #     Корр. счёт банка: {body.get("corr_acc")}\n \
        #     Банк: {body.get("bank_name")}\n \
        #     Контактное лицо: {body.get("contact_person")}\n \
        #     Участники: {body.get("participants")}\n \
        #     Комментарий: {body.get("comment")}\n',
        #     'ЦО Эверест <info@mail.coeverest.ru>',
        #     [f'{User.objects.filter(username="everest_dogovor")[0].email}'],
        # )
        # alert.send()

        # if body["email"]:
        #     req = requests.get(f'https://api.unisender.com/ru/api/subscribe?format=json&api_key=6g4bmkakk9yoxy5gjk5ydrggmj4iwhtri65ths6o&list_ids=17890264&fields[email]={body["email"]}&double_optin=0&overwrite=1')

        serializer.save()


class EducationTicketViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = EducationTicket.objects.all()
    serializer_class = EducationTicketSerializer
    permission_classes = []
    authentication_classes = []

    def perform_create(self, serializer):
        # body = self.request.data

        # alert = EmailMessage(
        #     'Заявка на корпоративное обучение',
        #     f'Организация: {body.get("org_name")}\n \
        #     Email: {body.get("email")}\n \
        #     Телефон: {body.get("phone_number")}\n \
        #     Сообщение: {body.get("message")}',
        #     'ЦО Эверест <info@mail.coeverest.ru>',
        #     [f'{User.objects.filter(username="everest_dogovor")[0].email}'],
        # )
        # alert.send()

        # if body["email"]:
        #     req = requests.get(f'https://api.unisender.com/ru/api/subscribe?format=json&api_key=6g4bmkakk9yoxy5gjk5ydrggmj4iwhtri65ths6o&list_ids=17890264&fields[email]={body["email"]}&double_optin=0&overwrite=1')

        serializer.save()
