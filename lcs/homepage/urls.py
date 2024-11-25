from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('ChooseUs/', ChooseUsView.as_view(), name='ChooseUs'),
    path('Review/', ReviewView.as_view(), name='Review'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
