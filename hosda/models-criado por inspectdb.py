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

class TbAlgoritmo(models.Model):
    idalgoritmo = models.IntegerField(db_column='IdAlgoritmo', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    rotulo = models.CharField(db_column='Rotulo', max_length=6) # Field name made lowercase.
    nomearquivo = models.CharField(db_column='NomeArquivo', max_length=45) # Field name made lowercase.
    diretorio = models.CharField(db_column='Diretorio', max_length=100) # Field name made lowercase.
    arqrelatorioalg = models.CharField(db_column='ArqRelatorioAlg', max_length=45) # Field name made lowercase.
    idtipoexecucao = models.ForeignKey('TbTipoexecucao', db_column='IdTipoExecucao') # Field name made lowercase.
    idheuristica = models.ForeignKey('TbHeuristica', db_column='IdHeuristica') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_algoritmo'

class TbBenchmarkexecucao(models.Model):
    idpesquisa = models.ForeignKey('TbPesquisa', db_column='IdPesquisa') # Field name made lowercase.
    idinstancia = models.ForeignKey('TbInstancia', db_column='IdInstancia') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_benchmarkexecucao'

class TbBenchmarkteste(models.Model):
    idpesquisa = models.ForeignKey('TbPesquisa', db_column='IdPesquisa') # Field name made lowercase.
    idinstancia = models.ForeignKey('TbInstancia', db_column='IdInstancia') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_benchmarkteste'

class TbBibliotecainst(models.Model):
    idbibliotecainst = models.IntegerField(db_column='IdBibliotecaInst', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200) # Field name made lowercase.
    processocriacao = models.CharField(db_column='ProcessoCriacao', max_length=200, blank=True) # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=200) # Field name made lowercase.
    diretorio = models.CharField(db_column='Diretorio', max_length=200) # Field name made lowercase.
    idtipobenchmark = models.ForeignKey('TbTipobenchmark', db_column='IdTipoBenchmark') # Field name made lowercase.
    idproblema = models.ForeignKey('TbProblema', db_column='IdProblema') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_bibliotecainst'

class TbExecucao(models.Model):
    idexecucao = models.IntegerField(db_column='IdExecucao', primary_key=True) # Field name made lowercase.
    data = models.DateField(db_column='Data') # Field name made lowercase.
    solucaoexec = models.FloatField(db_column='SolucaoExec') # Field name made lowercase.
    tempoexec = models.FloatField(db_column='TempoExec', blank=True, null=True) # Field name made lowercase.
    idinstancia = models.ForeignKey('TbInstancia', db_column='IdInstancia') # Field name made lowercase.
    idalgoritmo = models.ForeignKey(TbAlgoritmo, db_column='IdAlgoritmo') # Field name made lowercase.
    idpesquisa = models.ForeignKey('TbPesquisa', db_column='IdPesquisa') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_execucao'

class TbFluxoprocesso(models.Model):
    idfluxoprocesso = models.IntegerField(db_column='IdFluxoProcesso', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    codificacao = models.CharField(db_column='Codificacao', max_length=5) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_fluxoprocesso'

class TbFuncaoobjetivo(models.Model):
    idfuncaoobjetivo = models.IntegerField(db_column='IdFuncaoObjetivo', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    codificacao = models.CharField(db_column='Codificacao', max_length=5) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_funcaoobjetivo'

class TbGrupoteste(models.Model):
    idgrupoteste = models.IntegerField(db_column='IdGrupoTeste', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    idalgoritmo = models.ForeignKey(TbAlgoritmo, db_column='IdAlgoritmo') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_grupoteste'

class TbGrupotesteparametro(models.Model):
    idgrupoteste = models.ForeignKey(TbGrupoteste, db_column='IdGrupoTeste') # Field name made lowercase.
    idparametro = models.ForeignKey('TbParametro', db_column='IdParametro') # Field name made lowercase.
    valorparametrogrupo = models.FloatField(db_column='ValorParametroGrupo') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_grupotesteparametro'

class TbHeuristica(models.Model):
    idheuristica = models.IntegerField(db_column='IdHeuristica', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    codificacao = models.CharField(db_column='Codificacao', max_length=5) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_heuristica'

class TbInstancia(models.Model):
    idinstancia = models.IntegerField(db_column='IdInstancia', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200) # Field name made lowercase.
    solucaootima = models.FloatField(db_column='SolucaoOtima', blank=True, null=True) # Field name made lowercase.
    melhorsolucao = models.FloatField(db_column='MelhorSolucao') # Field name made lowercase.
    datamelhorsolucao = models.DateField(db_column='DataMelhorSolucao') # Field name made lowercase.
    nomearquivo = models.CharField(db_column='NomeArquivo', max_length=45) # Field name made lowercase.
    idbibliotecainst = models.ForeignKey(TbBibliotecainst, db_column='IdBibliotecaInst') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_instancia'

class TbParametrizacao(models.Model):
    idparametrizacao = models.IntegerField(db_column='IdParametrizacao', primary_key=True) # Field name made lowercase.
    data = models.DateField(db_column='Data') # Field name made lowercase.
    solucaoparam = models.FloatField(db_column='SolucaoParam') # Field name made lowercase.
    tempoparam = models.FloatField(db_column='TempoParam') # Field name made lowercase.
    idinstancia = models.ForeignKey(TbInstancia, db_column='IdInstancia') # Field name made lowercase.
    idgrupoteste = models.ForeignKey(TbGrupoteste, db_column='IdGrupoTeste') # Field name made lowercase.
    idalgoritmo = models.ForeignKey(TbAlgoritmo, db_column='IdAlgoritmo') # Field name made lowercase.
    idpesquisa = models.ForeignKey('TbPesquisa', db_column='IdPesquisa') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_parametrizacao'

class TbParametro(models.Model):
    idparametro = models.IntegerField(db_column='IdParametro', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    melhorvalor = models.FloatField(db_column='MelhorValor', blank=True, null=True) # Field name made lowercase.
    idalgoritmo = models.ForeignKey(TbAlgoritmo, db_column='IdAlgoritmo') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_parametro'

class TbPesquisa(models.Model):
    idpesquisa = models.IntegerField(db_column='IdPesquisa', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    rotulo = models.CharField(db_column='Rotulo', max_length=12) # Field name made lowercase.
    diretorio = models.CharField(db_column='Diretorio', max_length=100) # Field name made lowercase.
    arqrelatoriopesq = models.CharField(db_column='ArqRelatorioPesq', max_length=45) # Field name made lowercase.
    idpreprocessamento = models.ForeignKey('TbPreprocessamento', db_column='IdPreProcessamento') # Field name made lowercase.
    idproblema = models.ForeignKey('TbProblema', db_column='IdProblema') # Field name made lowercase.
    idbibliotecainst = models.ForeignKey(TbBibliotecainst, db_column='IdBibliotecaInst') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_pesquisa'

class TbPesquisaalgoritmo(models.Model):
    idpesquisa = models.ForeignKey(TbPesquisa, db_column='IdPesquisa') # Field name made lowercase.
    idalgoritmo = models.ForeignKey(TbAlgoritmo, db_column='IdAlgoritmo') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_pesquisaalgoritmo'

class TbPreprocessamento(models.Model):
    idpreprocessamento = models.IntegerField(db_column='IdPreProcessamento', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    codificacao = models.CharField(db_column='Codificacao', max_length=5) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_preprocessamento'

class TbProblema(models.Model):
    idproblema = models.IntegerField(db_column='IdProblema', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200) # Field name made lowercase.
    idtipoproblema = models.ForeignKey('TbTipoproblema', db_column='IdTipoProblema') # Field name made lowercase.
    idfluxoprocesso = models.ForeignKey(TbFluxoprocesso, db_column='IdFluxoProcesso') # Field name made lowercase.
    idfuncaoobjetivo = models.ForeignKey(TbFuncaoobjetivo, db_column='IdFuncaoObjetivo') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_problema'

class TbTipobenchmark(models.Model):
    idtipobenchmark = models.IntegerField(db_column='IdTipoBenchmark', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    codificacao = models.CharField(db_column='Codificacao', max_length=5) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_tipobenchmark'

class TbTipoexecucao(models.Model):
    idtipoexecucao = models.IntegerField(db_column='IdTipoExecucao', primary_key=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    codificacao = models.CharField(db_column='Codificacao', max_length=5) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_tipoexecucao'

class TbTipoproblema(models.Model):
    idtipoproblema = models.IntegerField(db_column='IdTipoProblema', unique=True) # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=60) # Field name made lowercase.
    codificacao = models.CharField(db_column='Codificacao', max_length=5) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_tipoproblema'

