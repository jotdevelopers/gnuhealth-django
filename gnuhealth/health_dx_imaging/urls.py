from django.urls import path

from . import views

urlpatterns = [
    # Dx-Imaging module urls start

    path('dx_imaging_requests/', views.dx_imaging_requests, name = "dx_imaging_requests"),
    path('dx_imaging_results/', views.dx_imaging_results, name = "dx_imaging_results"),
    path('dx_imaging_test_types/', views.dx_imaging_test_types, name = "dx_imaging_test_types"),
	
	# Dx-Imaging urls end
]