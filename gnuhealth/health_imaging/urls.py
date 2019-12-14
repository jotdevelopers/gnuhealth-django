from django.urls import path

from . import views

urlpatterns = [
    path('mainImagingTestTypes', views.mainImagingTestTypes, name='mainImagingTestTypes'),
    path('mainAddImagingTestType', views.mainAddImagingTestType, name='mainAddImagingTestType'),
    path('mainEditImagingTestType/<id>', views.mainEditImagingTestType, name='mainEditImagingTestType'),
    path('mainUpdateImagingTestType/<id>/', views.mainUpdateImagingTestType, name='mainUpdateImagingTestType'),
    path('mainDeleteImagingTestType/<id>/', views.mainDeleteImagingTestType, name='mainDeleteImagingTestType'),

    path('mainImagingTest', views.mainImagingTest, name='mainImagingTest'),
    path('mainAddImagingTest', views.mainAddImagingTest, name='mainAddImagingTest'),
    path('mainEditImagingTest/<id>', views.mainEditImagingTest, name='mainEditImagingTest'),
    path('mainUpdateImagingTest/<id>/', views.mainUpdateImagingTest, name='mainUpdateImagingTest'),
    path('mainDeleteImagingTest/<id>/', views.mainDeleteImagingTest, name='mainDeleteImagingTest'),

    path('imagingRequests', views.imagingRequests, name='imagingRequests'),
    path('addImagingRequest', views.addImagingRequest, name='addImagingRequest'),
    path('editImagingRequest/<id>/', views.editImagingRequest, name='editImagingRequest'),
    path('updateImagingRequest/<id>/', views.updateImagingRequest, name='updateImagingRequest'),
    path('deleteImagingRequest/<id>/', views.deleteImagingRequest, name='deleteImagingRequest'),
    path('searchPatient/<search_text>/', views.searchPatient, name='searchPatient'),
    path('searchDoctor/<search_text>/', views.searchDoctor, name='searchDoctor'),

    path('imagingResults', views.imagingResults, name='imagingResults'),
    path('addImagingResult', views.addImagingResult, name='addImagingResult'),
    path('editImagingResult/<id>/', views.editImagingResult, name='editImagingResult'),
    path('updateImagingResult/<id>/', views.updateImagingResult, name='updateImagingResult'),
    path('deleteImagingResult/<id>/', views.deleteImagingResult, name='deleteImagingResult'),
]