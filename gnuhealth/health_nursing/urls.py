from django.urls import path

from . import views

urlpatterns = [
    # Nursing module urls start

    path('ambulatory_care_main/', views.ambulatory_care_main, name = "ambulatory_care_main"),
    path('ambulatory_care_add/', views.ambulatory_care_add, name = "ambulatory_care_add"),
    path('roundings_main/', views.roundings_main, name = "roundings_main"),
    path('roundings_add/', views.roundings_add, name = "roundings_add"),
    
	# Nursing module urls end
]