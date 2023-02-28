from django.forms import ModelForm
from .models import Info 

class createInfo(ModelForm):
    class Meta:
        model = Info
        fields=['nombre', 'numero']

class personaEcargada(ModelForm):
    class Meta:
        model = Info
        fields=['tEncargado', 'contactado']
