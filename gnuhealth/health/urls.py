from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_pol', views.add_pol, name='add_pol'),
    path('sankey', views.sankey,name='sankey'),
    path('visits', views.visits,name='visits'),
    path('sunburst', views.sunburst,name='sunburst'),
    path('radar', views.radar,name='radar'),


]