from rest_framework import serializers

class VitalsValidator(serializers.Serializer):
    blood_pressure = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=7, error_messages={
        "required": "Blood pressure is a required field.",
        "null": "Blood pressure cannot be null.",
        "blank": "Blood pressure cannot be empty.",
        "max_length": "Blood pressure cannot exceed 7 characters."
    })

    bmi = serializers.FloatField(required=True, error_messages={
        "required": "BMI is a required field.",
        "invalid": "Invalid BMI value."
    })

    grbs = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=50, error_messages={
        "required": "GRBS is a required field.",
        "null": "GRBS cannot be null.",
        "blank": "GRBS cannot be empty.",
        "max_length": "GRBS cannot exceed 50 characters."
    })

    respiratory_rate = serializers.IntegerField(required=True, error_messages={
        "required": "Respiratory rate is a required field.",
        "invalid": "Invalid respiratory rate value."
    })

    weight = serializers.FloatField(required=True, error_messages={
        "required": "Weight is a required field.",
        "invalid": "Invalid weight value."
    })

    height = serializers.FloatField(required=True, error_messages={
        "required": "Height is a required field.",
        "invalid": "Invalid height value."
    })


class LabResultValidator(serializers.Serializer):
    hemoglobin = serializers.FloatField(required=True, error_messages={
        "required": "Hemoglobin is a required field.",
        "invalid": "Invalid hemoglobin value."
    })

    white_blood_cells = serializers.FloatField(required=True, error_messages={
        "required": "White blood cells count is a required field.",
        "invalid": "Invalid white blood cells count value."
    })

    platelets = serializers.FloatField(required=True, error_messages={
        "required": "Platelet count is a required field.",
        "invalid": "Invalid platelet count value."
    })

    test_name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=255, error_messages={
        "required": "Test name is a required field.",
        "null": "Test name cannot be null.",
        "blank": "Test name cannot be empty.",
        "max_length": "Test name cannot exceed 255 characters."
    })

    result_value = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=255, error_messages={
        "required": "Result value is a required field.",
        "null": "Result value cannot be null.",
        "blank": "Result value cannot be empty.",
        "max_length": "Result value cannot exceed 255 characters."
    })


class ImagingValidator(serializers.Serializer):
    scan_type = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=100, error_messages={
        "required": "Scan type is a required field.",
        "null": "Scan type cannot be null.",
        "blank": "Scan type cannot be empty.",
        "max_length": "Scan type cannot exceed 100 characters."
    })


class PrescriptionValidator(serializers.Serializer):
    medication_name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=100, error_messages={
        "required": "Medication name is a required field.",
        "null": "Medication name cannot be null.",
        "blank": "Medication name cannot be empty.",
        "max_length": "Medication name cannot exceed 100 characters."
    })

    dosage = serializers.CharField(required=True, max_length=50, error_messages={
        "required": "Dosage is a required field.",
        "max_length": "Dosage cannot exceed 50 characters."
    })

    frequency = serializers.CharField(required=True, max_length=50, error_messages={
        "required": "Frequency is a required field.",
        "max_length": "Frequency cannot exceed 50 characters."
    })

    duration = serializers.CharField(required=True, max_length=50, error_messages={
        "required": "Duration is a required field.",
        "max_length": "Duration cannot exceed 50 characters."
    })


class ServiceProcedureValidator(serializers.Serializer):
    procedure_name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=100, error_messages={
        "required": "Procedure name is a required field.",
        "null": "Procedure name cannot be null.",
        "blank": "Procedure name cannot be empty.",
        "max_length": "Procedure name cannot exceed 100 characters."
    })

    procedure_notes = serializers.CharField(required=True, error_messages={
        "required": "Procedure notes are a required field."
    })


from rest_framework import serializers

# Nursing Note Validator
class NursingNoteValidator(serializers.Serializer):
    description = serializers.CharField(required=True, allow_blank=False, error_messages={
        "required": "Description is a required field.",
        "blank": "Description cannot be empty."
    })

# Progress Note Validator
class ProgressNoteValidator(serializers.Serializer):
    status = serializers.ChoiceField(choices=[
        "Critical", "Serious", "Moderate", "Mild", "Recovered", "Stable", "Deteriorating", "Improving"
    ], error_messages={
        "invalid_choice": "Invalid status choice."
    })

# Treatment Chart Validator
class TreatmentChartValidator(serializers.Serializer):
    medicine_name = serializers.CharField(required=True, max_length=255, error_messages={
        "required": "Medicine name is a required field.",
        "max_length": "Medicine name cannot exceed 255 characters."
    })
    hrs_drops_mins = serializers.CharField(required=True, max_length=20, error_messages={
        "required": "Hrs/Drops/Min is a required field.",
        "max_length": "Hrs/Drops/Min cannot exceed 20 characters."
    })
    dose = serializers.CharField(required=True, max_length=100, error_messages={
        "required": "Dose is a required field.",
        "max_length": "Dose cannot exceed 100 characters."
    })
    time = serializers.TimeField(required=True, error_messages={
        "required": "Time is a required field."
    })
    medicine_details = serializers.CharField(required=True, error_messages={
        "required": "Medicine details are required."
    })

# Pain Assessment Validator
class PainAssessmentValidator(serializers.Serializer):
    pain_intensity = serializers.IntegerField(min_value=0, max_value=10, error_messages={
        "min_value": "Pain intensity cannot be below 0.",
        "max_value": "Pain intensity cannot exceed 10."
    })
    location_of_service = serializers.CharField(max_length=255, error_messages={
        "max_length": "Location cannot exceed 255 characters."
    })
    quality_of_service = serializers.ChoiceField(choices=["Constant", "Intermittent"], error_messages={
        "invalid_choice": "Invalid choice for quality of service."
    })
    character_of_service = serializers.JSONField(error_messages={
        "invalid": "Invalid character of service data."
    })
    factors_affecting_rating = serializers.CharField(error_messages={
        "invalid": "Invalid factors affecting rating."
    })
    factors_improving_experience = serializers.JSONField(error_messages={
        "invalid": "Invalid factors improving experience data."
    })

# Initial Assessment Validator
class InitialAssessmentValidator(serializers.Serializer):
    rating_title = serializers.CharField(required=False, allow_blank=True, max_length=255)
    relationship_to_feedback = serializers.CharField(required=False, allow_blank=True, max_length=255)
    feedback_date = serializers.DateField(required=False)
    duration_of_experience = serializers.CharField(required=False, allow_blank=True)
    present_illness = serializers.CharField(required=False, allow_blank=True)
    past_illness = serializers.CharField(required=False, allow_blank=True)
    experience_feedback = serializers.CharField(required=False, allow_blank=True)
    health_feedback = serializers.CharField(required=False, allow_blank=True)
    hart_feedback = serializers.CharField(required=False, allow_blank=True)
    stroke_feedback = serializers.CharField(required=False, allow_blank=True)
    other_feedback = serializers.CharField(required=False, allow_blank=True)

# Care Plan Feedback Validator
class CarePlanFeedbackValidator(serializers.Serializer):
    feedback_on_services = serializers.CharField(required=False, allow_blank=True)
    provisional_feedback = serializers.CharField(required=False, allow_blank=True)
    feedback_plan = serializers.CharField(required=False, allow_blank=True)
    expected_outcome_of_feedback = serializers.CharField(required=False, allow_blank=True)
    preventive_feedback_aspects = serializers.CharField(required=False, allow_blank=True)

# Risk Factor Validators
class RiskFactorValidator(serializers.Serializer):
    surgery_feedback = serializers.BooleanField(default=False)
    postpartum_feedback = serializers.BooleanField(default=False)
    condition_feedback = serializers.BooleanField(default=False)
    contraceptive_feedback = serializers.BooleanField(default=False)
    age_feedback = serializers.BooleanField(default=False)
    obesity_feedback = serializers.BooleanField(default=False)

class RiskFactor3Validator(RiskFactorValidator):
    surgical_feedback = serializers.BooleanField(default=False)
    access_feedback = serializers.BooleanField(default=False)
    health_condition_feedback = serializers.BooleanField(default=False)
    feedback_on_condition = serializers.BooleanField(default=False)
    bedridden_feedback = serializers.BooleanField(default=False)

class RiskFactor4Validator(RiskFactorValidator):
    history_of_feedback = serializers.BooleanField(default=False)
    heart_failure_feedback = serializers.BooleanField(default=False)
    resistance_feedback = serializers.BooleanField(default=False)
    deficiency_feedback = serializers.BooleanField(default=False)
    thrombocytopenia_feedback = serializers.BooleanField(default=False)
    heart_feedback = serializers.BooleanField(default=False)
    infection_feedback = serializers.BooleanField(default=False)
    mutation_feedback = serializers.BooleanField(default=False)
    antibody_feedback = serializers.BooleanField(default=False)
    disorder_feedback = serializers.BooleanField(default=False)
    syndrome_feedback = serializers.BooleanField(default=False)

class RiskFactor5Validator(RiskFactorValidator):
    elective_surgery_feedback = serializers.BooleanField(default=False)
    fracture_feedback = serializers.BooleanField(default=False)
    trauma_feedback = serializers.BooleanField(default=False)
    stroke_feedback = serializers.BooleanField(default=False)
    injury_feedback = serializers.BooleanField(default=False)
