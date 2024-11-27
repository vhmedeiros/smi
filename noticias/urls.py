from django.urls import path
from . import views

urlpatterns = [
    # Rotas para notícias
    path('noticias/list/', views.NoticiaListView.as_view(), name='noticia_list'),
    path('noticias/create/', views.NoticiaCreateView.as_view(),
         name='noticia_create'),
    path('noticias/<int:pk>/detail/', views.NoticiaDetailView.as_view(),
         name='noticia_detail'),
    path('noticias/<int:pk>/update/', views.NoticiaUpdateView.as_view(),
         name='noticia_update'),

    # Rotas para gerenciar editorias
    path('editorias/create/', views.EditoriaCreateView.as_view(),
         name='editoria_create'),
    path('editorias/delete/<int:pk>/',
         views.EditoriaDeleteView.as_view(), name='editoria_delete'),

    # Rotas para gerenciar tipos de notícias
    path('tipos-noticia/create/', views.TipoNoticiaCreateView.as_view(),
         name='tipo_noticia_create'),
    path('tipos-noticia/delete/<int:pk>/',
         views.TipoNoticiaDeleteView.as_view(), name='tipo_noticia_delete'),
]
