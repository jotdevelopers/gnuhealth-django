from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('labRequests', views.labRequests, name='labRequests'),
    path('addLabRequest', views.addLabRequest, name='addLabRequest'),
    path('editLabRequest/<id>/', views.editLabRequest, name='editLabRequest'),
    path('updateLabRequest/<id>/', views.updateLabRequest, name='updateLabRequest'),
    path('deleteLabRequest/<id>/', views.deleteLabRequest, name='deleteLabRequest'),
    #path('searchPatient/<search_text>/', views.searchPatient, name='searchPatient'),
    #path('searchType/<search_text>/', views.searchType, name='searchType'),
    #path('searchDoctor/<search_text>/', views.searchDoctor, name='searchDoctor'),

    path('labResults', views.labResults, name='labResults'),
    path('addLabResult', views.addLabResult, name='addLabResult'),
    path('editLabResult/<id>/', views.editLabResult, name='editLabResult'),
    path('updateLabResult/<id>/', views.updateLabResult, name='updateLabResult'),
    path('deleteLabResult/<id>/', views.deleteLabResult, name='deleteLabResult'),

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