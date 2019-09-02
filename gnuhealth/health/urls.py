from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('addpol', views.addpol, name='addpol'),
    path('addpolsubmit', views.addpolsubmit, name='addpolsubmit'),

]