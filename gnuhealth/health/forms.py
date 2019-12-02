from django import forms  
from health.models import * 
class polForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_pol   
        fields = "__all__" 