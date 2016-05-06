from django.contrib import admin
from .models import Problema, Tipoproblema, Funcaoobjetivo, Fluxoprocesso
from .models import Bibliotecainst, Tipobenchmark
# Register your models here.


# Administracao de Problemas
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
    
admin.site.register(Problema, ProblemaAdmin)    
admin.site.register(Tipoproblema, TipoproblemaAdmin)
admin.site.register(Fluxoprocesso, FluxoprocessoAdmin)    
admin.site.register(Funcaoobjetivo, FuncaoobjetivoAdmin)

admin.site.register(Bibliotecainst, BibliotecainstAdmin)    
admin.site.register(Tipobenchmark, TipobenchmarkAdmin)

