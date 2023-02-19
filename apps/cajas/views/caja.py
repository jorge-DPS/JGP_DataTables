import json
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView
from apps.cajas.models import (Caja)


class MenuMixin(object):
    menu = None

    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['menu'] = self.menu
        return context


class CajaListView(LoginRequiredMixin, TemplateView):
    template_name = 'version2/caja/list.html'
    menu="CAJA"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['lista_cajas'] = Caja.objects.order_by('-id')
        return context

class CajaView(LoginRequiredMixin, TemplateView):
    template_name = 'version2/caja/create.html'
    menu="CAJA"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['mensaje'] = "Este es un mensaje de prueba"
        return context

class CajaImprimirView(TemplateView):
    template_name = 'version2/caja/report.html'
    menu = "CAJA"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        caja = Caja.objects.get(pk=kwargs["pk"])
        context['lista_cajas'] = Caja.objects.all()
        context['caja'] = caja
        return context
