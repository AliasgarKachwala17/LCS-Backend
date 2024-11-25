from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ApplicationForm
from .serializers import ApplicationSerializer

class ApplicationView(APIView):
    def get(self, request, *args, **kwargs):
        query_set= ApplicationForm.objects.all()
        serializer = ApplicationSerializer(query_set, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Application submitted successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    