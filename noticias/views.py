from datetime import date
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Noticia, Editoria, TipoDeNoticia
from veiculos.models import Veiculo
from clientes.models import Cliente
from . import forms


class NoticiaListView(ListView):
    model = Noticia
    template_name = 'noticia_list.html'
    context_object_name = 'noticias'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        titulo = self.request.GET.get('titulo')
        conteudo = self.request.GET.get('conteudo')
        veiculo = self.request.GET.get('veiculo')
        uf = self.request.GET.get('uf')
        cidade = self.request.GET.get('cidade')

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        if conteudo:
            queryset = queryset.filter(conteudo__icontains=conteudo)

        if veiculo:
            queryset = queryset.filter(veiculo__id=veiculo)

        if uf:
            queryset = queryset.filter(veiculo__uf=uf)

        if cidade:
            queryset = queryset.filter(veiculo__cidade=cidade)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lista de veículos
        context['veiculos'] = Veiculo.objects.all()
        # Lista de UFs únicas dos veículos
        context['ufs'] = Veiculo.objects.values_list(
            'uf', flat=True).distinct()

        # Filtro de cidades baseado na UF
        uf_selecionada = self.request.GET.get('uf')
        if uf_selecionada:
            context['cidades'] = Veiculo.objects.filter(
                uf=uf_selecionada
            ).order_by('cidade').values_list('cidade', flat=True).distinct()
        else:
            context['cidades'] = []

        # Adiciona a data atual ao contexto
        context['today'] = date.today()
        return context


class NoticiaCreateView(CreateView):
    model = Noticia
    template_name = 'noticia_create.html'
    form_class = forms.NoticiaForm
    success_url = reverse_lazy('noticia_list')


class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticia_detail.html'
    context_object_name = 'noticias'


class NoticiaUpdateView(UpdateView):
    model = Noticia
    template_name = 'noticia_update.html'
    form_class = forms.NoticiaForm
    # success_url = reverse_lazy('noticia_list')

# Views para editorias


class EditoriaCreateView(CreateView):
    model = Editoria
    template_name = 'editoria_form.html'
    fields = ['veiculo', 'name']
    success_url = reverse_lazy('noticia_create')


class EditoriaDeleteView(DeleteView):
    model = Editoria
    success_url = reverse_lazy('noticia_create')


# Views para tipos de notícias
class TipoNoticiaCreateView(CreateView):
    model = TipoDeNoticia
    template_name = 'tipo_noticia_form.html'
    fields = ['tipo']
    success_url = reverse_lazy('noticia_create')


class TipoNoticiaDeleteView(DeleteView):
    model = TipoDeNoticia
    success_url = reverse_lazy('noticia_create')
