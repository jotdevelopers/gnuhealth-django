from django import forms  
from health_genetics.models import gnuhealth_genetics  
class HealthGeneticsForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_genetics   
        fields = ['_all_'] 