from django.conf.urls import patterns, include, url
from Framework.hosda.views import *

from django.contrib import admin

admin.autodiscover()

    
urlpatterns = patterns('Framework.hosda.views',
    # Examples:
    # url(r'^$', 'Framework.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #urls para pagina principal - HOME
    url(r'^$', 'home', name='home'),
    
    #urls da classe Problema
    url(r'^problema/$', 'problemaCadastro', name='problemaCadastro'),
    url(r'^problema/save$', 'problemaSave', name='problemaSave'),
    url(r'^problema/edit/(?P<problema_id>\d+)[/]$', 'problemaEdit', name='problemaEdit'),
    url(r'^problema/remove/(?P<problema_id>\d+)[/]$', 'problemaRemove', name='problemaRemove'),
    url(r'^problema/list', 'problemaList', name='problemaList'),
     
    #urls da Bibliotecainst 
    url(r'^bibliotecainst/$', 'bibliotecainstCadastro', name='bibliotecainstCadastro'),
    url(r'^bibliotecainst/save$', 'bibliotecainstSave', name='bibliotecainstSave'),
    url(r'^bibliotecainst/edit/(?P<bibliotecainst_id>\d+)[/]$', 'bibliotecainstEdit', name='bibliotecainstEdit'),
    url(r'^bibliotecainst/remove/(?P<bibliotecainst_id>\d+)[/]$', 'bibliotecainstRemove', name='bibliotecainstRemove'),
    url(r'^bibliotecainst/list', 'bibliotecainstList', name='bibliotecainstList'),  
    
    #urls de library
    #url(r'^$', 'library.views.index', name='index'),
    #url(r'^save/$', 'library.views.save', name='book.save'),
    #url(r'^edit/(?P<book_id>\d+)[/]$', 'library.views.edit', name='book.edit'),
    #url(r'^remove/(?P<book_id>\d+)[/]$', 'library.views.remove', name='book.remove'),
    
    
    #urls de bands
    #url(r'^bands/$', 'band_listing', name='bands'),
    #url(r'^bands/(?P<pk>\d+)/$', 'band_detail', name='band_detail'),
    #url(r'^bandform/$', BandForm.as_view(), name='band_form'),
    #url(r'^memberform/$', MemberForm.as_view(), name='member_form'),
    #url(r'^contact/$', 'band_contact', name='contact'),
    #url(r'^protected/$', 'protected_view', name='protected'),
    #url(r'^accounts/login/$', 'message'),
    
    url(r'^admin/', include(admin.site.urls), name='admin'),
    # to INSTALLED_APPS to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
