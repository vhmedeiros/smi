from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class ClienteListView(ListView):
    model = models.Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        razao_social = self.request.GET.get('razao_social')

        if razao_social:
            queryset = queryset.filter(razao_social__icontains=razao_social)

        return queryset


class ClienteCreateView(CreateView):
    model = models.Cliente
    template_name = 'cliente_create.html'
    form_class = forms.ClienteForm
    success_url = reverse_lazy('cliente_list')


class ClienteDetailView(DetailView):
    model = models.Cliente
    template_name = 'cliente_detail.html'


class ClienteUpdateView(UpdateView):
    model = models.Cliente
    template_name = 'cliente_update.html'
    form_class = forms.ClienteForm
    success_url = reverse_lazy('cliente_list')


class ClienteDeleteView(DeleteView):
    model = models.Cliente
    template_name = 'cliente_delete.html'
    success_url = reverse_lazy('cliente_list')
