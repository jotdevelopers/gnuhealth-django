from django.urls import path

from . import views

urlpatterns = [
    path('mainImagingTestTypes', views.mainImagingTestTypes, name='mainImagingTestTypes'),
    path('mainAddImagingTestType', views.mainAddImagingTestType, name='mainAddImagingTestType'),
    path('mainEditImagingTestType/<id>', views.mainEditImagingTestType, name='mainEditImagingTestType'),
    path('mainUpdateImagingTestType/<id>/', views.mainUpdateImagingTestType, name='mainUpdateImagingTestType'),
    path('mainDeleteImagingTestType/<id>/', views.mainDeleteImagingTestType, name='mainDeleteImagingTestType'),
]