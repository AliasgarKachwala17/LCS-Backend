from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.
class ChooseUsView(APIView):
    def get(self, request):
        query_set= ChooseUs.objects.all()
        print(query_set,"------------------")
        serializer = ChooseUsSerializer(query_set, many=True)
        return Response(serializer.data)


    def post(self, request):
        
        serializer = ChooseUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View for Review
class ReviewView(APIView):
    def get(self, request):
        query_set= Review.objects.all()
        serializer = ReviewSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)