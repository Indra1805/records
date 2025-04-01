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
    category = models.CharField(max_length=255,blank=True)
    summary = models.TextField(blank=True)
    report = models.FileField(upload_to='reports/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Abstract Model

class Vitals(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='vitals_records')
    recorded_by = models.CharField(max_length=255)
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
    title = models.CharField(max_length=255)



class Imaging(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='imaging_records')
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="imaging")
    scan_type = models.CharField(max_length=100)

class Prescription(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="prescriptions")
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

class ServiceProcedure(MedicalRecord):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='service_procedures')
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="procedures")
    procedure_name = models.CharField(max_length=100)
    procedure_notes = models.TextField()


# Models for adding note

# Nursing Notes

class NursingNotes(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Progress Notes

class ProgressNote(models.Model):
    STATUS_CHOICES = [
        ('critical', 'Critical'),
        ('serious', 'Serious'),
        ('moderate', 'Moderate'),
        ('mild', 'Mild'),
        ('recovered', 'Recovered'),
        ('stable', 'Stable'),
        ('deteriorating', 'Deteriorating'),
        ('improving', 'Improving'),
    ]

    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='progress_notes')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient.patient_name} - {self.status}'
    


# Treatment Chart

class TreatmentChart(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)  # One treatment chart per patient
    medicine_name = models.CharField(max_length=255)
    hrs_drops_mins = models.CharField(max_length=50)  # Stores Hrs/Drops/Mins as a string
    dose = models.CharField(max_length=50)
    time = models.TimeField()
    medicine_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Pain Assessment

class PainAssessment(models.Model):
    PAIN_INTENSITY_CHOICES = [(i, str(i)) for i in range(11)]  # 0 to 10

    QUALITY_OF_SERVICE_CHOICES = [
        ('constant', 'Constant Feedback'),
        ('intermittent', 'Intermittent Feedback'),
    ]

    CHARACTER_OF_SERVICE_CHOICES = [
        ('lacerating', 'Lacerating Feedback'),
        ('burning', 'Burning Feedback'),
        ('radiating', 'Radiating Feedback'),
    ]

    FACTORS_IMPROVING_EXPERIENCE_CHOICES = [
        ('reset', 'Reset Feedback'),
        ('medication', 'Medication Feedback'),
    ]

    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='pain_assessment')
    pain_intensity = models.IntegerField(choices=PAIN_INTENSITY_CHOICES, default=0)
    location_of_service = models.CharField(max_length=255, blank=True, null=True)
    quality_of_service = models.CharField(max_length=20, choices=QUALITY_OF_SERVICE_CHOICES, blank=True, null=True)
    character_of_service = models.JSONField(blank=True, null=True)  # Store multiple choices
    factors_affecting_rating = models.TextField(blank=True, null=True)
    factors_improving_experience = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.patient.patient_name} - Pain Assessment'
    

# Initial Assessment
class InitialAssessment(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
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


# Careplan Feedback

class CarePlanFeedback(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE) 
    feedback_on_services = models.TextField()  
    provisional_feedback = models.TextField()  
    feedback_plan = models.TextField()  
    expected_outcome = models.TextField()  
    preventive_feedback_aspects = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 


# Risk Assessment

class RiskFactor1(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    surgery = models.BooleanField(default=False)
    postpartum_feedback = models.BooleanField(default=False)
    condition_feedback = models.BooleanField(default=False)
    contraceptive_feedback = models.BooleanField(default=False)
    age_feedback = models.BooleanField(default=False)
    obesity = models.BooleanField(default=False)


class RiskFactor2(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    surgery = models.BooleanField(default=False)
    postpartum_feedback = models.BooleanField(default=False)
    condition_feedback = models.BooleanField(default=False)
    contraceptive_feedback = models.BooleanField(default=False)
    age_feedback = models.BooleanField(default=False)
    obesity = models.BooleanField(default=False)
    

class RiskFactor3(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    age_feedback = models.BooleanField(default=False)
    surgery_feedback = models.BooleanField(default=False)
    surgical_feedback = models.BooleanField(default=False)
    access_feedback = models.BooleanField(default=False)
    health_condition_feedback = models.BooleanField(default=False)
    feedback_on_condition = models.BooleanField(default=False)
    bedridden_feedback = models.BooleanField(default=False)
    

class RiskFactor4(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    history_of_feedback = models.BooleanField(default=False)
    heart_failure_feedback = models.BooleanField(default=False)
    resistance_feedback = models.BooleanField(default=False)
    deficiency_feedback = models.BooleanField(default=False)
    health_condition_feedback = models.BooleanField(default=False)
    condition_feedback = models.BooleanField(default=False)
    thrombocytopenia_feedback = models.BooleanField(default=False)
    heart_feedback = models.BooleanField(default=False)
    infection_feedback = models.BooleanField(default=False)
    mutation_feedback = models.BooleanField(default=False)
    antibody_feedback = models.BooleanField(default=False)
    disorder_feedback = models.BooleanField(default=False)
    syndrome_feedback = models.BooleanField(default=False)
    

class RiskFactor5(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    elective_surgery_feedback = models.BooleanField(default=False)
    fracture_feedback = models.BooleanField(default=False)
    trauma_feedback = models.BooleanField(default=False)
    surgery_feedback = models.BooleanField(default=False)
    stroke_feedback = models.BooleanField(default=False)
    injury_feedback = models.BooleanField(default=False)

