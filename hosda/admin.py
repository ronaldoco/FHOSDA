from django.contrib import admin

from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import Problema, Tipoproblema, Funcaoobjetivo, Fluxoprocesso
from .models import Bibliotecainst, Tipobenchmark
from .models import Algoritmo, Tipoexecucao, Heuristica
from .models import Parametro
from .models import Pesquisa, Preprocessamento
from .models import Instancia
from .models import Grupoteste
from .models import Pesquisaalgoritmo, Benchmarkexecucao, Benchmarkteste
from .models import Grupotesteparametro



class ProblemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'tipoproblema', 'fluxoprocesso', 'funcaoobjetivo')
    ordering = ["nome"]
    search_fields = ("nome",)
    list_filter = ("nome",)

class TipoproblemaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codificacao')

class FluxoprocessoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codificacao')

class FuncaoobjetivoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codificacao')

# Administracao de Bibliotecas de Instancias
class BibliotecainstAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'processocriacao', 'referencia', 'diretorio', 'tipobenchmark', 'problema')
    ordering = ["nome"]
    search_fields = ("nome",)
    list_filter = ("nome",)

class TipobenchmarkAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codificacao')
    
class AlgoritmoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'rotulo', 'descricao', 'estrategias', 'referencias', 'ambientedesenv', 'parametros', 'nomearquivo', 'diretorio', 'tipoexecucao', 'heuristica', 'usuario')
    ordering = ["nome"]
    search_fields = ("nome",)
    list_filter = ("nome",)

class TipoexecucaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codificacao')
    
class HeuristicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codificacao')

class PesquisaAdmin(admin.ModelAdmin):
    list_display = (
                    'nome',
                    'rotulo',
                    'descricao',
                    'preprocessamento',
                    'problema',
                    'bibliotecainst',
    )
    algoritmos_pesq = {models.ManyToManyField: {'widget': FilteredSelectMultiple("algoritmos pesquisa", is_stacked=False)},}
    ordering = ["nome"]
    search_fields = ("nome",)
    list_filter = ("nome",)

class PreprocessamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codificacao')

class InstanciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'solucaootima', 'melhorsolucao', 'datamelhorsolucao', 'nomearquivo')
    ordering = ["nome"]
    search_fields = ("nome",)
    list_filter = ("nome",)

class ParametroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'melhorvalor', 'ordem', 'algoritmo')
    ordering = ["nome"]
    search_fields = ("nome",)
    list_filter = ("nome",)

class GrupotesteparametroInline(admin.TabularInline):
    model = Grupotesteparametro
    extra = 1

class GrupotesteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'algoritmo')
    ordering = ["nome"]
    search_fields = ("nome",)
    list_filter = ("nome",)
    inlines = (GrupotesteparametroInline,)
    exclude = ('parametros_grupo',)

admin.site.register(Problema, ProblemaAdmin)    
admin.site.register(Tipoproblema, TipoproblemaAdmin)
admin.site.register(Fluxoprocesso, FluxoprocessoAdmin)    
admin.site.register(Funcaoobjetivo, FuncaoobjetivoAdmin)

admin.site.register(Bibliotecainst, BibliotecainstAdmin)    
admin.site.register(Tipobenchmark, TipobenchmarkAdmin)

admin.site.register(Algoritmo, AlgoritmoAdmin)    
admin.site.register(Tipoexecucao, TipoexecucaoAdmin)
admin.site.register(Heuristica, HeuristicaAdmin)

admin.site.register(Pesquisa, PesquisaAdmin)
#admin.site.register(Pesquisa)

admin.site.register(Preprocessamento, PreprocessamentoAdmin)

admin.site.register(Instancia, InstanciaAdmin)

admin.site.register(Parametro, ParametroAdmin)

admin.site.register(Grupoteste, GrupotesteAdmin)

admin.site.register(Grupotesteparametro)

admin.site.register(Pesquisaalgoritmo)

admin.site.register(Benchmarkexecucao)

admin.site.register(Benchmarkteste)