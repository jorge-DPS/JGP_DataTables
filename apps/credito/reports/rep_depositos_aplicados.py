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

class ReporteCreditoAplicados(View):

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
        pdf.drawString(8 * cm, 28.2 * cm , "Depósitos Aplicados")
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.setFont("Vera", 7)
        pdf.setFillColorRGB(0,0,0) 
        pdf.drawString(17.7 * cm,28.4 * cm,"Fecha: "+fecha_actual)
        pdf.drawString(17.7 * cm,28 * cm,"Usuario: "+user_actual.username)
#/////////////////////////////METODOS DE LOS DATOS EN CELDA************************************************
    def cabecera_datos(self,pdf,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig):
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
        #pdf.drawString(1 * cm, 26.8 * cm , "Asesor comercial:")
        #pdf.drawString(8 * cm, 26.8 * cm , "Sucursal:")
        pdf.drawString(15 * cm, 26.8 * cm , "Periodo:")
###************************CELDAS DATOS PERSONALES ******************************************************
        #self.asesor(pdf,style,asesor,row_celda,grid,fontsize,backgroud,valig)
        #self.sucursal(pdf,style,sucursal,row_celda,grid,fontsize,backgroud,valig)
        self.periodo(pdf,style,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig)
        
#************************DATOS PERSONALES************************************************
    def get(self, request, *args, **kwargs):
        #Datos json
        fecha_inicio=kwargs['fecha_inicio']
        fecha_fin=kwargs['fecha_fin']
        #fecha_fin='2025-01-03'
        #hora_inicio='2000:00'
        hora_inicio=kwargs['hora_inicio']
        #hora_fin='2023:59'
        hora_fin=kwargs['hora_fin']
        print("*********************fecha",fecha_inicio)
        
        
        datos_json = requests.get("http://192.168.100.30:8003/api/v1/cre/rep/depositos-aplicados?inicial="+fecha_inicio+"%"+hora_inicio+"&final="+fecha_fin+"%"+hora_fin).text
        datos_diccionario = json.loads(datos_json)
        estado=datos_diccionario["success"]
        
        y = 700 #control de la cordenada desde abajo
        periodo_inicio=fecha_inicio
        periodo_final=fecha_fin
        datos_clientes=datos_diccionario["data"]
        #Suma el total de monto
        suma=0
        for item in datos_clientes:
            suma=suma+float(item["monto_depositado"])
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
        self.cabecera_datos(pdf,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig)
        ####################################################################################
    # esta es la parte de la paginacion
        max_len = 26 # se define la cantidad por pagina(previamente calculado)
        heigth_data = len(partes)  # se obtiene la longitud de la lista de datos a mostrar
        if heigth_data <= max_len: # si la cantidad de elementos de la lista es menor que la cantidad definida por paginas, en este caso 25 se pasa la lista tal cual
            partes = list(partes)
            #suma total
            
            y_total= (y - (len(partes) * 25))-0.5*cm
            pdf.setFont("VeraBd", 8)
            pdf.drawString(17 * cm, y_total-0.1*cm , "Total:")
            total_suma_cel=[total_suma]
            detalle_orden = Table([total_suma_cel],colWidths=2*cm,rowHeights=11)
            detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),('ALIGN',(0,0),(-1,0),'RIGHT'),('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),]))
            detalle_orden.wrapOn(pdf, 800, 600)
            detalle_orden.drawOn(pdf, 18 * cm, y_total-0.2*cm)
            
            self.tabla(pdf, partes,  y - (len(partes) * 25))
        
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
                    self.cabecera_datos(pdf,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig)
                    
                    #suma total
                    if((page+1)==len(range(0, int(pages_needed)))):
                        y_total= (y - (len(record)*25))-0.5*cm
                        pdf.setFont("VeraBd", 8)
                        pdf.drawString(17 * cm, y_total-0.1*cm , "Total:")
                        total_suma_cel=[total_suma]
                        detalle_orden = Table([total_suma_cel],colWidths=2*cm,rowHeights=11)
                        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),('ALIGN',(0,0),(-1,0),'RIGHT'),('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),]))
                        detalle_orden.wrapOn(pdf, 800, 600)
                        detalle_orden.drawOn(pdf, 18 * cm, y_total-0.2*cm)
                    #---------   
                    self.tabla(pdf, record, y - (len(record) * 25)) 
                      
                else:
                    #suma total
                    if((page+1)==len(range(0, int(pages_needed)))):
                        y_total= (y - (len(record)*25))-0.5*cm
                        pdf.setFont("VeraBd", 8)
                        pdf.drawString(17 * cm, y_total-0.1*cm , "Total:")
                        total_suma_cel=[total_suma]
                        detalle_orden = Table([total_suma_cel],colWidths=2*cm,rowHeights=11)
                        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),('ALIGN',(0,0),(-1,0),'RIGHT'),('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),]))
                        detalle_orden.wrapOn(pdf, 800, 600)
                        detalle_orden.drawOn(pdf, 18 * cm, y_total-0.2*cm)
                    #---------   
                    self.tabla(pdf, record, y - (len(record) * 25)) 
                    self.cabecera_logo(pdf)
                    self.cabecera_datos(pdf,periodo_inicio,periodo_final,row_celda,grid,fontsize,backgroud,valig)
              
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
        
        headers = ['ID','Operación','Nombre de cliente', 'Banco', 'Fecha \ndepósito','Forma \naplicación','Monto']
        lista=[(item['id'],Paragraph(item['codigo_operacion'],dato),Paragraph(item['nombre_completo'],dato),Paragraph(item['banco'],dato),Paragraph(item['fecha_deposito'],dato),Paragraph(item['forma_aplicacion'],dato),item['monto_depositado'])
                     for item in partes]
        
        table = Table([headers] + lista, colWidths=[0.8*cm,2.5*cm,4.5*cm, 4*cm , 2.8 *cm ,2.7*cm, 1.7*cm],rowHeights=25)
        table.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                #('ALIGN',(0,0),(2,0),'LEFT'),
                ('ALIGN', (6,0), (-1,-1), 'RIGHT'),
                #('LINEABOVE',(0,0),(-1,-1),1,colors.gray),
                #('GRID', (7, 0), (-1, -1), 0, colors.white),
                ('GRID', (0, 0), (-1, -1), 0, colors.black),
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
    