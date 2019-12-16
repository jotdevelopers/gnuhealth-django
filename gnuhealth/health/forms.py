from django import forms  
from health.models import * 
from django import forms
from django.forms import ModelMultipleChoiceField
from health_configuration.models import *
from health_institutions.models import *
from health_party.models import *
from django_select2.forms import Select2MultipleWidget

class polForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_pol   
        fields = "__all__" 
        procedure = ModelMultipleChoiceField(queryset=gnuhealth_procedure.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        person = ModelMultipleChoiceField(queryset=party_party.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        institution = ModelMultipleChoiceField(queryset=gnuhealth_institution.objects.values_list('name', flat=True), widget=Select2MultipleWidget)
        health_condition = ModelMultipleChoiceField(queryset=gnuhealth_pathology.objects.values_list('name', flat=True), widget=Select2MultipleWidget)


class patientForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_patient   
        fields = "__all__" 
       