from django.urls import path

from . import views

urlpatterns = [
	# Pediatrics module urls start

    path('newborn_main/', views.newborn_main, name = "newborn_main"),
    path('psc_main/', views.psc_main, name = "psc_main"),
    path('newborn_add', views.newborn_add, name = "newborn_add"),
    path('psc_add/', views.psc_add, name = "psc_add"),
    
	# Pediatrics module urls end
]