import json
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView
from apps.administracion.models import (Persona)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView


class MenuMixin(object):
    menu = None

    def get_context_data(self, **kwargs):
        context = super(MenuMixin, self).get_context_data(**kwargs)
        context['menu'] = self.menu
        return context

class PersonaListView(LoginRequiredMixin, TemplateView):
    template_name = 'version2/persona/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        print("PERSONA--------->", Persona.objects.all())
        context['lista_personas'] = Persona.objects.filter(eliminado_en = None).order_by('-id')
        context['mensaje'] = "Este es un mensaje de prueba"
        return context

class PersonaCreateView(MenuMixin, LoginRequiredMixin, TemplateView ):
    template_name = 'version2/persona/create.html'
    model = Persona
    menu = "persona"

    def get_queryset(self):
        return super().get_queryset()

class PersonaReporteView(LoginRequiredMixin, TemplateView):
    template_name = 'version2/persona/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        persona = Persona.objects.get(pk=kwargs["pk"])
        print("PERSONA--------->", Persona.objects.all())
        context['lista_personas'] = Persona.objects.all()
        context['persona'] = persona
        return context

class PersonaDetalleView(LoginRequiredMixin, TemplateView):
    template_name = 'version2/persona/detalle.html'
    menu = "PERSONA"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        persona = Persona.objects.get(pk=kwargs["pk"])

        print("Persona--------->", Persona.objects.all())
        context['lista_personas'] = Persona.objects.all()
        context['persona'] = persona
        return context

class PersonaEditarView(LoginRequiredMixin, TemplateView, PermissionRequiredMixin):
    template_name = 'version2/persona/edit.html'
    menu = "DEPOSITOS"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['lista_personas'] = Persona.objects.all()
        context['persona'] = Persona.objects.get(id=kwargs['pk'])
    
        return context


