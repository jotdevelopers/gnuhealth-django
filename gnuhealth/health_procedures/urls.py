from django.urls import path

from . import views

urlpatterns = [
    # Procedures module urls start

    path('procedures_main/', views.procedures_main, name = "procedures_main"),
    
	# Procedures urls end
]