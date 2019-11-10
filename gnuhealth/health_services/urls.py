from django.urls import path

from . import views

urlpatterns = [
    # Health Services module urls start

    path('health_services_main/', views.health_services_main, name = "health_services_main"),
    path('health_services_add/', views.health_services_add, name = "health_services_add"),
    path('created_invoices_main/', views.created_invoices_main, name = "created_invoices_main"),
    path('created_invoices_add/', views.created_invoices_add, name = "created_invoices_add"),
	
	# Health Services urls end
]