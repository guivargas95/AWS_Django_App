from django.contrib import admin
from .models import Noticias

class ListandoNoticias(admin.ModelAdmin):
    list_display = ('id', 'titulo_noticia', 'categoria_noticia')
    list_display_links = ('id', 'titulo_noticia')
    search_fields = ('titulo_noticia',)
    list_filter = ('categoria_noticia',)


admin.site.register(Noticias, ListandoNoticias)

