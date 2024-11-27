from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


class EmpresaListView(ListView):
    model = models.Empresa
    template_name = 'empresa_list.html'
    context_object_name = 'empresas'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('razao_social')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class EmpresaCreateView(CreateView):
    model = models.Empresa
    template_name = 'empresa_create.html'
    form_class = forms.EmpresaForm
    success_url = reverse_lazy('empresa_list')


class EmpresaDetailView(DetailView):
    model = models.Empresa
    template_name = 'empresa_detail.html'


class EmpresaUpdateView(UpdateView):
    model = models.Empresa
    template_name = 'empresa_update.html'
    form_class = forms.EmpresaForm
    success_url = reverse_lazy('empresa_list')


class EmpresaDeleteView(DeleteView):
    model = models.Empresa
    template_name = 'empresa_delete.,tml'
    success_url = reverse_lazy('empresa_list')
