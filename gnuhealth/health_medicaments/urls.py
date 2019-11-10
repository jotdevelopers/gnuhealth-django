from django.urls import path

from . import views

urlpatterns = [
    # Medicaments module urls start

    path('medicament_main/', views.medicament_main, name = "medicament_main"),
    path('medication_frequencies/', views.medication_frequencies, name = "medication_frequencies"),
	
	# Medicaments urls end
]