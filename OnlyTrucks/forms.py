from django import forms
from OnlyTrucks.models import Camion, Remolques

class CamionForm(forms.ModelForm):
    class Meta:
        model=Camion
        fields= '__all__'

class RemolquesForm(forms.ModelForm):
    class Meta:
        model=Remolques
        fields= '__all__'
        
        
  