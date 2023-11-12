from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from everest_app.models import Seminar, Lector, SeminarPriceItem
from everest_app.serializers import SeminarSerializer, LectorSerializer, SeminarPriceItemSerializer


def everest_page(request):
    return render(request, 'everest_app/index.html')


class SeminarViewSet(ModelViewSet):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description', 'sphere', 'date_start', 'lector', 'seminar_format', 'location_city', 'location_place', 'is_actual', 'is_published']


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
    filterset_fields = ['seminar', 'title', 'price']


@api_view(['POST'])
def feedback_view(request):
    alert = EmailMessage(
        'Обратная связь',
        f'Имя: {request.data.get("name")}\nEmail: {request.data.get("email")}\n\nСообщение: {request.data.get("message")}',
        'info@mail.coeverest.ru',
        [f'{User.objects.filter(username="everest_info")[0].email}'],
    )
    alert.send()

    return HttpResponse('200 OK')
