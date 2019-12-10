from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('labTestUnits', views.labTestUnits, name='labTestUnits'),
    path('addLabTestUnits', views.addLabTestUnits, name='addLabTestUnits'),
    path('editLabTestUnits/<id>/', views.editLabTestUnits, name='editLabTestUnits'),
    path('updateLabTestUnits/<id>/', views.updateLabTestUnits, name='updateLabTestUnits'),
    path('deleteLabTestUnits/<id>/', views.deleteLabTestUnits, name='deleteLabTestUnits'),

    path('labTestType', views.labTestType, name='labTestType'),
    path('addLabTestType', views.addLabTestType, name='addLabTestType'),
    path('editLabTestType/<id>/', views.editLabTestType, name='editLabTestType'),
    path('updateLabTestType/<id>/', views.updateLabTestType, name='updateLabTestType'),
    path('deleteLabTestType/<id>/', views.deleteLabTestType, name='deleteLabTestType'),

    # path('addlabtestrequest', views.addlabtestrequest, name='addlabtestrequest'),
    # path('labtestresult', views.labtestresult, name='labtestresult'),

    # # Laboratory module urls start

    # path('lab_test_types/', views.lab_test_types, name = "lab_test_types"),
    # path('lab_test_units/', views.lab_test_units, name = "lab_test_units"),
    
	# Laboratory urls end
]