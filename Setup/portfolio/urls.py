from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('em_breve', views.em_breve, name='em_breve'),
    #path('pizza', views.pizza, name='pizza'),
    #path('<int:receita_id>', views.receita, name='receita'),
    
    
]
