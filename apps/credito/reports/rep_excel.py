import json

import requests
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView
from apps.cajas.models import (Caja)
from apps.accounts.models import User
from apps.empresa.models.sucursal import Sucursal

from django.views import View
from django.http import HttpResponse
from reportlab.platypus import *
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (Image, Table, Frame,BaseDocTemplate, Frame, Paragraph, 
                    NextPageTemplate, PageBreak, PageTemplate)
from reportlab.lib.units import inch,mm,cm
from reportlab.lib.utils import ImageReader
from PIL import Image
from reportlab.lib.pagesizes import A4
from django.conf import settings
from io import BytesIO
from django.views.generic import View
from reportlab.lib.pagesizes import letter, landscape
from datetime import datetime,timedelta
from rest_framework.response import Response
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, landscape, portrait
from reportlab.lib.enums import TA_CENTER,TA_LEFT

import math

import pandas as pd


class Convertidor(View):

   
    def get(self, request):
        #Datos json
        datos_JSON =  """
        {
            "asesor_comercial": "Sandra Villarreal",
            "sucursal": "El Carmen",
            "periodo_inicio": "01/11/2022",
            "periodo_final": "29/12/2022",
            "cliente": [
                {
                    "fecha": "03/11/2022 17:45",
                    "nombre": "Evelyn Tania ini1",
                    "apellidos": "Rocha Linares",
                    "direccion": "Av america, Zona Villa",
                    "asunto": "Evaluacion",
                    "detalle": "Luis terraza, prueba de texto largo en la celdaprueba de texto largo en la celda ",
                    "monto": "9.9"
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Evelyn Tania ini 2",
                    "apellidos": "Rocha Linares",
                    "direccion": "Av america, Zona Villa",
                    "asunto": "Evaluacion",
                    "detalle": "Marcelino Alejandro Maldonado choquecallata",
                    "monto": "9.9"
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos ini 3",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
                    "monto": "9.9"
                },
                
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos",
                    "apellidos": "Mamani ",
                    "direccion": "Av america de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis",
                    "monto": "9.9"
                },
                
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
                    "monto": "9.9"
                }
                
                
                
                
            ]
        }
        """
        # Convertir cadena de caracteres JSON a un diccionario
        datos_diccionario = json.loads(datos_JSON)
        asesor=datos_diccionario["asesor_comercial"]
        sucursal=datos_diccionario["sucursal"]
        periodo_inicio=datos_diccionario["periodo_inicio"]
        periodo_final=datos_diccionario["periodo_final"]
        datos_clientes=datos_diccionario["cliente"]
        df=pd.read_json(datos_clientes)
        df.to_excel('convertido.xls')
       