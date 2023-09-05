from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *


router = SimpleRouter()

router.register(r'api/seminars', SeminarViewSet)
router.register(r'api/lectors', LectorViewSet)
router.register(r'api/request-seminar', TicketViewSet)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', everest_page)
]

urlpatterns += router.urls
