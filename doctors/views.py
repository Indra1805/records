from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils.timezone import now
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from .models import *
from .serializers import DoctorAvailabilitySerializer
from .serializers import AvailableSlotsSerializer
from django.db.models import Q
from django.core.cache import cache


from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.utils.timezone import now
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import DoctorAvailability
from .serializers import DoctorAvailabilitySerializer

class DoctorAvailabilityAPIView(APIView):
    def get(self, request, pk=None, doctor_id=None):
        """Fetch doctor details along with available slots"""

        # doctors_count = DoctorAvailability.objects.count()
        context = {
            "success": 1,
            "message": "Data fetched successfully.",
            "data": {},
            # "d_count": doctors_count,
        }

        try:
            if pk:
                # Fetch a single doctor
                doctor = get_object_or_404(DoctorAvailability, pk=pk)
                serializer = DoctorAvailabilitySerializer(doctor)
                slots = self.get_available_slots(doctor)
                context["data"] = serializer.data
                context["availability_slots"] = slots

            elif doctor_id:
                # Fetch a single doctor for availability slots
                doctor = get_object_or_404(DoctorAvailability, id=doctor_id)
                slots = self.get_available_slots(doctor)
                context["data"] = {"doctor": doctor.d_name, "available_slots": slots}

            else:
                # Fetch all doctors
                doctors = DoctorAvailability.objects.all()
                if not doctors:
                    return Response({"error": "No doctors found"}, status=status.HTTP_404_NOT_FOUND)

                doctor_data = []
                for doctor in doctors:
                    slots = self.get_available_slots(doctor)
                    doctor_data.append({
                       "d_id": doctor.d_id,
                        "d_name": doctor.d_name,
                        "d_department": str(doctor.d_department),
                        "d_phn_no": doctor.d_phn_no,
                        "d_email": doctor.d_email,
                        "d_ward_no": doctor.d_ward_no,
                        "d_start_time": doctor.d_start_time.strftime('%I:%M %p'),
                        "d_end_time": doctor.d_end_time.strftime('%I:%M %p'),
                        "d_education_info": doctor.d_education_info,
                        "d_certifications": doctor.d_certifications,
                        "d_available_days": doctor.d_available_days,  # Include available days
                        "d_available_slots": slots  # Include slots
                    })

                context["data"] = doctor_data

        except DoctorAvailability.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": "An error occurred", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(context, status=status.HTTP_200_OK)

    def get_available_slots(self, doctor):
        
        """Helper function to generate available slots for a doctor"""
        start_time = datetime.combine(now().date(), doctor.d_start_time)
        end_time = datetime.combine(now().date(), doctor.d_end_time)
        slots = []
        post_break_slots = 0

        while start_time < end_time:
            time_str = start_time.strftime('%I:%M %p')

            if time_str == "12:00 PM":
                slots.append({"time": time_str, "status": "Break"})
                start_time += timedelta(hours=2)  # Skip 2 hours for break
            elif start_time >= datetime.combine(now().date(), datetime.strptime("02:00 PM", "%I:%M %p").time()):
                if post_break_slots < 2:
                    slots.append({"time": time_str, "status": "Available"})
                    post_break_slots += 1
            else:
                slots.append({"time": time_str, "status": "Available"})

            start_time += timedelta(hours=1)

        return slots

    
    def post(self, request):
        context = {
            "success": 1,
            "message": "Data saved successfully.",
            "data": {}
        }
        try:
            serializer = DoctorAvailabilitySerializer(data=request.data)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)
            print(serializer.errors)
            doctor = serializer.save()
            context["data"] = DoctorAvailabilitySerializer(doctor).data
        except ValidationError as e:
            context["success"] = 0
            context["message"] = e.args[0]
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)

        print(request.data)
        return Response(context, status=status.HTTP_201_CREATED if context["success"] else status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        context = {
            "success": 1,
            "message": "Data updated successfully.",
            "data": {}
        }
        try:
            doctor = get_object_or_404(DoctorAvailability, pk=pk)
            serializer = DoctorAvailabilitySerializer(doctor, data=request.data, partial=True)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)

            doctor = serializer.save()
            context["data"] = DoctorAvailabilitySerializer(doctor).data
        except ValidationError as e:
            context["success"] = 0
            context["message"] = e.args[0]
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)

        return Response(context, status=status.HTTP_200_OK if context["success"] else status.HTTP_400_BAD_REQUEST)

class DoctorSearchView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            doctors = DoctorAvailability.objects.all()
            
            d_id = request.query_params.get('d_id', None)
            d_name = request.query_params.get('d_name', None)
            d_department_name = request.query_params.get('d_department_name', None)
            
            if d_id:
                doctors = doctors.filter(d_id=d_id)
            if d_name:
                doctors = doctors.filter(d_name__icontains=d_name)
            if d_department_name:
                doctors = doctors.filter(d_department__name__icontains=d_department_name)
            
            serializer = DoctorAvailabilitySerializer(doctors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

