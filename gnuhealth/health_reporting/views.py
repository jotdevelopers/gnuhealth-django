from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")

# Reporting module functions start
def amputations_main(request):
	return render(request, "health_reporting/reporting-amputations.html")
	
def evaluations_reports_main(request):
	return render(request, "health_reporting/reporting-evaluations-report.html")
	
def injury_surveillance_system_main(request):
	return render(request, "health_reporting/reporting-injury-surveillance-system.html")
	
def operational_sectors_by_institution_add(request):
	return render(request, "health_reporting/reporting-operational-sectors-by-institution-add.html")
	
def operational_sectors_by_institution_main(request):
	return render(request, "health_reporting/reporting-operational-sectors-by-institution.html")
	
def ophthalmology_evaluation_add_findings(request):
	return render(request, "health_reporting/reporting-ophthalmology-evaluation-add-findings.html")
	
def ophthalmology_evaluation_add(request):
	return render(request, "health_reporting/reporting-ophthalmology-evaluation-add.html")
	
def ophthalmology_evaluation_main(request):
	return render(request, "health_reporting/reporting-ophthalmology-evaluation-main.html")
	
def patient_evaluations(request):
	return render(request, "health_reporting/reporting-patient-evaluations.html")
	
def protheses(request):
	return render(request, "health_reporting/reporting-protheses.html")
	
def socioeconomic_assessments_add(request):
	return render(request, "health_reporting/reporting-socio-economic-assessments-add.html")
	
def socioeconomic_assessments_main(request):
	return render(request, "health_reporting/reporting-socio-economic-assessments.html")
	
def specialties_by_health_professionals(request):
	return render(request, "health_reporting/reporting-specialties-by-health-professionals.html")
	
def specialties_by_institution_add(request):
	return render(request, "health_reporting/reporting-specialties-by-institution-add.html")
	
def specialties_by_institution_main(request):
	return render(request, "health_reporting/reporting-specialties-by-institution.html")
	
def summary_report_search_institution(request):
	return render(request, "health_reporting/reporting-summary-report-search-institution.html")
	
def summary_report_main(request):
	return render(request, "health_reporting/reporting-summary-report.html")
	
def top_diseases(request):
	return render(request, "health_reporting/reporting-top-diseases.html")
# Reporting module functions end    