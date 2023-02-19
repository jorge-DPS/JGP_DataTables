import json
import datetime
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView
from apps.procesos.arqueo.models import (Caja)

class MenuMixin(object):
    menu = None

    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['menu'] = self.menu
        return context


class CajaListView(MenuMixin, LoginRequiredMixin, TemplateView):
    template_name = 'version2/caja/arqueo/list.html'
    menu = "CAJA"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['lista_caja'] = Caja.objects.order_by('-id')
        return context


class CajaCreateView(MenuMixin, LoginRequiredMixin, TemplateView):
    template_name = 'version2/caja/arqueo/create.html'
    menu = "CAJA"

    def get_queryset(self):
        return super().get_queryset()

class CajaDetalleView(LoginRequiredMixin, TemplateView):
    template_name = 'version2/caja/arqueo/detalle.html'
    menu = "CAJA"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        caja = Caja.objects.get(pk=kwargs["pk"])

        print("CAJA--------->", Caja.objects.all())
        context['lista_caja'] = Caja.objects.all()
        context['caja'] = caja
        return context

class CajaImprimirView(TemplateView):
    template_name = 'version2/caja/arqueo/report.html'
    menu = "CAJA"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        caja = Caja.objects.get(pk=kwargs["pk"])
        context['lista_caja'] = Caja.objects.all()
        context['caja'] = caja
        return context
