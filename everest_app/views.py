from django.contrib.auth.models import User
import requests
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from everest_app.models import Seminar, Lector, SeminarPriceItem
from everest_app.serializers import SeminarSerializer, LectorSerializer, SeminarPriceItemSerializer


def everest_page(request):
    return render(request, 'everest_app/index.html')


class SeminarViewSet(ModelViewSet):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    filterset_fields = ['title', 'description', 'sphere', 'date_start', 'lector', 'seminar_format', 'location_city',
                        'location_place', 'is_actual', 'is_published']


class LectorViewSet(ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'first_name', 'last_name', 'is_published']


class SeminarPriceItemViewSet(ModelViewSet):
    queryset = SeminarPriceItem.objects.all()
    serializer_class = SeminarPriceItemSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    filterset_fields = ['seminar', 'title', 'price']


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def feedback_view(request):
    alert = EmailMessage(
        'Обратная связь',
        f'Имя: {request.data.get("name")}\n \
            Email: {request.data.get("email")}\n\n \
            Сообщение: {request.data.get("message")}',
        'ЦО Эверест <info@mail.coeverest.ru>',
        [f'{User.objects.filter(username="everest_info")[0].email}'],
    )
    alert.send()
    requests.get(f'https://api.unisender.com/ru/api/subscribe?format=json&api_key'
                 f'=6g4bmkakk9yoxy5gjk5ydrggmj4iwhtri65ths6o&list_ids=17890264&fields[email]={request.data.get(
                     "email")}&double_optin=0&overwrite=1')

    return HttpResponse('200 OK')
