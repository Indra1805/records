from rest_framework import serializers
from .models import Vitals, LabResult,Imaging,Prescription,ServiceProcedure
from patients.models import Patient
from .models import NursingNotes,ProgressNote,TreatmentChart, PainAssessment,InitialAssessment,CarePlanFeedback,RiskFactor1,RiskFactor2,RiskFactor3,RiskFactor4,RiskFactor5
from .validators import validate_character_of_service,validate_factors_improving_experience,RiskFactor1Validator,RiskFactor2Validator,RiskFactor3Validator,RiskFactor4Validator,RiskFactor5Validator


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


# Nursing Notes
class NursingNotesSerializer(serializers.ModelSerializer):
    patient = serializers.CharField(source='patient.patient_id')

    class Meta:
        model = NursingNotes
        fields = '__all__'


# Progress Notes

class ProgressNoteSerializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.patient_id', read_only=True)

    class Meta:
        model = ProgressNote
        fields = ['patient_id', 'status', 'created_at', 'updated_at', 'patient']
        extra_kwargs = {
            'patient': {'write_only': True}
        }

# Treatment Chart
class TreatmentChartSerializer(serializers.ModelSerializer):
    patient = serializers.CharField(source='patient.patient_id')
    class Meta:
        model = TreatmentChart
        fields = '__all__'


# Pain Assessment

class PainAssessmentSerializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.patient_id', read_only=True)
    character_of_service = serializers.ListField(child=serializers.CharField(), validators=[validate_character_of_service])
    factors_improving_experience = serializers.ListField(child=serializers.CharField(), validators=[validate_factors_improving_experience])

    class Meta:
        model = PainAssessment
        fields = [
            'patient_id', 'pain_intensity', 'location_of_service', 
            'quality_of_service', 'character_of_service', 
            'factors_affecting_rating', 'factors_improving_experience',
            'created_at', 'updated_at', 'patient'
        ]
        extra_kwargs = {
            'patient': {'write_only': True},
        }

# Initial Assessment
class InitialAssessmentSerializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.patient_id', read_only=True)

    class Meta:
        model = InitialAssessment
        fields = ['patient_id', 'rating_title', 'relationship_to_feedback', 'feedback_date','duration_of_experience','present_illness','past_illness','experience_feedback','health_feedback','hart_feedback','stroke_feedback','other_feedback', 'patient']
        extra_kwargs = {
            'patient': {'write_only': True}
        }

# Careplan Feedback

class CarePlanFeedbackSerializer(serializers.ModelSerializer):
    patient = serializers.CharField(source='patient.patient_id')
    class Meta:
        model = CarePlanFeedback
        fields = '__all__'


# Risk Assessment

# Common function to calculate total_score
def calculate_total_score(data, boolean_fields):
    return sum(data.get(field, False) for field in boolean_fields)

# RiskFactor1 Serializer
class RiskFactor1Serializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.patient_id', read_only=True)
    surgery = serializers.BooleanField(required=False)
    postpartum_feedback = serializers.BooleanField(required=False)
    contraceptive_feedback = serializers.BooleanField(required=False)
    age_feedback = serializers.BooleanField(required=False)
    condition_feedback = serializers.BooleanField(required=False)
    obesity = serializers.BooleanField(required=False)
    total_score = serializers.SerializerMethodField()


    class Meta:
        model = RiskFactor1
        fields = '__all__'

        extra_kwargs = {
            'patient': {'write_only': True}
        }

    def get_total_score(self, obj):
        boolean_fields = ['surgery', 'postpartum_feedback', 'contraceptive_feedback', 'age_feedback', 'condition_feedback', 'obesity']
        data = {field: getattr(obj, field) for field in boolean_fields}
        return calculate_total_score(data, boolean_fields)

# RiskFactor2 Serializer
class RiskFactor2Serializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.patient_id', read_only=True)
    surgery = serializers.BooleanField(required=False)
    postpartum_feedback = serializers.BooleanField(required=False)
    contraceptive_feedback = serializers.BooleanField(required=False)
    age_feedback = serializers.BooleanField(required=False)
    condition_feedback = serializers.BooleanField(required=False)
    obesity = serializers.BooleanField(required=False)
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = RiskFactor2
        fields = '__all__'

        extra_kwargs = {
            'patient': {'write_only': True}
        }

    def get_total_score(self, obj):
        boolean_fields = ['surgery', 'postpartum_feedback', 'contraceptive_feedback', 'age_feedback', 'condition_feedback', 'obesity']
        data = {field: getattr(obj, field) for field in boolean_fields}
        return calculate_total_score(data, boolean_fields)

# RiskFactor3 Serializer
class RiskFactor3Serializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.patient_id', read_only=True)
    age_feedback = serializers.BooleanField(required=False)
    surgery_feedback = serializers.BooleanField(required=False)
    surgical_feedback = serializers.BooleanField(required=False)
    access_feedback = serializers.BooleanField(required=False)
    health_condition_feedback = serializers.BooleanField(required=False)
    feedback_on_condition = serializers.BooleanField(required=False)
    bedridden_feedback = serializers.BooleanField(required=False)
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = RiskFactor3
        fields = '__all__'

        extra_kwargs = {
            'patient': {'write_only': True}
        }

    def get_total_score(self, obj):
        boolean_fields = ['age_feedback', 'surgery_feedback', 'surgical_feedback', 'access_feedback',
                           'health_condition_feedback', 'feedback_on_condition', 'bedridden_feedback']
        data = {field: getattr(obj, field) for field in boolean_fields}
        return calculate_total_score(data, boolean_fields)

# RiskFactor4 Serializer
class RiskFactor4Serializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.patient_id', read_only=True)
    history_of_feedback = serializers.BooleanField(required=False)
    heart_failure_feedback = serializers.BooleanField(required=False)
    resistance_feedback = serializers.BooleanField(required=False)
    deficiency_feedback = serializers.BooleanField(required=False)
    health_condition_feedback = serializers.BooleanField(required=False)
    condition_feedback = serializers.BooleanField(required=False)
    thrombocytopenia_feedback = serializers.BooleanField(required=False)
    heart_feedback = serializers.BooleanField(required=False)
    infection_feedback = serializers.BooleanField(required=False)
    mutation_feedback = serializers.BooleanField(required=False)
    antibody_feedback = serializers.BooleanField(required=False)
    disorder_feedback = serializers.BooleanField(required=False)
    syndrome_feedback = serializers.BooleanField(required=False)
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = RiskFactor4
        fields = '__all__'

        extra_kwargs = {
            'patient': {'write_only': True}
        }

    def get_total_score(self, obj):
        boolean_fields = ['history_of_feedback', 'heart_failure_feedback', 'resistance_feedback',
                           'deficiency_feedback', 'health_condition_feedback', 'condition_feedback',
                           'thrombocytopenia_feedback', 'heart_feedback', 'infection_feedback',
                           'mutation_feedback', 'antibody_feedback', 'disorder_feedback', 'syndrome_feedback']
        data = {field: getattr(obj, field) for field in boolean_fields}
        return calculate_total_score(data, boolean_fields)

# RiskFactor5 Serializer
class RiskFactor5Serializer(serializers.ModelSerializer):
    patient_id = serializers.CharField(source='patient.patient_id', read_only=True)
    elective_surgery_feedback = serializers.BooleanField(required=False)
    fracture_feedback = serializers.BooleanField(required=False)
    trauma_feedback = serializers.BooleanField(required=False)
    surgery_feedback = serializers.BooleanField(required=False)
    stroke_feedback = serializers.BooleanField(required=False)
    injury_feedback = serializers.BooleanField(required=False)
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = RiskFactor5
        fields = '__all__'

        extra_kwargs = {
            'patient': {'write_only': True}
        }

    def get_total_score(self, obj):
        boolean_fields = ['elective_surgery_feedback', 'fracture_feedback', 'trauma_feedback',
                           'surgery_feedback', 'stroke_feedback', 'injury_feedback']
        data = {field: getattr(obj, field) for field in boolean_fields}
        return calculate_total_score(data, boolean_fields)
