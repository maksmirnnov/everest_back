from django.urls import path, re_path
from rest_framework.routers import SimpleRouter
from .views import *


router = SimpleRouter()

router.register(r'api/seminars', SeminarViewSet)
router.register(r'api/lectors', LectorViewSet)
router.register(r'api/prices', SeminarPriceItemViewSet)

urlpatterns = [
    path('', everest_page),
    path('feedback/', feedback_view),
    path('seminars/', everest_page),
    re_path(r'^seminars\/[\w\d\-_]+\/$', everest_page),
    path('lectors/', everest_page),
    re_path(r'^lectors\/[\w\d\-_]+\/$', everest_page),
    path('education/', everest_page),
    path('feedback/', feedback_view),
]

urlpatterns += router.urls
