from django.urls import path

from . import views

urlpatterns = [
    # Reporting module urls start

    path('amputations_main/', views.amputations_main, name = "amputations_main"),
    path('evaluations_reports_main/', views.evaluations_reports_main, name = "evaluations_reports_main"),
    path('injury_surveillance_system_main/', views.injury_surveillance_system_main, name = "injury_surveillance_system_main"),
    path('operational_sectors_by_institution_add/', views.operational_sectors_by_institution_add, name = "operational_sectors_by_institution_add"),
    path('operational_sectors_by_institution_main/', views.operational_sectors_by_institution_main, name = "operational_sectors_by_institution_main"),
    path('ophthalmology_evaluation_add_findings/', views.ophthalmology_evaluation_add_findings, name = "ophthalmology_evaluation_add_findings"),
    path('ophthalmology_evaluation_add/', views.ophthalmology_evaluation_add, name = "ophthalmology_evaluation_add"),
    path('ophthalmology_evaluation_main/', views.ophthalmology_evaluation_main, name = "ophthalmology_evaluation_main"),
    path('patient_evaluations/', views.patient_evaluations, name = "patient_evaluations"),
    path('protheses/', views.protheses, name = "protheses"),
    path('socioeconomic_assessments_add/', views.socioeconomic_assessments_add, name = "socioeconomic_assessments_add"),
    path('socioeconomic_assessments_main/', views.socioeconomic_assessments_main, name = "socioeconomic_assessments_main"),
    path('specialties_by_health_professionals/', views.specialties_by_health_professionals, name = "specialties_by_health_professionals"),
    path('specialties_by_institution_add/', views.specialties_by_institution_add, name = "specialties_by_institution_add"),
    path('specialties_by_institution_main/', views.specialties_by_institution_main, name = "specialties_by_institution_main"),
    path('summary_report_search_institution/', views.summary_report_search_institution, name = "summary_report_search_institution"),
    path('summary_report_main/', views.summary_report_main, name = "summary_report_main"),
    path('top_diseases/', views.top_diseases, name = "top_diseases"),
    
	# Reporting module urls end
]