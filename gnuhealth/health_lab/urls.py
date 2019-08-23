from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addlabtestrequest', views.addlabtestrequest, name='addlabtestrequest'),
    path('labtestresult', views.labtestresult, name='labtestresult'),
]