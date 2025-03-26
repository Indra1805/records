from rest_framework import serializers
from patients.models import Patient, Invoice
from rec_app.models import Prescription

# Create the serailizers over here



class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'patient_name', 'doctor_name', 'date', 'time', 'age',
            'appointment_type', 'notes', 'gender', 'phno', 'billing','ward_no','diagnosis'
        ]
        extra_kwargs = {'phno': {'required': False}}


        
class PatientSerializer(serializers.ModelSerializer):
    billing = InvoiceSerializer()

    class Meta:
        model = Patient
        fields = '__all__'

