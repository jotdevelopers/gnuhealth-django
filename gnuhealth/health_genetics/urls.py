from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addgenetics', views.addgenetics, name='addgenetics'),

]