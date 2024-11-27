from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('veiculos.urls')),
    path('', include('clientes.urls')),
    path('', include('empresas.urls')),
    path('', include('noticias.urls')),
]

# Adiciona suporte para servir arquivos de mídia no modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
