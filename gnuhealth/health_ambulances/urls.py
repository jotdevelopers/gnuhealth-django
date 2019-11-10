from django.urls import path

from . import views

urlpatterns = [
    # Ambulance Support module urls start

    path('ambulances_in_support_req_main/', views.ambulances_in_support_req_main, name = "ambulances_in_support_req_main"),
    path('ambulances_in_support_req_add/', views.ambulances_in_support_req_add, name = "ambulances_in_support_req_add"),
	
	# Ambulances Support urls end
]