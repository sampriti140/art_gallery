from django import forms
from .models import*

class uform(forms.ModelForm):
    class Meta:
        model = prod
        fields = "__all__"

       
       
        

class dform(forms.ModelForm):
    class Meta:
        model = formation
        fields = "__all__"