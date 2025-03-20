from django.urls import path
from .views import MedicalRecordAPIView

urlpatterns = [
    path('records/<str:record_type>/', MedicalRecordAPIView.as_view()),
    path('records/<str:record_type>/<int:patient_id>/', MedicalRecordAPIView.as_view()),
    path('records/<str:record_type>/update/<int:record_id>/', MedicalRecordAPIView.as_view()),
]
