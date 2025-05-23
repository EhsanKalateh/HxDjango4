from django.urls import path
from .views import *

urlpatterns = [
    path('patient/check/', check_or_create_patient, name='corc_patient'),
    path('patient/new/', create_patient, name='new_patient_info'),
    path('patient/<slug:personal_id>/', calculate_zscore, name='zscore'),
    path('patient/<slug:personal_id>/overview/', patient_record_view, name='patient_records'),

]
