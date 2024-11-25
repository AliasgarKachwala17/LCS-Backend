from django.urls import path
from .views import *


urlpatterns = [
    path('contactform/', ContactUsView.as_view(), name='contact-form'),
]