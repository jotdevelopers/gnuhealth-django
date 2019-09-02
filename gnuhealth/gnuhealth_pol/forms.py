from django import forms  
from health.models import gnuhealth_pol  
class HealthpolForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_pol   
        fields = "__all__" 