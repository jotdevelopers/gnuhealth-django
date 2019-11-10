from django.urls import path

from . import views

urlpatterns = [
    # Support Center module urls start

    path('support_center_main/', views.support_center_main, name = "support_center_main"),
    path('support_center_add/', views.support_center_add, name = "support_center_add"),
    path('ambulances/', views.ambulances, name = "ambulances"),
    
	# Support Center module urls end
]