from django.urls import path
from .views import MedicalRecordAPIView, get_record_fields

urlpatterns = [
    path('medical-records/', MedicalRecordAPIView.as_view(), name='medical-record-list-create'),
    path('medical-records/<int:pk>/', MedicalRecordAPIView.as_view(), name='medical-record-detail'),
    path('record-fields/', get_record_fields, name='record-fields'),
]
