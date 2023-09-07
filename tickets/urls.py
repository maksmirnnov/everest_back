from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()

router.register(r'api/request-seminar', TicketViewSet)
router.register(r'api/request-education', EducationTicketViewSet)

urlpatterns = []

urlpatterns += router.urls
