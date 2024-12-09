from django.urls import path
from .views import CaseStudyView, SearchButtonView, IndustriesView, JobApplicationListCreateView, JobApplicationRetrieveUpdateDestroyView

urlpatterns = [
    path('case-studies/', CaseStudyView.as_view(), name='case-studies'),
    path('search-button/', SearchButtonView.as_view(), name='search-button'),
    path('industries/', IndustriesView.as_view(), name='industries'),
    path('job-applications/', JobApplicationListCreateView.as_view(), name='job-application-list-create'),
    path('job-applications/<int:pk>/', JobApplicationRetrieveUpdateDestroyView.as_view(), name='job-application-detail'),
]