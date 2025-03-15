from django.urls import path
from .views import MedicalRecordViewSet, get_record_fields

urlpatterns = [
    path("medical_records/create/", MedicalRecordViewSet.as_view({"post": "create"})),
    path("medical_records/list/", MedicalRecordViewSet.as_view({"get": "list"})),
    path("medical_records/fields/", get_record_fields),
]
