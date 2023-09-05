from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from everest_app.models import Seminar, Lector, Ticket
from everest_app.serializers import SeminarSerializer, LectorSerializer, TicketSerializer


def everest_page(request):
    return render(request, 'everest_app/index.html')


class SeminarViewSet(ModelViewSet):
    queryset = Seminar.objects.all()
    serializer_class = SeminarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description', 'sphere', 'date_start', 'lector', 'seminar_format', 'location', 'price', 'is_actual', 'is_published']


class LectorViewSet(ModelViewSet):
    queryset = Lector.objects.all()
    serializer_class = LectorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'first_name', 'last_name']


class TicketViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
