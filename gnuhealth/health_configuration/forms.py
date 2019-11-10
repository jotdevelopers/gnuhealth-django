from django import forms
from health_configuration.models import gnuhealth_ethnicity
from health_configuration.models import gnuhealth_occupation

class ethnicityForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_ethnicity
        fields = "__all__"
        
        
class occupationForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_occupation
        fields = "__all__"