# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Vitals, LabResult
# from .serializers import VitalsSerializer, LabResultSerializer, get_serializer_class

# class MedicalRecordViewSet(viewsets.ViewSet):

#     def create(self, request, *args, **kwargs):
#         record_type = request.data.get("record_type")
#         serializer_class = get_serializer_class(record_type)
 
#         if not serializer_class:
#             return Response({"error": "Invalid record type"}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def list(self, request, *args, **kwargs):
#         record_type = request.query_params.get("record_type")
#         serializer_class = get_serializer_class(record_type)

#         if not serializer_class:
#             return Response({"error": "Invalid record type"}, status=status.HTTP_400_BAD_REQUEST)

#         model_class = serializer_class.Meta.model
#         queryset = model_class.objects.all()
#         serializer = serializer_class(queryset, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def get_record_fields(request):
#     fields_data = {
#         "vitals": ["recorded_by", "recorded_datetime", "temperature", "blood_pressure", "heart_rate",
#                    "oxygen_level", "respiratory_rate", "weight", "height"],
#         "lab_results": ["doctor", "category", "hemoglobin", "white_blood_cells", "platelets", "test_name", "result_value"],
#         "imaging":["doctor","scan_type","scan_result"],
#         "prescription":["doctor","medication_time","dosage","frequency","duration"],
#         "service_procedure":["doctor","procedure_name","procedure_notes"]
#     }
#     return Response(fields_data)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vitals, LabResult, Imaging, Prescription, ServiceProcedure
from .serializers import VitalsSerializer, LabResultSerializer, ImagingSerializer, PrescriptionSerializer, ServiceProcedureSerializer, get_serializer_class

class MedicalRecordAPIView(APIView):
    
    def get_model(self, record_type):
        model_mapping = {
            "vitals": Vitals,
            "lab_results": LabResult,
            "imaging": Imaging,
            "prescription": Prescription,
            "serviceprocedure": ServiceProcedure
        }
        return model_mapping.get(record_type)

    def get(self, request, record_type, patient_id=None):
        model = self.get_model(record_type)
        if not model:
            return Response({"error": "Invalid record type"}, status=status.HTTP_400_BAD_REQUEST)

        if patient_id:
            records = model.objects.filter(patient_id=patient_id)
        else:
            records = model.objects.all()
        
        serializer = get_serializer_class(record_type)(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, record_type):
        serializer_class = get_serializer_class(record_type)
        if not serializer_class:
            return Response({"error": "Invalid record type"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, record_type, record_id):
        model = self.get_model(record_type)
        if not model:
            return Response({"error": "Invalid record type"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            record = model.objects.get(id=record_id)
        except model.DoesNotExist:
            return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer_class = get_serializer_class(record_type)
        serializer = serializer_class(record, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



