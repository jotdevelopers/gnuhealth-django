from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('coming_soon', views.coming_soon, name='coming_soon'),
    path('visit-history', views.visitHistory, name='visit-history'),
    path('patient-visits', views.patientVisits, name='patient-visits'),
    path('patient-history', views.patientHistory, name='patient-history'),
    path('patient-tests', views.patientTests, name='patient-tests'),
]