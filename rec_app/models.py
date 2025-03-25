from django.db import models
from patients.models import Patient


# create your models here

class StaffUsers(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Models for adding rceords

class MedicalRecord(models.Model):
    RECORD_TYPES = [
        ("vitals", "Vitals"),
        ("lab_results", "Lab Results"),
        ("imaging", "Imaging"),
        ("prescription", "Prescription"),
        ("services_procedures", "Services & Procedures"),
    ]
    
    record_type = models.CharField(max_length=50, choices=RECORD_TYPES)
    category = models.CharField(max_length=255)
    summary = models.TextField()
    report = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Abstract Model

class Vitals(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='vitals_records')
    recorded_by = models.CharField(max_length=255)
    recorded_datetime = models.DateTimeField()
    blood_pressure = models.CharField(max_length=50)
    bmi = models.FloatField()
    grbs = models.CharField(max_length=50)
    cvs = models.CharField(max_length=50)
    cns = models.CharField(max_length=50)
    respiratory_rate = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()

class LabResult(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_results')
    doctor = models.ForeignKey(StaffUsers,on_delete=models.CASCADE)
    hemoglobin = models.FloatField()
    white_blood_cells = models.FloatField()
    platelets = models.FloatField()
    test_name = models.CharField(max_length=255)
    result_value = models.CharField(max_length=255)



class Imaging(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='imaging_records')
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="imaging")
    scan_type = models.CharField(max_length=100)

class Prescription(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="prescriptions")
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

class ServiceProcedure(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='service_procedures')
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="procedures")
    procedure_name = models.CharField(max_length=100)
    procedure_notes = models.TextField()


# Models for adding note


class NursingNote(models.Model):
    description = models.TextField()

    def __str__(self):
        return f"Nursing Note {self.id}"

class ProgressNote(models.Model):
    STATUS_CHOICES = [
        ("Critical", "Critical"),
        ("Serious", "Serious"),
        ("Moderate", "Moderate"),
        ("Mild", "Mild"),
        ("Recovered", "Recovered"),
        ("Stable", "Stable"),
        ("Deteriorating", "Deteriorating"),
        ("Improving", "Improving"),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Stable")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

# Treatment Chart Table
class TreatmentChart(models.Model):
    medicine_name = models.CharField(max_length=255) 
    hrs_drops_mins = models.CharField(max_length=20)  # Hrs/Drops/Min
    dose = models.CharField(max_length=100)  # Dose Quantity
    time = models.TimeField()  # Time to give medicine
    medicine_details = models.TextField()  # Medicine Description
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.medicine_details} at {self.time}"


# Pain Assessment Table
class PainAssessment(models.Model):
    PAIN_INTENSITY_CHOICES = [(i, i) for i in range(11)]  # 0-10 scale

    pain_intensity = models.IntegerField(choices=PAIN_INTENSITY_CHOICES)
    location_of_service = models.CharField(max_length=255)
    quality_of_service = models.CharField(max_length=50, choices=[('Constant', 'Constant Feedback'), ('Intermittent', 'Intermittent Feedback')])
    character_of_service = models.JSONField(default=list)  # List of selected checkboxes
    factors_affecting_rating = models.TextField()
    factors_improving_experience = models.JSONField(default=list)  # List of selected checkboxes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pain Assessment - {self.id}'

# Initial Assessment Table
class InitialAssessment(models.Model):
    rating_title = models.CharField(max_length=255, blank=True, null=True)
    relationship_to_feedback = models.CharField(max_length=255, blank=True, null=True)
    feedback_date = models.DateField(blank=True, null=True)
    duration_of_experience = models.TextField(blank=True, null=True)
    present_illness = models.TextField(blank=True, null=True)
    past_illness = models.TextField(blank=True, null=True)
    experience_feedback = models.TextField(blank=True, null=True)
    health_feedback = models.TextField(blank=True, null=True)
    hart_feedback = models.TextField(blank=True, null=True)
    stroke_feedback = models.TextField(blank=True, null=True)
    other_feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.rating_title

# Care Plan Feedback Table
class CarePlanFeedback(models.Model):
    feedback_on_services = models.TextField(blank=True, null=True)
    provisional_feedback = models.TextField(blank=True, null=True)
    feedback_plan = models.TextField(blank=True, null=True)
    expected_outcome_of_feedback = models.TextField(blank=True, null=True)
    preventive_feedback_aspects = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.feedback_on_services[:50] if self.feedback_on_services else "No Feedback"

# Risk Assessment Tables
class RiskFactor1(models.Model):
    surgery_feedback = models.BooleanField(default=False)
    postpartum_feedback = models.BooleanField(default=False)
    condition_feedback = models.BooleanField(default=False)
    contraceptive_feedback = models.BooleanField(default=False)
    age_feedback = models.BooleanField(default=False)
    obesity_feedback = models.BooleanField(default=False)

    def __str__(self):
        return f"Surgery: {self.surgery_feedback}, Obesity: {self.obesity_feedback}"

class RiskFactor2(models.Model):
    surgery_feedback = models.BooleanField(default=False)
    postpartum_feedback = models.BooleanField(default=False)
    condition_feedback = models.BooleanField(default=False)
    contraceptive_feedback = models.BooleanField(default=False)
    age_feedback = models.BooleanField(default=False)
    obesity_feedback = models.BooleanField(default=False)

    def __str__(self):
        return f"Risk Factor 2 - Surgery: {self.surgery_feedback}, Obesity: {self.obesity_feedback}"

class RiskFactor3(models.Model):
    age_feedback = models.BooleanField(default=False)
    surgery_feedback = models.BooleanField(default=False)
    surgical_feedback = models.BooleanField(default=False)
    access_feedback = models.BooleanField(default=False)
    health_condition_feedback = models.BooleanField(default=False)
    feedback_on_condition = models.BooleanField(default=False)
    bedridden_feedback = models.BooleanField(default=False)

    def __str__(self):
        return f"Risk Factor 3 - Age: {self.age_feedback}, Surgery: {self.surgery_feedback}"

class RiskFactor4(models.Model):
    history_of_feedback = models.BooleanField(default=False)
    heart_failure_feedback = models.BooleanField(default=False)
    resistance_feedback = models.BooleanField(default=False)
    deficiency_feedback = models.BooleanField(default=False)
    health_condition_feedback = models.BooleanField(default=False)
    feedback_on_condition = models.BooleanField(default=False)
    condition_feedback = models.BooleanField(default=False)
    thrombocytopenia_feedback = models.BooleanField(default=False)
    heart_feedback = models.BooleanField(default=False)
    infection_feedback = models.BooleanField(default=False)
    mutation_feedback = models.BooleanField(default=False)
    antibody_feedback = models.BooleanField(default=False)
    disorder_feedback = models.BooleanField(default=False)
    syndrome_feedback = models.BooleanField(default=False)

    def __str__(self):
        return f"Risk Factor 4 - Heart Failure: {self.heart_failure_feedback}, Disorder: {self.disorder_feedback}"

class RiskFactor5(models.Model):
    elective_surgery_feedback = models.BooleanField(default=False)
    fracture_feedback = models.BooleanField(default=False)
    trauma_feedback = models.BooleanField(default=False)
    surgery_feedback = models.BooleanField(default=False)
    stroke_feedback = models.BooleanField(default=False)
    injury_feedback = models.BooleanField(default=False)

    def __str__(self):
        return f"Risk Factor 5 - Surgery: {self.surgery_feedback}, Stroke: {self.stroke_feedback}"

