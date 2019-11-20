from django import forms
from health_hospitalizations.models import *

class mealOrderForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_inpatient_meal_order
        fields = "__all__"
        