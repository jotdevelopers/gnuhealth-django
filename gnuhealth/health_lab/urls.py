from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addlabtestrequest', views.addlabtestrequest, name='addlabtestrequest'),
    path('labtestresult', views.labtestresult, name='labtestresult'),

    # Laboratory module urls start

    path('lab_test_types/', views.lab_test_types, name = "lab_test_types"),
    path('lab_test_units/', views.lab_test_units, name = "lab_test_units"),
    
	# Laboratory urls end
]