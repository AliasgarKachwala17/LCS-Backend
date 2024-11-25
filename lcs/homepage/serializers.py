from rest_framework import serializers
from .models import *

class ChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChooseUs
        fields ='__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields ='__all__'