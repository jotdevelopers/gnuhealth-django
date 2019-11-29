from django import forms
from health_demographics.models import *
from ajax_select.fields import AutoCompleteSelectMultipleField


class familyForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_family
        fields = "__all__"
        
class familyMemberForm(forms.ModelForm):
    class Meta:  
        model = gnuhealth_family_member
        fields = "__all__"


