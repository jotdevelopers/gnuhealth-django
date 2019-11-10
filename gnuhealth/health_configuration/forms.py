from django import forms
from health_configuration.models import gnuhealth_ethnicity


class ethnicityForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_ethnicity
        fields = "__all__"