from django import forms  
from health_surgery.models import * 

class surgeryForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_surgery
        fields = "__all__"
        