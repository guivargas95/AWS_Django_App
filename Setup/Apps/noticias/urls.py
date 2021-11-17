from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('<int:noticia_id>', views.noticia, name='noticia'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('criar/noticia', views.cria_noticia, name='cria_noticia'),
    path('deleta/<int:noticia_id>', views.deleta_noticia, name='deleta_noticia'),
    path('edita_noticia', views.atualiza_noticia, name='atualiza_noticia'),
    path('edita/<int:noticia_id>', views.edita_noticia, name='edita_noticia'),
    path('buscar', views.buscar, name='buscar'),
    path('buscar_dashboard', views.buscar_dashboard, name='buscar_dashboard'),
    #path('cria/receita', cria_receita, name='cria_receita'),
    #path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    #path('edita/<int:receita_id>', edita_receita, name='edita_receita'),
    #path('atualiza_receita', atualiza_receita, name='atualiza_receita'),
    
        
]