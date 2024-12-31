from django import forms
from .models import*

class add_workerform(forms.ModelForm):
    class Meta:
        model=addworker_model
        fields="__all__"

class add_jobform(forms.ModelForm):
    class Meta:
        model=addjob_model
        fields="__all__"        

class signupform(forms.ModelForm):
    class Meta:
        model=signupmodel
        fields="__all__" 

class contactform(forms.ModelForm):
    class Meta:
        model=contactmodel
        fields="__all__"               