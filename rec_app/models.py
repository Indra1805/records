from django.db import models

class StaffUsers(models.Model):
    name = models.CharField(max_length=30,unique=False)

    def __str__(self):
        return self.name
    

class Patient(models.Model):
    name = models.CharField(max_length=255,unique=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class MedicalRecord(models.Model):
    RECORD_TYPES = [
        ("vitals", "Vitals"),
        ("lab_results", "Lab Results"),
        ("imaging", "Imaging"),
        ("prescription", "Prescription"),
        ("services_procedures", "Services & Procedures"),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=50, choices=RECORD_TYPES)
    summary = models.TextField()
    report = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Abstract Model

class Vitals(MedicalRecord):
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
    doctor = models.ForeignKey(StaffUsers,on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    hemoglobin = models.FloatField()
    white_blood_cells = models.FloatField()
    platelets = models.FloatField()
    test_name = models.CharField(max_length=255)
    result_value = models.CharField(max_length=255)



class Imaging(MedicalRecord):
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="imaging")
    scan_type = models.CharField(max_length=100)

class Prescription(MedicalRecord):
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="prescriptions")
    medication_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

class ServiceProcedure(MedicalRecord):
    doctor = models.ForeignKey(StaffUsers, on_delete=models.CASCADE, related_name="procedures")
    procedure_name = models.CharField(max_length=100)
    procedure_notes = models.TextField()
