from rest_framework import serializers
from .models import *


class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = '__all__'

class IndustriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industries
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'