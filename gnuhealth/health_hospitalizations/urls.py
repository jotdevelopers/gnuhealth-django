from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mealOrders', views.mealOrders, name='mealOrders'),
    path('addMealOrder', views.addMealOrder, name='addMealOrder'),
    path('editMealOrder/<id>', views.editMealOrder, name='editMealOrder'),
    path('updateMealOrder/<id>/', views.updateMealOrder, name='updateMealOrder'),
    path('deleteMealOrder/<id>/', views.deleteMealOrder, name='deleteMealOrder'),
]