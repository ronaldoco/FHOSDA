from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
#Classe Problema
from .forms import ProblemaForm
from .models import Problema
# Classe Bibliotecainst
from .forms import BibliotecainstForm
from .models import Bibliotecainst



#################################
#  Pagina proncipal do Sistema  #
#################################
def home(request):
    return render(request, 'home.html')


######################
#  CRUD de Problema  #
######################
def problemaCadastro(request):
    problema_list = Problema.objects.all()
    
    problema_form = ProblemaForm()
    
    return render(request,'hosda/problemaCadastro.html', {'problema_list': problema_list, 'problema_form': problema_form})

def problemaSave(request):
    print 'POST ==============='
    print request.POST
    print 'GET================='
    print request.GET

    problema_form = ProblemaForm(request.POST or None)
    
    if problema_form.is_valid():
        form_clean = problema_form.cleaned_data
        
        pk = form_clean.get('id', None)
        if not pk:
            print 'Novo registro'
            problema_model = Problema(**form_clean)
            problema_model.save()
        else:
            print 'Editando registro'
            problema_model = get_object_or_404(Problema, pk=pk)
            
            problema_model.nome = form_clean.get('nome', '')
            problema_model.descricao = form_clean.get('descricao', '')
            problema_model.tipoproblema = form_clean.get('tipoproblema', '')
            problema_model.fluxoprocesso = form_clean.get('fluxoprocesso', '')
            problema_model.funcaoobjetivo = form_clean.get('funcaoobjetivo', '')
            
            problema_model.save()
        #return HttpResponseRedirect(reverse('home'))
    
    problema_list = Problema.objects.all()
    problema_form = ProblemaForm()
    return render(request, 'hosda/problemaCadastro.html', {'problema_list': problema_list, 'problema_form': problema_form})

def problemaEdit(request, problema_id):
    print 'POST ==============='
    print request.POST
    print 'GET================='
    print request.GET
    print problema_id
    problema_list = Problema.objects.all()
    problema = model_to_dict(get_object_or_404(Problema, pk=problema_id))
    problema_form = ProblemaForm(initial=problema)
    return render(request, 'hosda/problemaCadastro.html', {'problema_list': problema_list, 'problema_form': problema_form})


def problemaRemove(request, problema_id):
    problema = get_object_or_404(Problema, pk=problema_id)
    problema.delete()
    problema_form = ProblemaForm()
    problema_list = Problema.objects.all()
    return render(request, 'hosda/problemaCadastro.html', {'problema_list': problema_list, 'problema_form': problema_form})

def problemaList(request):
    problema_list = Problema.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        problema_list = problema_list.filter(nome__icontains=var_get_search)
    return render(request, 'hosda/problemaList.html', {'problema_list': problema_list})

############################
#  CRUD de Bibliotecainst  #
############################
def bibliotecainstCadastro(request):
    bibliotecainst_list = Bibliotecainst.objects.all()
    
    bibliotecainst_form = BibliotecainstForm()
    
    return render(request,'hosda/bibliotecainstCadastro.html', {'bibliotecainst_list': bibliotecainst_list, 'bibliotecainst_form': bibliotecainst_form})

def bibliotecainstSave(request):

    bibliotecainst_form = BibliotecainstForm(request.POST or None)
    
    if bibliotecainst_form.is_valid():
        form_clean = bibliotecainst_form.cleaned_data
        pk = form_clean.get('id', None)
        if not pk:
            print 'Novo registro'
            bibliotecainst_model = Bibliotecainst(**form_clean)
            bibliotecainst_model.save()
        else:
            print 'Editando registro'
            bibliotecainst_model = get_object_or_404(Bibliotecainst, pk=pk)
            
            bibliotecainst_model.nome = form_clean.get('nome', '')
            bibliotecainst_model.descricao = form_clean.get('descricao', '')
            bibliotecainst_model.processocriacao = form_clean.get('processocriacao', '')
            bibliotecainst_model.referencia = form_clean.get('referencia', '')
            bibliotecainst_model.diretorio = form_clean.get('diretorio', '')
            bibliotecainst_model.tipobenchmark = form_clean.get('tipobenchmark', '')
            bibliotecainst_model.problema = form_clean.get('problema', '')
            
            bibliotecainst_model.save()
        #return HttpResponseRedirect(reverse('home'))
    
    bibliotecainst_list = Bibliotecainst.objects.all()
    bibliotecainst_form = BibliotecainstForm()
    return render(request, 'hosda/bibliotecainstCadastro.html', {'bibliotecainst_list': bibliotecainst_list, 'bibliotecainst_form': bibliotecainst_form})

def bibliotecainstEdit(request, bibliotecainst_id):
    bibliotecainst_list = Bibliotecainst.objects.all()
    bibliotecainst = model_to_dict(get_object_or_404(Bibliotecainst, pk=bibliotecainst_id))
    bibliotecainst_form = BibliotecainstForm(initial=bibliotecainst)
    return render(request, 'hosda/bibliotecainstCadastro.html', {'bibliotecainst_list': bibliotecainst_list, 'bibliotecainst_form': bibliotecainst_form})

def bibliotecainstRemove(request, bibliotecainst_id):
    bibliotecainst = get_object_or_404(Bibliotecainst, pk=bibliotecainst_id)
    bibliotecainst.delete()
    bibliotecainst_form = BibliotecainstForm()
    bibliotecainst_list = Bibliotecainst.objects.all()
    return render(request, 'hosda/bibliotecainstCadastro.html', {'bibliotecainst_list': bibliotecainst_list, 'bibliotecainst_form': bibliotecainst_form})

def bibliotecainstList(request):
    bibliotecainst_list = Bibliotecainst.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        bibliotecainst_list = bibliotecainst_list.filter(nome__icontains=var_get_search)
    return render(request, 'hosda/bibliotecainstList.html', {'bibliotecainst_list': bibliotecainst_list})

