from django import forms  
from health_health_professionals.models import *
from health_configuration.models import *
from django.forms import ModelMultipleChoiceField
from django_select2.forms import Select2MultipleWidget
class healthProfForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_healthprofessional   
        fields = "__all__" 
        