from django.contrib import admin
from .models import Vitals, Patient, StaffUsers, LabResult

# Register your models here.

@admin.register(StaffUsers)
class StaffUsersAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','name']


