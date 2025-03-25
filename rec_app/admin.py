from django.contrib import admin
from .models import Vitals, Patient, StaffUsers, LabResult

# Register your models here.

@admin.register(StaffUsers)
class StaffUsersAdmin(admin.ModelAdmin):
    list_display = ['id','name']




from django.contrib import admin
from .models import (
    InitialAssessment, CarePlanFeedback, 
    RiskFactor1, RiskFactor2, RiskFactor3, 
    RiskFactor4, RiskFactor5,NursingNote,
    ProgressNote,TreatmentChart,PainAssessment
)


# add notes

admin.site.register(NursingNote)

admin.site.register(ProgressNote)

@admin.register(TreatmentChart)
class TreatmentChartAdmin(admin.ModelAdmin):
    list_display = ('medicine_name', 'dose', 'time', 'created_at')


admin.site.register(PainAssessment)

# Register models
@admin.register(InitialAssessment)
class InitialAssessmentAdmin(admin.ModelAdmin):
    list_display=('rating_title', 'relationship_to_feedback', 'feedback_date', 'duration_of_experience','present_illness','past_illness','experience_feedback','health_feedback','hart_feedback','stroke_feedback','other_feedback')

@admin.register(CarePlanFeedback)
class CarePlanFeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_on_services','provisional_feedback','feedback_plan','expected_outcome_of_feedback','preventive_feedback_aspects')

@admin.register(RiskFactor1)
class RiskFactor1Admin(admin.ModelAdmin):
    list_display=('surgery_feedback','postpartum_feedback','condition_feedback','contraceptive_feedback','age_feedback','obesity_feedback')

@admin.register(RiskFactor2)
class RiskFactor2Admin(admin.ModelAdmin):
    list_display=('surgery_feedback','postpartum_feedback','condition_feedback','contraceptive_feedback','age_feedback','obesity_feedback')

@admin.register(RiskFactor3)
class RiskFactor3Admin(admin.ModelAdmin):
    list_display=('age_feedback', 'surgery_feedback','surgical_feedback','access_feedback','health_condition_feedback','feedback_on_condition','bedridden_feedback')

@admin.register(RiskFactor4)
class RiskFactor4Admin(admin.ModelAdmin):
    list_display=('history_of_feedback','heart_failure_feedback','resistance_feedback','deficiency_feedback','health_condition_feedback','feedback_on_condition','condition_feedback','thrombocytopenia_feedback','heart_feedback','infection_feedback','mutation_feedback', 'antibody_feedback','disorder_feedback','syndrome_feedback')

@admin.register(RiskFactor5)
class RiskFactor5Admin(admin.ModelAdmin):
    list_display=( 'elective_surgery_feedback', 'fracture_feedback','trauma_feedback' ,'surgery_feedback' , 'stroke_feedback','injury_feedback')