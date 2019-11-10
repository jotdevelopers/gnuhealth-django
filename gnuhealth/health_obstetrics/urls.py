from django.urls import path

from . import views

urlpatterns = [
    # Obstetrics module urls start

    path('obstetric_main/', views.obstetric_main, name = "obstetric_main"),
    path('obstetric_add/', views.obstetric_add, name = "obstetric_add"),
    path('perinatal_info_monitors/', views.perinatal_info_monitors, name = "perinatal_info_monitors"),
    path('perinatal_info/', views.perinatal_info, name = "perinatal_info"),
    path('prenatal_evaluations/', views.prenatal_evaluations, name = "prenatal_evaluations"),
    path('puerperium_monitor/', views.puerperium_monitor, name = "puerperium_monitor"),
    
	# Obstetrics module urls end
]