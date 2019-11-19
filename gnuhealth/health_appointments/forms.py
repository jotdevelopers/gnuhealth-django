from django import forms  
from health_appointments.models import *
class appointmentForm(forms.ModelForm):  
    class Meta:  
        model = gnuhealth_appointment   
        fields = "__all__" 