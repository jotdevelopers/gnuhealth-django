from django import forms  
from health_lab.models import gnuhealth_lab  
class HealthLabForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_lab   
        fields = ['_all_'] 