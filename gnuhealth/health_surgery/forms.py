from django import forms  
from health_surgery.models import gnuhealth_surgery  
class HealthSurgeryForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_surgery   
        fields = ['_all_'] 