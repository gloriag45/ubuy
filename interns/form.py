from django import forms
from .models import Task,Interns

class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields ='__all__'

class InternForm(forms.ModelForm):
    class Meta:
        model=Interns
        fields ='__all__'        