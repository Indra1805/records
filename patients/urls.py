from django.urls import path
from .views import PatientAPIView,GetPatientAPIView,PatientUpdateAPIView

urlpatterns = [
    path('create/', PatientAPIView.as_view(), name='patient_api_view'),
    path('patients/', GetPatientAPIView.as_view(), name='patients'),
    path('update/<int:pk>/', PatientUpdateAPIView.as_view(), name='patient-update'),
]


