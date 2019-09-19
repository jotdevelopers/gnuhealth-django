from django import forms  
from health.models import gnuhealth_pol  
class PolForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_pol   
        fields = "__all__" 