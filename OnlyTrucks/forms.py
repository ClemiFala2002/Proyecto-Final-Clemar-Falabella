from django import forms
from OnlyTrucks.models import Camion, Remolques, Concesionaria

class CamionForm(forms.ModelForm):
    class Meta:
        model=Camion
        fields= '__all__'

class RemolquesForm(forms.ModelForm):
    class Meta:
        model=Remolques
        fields= '__all__'
        
        
class ConsesionariaForm(forms.ModelForm):
    class Meta:
        model=Concesionaria
        fields= '__all__'       