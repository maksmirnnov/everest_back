from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter()

router.register(r'api/seminars', SeminarViewSet)
router.register(r'api/lectors', LectorViewSet)

urlpatterns = [
    path('', everest_page),
    path('feedback/', feedback_view),
]

urlpatterns += router.urls
