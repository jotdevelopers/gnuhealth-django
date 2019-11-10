from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('coming_soon', views.coming_soon, name='coming_soon'),
]