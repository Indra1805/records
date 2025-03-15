from rest_framework import serializers
from .models import Vitals, LabResult,Imaging,Prescription,ServiceProcedure

class VitalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitals
        fields = '__all__'

class LabResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResult
        fields = '__all__'

class ImagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imaging
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class ServiceProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProcedure
        fields = '__all__'

def get_serializer_class(record_type):
    serializer_mapping = {
        "vitals": VitalsSerializer,
        "lab_results": LabResultSerializer,
        "imaging":ImagingSerializer,
        "prescription":PrescriptionSerializer,
        "serviceprocedure":ServiceProcedureSerializer
    }
    return serializer_mapping.get(record_type)