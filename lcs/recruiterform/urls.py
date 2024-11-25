from django.urls import path
from .views import *


urlpatterns = [
    path('Applicationform/', ApplicationView.as_view(), name='ApplicationForm'),
]