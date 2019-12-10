from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('coming_soon', views.coming_soon, name='coming_soon'),
    path('visit-history', views.visitHistory, name='visit-history'),
    path('patient-visits', views.patientVisits, name='patient-visits'),
    path('patient-history', views.patientHistory, name='patient-history'),
    path('patient-tests', views.patientTests, name='patient-tests'),

    path('nationOne', views.nationOne, name='nationOne'),
    path('d1', views.d1, name='d1'),
    path('c1', views.c1, name='c1'),
    path('n1', views.n1, name='n1'),

    path('nationTwo', views.nationTwo, name='nationTwo'),
    path('d2', views.d2, name='d2'),
    path('c2', views.c2, name='c2'),
    path('n2', views.n2, name='n2'),

    path('nationThree', views.nationThree, name='nationThree'),
    path('d3', views.d3, name='d3'),
    path('c3', views.c3, name='c3'),
    path('n3', views.n3, name='n3'),

    path('nationFour', views.nationFour, name='nationFour'),
    path('d4', views.d4, name='d4'),
    path('c4', views.c4, name='c4'),
    path('n4', views.n4, name='n4'),

    path('sunOne', views.sunOne, name='sunOne'),
    path('sd1', views.sd1, name='sd1'),
    path('sc1', views.sc1, name='sc1'),
    path('sj1', views.sj1, name='sj1'),

    path('sunTwo', views.sunTwo, name='sunTwo'),
    path('sd2', views.sd2, name='sd2'),
    path('sc2', views.sc2, name='sc2'),
    path('sj2', views.sj2, name='sj2'),

    path('treeOne', views.treeOne, name='treeOne'),
    path('td1', views.td1, name='td1'),
    path('tc1', views.tc1, name='tc1'),

    path('treeTwo', views.treeTwo, name='treeTwo'),
    path('td2', views.td2, name='td2'),
    path('tc2', views.tc2, name='tc2'),

    path('treeThree', views.treeThree, name='treeThree'),
    path('td3', views.td3, name='td3'),
    path('tc3', views.tc3, name='tc3'),

    path('treeFour', views.treeFour, name='treeFour'),
    path('td4', views.td4, name='td4'),
    path('tc4', views.tc4, name='tc4'),
]