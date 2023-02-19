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
from apps.contrib.api.viewsets import ModelCreateListViewSet
class ReporteRutas_excel(ModelCreateListViewSet):
    def excel(self, request):
        nombre='rutaejemplo'
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
        datos_clientes=datos_diccionario["cliente"]
        df_json = pd.json_normalize(datos_clientes)
        df_json.to_excel('reports/'+nombre+'.xlsx')
        return Response({"mensaje":"Se descargo el archivo "+nombre})
        
        

class ReporteRutas(View):

    def cabecera_logo(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = ImageReader('web/static/assets/media/Logos_JDGP/logomediano.jpg')
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen,1 * cm, 26 *cm,width=50*mm,height=50*mm,preserveAspectRatio=True)                
        #************************************ENCABEZADO***********************************************************************************************
        fecha_actual=datetime.now().strftime('%d/%m/%Y')
        user_actual=User.objects.get(id=self.request.user.pk)
#*****************VARIABLES GLOBALES****************************
        color_oscuro_R= 23.0/255
        color_oscuro_G= 25.0/255
        color_oscuro_B= 50.0/255
        color_plomo_RGB= 221
       #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("VeraBd", 16)
        pdf.setFillColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B) 
        pdf.drawString(10 * cm, 28.2 * cm , "Rutas")
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.setFont("Vera", 7)
        pdf.setFillColorRGB(0,0,0) 
        pdf.drawString(17.7 * cm,28.4 * cm,"Fecha: "+fecha_actual)
        pdf.drawString(17.7 * cm,28 * cm,"Usuario: "+user_actual.username)
#/////////////////////////////METODOS DE LOS DATOS EN CELDA************************************************
    def cabecera_datos(self,pdf,asesor,sucursal,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig):
         #*****************VARIABLES GLOBALES****************************
         #estilos de letras
        style = ParagraphStyle(
            name='Normal',
            fontName='Vera',
            fontSize=8,
            spaceAfter = 6,
            spaceBefore = 6,
            spaceShrinkage = 0.05,
            borderPadding = 5
        )
        color_oscuro_R= 23.0/255
        color_oscuro_G= 25.0/255
        color_oscuro_B= 50.0/255
        tamano_letra=8
        #******************************LINEAS GRUESAS*****************************
        pdf.setStrokeColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
        pdf.setFillColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
        pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
        pdf.roundRect(1*cm, 26.2*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
        #************************************ENCABEZADO***********************************************************************************************
#****************TEXTOS EN NEGRILLLAS
        pdf.setFont("VeraBd", 8)
        pdf.drawString(1 * cm, 26.8 * cm , "Asesor comercial:")
        pdf.drawString(8 * cm, 26.8 * cm , "Sucursal:")
        pdf.drawString(15 * cm, 26.8 * cm , "Periodo:")
###************************CELDAS DATOS PERSONALES ******************************************************
        self.asesor(pdf,style,asesor,row_celda,grid,fontsize,backgroud,valig)
        self.sucursal(pdf,style,sucursal,row_celda,grid,fontsize,backgroud,valig)
        self.periodo(pdf,style,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig)
        
#************************DATOS PERSONALES************************************************
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
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
                },
                
                {
                    "fecha": "10/11/2022 17:45",
                    "nombre": "Juan Carlos junior",
                    "apellidos": "Mamani Choquecallata",
                    "direccion": "Av america, Zona mariscal sucre de el alto",
                    "asunto": "Seguimiento",
                    "detalle": "Luis terraza",
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
        y = 510 #control de la cordenada desde abajo
        asesor=datos_diccionario["asesor_comercial"]
        sucursal=datos_diccionario["sucursal"]
        periodo_inicio=datos_diccionario["periodo_inicio"]
        periodo_final=datos_diccionario["periodo_final"]
        datos_clientes=datos_diccionario["cliente"]
        #Suma el total de monto
        suma=0
        for item in datos_clientes:
            suma=suma+float(item["monto"])
        print("suma total ",round(suma,3))
        total_suma=str(round(suma,3))
        #*****************VARIABLES GLOBALES****************************
        
        color_oscuro_R= 23.0/255
        color_oscuro_G= 25.0/255
        color_oscuro_B= 50.0/255
        tamano_letra=8
#************estilos de las celdas
        grid='GRID', (0, 0), (-1, -1), 1, colors.gray
        fontsize='FONTSIZE', (0, 0), (-1, -1), tamano_letra
        backgroud='BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))
        valig='VALIGN', (0,0), (-1, -1), 'MIDDLE'
        row_celda=14
        response = HttpResponse(content_type="application/pdf")
        #response['Content-Disposition'] = 'attachment; filename = Reporte'
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer,pagesize=portrait(A4))
        partes = datos_clientes 
        #************************************ENCABEZADO***********************************************************************************************
        self.cabecera_logo(pdf)
        self.cabecera_datos(pdf,asesor,sucursal,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig)
        ####################################################################################
    # esta es la parte de la paginacion
        max_len = 22 # se define la cantidad por pagina(previamente calculado)
        heigth_data = len(partes)  # se obtiene la longitud de la lista de datos a mostrar
        if heigth_data <= max_len: # si la cantidad de elementos de la lista es menor que la cantidad definida por paginas, en este caso 25 se pasa la lista tal cual
            partes = list(partes)
            
            self.tabla(pdf, partes,  y - (len(partes) * 21))
        
        elif heigth_data > max_len:
            partes = list(partes)[::-1] # esto es solo para invertir la lista
            pages_needed = math.ceil(float(heigth_data / max_len)) #se obtiene la cantidad de paginas necesarias a partir de la cantidad de datos en la lista
            iterator = max_len # se guarda el valor en un iterador
            for page in range(0, int(pages_needed)): # esta parte se explica por si sola
                    #----------------------------------------------
                total_paginas=str(len(range(0, int(pages_needed))))
                contador_paginas=str(page+1)
                pdf.setFont("Vera", 9)
                pdf.drawString(10.2 * cm, 0.5 * cm , contador_paginas+'/'+total_paginas)
                record = []
                if max_len < len(partes):
                    iterator = max_len
                else:
                    iterator = len(partes)
                for i in range(0, iterator):
                    record.append(partes.pop())
                if iterator > 0:
                    self.cabecera_logo(pdf)
                    self.cabecera_datos(pdf,asesor,sucursal,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig)
                    
                    #suma total
                    if((page+1)==len(range(0, int(pages_needed)))):
                        y_total= (y - (len(record)*21))-0.5*cm
                        pdf.setFont("VeraBd", 8)
                        pdf.drawString(17 * cm, y_total-0.1*cm , "Total:")
                        total_suma_cel=[total_suma]
                        detalle_orden = Table([total_suma_cel],colWidths=2*cm,rowHeights=11)
                        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),('ALIGN',(0,0),(-1,0),'RIGHT'),('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),]))
                        detalle_orden.wrapOn(pdf, 800, 600)
                        detalle_orden.drawOn(pdf, 18 * cm, y_total-0.2*cm)
                    #---------  
                    self.tabla(pdf, record, y - (len(record) * 21)) 
                      
                else:
                    #suma total
                    if((page+1)==len(range(0, int(pages_needed)))):
                        y_total= (y - (len(record)*21))-0.5*cm
                        pdf.setFont("VeraBd", 8)
                        pdf.drawString(17 * cm, y_total-0.1*cm , "Total:")
                        total_suma_cel=[total_suma]
                        detalle_orden = Table([total_suma_cel],colWidths=2*cm,rowHeights=11)
                        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),('ALIGN',(0,0),(-1,0),'RIGHT'),('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),]))
                        detalle_orden.wrapOn(pdf, 800, 600)
                        detalle_orden.drawOn(pdf, 18 * cm, y_total-0.2*cm)
                    #---------   
                    self.tabla(pdf, record, y - (len(record) * 21)) 
                    self.cabecera_logo(pdf)
                    self.cabecera_datos(pdf,asesor,sucursal,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig)
              
        #************************************ENCABEZADO***********************************************************************************************
        #pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
    
    def tabla(self, pdf, partes, y):
        width, height = A4
        styles=getSampleStyleSheet()
        dato = styles["Normal"]
        dato.agnment=TA_LEFT
        dato.fontSize=8
        flag = True
        
        headers = ['Fecha', 'Cliente', 'Dirección-Ubicación','Asunto','Detalle','Monto']
        lista=[(item['fecha'],Paragraph(item['nombre']+'\n'+item['apellidos'],dato),
                            Paragraph(item['direccion'],dato),Paragraph(item['asunto'],dato),
                            Paragraph(item['detalle'],dato),item['monto'])
                     for item in partes]
        
        table = Table([headers] + lista, colWidths=[2.7*cm, 4*cm, 4.5*cm , 2*cm,4.5 *cm,1.3*cm])
        table.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(4,0),'LEFT'),
                ('ALIGN', (5,0), (-1,-1), 'RIGHT'),
                ('LINEABOVE',(0,0),(-1,-1),1,colors.gray),
                ('GRID', (6, 0), (-1, -1), 0, colors.white),
                ('BOX',(0,0),(-1,-1),1,colors.gray),
                ('FONT', (0,0), (-1,0), 'VeraBd',8  ),
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        table.wrapOn(pdf, width, height)
        table.drawOn(pdf, 1*cm, y)
        
        pdf.showPage()
        
        
    def asesor(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [Paragraph(dato,style = style)]
        detalle_orden = Table([celda],colWidths=3.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 26.7 * cm)
    def sucursal(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [Paragraph(dato,style = style)]
        detalle_orden = Table([celda],colWidths=4*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 9.7 * cm, 26.7 * cm)
    def periodo(self,pdf,style,periodo_inicio,periodo_fin,row_celda,grid,fontsize,backgroud,valig):
        celda = [periodo_inicio+' al '+periodo_fin]
        detalle_orden = Table([celda],colWidths=3.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 16.5 * cm, 26.7 * cm)
    