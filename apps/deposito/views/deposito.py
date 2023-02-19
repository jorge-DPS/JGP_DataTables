import json
import datetime
from django.views.generic import (TemplateView, DetailView, CreateView)
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.deposito.models import Deposito
from apps.deposito.views.formulario import DepositoForm
from django.utils import timezone
from django.urls import reverse_lazy


class ZonaListView(TemplateView, PermissionRequiredMixin):
    permission_required="deposito.view_zona"
    template_name = 'version2/deposito/lista.html'
    def get_queryset(self):
        return Deposito.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['deposito'] = Deposito.objects.filter(eliminado_en=None).order_by('-id')
        return context

class ZonaCreateView(CreateView,PermissionRequiredMixin):
    permission_required = "deposito.add_zona"
    model = Deposito
    form_class = DepositoForm
    template_name = 'version2/deposito/create.html'
    #success_url = reverse_lazy('lista_zona:deposito') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deposito'] = timezone.now()
        return context

class ZonaUpdateView(TemplateView):
    model = Deposito
    #fields = ['descripcion', 'localidad']
    form_class = DepositoForm
    template_name = 'version2/deposito/edit.html'
    menu = Deposito
    #success_url = reverse_lazy('lista_zona:deposito') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deposito'] = Deposito.objects.get(id=kwargs['pk'])
        return context