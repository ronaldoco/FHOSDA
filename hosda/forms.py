#-*- encoding: utf-8 -*-
from django import forms

from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import extras
from django.forms.models import inlineformset_factory

from .models import Problema, Tipoproblema, Fluxoprocesso, Funcaoobjetivo
from .models import Bibliotecainst, Tipobenchmark
from .models import Algoritmo, Tipoexecucao, Heuristica
from .models import Pesquisa, Preprocessamento
from .models import Instancia
from .models import Parametro
from .models import Grupoteste
from .models import User
from .models import Grupotesteparametro

class ProblemaForm(forms.ModelForm):  
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Problema
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': '3'}),
        }

class BibliotecainstForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Bibliotecainst   
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': '3'}),
            'processocriacao': forms.Textarea(attrs={'rows': '3'}),
        }

class AlgoritmoForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Algoritmo   
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': '3'}),
            'estrategias': forms.Textarea(attrs={'rows': '3'}),
            'ambientedesenv': forms.Textarea(attrs={'rows': '3'}),
        }

class ParametroForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Parametro   
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': '3'}),
        }

class PesquisaForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Pesquisa   
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': '3'}),
            'objetivos': forms.Textarea(attrs={'rows': '3'}),
            'resultados': forms.Textarea(attrs={'rows': '3'}),
            'ambienteexec': forms.Textarea(attrs={'rows': '3'}),
        }

"""
class PesquisaForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    nome = forms.CharField(label='Nome', max_length=60)
    rotulo = forms.CharField(label='Rotulo', max_length=12)
    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '3'}), 
        label='Descrição', 
        max_length=500, 
    )
    objetivos = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '3'}), 
        label='Objetivos', 
        max_length=500, 
        required=False,
    )
    resultados = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '3'}), 
        label='Resultados Esperados', 
        max_length=500, 
        required=False,
    )
    equipe = forms.CharField(label='Equipe', max_length=200, required=False) 
    ambienteexec = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '3'}), 
        label='Ambiente de Execucao', 
        max_length=500, 
        required=False,
    )
    diretorio = forms.CharField(label='Diretório', max_length=100)
    preprocessamento = forms.ModelChoiceField(label='Pre-processamento', queryset=Preprocessamento.objects.all())
    problema = forms.ModelChoiceField(label='Problema', queryset=Problema.objects.all())
    bibliotecainst = forms.ModelChoiceField(label='Biblioteca de Instancias', queryset=Bibliotecainst.objects.all())
    algoritmos_pesq = forms.ModelMultipleChoiceField(
        label='Algoritmos Selecionados',
        queryset=Algoritmo.objects.all(),
        #widget=FilteredSelectMultiple("Algoritmos", is_stacked=False)
    )
    benchmarks_exec = forms.ModelMultipleChoiceField(
        label='Benchmarks de Execução',
        queryset=Instancia.objects.all()
    )
    benchmarks_test = forms.ModelMultipleChoiceField(
        label='Benchmarks de Teste',
        queryset=Instancia.objects.all()
    )
    usuario = forms.ModelChoiceField(label='Usuario', queryset=User.objects.all())
"""

class InstanciaForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Instancia   
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': '3'}),
        }

class GrupotesteForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    parametros_grupo = inlineformset_factory(Parametro, Grupotesteparametro, fk_name='parametro', fields=('parametro', 'valorparametrogrupo'))
    class Meta:
        model = Grupoteste   
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': '3'}),
        } 

class UserForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = User
"""            
class UserForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    password = forms.CharField(label='Senha', max_length=128)
    last_login = forms.DateTimeField(label='Ultimo Login', required=False)
    is_superuser = forms.BooleanField(label='Super-usuario')
    username = forms.CharField(label='Nome do usuario', max_length=30)
    first_name = forms.CharField(label='Primeiro Nome', max_length=30)
    last_name = forms.CharField(label='Ultimo Nomeo', max_length=30)
    email = forms.CharField(label='email', max_length=75)
    is_staff = forms.BooleanField(label='Equipe')
    is_activer = forms.BooleanField(label='Usuario ativo')
    date_joined = forms.DateTimeField(label='Data de Cadastro', required=False)

    """