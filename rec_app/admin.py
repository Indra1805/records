from django.contrib import admin
from .models import Vitals, Patient, StaffUsers, LabResult

# Register your models here.

@admin.register(StaffUsers)
class StaffUsersAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Vitals)
class VitalsAdmin(admin.ModelAdmin):
    list_display = ['recorded_by','temperature','blood_pressure','heart_rate']

@admin.register(LabResult)
class LabResultsAdmin(admin.ModelAdmin):
    list_display = ['doctor','white_blood_cells','hemoglobin','platelets']