from rest_framework import serializers
from .models import Vitals, LabResult,Imaging,Prescription,ServiceProcedure

# serializers for Adding Records

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


# serializers for adding note

from rest_framework import serializers
from .models import (
    NursingNote,
    ProgressNote,
    TreatmentChart,
    PainAssessment,
    InitialAssessment, 
    CarePlanFeedback, 
    RiskFactor1, 
    RiskFactor2, 
    RiskFactor3, 
    RiskFactor4, 
    RiskFactor5
)

class NursingNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NursingNote
        fields = '__all__'


class ProgressNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressNote
        fields = "__all__"

class TreatmentChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentChart
        fields = '__all__'

class PainAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PainAssessment
        fields = '__all__'

class InitialAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialAssessment
        fields = '__all__'

class CarePlanFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarePlanFeedback
        fields = '__all__'

class RiskFactor1Serializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFactor1
        fields = '__all__'

class RiskFactor2Serializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFactor2
        fields = '__all__'

class RiskFactor3Serializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFactor3
        fields = '__all__'

class RiskFactor4Serializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFactor4
        fields = '__all__'

class RiskFactor5Serializer(serializers.ModelSerializer):
    class Meta:
        model = RiskFactor5
        fields = '__all__'
