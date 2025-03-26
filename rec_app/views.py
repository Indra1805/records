from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from . import models, serializers, validators
from rec_app.models import *
from rec_app.serializers import *
from rec_app.validators import *
from rest_framework.views import APIView
from core import messages
from core.exceptions import SerializerError
from django.db import transaction
from rec_app.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .serializers import get_serializer_class
from core import messages


def get_serializer_class(record_type):
    serializer_classes = {
        "vitals": VitalsSerializer,
        "lab_results": LabResultSerializer,
        "imaging": ImagingSerializer,
        "prescription": PrescriptionSerializer,
        "service_procedure": ServiceProcedureSerializer,
    }
    return serializer_classes.get(record_type)


# class MedicalRecordRetrieveAPIView(APIView):
#     def get(self, request):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             record_type = request.query_params.get("record_type")
#             serializer_class = get_serializer_class(record_type)

#             if not serializer_class:
#                 context["success"] = 0
#                 context["message"] = "Invalid record type"
#                 return Response(context)

#             model_class = serializer_class.Meta.model
#             queryset = model_class.objects.all()
#             serializer = serializer_class(queryset, many=True)
#             context["data"] = serializer.data
#             return Response(context)

#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)




class MedicalRecordRetrieveAPIView(APIView): 
    def get(self, request):
        context = {"success": 1, "message": "Data Retrieved", "data": {}}
        try:
            record_type = request.query_params.get("record_type")
            patient_id = request.query_params.get("patient_id")
            patient_name = request.query_params.get("patient_name")
            record_id = request.query_params.get("record_id")

            serializer_class = get_serializer_class(record_type)

            if not serializer_class:
                context["success"] = 0
                context["message"] = "Invalid record type"
                return Response(context)

            model_class = serializer_class.Meta.model
            queryset = model_class.objects.all()

            # Filtering Logic
            filters = Q()
            if patient_id:
                filters &= Q(patient__id=patient_id)
            if patient_name:
                filters &= Q(patient__patient_name__icontains=patient_name)
            if record_id:
                filters &= Q(id=record_id)

            queryset = queryset.filter(filters)

            serializer = serializer_class(queryset, many=True)
            context["data"] = serializer.data
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)




class MedicalRecordCreateAPIView(APIView):
    def post(self, request):
        context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
        try:
            record_type = request.data.get("record_type")
            serializer_class = get_serializer_class(record_type)

            if not serializer_class:
                context["success"] = 0
                context["message"] = "Invalid record type"
                return Response(context)

            serializer = serializer_class(data=request.data)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)




class MedicalRecordUpdateAPIView(APIView):
    def put(self, request, pk):
        context = {"success": 1, "message": messages.DATA_UPDATED, "data": {}}
        try:
            record_type = request.data.get("record_type")
            serializer_class = get_serializer_class(record_type)

            if not serializer_class:
                context["success"] = 0
                context["message"] = "Invalid record type"
                return Response(context)

            model_class = serializer_class.Meta.model
            instance = model_class.objects.get(pk=pk)

            serializer = serializer_class(instance, data=request.data, partial=True)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)

        except model_class.DoesNotExist:
            context["success"] = 0
            context["message"] = "Record not found"
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)










# class MedicalRecordAPIView(APIView):

#     def post(self, request):
#         context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
#         try:
#             record_type = request.data.get("record_type")
#             serializer_class = get_serializer_class(record_type)

#             if not serializer_class:
#                 context["success"] = 0
#                 context["message"] = "Invalid record type"
#                 return Response(context)

#             validator = serializer_class(data=request.data)
#             if not validator.is_valid():
#                 raise SerializerError(validator.errors)

#             validator.save()
#             context["data"] = validator.data
#             return Response(context)

#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def get(self, request):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             record_type = request.query_params.get("record_type")
#             serializer_class = get_serializer_class(record_type)

#             if not serializer_class:
#                 context["success"] = 0
#                 context["message"] = "Invalid record type"
#                 return Response(context)

#             model_class = serializer_class.Meta.model
#             queryset = model_class.objects.all()
#             validator = serializer_class(queryset, many=True)
#             context["data"] = validator.data
#             return Response(context)

#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def put(self, request, pk):
#         context = {"success": 1, "message": messages.DATA_UPDATED, "data": {}}
#         try:
#             record_type = request.data.get("record_type")
#             serializer_class = get_serializer_class(record_type)

#             if not serializer_class:
#                 context["success"] = 0
#                 context["message"] = "Invalid record type"
#                 return Response(context)

#             model_class = serializer_class.Meta.model
#             instance = model_class.objects.get(pk=pk)

#             validator = serializer_class(instance, data=request.data, partial=True)
#             if not validator.is_valid():
#                 raise SerializerError(validator.errors)

#             validator.save()
#             context["data"] = validator.data
#             return Response(context)

#         except model_class.DoesNotExist:
#             context["success"] = 0
#             context["message"] = "Record not found"
#             return Response(context)

#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)




class NursingNoteRetrieveAPIView(APIView):
    def get(self, request):
        context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
        try:
            notes = NursingNote.objects.all()
            serializer = NursingNoteSerializer(notes, many=True)
            context["data"] = serializer.data
            return Response(context)
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)





class NursingNoteCreateAPIView(APIView):
    def post(self, request):
        context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
        try:
            serializer = NursingNoteSerializer(data=request.data)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)



# class NursingNoteView(APIView):

#     def get(self, request):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             notes = NursingNote.objects.all()
#             serializer = NursingNoteSerializer(notes, many=True)
#             context["data"] = serializer.data
#             return Response(context)
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def post(self, request):
#         context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
#         try:
#             validator = NursingNoteSerializer(data=request.data)
#             if not validator.is_valid():
#                 raise SerializerError(validator.errors)

#             validator.save()
#             context["data"] = validator.data
#             return Response(context)
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)




class ProgressNoteRetrieveAPIView(APIView):
    def get(self, request, pk=None):
        context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
        try:
            if pk:
                progress_note = get_object_or_404(ProgressNote, pk=pk)
                serializer = ProgressNoteSerializer(progress_note)
            else:
                progress_notes = ProgressNote.objects.all()
                serializer = ProgressNoteSerializer(progress_notes, many=True)
            
            context["data"] = serializer.data
            return Response(context)
        
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)




class ProgressNoteCreateAPIView(APIView):
    def post(self, request):
        context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
        try:
            serializer = ProgressNoteSerializer(data=request.data)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)
            
            serializer.save()
            context["data"] = serializer.data
            return Response(context)
        
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)




class ProgressNoteUpdateAPIView(APIView):
    def put(self, request, pk):
        context = {"success": 1, "message": messages.DATA_UPDATED, "data": {}}
        try:
            progress_note = get_object_or_404(ProgressNote, pk=pk)
            serializer = ProgressNoteSerializer(progress_note, data=request.data, partial=True)

            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)
        
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)



# class ProgressNoteView(APIView):

#     def post(self, request):
#         context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
#         try:
#             serializer = ProgressNoteSerializer(data=request.data)
#             if not serializer.is_valid():
#                 raise SerializerError(serializer.errors)
            
#             serializer.save()
#             context["data"] = serializer.data
#             return Response(context)
        
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def get(self, request, pk=None):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             if pk:
#                 progress_note = get_object_or_404(ProgressNote, pk=pk)
#                 serializer = ProgressNoteSerializer(progress_note)
#             else:
#                 progress_notes = ProgressNote.objects.all()
#                 serializer = ProgressNoteSerializer(progress_notes, many=True)
            
#             context["data"] = serializer.data
#             return Response(context)
        
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def put(self, request, pk):
#         context = {"success": 1, "message": messages.DATA_UPDATED, "data": {}}
#         try:
#             progress_note = get_object_or_404(ProgressNote, pk=pk)
#             serializer = ProgressNoteSerializer(progress_note, data=request.data, partial=True)

#             if not serializer.is_valid():
#                 raise SerializerError(serializer.errors)

#             serializer.save()
#             context["data"] = serializer.data
#             return Response(context)
        
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)




class TreatmentChartRetrieveAPIView(APIView):
    def get(self, request):
        context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
        try:
            treatments = TreatmentChart.objects.all()
            serializer = TreatmentChartSerializer(treatments, many=True)
            context["data"] = serializer.data
            return Response(context)
        
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)





class TreatmentChartCreateAPIView(APIView):
    def post(self, request):
        context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
        try:
            serializer = TreatmentChartSerializer(data=request.data)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)



# class TreatmentChartView(APIView):

#     def post(self, request):
#         context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
#         try:
#             serializer = TreatmentChartSerializer(data=request.data)
#             if not serializer.is_valid():
#                 raise SerializerError(serializer.errors)

#             serializer.save()
#             context["data"] = serializer.data
#             return Response(context)

#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def get(self, request):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             treatments = TreatmentChart.objects.all()
#             serializer = TreatmentChartSerializer(treatments, many=True)
#             context["data"] = serializer.data
#             return Response(context)
        
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)




class PainAssessmentRetrieveAPIView(APIView):
    def get(self, request):
        context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
        try:
            assessments = PainAssessment.objects.all()
            serializer = PainAssessmentSerializer(assessments, many=True)
            context["data"] = serializer.data
            return Response(context)
        
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)




class PainAssessmentCreateAPIView(APIView):
    def post(self, request):
        context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
        try:
            serializer = PainAssessmentSerializer(data=request.data)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)


# class PainAssessmentView(APIView):

#     def post(self, request):
#         context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
#         try:
#             serializer = PainAssessmentSerializer(data=request.data)
#             if not serializer.is_valid():
#                 raise SerializerError(serializer.errors)

#             serializer.save()
#             context["data"] = serializer.data
#             return Response(context)

#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def get(self, request):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             assessments = PainAssessment.objects.all()
#             serializer = PainAssessmentSerializer(assessments, many=True)
#             context["data"] = serializer.data
#             return Response(context)
        
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)




class InitialAssessmentRetrieveAPIView(APIView):
    def get(self, request):
        context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
        try:
            assessments = InitialAssessment.objects.all()
            serializer = InitialAssessmentSerializer(assessments, many=True)
            context["data"] = serializer.data
            return Response(context)
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)




class InitialAssessmentCreateAPIView(APIView):
    def post(self, request):
        context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
        try:
            serializer = InitialAssessmentSerializer(data=request.data)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)


# class InitialAssessmentView(APIView):

#     def get(self, request):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             assessments = InitialAssessment.objects.all()
#             serializer = InitialAssessmentSerializer(assessments, many=True)
#             context["data"] = serializer.data
#             return Response(context)
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def post(self, request):
#         context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
#         try:
#             validator = InitialAssessmentSerializer(data=request.data)
#             if not validator.is_valid():
#                 raise SerializerError(validator.errors)
            
#             validator.save()
#             context["data"] = validator.data
#             return Response(context)
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)




class CarePlanFeedbackRetrieveAPIView(APIView):
    def get(self, request):
        context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
        try:
            feedbacks = CarePlanFeedback.objects.all()
            serializer = CarePlanFeedbackSerializer(feedbacks, many=True)
            context["data"] = serializer.data
            return Response(context)
        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)




class CarePlanFeedbackCreateAPIView(APIView):
    def post(self, request):
        context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
        try:
            serializer = CarePlanFeedbackSerializer(data=request.data)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)


# class CarePlanFeedbackView(APIView):

#     def get(self, request):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             feedbacks = CarePlanFeedback.objects.all()
#             serializer = CarePlanFeedbackSerializer(feedbacks, many=True)
#             context["data"] = serializer.data
#             return Response(context)
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def post(self, request):
#         context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
#         try:
#             validator = CarePlanFeedbackSerializer(data=request.data)
#             if not validator.is_valid():
#                 raise SerializerError(validator.errors)
            
#             validator.save()
#             context["data"] = validator.data
#             return Response(context)
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)




class RiskFactorsRetrieveAPIView(APIView):
    def get(self, request):
        context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
        try:
            risk1_data = RiskFactor1.objects.all()
            risk2_data = RiskFactor2.objects.all()
            risk3_data = RiskFactor3.objects.all()
            risk4_data = RiskFactor4.objects.all()
            risk5_data = RiskFactor5.objects.all()

            context["data"] = {
                "risk_factor1": RiskFactor1Serializer(risk1_data, many=True).data,
                "risk_factor2": RiskFactor2Serializer(risk2_data, many=True).data,
                "risk_factor3": RiskFactor3Serializer(risk3_data, many=True).data,
                "risk_factor4": RiskFactor4Serializer(risk4_data, many=True).data,
                "risk_factor5": RiskFactor5Serializer(risk5_data, many=True).data,
            }
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)




class RiskFactorCreateAPIView(APIView):
    def post(self, request):
        context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
        try:
            risk_type = request.data.get('risk_type')
            serializer_class = {
                "risk_factor1": RiskFactor1Serializer,
                "risk_factor2": RiskFactor2Serializer,
                "risk_factor3": RiskFactor3Serializer,
                "risk_factor4": RiskFactor4Serializer,
                "risk_factor5": RiskFactor5Serializer,
            }.get(risk_type)

            if not serializer_class:
                context["success"] = 0
                context["message"] = "Invalid risk_type"
                return Response(context)

            serializer = serializer_class(data=request.data)
            if not serializer.is_valid():
                context["success"] = 0
                context["message"] = serializer.errors
                return Response(context)

            serializer.save()
            context["data"] = serializer.data
            return Response(context)

        except Exception as e:
            context["success"] = 0
            context["message"] = str(e)
            return Response(context)


# class RiskFactorsCombinedView(APIView):

#     def get(self, request):
#         context = {"success": 1, "message": messages.DATA_RETRIEVED, "data": {}}
#         try:
#             risk1_data = RiskFactor1.objects.all()
#             risk2_data = RiskFactor2.objects.all()
#             risk3_data = RiskFactor3.objects.all()
#             risk4_data = RiskFactor4.objects.all()
#             risk5_data = RiskFactor5.objects.all()

#             context["data"] = {
#                 "risk_factor1": RiskFactor1Serializer(risk1_data, many=True).data,
#                 "risk_factor2": RiskFactor2Serializer(risk2_data, many=True).data,
#                 "risk_factor3": RiskFactor3Serializer(risk3_data, many=True).data,
#                 "risk_factor4": RiskFactor4Serializer(risk4_data, many=True).data,
#                 "risk_factor5": RiskFactor5Serializer(risk5_data, many=True).data,
#             }
#             return Response(context)
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)

#     def post(self, request):
#         context = {"success": 1, "message": messages.DATA_SAVED, "data": {}}
#         try:
#             risk_type = request.data.get('risk_type')
#             serializer_class = {
#                 "risk_factor1": RiskFactor1Serializer,
#                 "risk_factor2": RiskFactor2Serializer,
#                 "risk_factor3": RiskFactor3Serializer,
#                 "risk_factor4": RiskFactor4Serializer,
#                 "risk_factor5": RiskFactor5Serializer,
#             }.get(risk_type)

#             if not serializer_class:
#                 context["success"] = 0
#                 context["message"] = "Invalid risk_type"
#                 return Response(context)

#             validator = serializer_class(data=request.data)
#             if not validator.is_valid():
#                 raise SerializerError(validator.errors)
            
#             validator.save()
#             context["data"] = validator.data
#             return Response(context)
#         except Exception as e:
#             context["success"] = 0
#             context["message"] = str(e)
#             return Response(context)



