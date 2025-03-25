from django.urls import path
from django.http import HttpResponse
from .views import *



urlpatterns = [ 
    path('doctors/', DoctorAvailabilityAPIView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorAvailabilityAPIView.as_view(), name='doctor-detail'),
    path('doctor/',DoctorSearchView.as_view(),name='doctor'),
]
