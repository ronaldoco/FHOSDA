from django import forms
from .models import Problema
from .models import Bibliotecainst

class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problema

class BibliotecainstForm(forms.ModelForm):
    class Meta:
        model = Bibliotecainst        
        