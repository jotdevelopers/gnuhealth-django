from django import forms  
from health_genetics.models import gnuhealth_patient_genetic_risk  
class HealthGeneticsForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_patient_genetic_risk   
        fields = "__all__" 