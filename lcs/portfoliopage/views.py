from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.db.models import Q
from .serializers import *
from .models import *
# Create your views here.

class CaseStudyView(APIView):
    def get(self, request, pk=None):
        if not pk:

            case_studies = CaseStudy.objects.all()
            serializer = CaseStudySerializer(case_studies, many=True)
            return Response(serializer.data)
        else:
            case_study=get_object_or_404(CaseStudy,pk=pk)
            serializer = CaseStudySerializer(case_study)
            return Response(serializer.data)


class SearchButtonView(APIView):
    def get(self, request, *args, **kwargs):
        # Get query parameters for search
        search_query = request.query_params.get('search', None)

        if search_query:
            # Use Q objects to filter based on multiple fields
            case_studies = CaseStudy.objects.filter(
                Q(project_name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(tags__icontains=search_query)
            )
            if case_studies.exists():
                # Serialize the filtered results
                serializer = CaseStudySerializer(case_studies, many=True)
                return Response(serializer.data)
            else:
                raise NotFound(detail="No case studies found matching the search query.")
        else:
            # Return all case studies if no search query is provided
            case_studies = CaseStudy.objects.all()
            serializer = CaseStudySerializer(case_studies, many=True)
            return Response(serializer.data)


class IndustriesView(APIView):
    def get(self, request,pk=None):
        if not pk:
            industries = Industries.objects.all()
            serializer = IndustriesSerializer(industries, many=True)
            return Response(serializer.data)
        else:
            industry=get_object_or_404(Industries,pk=pk)
            serializer = IndustriesSerializer(industry)
            return Response(serializer.data)


class JobApplicationListCreateView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    

class JobApplicationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    lookup_field = "pk"