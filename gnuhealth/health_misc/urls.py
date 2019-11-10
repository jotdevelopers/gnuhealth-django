from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Misc module urls start

    path('pediatrics_growth_chart/', views.pediatrics_growth_chart, name = "pediatrics_growth_chart"),
	
	# Misc urls end
]