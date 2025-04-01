from django.contrib import admin
from .models import Vitals, Patient, StaffUsers, LabResult

# Register your models here.

@admin.register(StaffUsers)
class StaffUsersAdmin(admin.ModelAdmin):
    list_display = ['id','name']







# add notes

