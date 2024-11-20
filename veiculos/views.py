from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class VeiculoListView(ListView):
    model = models.Veiculo
    template_name = 'veiculo_list.html'
    context_object_name = 'veiculos'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class VeiculoCreateView(CreateView):
    model = models.Veiculo
    template_name = 'veiculo_create.html'
    form_class = forms.VeiculoForm
    success_url = reverse_lazy('veiculo_list')


class VeiculoDetailView(DetailView):
    model = models.Veiculo
    template_name = 'veiculo_detail.html'


class VeiculoUpdateView(UpdateView):
    model = models.Veiculo
    template_name = 'veiculo_update.html'
    form_class = forms.VeiculoForm
    success_url = reverse_lazy('veiculo_list')


class VeiculoDeleteView(DeleteView):
    model = models.Veiculo
    template_name = 'veiculo_delete.html'
    success_url = reverse_lazy('veiculo_list')
