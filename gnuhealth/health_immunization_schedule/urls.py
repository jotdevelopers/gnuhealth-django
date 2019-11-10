from django.urls import path

from . import views

urlpatterns = [
    # Immunization module urls start

    path('vaccine_doses/', views.vaccine_doses, name = "vaccine_doses"),
    
	# Immunization urls end

]