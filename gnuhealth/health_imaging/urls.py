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
]