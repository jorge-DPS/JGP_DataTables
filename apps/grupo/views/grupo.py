import json
import datetime
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from apps.grupo.models import Grupo
#from apps.grupo.views.formulario import ZonaForm
from django.utils import timezone
from django.urls import reverse_lazy


class GrupoListView(TemplateView, PermissionRequiredMixin):
    permission_required="grupo.view_zona"
    template_name = 'version2/grupo_solidario/lista.html'
    def get_queryset(self):
        return Grupo.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grupo'] = Grupo.objects.filter(eliminado_en=None).order_by('-id')
        return context

class GrupoCreateView(CreateView,PermissionRequiredMixin):
    permission_required = "grupo.add_zona"
    model = Grupo
    template_name = 'version2/grupo_solidario/create.html'
    success_url = reverse_lazy('lista_grupo:grupo') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupo'] = timezone.now()
        return context

class GrupoUpdateView(TemplateView):
    model = Grupo
    template_name = 'version2/grupo_solidario/edit.html'
    menu = Grupo
    success_url = reverse_lazy('lista_grupo:grupo') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grupo'] = Grupo.objects.get(codigo_grupo=kwargs['codigo_grupo'])
        return context