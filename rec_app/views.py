from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Vitals, LabResult, Imaging, Prescription, ServiceProcedure
from .serializers import VitalsSerializer, LabResultSerializer, ImagingSerializer, PrescriptionSerializer, ServiceProcedureSerializer


def get_serializer_class(record_type):
    serializer_classes = {
        "vitals": VitalsSerializer,
        "lab_results": LabResultSerializer,
        "imaging": ImagingSerializer,
        "prescription": PrescriptionSerializer,
        "service_procedure": ServiceProcedureSerializer,
    }
    return serializer_classes.get(record_type)


class MedicalRecordAPIView(APIView):

    def post(self, request, *args, **kwargs):
        record_type = request.data.get("record_type")
        serializer_class = get_serializer_class(record_type)

        if not serializer_class:
            return Response({"error": "Invalid record type"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        record_type = request.query_params.get("record_type")
        serializer_class = get_serializer_class(record_type)

        if not serializer_class:
            return Response({"error": "Invalid record type"}, status=status.HTTP_400_BAD_REQUEST)

        model_class = serializer_class.Meta.model
        queryset = model_class.objects.all()
        serializer = serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        record_type = request.data.get("record_type")
        record_id = kwargs.get('pk')
        serializer_class = get_serializer_class(record_type)

        if not serializer_class:
            return Response({"error": "Invalid record type"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            model_class = serializer_class.Meta.model
            instance = model_class.objects.get(pk=record_id)
        except model_class.DoesNotExist:
            return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_record_fields(request):
    fields_data = {
        "vitals": ["recorded_by", "recorded_datetime", "blood_pressure", "bmi", "grbs", "cvs", "cns", "respiratory_rate", "weight", "height"],
        "lab_results": ["doctor", "category", "hemoglobin", "white_blood_cells", "platelets", "test_name", "result_value"],
        "imaging": ["doctor", "scan_type"],
        "prescription": ["doctor", "medication_name", "dosage", "frequency", "duration"],
        "service_procedure": ["doctor", "procedure_name", "procedure_notes"]
    }
    return Response(fields_data)
