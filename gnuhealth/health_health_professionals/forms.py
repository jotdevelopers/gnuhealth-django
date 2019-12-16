from django import forms  
from health_health_professionals.models import *
from health_configuration.models import *
from health_party.models import *
from health_institutions.models import *
from django.forms import ModelMultipleChoiceField
from django_select2.forms import Select2MultipleWidget
class healthProfForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_healthprofessional   
        fields = "__all__" 
        name = ModelMultipleChoiceField(queryset=party_party.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        institution = ModelMultipleChoiceField(queryset=gnuhealth_institution.objects.values_list('name', flat=True), widget=Select2MultipleWidget)

        