import json
import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (TemplateView, DetailView, CreateView)
from braces.views import LoginRequiredMixin
from apps.zona.models import Zona
from apps.zona.views.formulario import ZonaForm
from django.utils import timezone
from django.urls import reverse_lazy

#--------DATATABLES-----
class Datatableslocalidad(TemplateView):
    #permission_required="zona.view_zona"
    # PARA VER DEL TEMPLATE DE ALEX 
    template_name = 'version2/zona/list_data.html'
    #FUERA DEL VERSION2
    #template_name = 'datatables.html'
#-----------------FIN DATATABLES


class ZonaListView(PermissionRequiredMixin,LoginRequiredMixin,TemplateView):
    permission_required="zona.view_zona" 
    template_name = 'version2/zona/lista.html'
    def get_queryset(self):
        return Zona.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['zona'] = Zona.objects.filter(eliminado_en=None).order_by('-id')
        return context

class ZonaCreateView(PermissionRequiredMixin,CreateView):
    permission_required = "zona.add_zona"
    model = Zona
    form_class = ZonaForm
    template_name = 'version2/zona/create.html'
    permission_denied_message = 'no esta autorizado'
    #success_url = reverse_lazy('lista_zona:zona') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zona'] = timezone.now()
        return context

class ZonaUpdateView(PermissionRequiredMixin,TemplateView):
    permission_required="zona.change_zona"
    model = Zona
    #fields = ['descripcion', 'localidad']
    form_class = ZonaForm
    template_name = 'version2/zona/edit.html'
    menu = Zona
    #success_url = reverse_lazy('lista_zona:zona') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zona'] = Zona.objects.get(id=kwargs['pk'])
        return context

class ZonaDetalleView(PermissionRequiredMixin,TemplateView):
    permission_required="zona.view_zona"
    model = Zona
    form_class = ZonaForm
    template_name = 'version2/zona/detail.html'
    menu = Zona
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zona'] = Zona.objects.get(pk=kwargs['pk'])
        return context
