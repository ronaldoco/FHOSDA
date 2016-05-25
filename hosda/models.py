#-*- encoding: utf-8 -*-

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
from django.forms import ModelForm
from django.contrib.auth.models import User
from setuptools.package_index import unique_values


class Tipoexecucao(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    codificacao = models.CharField(max_length=5, verbose_name = u'Codificação')
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Heuristica(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome') 
    codificacao = models.CharField(max_length=5, verbose_name = u'Codificação') 
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Algoritmo(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    rotulo = models.CharField(max_length=6, verbose_name = u'Rótulo')
    descricao = models.TextField(max_length=500, verbose_name = u'Descrição')
    estrategias = models.TextField(max_length=500, blank=True, null=True, verbose_name = u'Estartégias')
    referencias = models.CharField(max_length=200, blank=True, null=True, verbose_name = u'Referências')
    ambientedesenv = models.TextField(max_length=500, blank=True, null=True, verbose_name = u'Ambiente de Desenvolvimento')
    parametros = models.CharField(max_length=200, blank=True, null=True, verbose_name = u'Parâmetros')
    nomearquivo = models.CharField(max_length=45, verbose_name = u'Nome do Arquivo')
    diretorio = models.CharField(max_length=100, verbose_name = u'Diretório')
    tipoexecucao = models.ForeignKey(Tipoexecucao, verbose_name = u'Tipo de Execução')
    heuristica = models.ForeignKey(Heuristica, verbose_name = u'Heurística')
    usuario = models.ForeignKey(User, verbose_name = u'Usuário')
    class Meta:
        ordering = ['nome']
        verbose_name = 'Algoritmo'
        verbose_name_plural = 'Algoritmos'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Fluxoprocesso(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    codificacao = models.CharField(max_length=5, verbose_name = u'Codificação')
    class Meta:
        ordering = ['codificacao']
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Funcaoobjetivo(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    codificacao = models.CharField(max_length=5, verbose_name = u'Codificação')
    class Meta:
        ordering = ['codificacao']
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Parametro(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    descricao = models.CharField(max_length=200, blank=True, null=True, verbose_name = u'Descrição')
    melhorvalor = models.FloatField(blank=True, null=True, verbose_name = u'Melhor Valor')
    ordem = models.IntegerField(unique = True, verbose_name = u'Ordem')
    algoritmo = models.ForeignKey(Algoritmo, verbose_name = u'Algoritmo')
    class Meta:
        ordering = ['nome']
        verbose_name = 'Parâmetro'
        verbose_name_plural = 'Parâmetros'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Grupoteste(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    descricao = models.CharField(max_length=200, blank=True, null=True, verbose_name = u'Descrição')
    algoritmo = models.ForeignKey(Algoritmo, verbose_name = u'Algoritmo')
    parametros_grupo = models.ManyToManyField(
        Parametro,
        verbose_name = u'Parâmetros - Grupo de Teste',
        through='Grupotesteparametro',
        related_name='parametros_grupo'
    )

class Grupotesteparametro(models.Model):
    grupoteste = models.ForeignKey(Grupoteste, verbose_name = u'Grupo de Teste')
    parametro = models.ForeignKey(Parametro, verbose_name = u'Parametro')
    valorparametrogrupo = models.FloatField(null=True, verbose_name = u'Valor de parametro no Grupo')
    class Meta():
        auto_created=True

class Preprocessamento(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    codificacao = models.CharField(max_length=5, verbose_name = u'Codificação')
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Tipoproblema(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    codificacao = models.CharField(max_length=5, verbose_name = u'Codificação')
    class Meta:
        ordering = ['codificacao']
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)
    def __str__(self):
        return self.nome

class Problema(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    descricao = models.TextField(max_length=500,  verbose_name = u'Descrição')
    tipoproblema = models.ForeignKey(Tipoproblema,  verbose_name = u'Tipo de Problema')
    fluxoprocesso = models.ForeignKey(Fluxoprocesso,  verbose_name = u'Fluxo de Processo')
    funcaoobjetivo = models.ForeignKey(Funcaoobjetivo,  verbose_name = u'Função Objetivo')
    class Meta:
        ordering = ['id']
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Tipobenchmark(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    codificacao = models.CharField(max_length=5, verbose_name = u'Codificação')
    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.codificacao)

class Bibliotecainst(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome') 
    descricao = models.TextField(max_length=500, verbose_name = u'Descrição')
    processocriacao = models.TextField(max_length=500, blank=True, null=True, verbose_name = u'Pré-processamento')
    referencia = models.CharField(max_length=200, verbose_name = u'Referência')
    diretorio = models.CharField(max_length=200, verbose_name = u'Diretorio') #FilePathField(path='bibliotecas/'
    tipobenchmark = models.ForeignKey(Tipobenchmark, verbose_name = u'Tipo de Benchmark')
    problema = models.ForeignKey(Problema, verbose_name = u'Problema') 
    class Meta:
        ordering = ['id']
        verbose_name = 'Biblioteca de intâncias'
        verbose_name_plural = 'Bibliotecas de intâncias'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Instancia(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    descricao = models.TextField(max_length=500, verbose_name = u'Descrição')
    solucaootima = models.FloatField(blank=True, null=True, verbose_name = u'Solução Ótima') 
    melhorsolucao = models.FloatField(blank=True, null=True, verbose_name = u'Melhor Solução')
    datamelhorsolucao = models.DateField(blank=True, null=True, verbose_name = u'Data da Melhor Solução')
    nomearquivo = models.CharField(max_length=75, verbose_name = u'Nome do Arquivo')  #FileField(upload_to='/bibliotecas/',
    bibliotecainst = models.ForeignKey(Bibliotecainst, verbose_name = u'Biblioteca de Instância')
    class Meta:
        ordering = ['nome']
        verbose_name = 'Instância'
        verbose_name_plural = 'Instâncias'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Pesquisa(models.Model):
    nome = models.CharField(max_length=60, verbose_name = u'Nome')
    rotulo = models.CharField(max_length=12, verbose_name = u'Rótulo')
    descricao = models.TextField(max_length=500, verbose_name = u'Descrição')
    objetivos = models.TextField(max_length=500, blank=True, null=True, verbose_name = u'Objetivos')
    resultados = models.TextField(max_length=500, blank=True, null=True, verbose_name = u'Resultados')
    equipe = models.CharField(max_length=200, blank=True, null=True, verbose_name = u'Equipe')
    ambienteexec = models.TextField(max_length=500, blank=True, null=True, verbose_name = u'Ambiente de Execução')
    diretorio = models.CharField(max_length=100, verbose_name = u'Diretório')
    preprocessamento = models.ForeignKey(Preprocessamento, verbose_name = u'Pré-processamento')
    problema = models.ForeignKey(Problema, verbose_name = u'Problema')
    bibliotecainst = models.ForeignKey(Bibliotecainst, verbose_name = u'Biblioteca de Instâncias')
    algoritmos_pesq = models.ManyToManyField(
        Algoritmo,
        verbose_name = u'Algoritmo - Pesquisa',
        through='Pesquisaalgoritmo',
        related_name='algoritmos_pesq'
    )
    benchmarks_exec = models.ManyToManyField(
        Instancia,
        through='Benchmarkexecucao',
        related_name='benchmarks_exec+'
    )
    benchmarks_test = models.ManyToManyField(
        Instancia,
        through='Benchmarkteste',
        related_name='benchmarks_test+'
    )
    usuario = models.ForeignKey(User, verbose_name = u'Usuário')
    class Meta:
        ordering = ['nome']
        verbose_name = 'Pesquisa'
        verbose_name_plural = 'Pesquisas'
    def __unicode__(self):
        return self.nome
    def __str__(self):
        return self.nome

class Benchmarkexecucao(models.Model):
    pesquisa = models.ForeignKey(Pesquisa, verbose_name = u'Pesquisa')
    instancia = models.ForeignKey(Instancia, verbose_name = u'Instância')
    class Meta():
        auto_created=True
    def __unicode__(self):
        return self.instancia    

class Benchmarkteste(models.Model):
    pesquisa = models.ForeignKey(Pesquisa, verbose_name = u'Pesquisa')
    instancia = models.ForeignKey(Instancia, verbose_name = u'Instância')
    class Meta():
        auto_created=True
    def __unicode__(self):
        return self.instancia    

class Pesquisaalgoritmo(models.Model):
    pesquisa = models.ForeignKey(Pesquisa, verbose_name = u'Pesquisa', on_delete=models.CASCADE)
    algoritmo = models.ForeignKey(Algoritmo, verbose_name = u'Algoritmo', on_delete=models.CASCADE)
    class Meta():
        auto_created=True
    def __unicode__(self):
        return self.algoritmo    

class Execucao(models.Model):
    data = models.DateTimeField(verbose_name = u'Data Execução')
    solucaoexec = models.FloatField(verbose_name = u'Solução Execução')
    tempoexec = models.FloatField(blank=True, null=True, verbose_name = u'Tempo Exucução') 
    instancia = models.ForeignKey(Instancia, verbose_name = u'Instância')
    algoritmo = models.ForeignKey(Algoritmo, verbose_name = u'Algoritmo')
    pesquisa = models.ForeignKey(Pesquisa, verbose_name = u'Pesquisa')

class Parametrizacao(models.Model):
    data = models.DateTimeField(verbose_name = u'Data Parametrização')
    solucaoparam = models.FloatField(verbose_name = u'Solução Parametrização')
    tempoparam = models.FloatField(blank=True, null=True, verbose_name = u'Tempo Parametrização')
    instancia = models.ForeignKey(Instancia, verbose_name = u'Instância')
    grupoteste = models.ForeignKey(Grupoteste, verbose_name = u'Grupo de Teste')
    algoritmo = models.ForeignKey(Algoritmo, verbose_name = u'Algoritmo')
    pesquisa = models.ForeignKey(Pesquisa, verbose_name = u'Pesquisa')



