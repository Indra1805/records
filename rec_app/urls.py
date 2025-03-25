from django.urls import path
from .views import (MedicalRecordAPIView,    
                    InitialAssessmentView,
                    CarePlanFeedbackView,
                    RiskFactorsCombinedView,
                    NursingNoteView,
                    ProgressNoteView,
                    TreatmentChartView,
                    PainAssessmentView)

urlpatterns = [
    # requests for records
    path('medical-records/', MedicalRecordAPIView.as_view(), name='medical-record-list-create'),
    path('medical-records/<int:pk>/', MedicalRecordAPIView.as_view(), name='medical-record-detail'),

    # requests for notes
    path('nursing-notes/', NursingNoteView.as_view(), name='nursing-notes'),
    path('treatment-chart/', TreatmentChartView.as_view(), name='treatment-chart'),
    path("progress-notes/", ProgressNoteView.as_view()),  # Create
    path("progress-notes/<int:pk>/", ProgressNoteView.as_view()),  # Update
    path('pain-assessments/', PainAssessmentView.as_view(), name='pain-assessment-list'),
    path('initial-assessment/', InitialAssessmentView.as_view(), name='initial-assessment-list'),
    path('care-plan-feedback/', CarePlanFeedbackView.as_view(), name='care-plan-feedback-list'),
    path('risk-factors/', RiskFactorsCombinedView.as_view(), name='risk-factors-combined'),
]
