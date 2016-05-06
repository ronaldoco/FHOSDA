# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from setuptools.package_index import unique_values


class Tipoexecucao(models.Model):
    nome = models.CharField(max_length=60)
    codificacao = models.CharField(max_length=5)
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Heuristica(models.Model):
    nome = models.CharField(max_length=60) 
    codificacao = models.CharField(max_length=5) 
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Algoritmo(models.Model):
    nome = models.CharField(max_length=60)
    rotulo = models.CharField(max_length=6)
    descricao = models.TextField(max_length=500)
    estrategias = models.TextField(max_length=500, blank=True, null=True)
    referencias = models.CharField(max_length=200, blank=True, null=True)
    ambientedesenv = models.TextField(max_length=500, blank=True, null=True)
    parametros = models.CharField(max_length=200, blank=True, null=True)
    nomearquivo = models.CharField(max_length=45)
    diretorio = models.CharField(max_length=100)
    tipoexecucao = models.ForeignKey(Tipoexecucao)
    heuristica = models.ForeignKey(Heuristica)
    usuario = models.ForeignKey(User)
    class Meta:
        ordering = ['nome']
        verbose_name = 'algoritmo'
        verbose_name_plural = 'algoritmos'

class Fluxoprocesso(models.Model):
    nome = models.CharField(max_length=60)
    codificacao = models.CharField(max_length=5)
    class Meta:
        ordering = ['codificacao']
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Funcaoobjetivo(models.Model):
    nome = models.CharField(max_length=60)
    codificacao = models.CharField(max_length=5)
    class Meta:
        ordering = ['codificacao']
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Grupoteste(models.Model):
    nome = models.CharField(max_length=60)
    algoritmo = models.ForeignKey(Algoritmo)

class Parametro(models.Model):
    nome = models.CharField(max_length=60)
    melhorvalor = models.FloatField(blank=True, null=True)
    ordem = models.IntegerField(unique = True)
    algoritmo = models.ForeignKey(Algoritmo)
    class Meta:
        ordering = ['nome']
        verbose_name = 'parametro'
        verbose_name_plural = 'parametros'

class Grupotesteparametro(models.Model):
    grupoteste = models.ForeignKey(Grupoteste)
    parametro = models.ForeignKey(Parametro)
    valorparametrogrupo = models.FloatField()

class Preprocessamento(models.Model):
    nome = models.CharField(max_length=60)
    codificacao = models.CharField(max_length=5)
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Tipoproblema(models.Model):
    nome = models.CharField(max_length=60)
    codificacao = models.CharField(max_length=5)
    class Meta:
        ordering = ['codificacao']
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)
    def __str__(self):
        return self.nome

class Problema(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField(max_length=500)
    tipoproblema = models.ForeignKey(Tipoproblema)
    fluxoprocesso = models.ForeignKey(Fluxoprocesso)
    funcaoobjetivo = models.ForeignKey(Funcaoobjetivo)
    class Meta:
        ordering = ['id']
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Tipobenchmark(models.Model):
    nome = models.CharField(max_length=60)
    codificacao = models.CharField(max_length=5)
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Bibliotecainst(models.Model):
    nome = models.CharField(max_length=60) 
    descricao = models.TextField(max_length=500)
    processocriacao = models.TextField(max_length=500, blank=True, null=True)
    referencia = models.CharField(max_length=200)
    diretorio = models.CharField(max_length=200) #FilePathField(path='/bibliotecas/'
    tipobenchmark = models.ForeignKey(Tipobenchmark)
    problema = models.ForeignKey(Problema) 
    class Meta:
        ordering = ['id']
        verbose_name = 'Biblioteca de intancias'
        verbose_name_plural = 'Bibliotecas de intancias'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Instancia(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField(max_length=500)
    solucaootima = models.FloatField(blank=True, null=True) 
    melhorsolucao = models.FloatField(blank=True, null=True)
    datamelhorsolucao = models.DateField(blank=True, null=True)
    nomearquivo = models.CharField(max_length=75)  #FileField(upload_to='/bibliotecas/',
    bibliotecainst = models.ForeignKey(Bibliotecainst)
    class Meta:
        ordering = ['nome']
        verbose_name = 'Instancia'
        verbose_name_plural = 'Instancias'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Pesquisa(models.Model):
    nome = models.CharField(max_length=60)
    rotulo = models.CharField(max_length=12)
    descricao = models.TextField(max_length=500)
    objetivos = models.TextField(max_length=500, blank=True, null=True)
    resultados = models.TextField(max_length=500, blank=True, null=True)
    equipe = models.CharField(max_length=200, blank=True, null=True)
    ambienteexec = models.TextField(max_length=500, blank=True, null=True)
    diretorio = models.CharField(max_length=100)
    preprocessamento = models.ForeignKey(Preprocessamento)
    problema = models.ForeignKey(Problema)
    bibliotecainst = models.ForeignKey(Bibliotecainst)
    usuario = models.ForeignKey(User)
    class Meta:
        ordering = ['nome']
        verbose_name = 'Pesquisa'
        verbose_name_plural = 'Pesquisas'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Benchmarkexecucao(models.Model):
    pesquisa = models.ForeignKey(Pesquisa)
    instancia = models.ForeignKey(Instancia)

class Benchmarkteste(models.Model):
    pesquisa = models.ForeignKey(Pesquisa)
    instancia = models.ForeignKey(Instancia)

class Pesquisaalgoritmo(models.Model):
    pesquisa = models.ForeignKey(Pesquisa)
    algoritmo = models.ForeignKey(Algoritmo)

class Execucao(models.Model):
    data = models.DateTimeField()
    solucaoexec = models.FloatField()
    tempoexec = models.FloatField(blank=True, null=True) 
    instancia = models.ForeignKey(Instancia)
    algoritmo = models.ForeignKey(Algoritmo)
    pesquisa = models.ForeignKey(Pesquisa)

class Parametrizacao(models.Model):
    data = models.DateTimeField()
    solucaoparam = models.FloatField()
    tempoparam = models.FloatField(blank=True, null=True)
    instancia = models.ForeignKey(Instancia)
    grupoteste = models.ForeignKey(Grupoteste)
    algoritmo = models.ForeignKey(Algoritmo)
    pesquisa = models.ForeignKey(Pesquisa)



