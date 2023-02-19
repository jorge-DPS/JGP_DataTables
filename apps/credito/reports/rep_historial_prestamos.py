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

from datetime import datetime

import math
#-----------------fuentes
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
    

class HistorialPrestamos(View):

    def cabecera_logo(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = ImageReader('web/static/assets/media/Logos_JDGP/logomediano.jpg')
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen,1 * cm, 26 *cm,width=50*mm,height=50*mm,preserveAspectRatio=True)                
        #************************************ENCABEZADO***********************************************************************************************
        fecha_actual=datetime.now().strftime('%d/%m/%Y')
        user_actual=User.objects.get(id=self.request.user.pk)
#*****************VARIABLES GLOBALES****************************
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.setFont("Vera", 7)
        pdf.setFillColorRGB(0,0,0) 
        pdf.drawString(17.7 * cm,28.4 * cm,"Fecha: "+fecha_actual)
        pdf.drawString(17.7 * cm,28 * cm,"Usuario: "+user_actual.username)
#/////////////////////////////CABEZERA DATOS************************************************
    def cabecera_datos(self,pdf):
        # Convertir cadena de caracteres JSON a un diccionario
        #*****************VARIABLES GLOBALES****************************
        color_oscuro_R= 23.0/255
        color_oscuro_G= 25.0/255
        color_oscuro_B= 50.0/255
        tamano_letra=9
#************estilos de las celdas
        style = ParagraphStyle(
            name='Normal',
            fontName='Vera',
            fontSize=8,
            spaceAfter = 6,
            spaceBefore = 6,
            spaceShrinkage = 0.05,
            borderPadding = 5
        )
        
        styles=getSampleStyleSheet()
        dato_estilo = styles["Normal"]
        dato_estilo.agnment=TA_LEFT
        dato_estilo.fontSize=8
        
        grid='GRID', (0, 0), (-1, -1), 1, colors.gray
        fontsize='FONTSIZE', (0, 0), (-1, -1), tamano_letra
        backgroud='BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))
        valig='VALIGN', (0,0), (-1, -1), 'MIDDLE'
        fuente='FONT', (0,0), (-1,-1), 'Vera',tamano_letra  
        row_celda=13
        
        #******************************LINEAS GRUESAS*****************************
        pdf.setStrokeColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
        pdf.setFillColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
        pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
        pdf.roundRect(1*cm, 25.6*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
        #************************************ENCABEZADO***********************************************************************************************
#****************TEXTOS EN NEGRILLLAS
        pdf.setFont("VeraBd", 15)
        pdf.drawString(7.5 * cm, 28.5 * cm , "Historial de Prestamos")
        pdf.setFont("Helvetica-Bold", 9)
        pdf.drawString(9 * cm, 28 * cm , "Todas las operaciones")
        pdf.drawString(1 * cm, 26.8 * cm , "Nombre completo:")
        pdf.drawString(10.3 * cm, 26.8 * cm , "Nro de documento:")
        pdf.drawString(16.3 * cm, 26.8 * cm , "Estado:")
        pdf.drawString(1 * cm, 26.1 * cm , "Observaciones:")
###************************CELDAS DATOS PERSONALES ******************************************************
        dato=''
        self.nombre_cliente(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.num_documento(pdf,style,dato_estilo,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.estado(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.observacion(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)

#************************DATOS PERSONALES************************************************
    def get(self, request):
        datos_JSON =  """
        {
            "total":"99999.12",
            "datos": [
                {
                    "codigo":"123456789012",
                    "estado":"1",
                    "tipo":"Titular",
                    "descripcion":"Credito individual",
                    "fecha":"02/01/2023",
                    "monto":3000.12,
                    "saldo":"9802.25",
                    "num_cuota":12,
                    "cuota":4,
                    "frecuencia":"Semanales",
                    "dias":338,
                    "situacion":"Cancelado",
                    "fecha_cancelado":"08/01/2023",
                    "asesor":208
                }
                
                     
            ]
        }
        """
        
        datos_solicitud = json.loads(datos_JSON)
        
        datos_tabla=datos_solicitud["datos"]
        
        suma=0
        for item in datos_tabla:
            suma=suma+float(item["monto"])
        #print("suma total ",round(suma,2))
        total_final=round(suma,2)
        #estilos
        #*****************VARIABLES GLOBALES****************************
        color_oscuro_R= 23.0/255
        color_oscuro_G= 25.0/255
        color_oscuro_B= 50.0/255
        tamano_letra=9
        style = ParagraphStyle(
            name='Normal',
            fontName='Vera',
            fontSize=8,
            spaceAfter = 6,
            spaceBefore = 6,
            spaceShrinkage = 0.05,
            borderPadding = 5
        )
        grid='GRID', (0, 0), (-1, -1), 1, colors.gray
        fontsize='FONTSIZE', (0, 0), (-1, -1), tamano_letra
        backgroud='BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))
        valig='VALIGN', (0,0), (-1, -1), 'MIDDLE'
        fuente='FONT', (0,0), (-1,-1), 'Vera',tamano_letra  
        row_celda=13
        response = HttpResponse(content_type="application/pdf")
        #response['Content-Disposition'] = 'attachment; filename = Reporte'
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer,pagesize=portrait(A4))
        #************************************ENCABEZADO***********************************************************************************************
        
        self.cabecera_logo(pdf)
        self.cabecera_datos(pdf)
        
        dato=''
        self.tabla_deuda_directa(pdf,style,datos_tabla,total_final,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.tabla_deuda_indirectas(pdf,style,datos_tabla,total_final,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.tabla_totales(pdf,style,datos_tabla,total_final,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        
        pdf.setFont("Vera", 8)
        pdf.drawString(10.2 * cm, 0.5 * cm , "1/1")
       
        
####################################################################################
        
        #pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla_deuda_directa(self,pdf,style,datos_tabla,total_final,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        #caja_impreso=Caja.objects.all()
        style = ParagraphStyle(
            name='Normal_CENTER',
            fontName='Helvetica',
            fontSize=8,
            alignment=TA_CENTER,
        )
        encabezado = ('DEUDAS DIRECTAS','' , '', '','', '','','','','','','','','')
        encabezados = (Paragraph('Codigo Operación',style = style),'Est.' ,'Tipo\nObligado',Paragraph('Descripción de operación',style = style),'Fecha\nDesemb.', 'Monto\nDesemb','Saldo\nCapital','Num\nCuo.','Cuo\nPend','Frecuencia','Dias\nAcum','Situación','Fecha\nCanc.','Asesor')
        totales=('Operaciones activas: 2 / Total operaciones desembolsadas:8','','','','','','','','','','','','','')
        #Creamos una lista de tuplas que van a contener a las personas
        #cuentas_cobrar=CuentasPorCobrar.objects.filter(caja_id=caja_pk).filter(eliminado_en = None)
        detalles=[]
        cont=0
        for item in datos_tabla:
            cont+=1
            lista= (item['codigo'],item['estado'],item['tipo'],item['descripcion'],item['fecha'],item['monto'],item['saldo'],item['num_cuota'],item['cuota'],item['frecuencia'],item['dias'],item['situacion'],item['fecha_cancelado'],item['asesor'])
            detalles.append(lista)
        #--------------------
        while cont < 10 :
            cont+=1
            lista=(cont,'-','-','-','-','-','-','-','-','-','-','')
            detalles.append(lista)
        detalles.append(totales)
        
        detalle_orden = Table([encabezado]+[encabezados] + detalles,
            colWidths=[2*cm,0.6*cm,1.3*cm,2.5*cm,1.6*cm,1.5*cm,1.5*cm,0.8*cm,0.8*cm,1.6*cm,0.8*cm,1.5*cm,1.5*cm,1*cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('ALIGN', (0,-1), (-1,-1), 'LEFT'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                ('FONTSIZE', (0, 2), (-1, -1),8),
                ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                ('BOX',(0,0),(-1,-1),1,colors.black),
                ('GRID', (-1, -1), (0, 1), 0, colors.white),
                ('SPAN',(0,0),(-1,0)),
                ('SPAN',(0,-1),(-1,-1)),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 1*cm,16.5*cm)
        #************************************totales y resultados de pagina***********************************************************************************************
        
    def tabla_deuda_indirectas(self,pdf,style,datos_tabla,total_final,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        style = ParagraphStyle(
            name='Normal_CENTER',
            fontName='Helvetica',
            fontSize=8,
            alignment=TA_CENTER,
        )
        encabezado = ('DEUDAS INDIRECTAS','' , '', '','', '','','','','','','','','')
        encabezados = (Paragraph('Codigo Operación',style = style),'Est.' ,'Tipo\nObligado',Paragraph('Titular de operación',style = style),'Fecha\nDesemb.', 'Monto\nDesemb','Saldo\nCapital','Num\nCuo.','Cuo\nPend','Frecuencia','Dias\nAcum','Situación','Fecha\nCanc.','Asesor')
        totales=('Operaciones activas: 2 / Total operaciones desembolsadas:8','','','','','','','','','','','','','')
        detalles=[]
        cont=0
        for item in datos_tabla:
            cont+=1
            lista= (item['codigo'],item['estado'],item['tipo'],item['descripcion'],item['fecha'],item['monto'],item['saldo'],item['num_cuota'],item['cuota'],item['frecuencia'],item['dias'],item['situacion'],item['fecha_cancelado'],item['asesor'])
            detalles.append(lista)
        #--------------------
        while cont < 10 :
            cont+=1
            lista=(cont,'-','-','-','-','-','-','-','-','-','-','')
            detalles.append(lista)
        detalles.append(totales)
        detalle_orden = Table([encabezado]+[encabezados] + detalles,
            colWidths=[2*cm,0.6*cm,1.3*cm,2.5*cm,1.6*cm,1.5*cm,1.5*cm,0.8*cm,0.8*cm,1.6*cm,0.8*cm,1.5*cm,1.5*cm,1*cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('ALIGN', (0,-1), (-1,-1), 'LEFT'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                ('FONTSIZE', (0, 2), (-1, -1),8),
                ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                ('BOX',(0,0),(-1,-1),1,colors.black),
                ('GRID', (-1, -1), (0, 1), 0, colors.white),
                ('SPAN',(0,0),(-1,0)),
                ('SPAN',(0,-1),(-1,-1)),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 1*cm,7.5*cm)
        #************************************totales y resultados de pagina***********************************************************************************************
    def tabla_totales(self,pdf,style,datos_tabla,total_final,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        encabezado = ('Tipo\nObligado','Vigente' ,'', 'En Mora','', 'Castigado','','Total General','')
        encabezados = ('' ,'Ope.','Saldo Capital','Ope.','Saldo Capital','Ope.','Saldo Capital','Ope.','Saldo Capital')
        detalles=[]
        cont=0
        #for item in datos_tabla:
        #    cont+=1
        #    lista= (item['codigo'],item['estado'],item['tipo'],item['descripcion'],item['fecha'],item['monto'],item['saldo'],item['num_cuota'],item['cuota'],item['frecuencia'],item['dias'],item['situacion'],item['fecha_cancelado'],item['asesor'])
        #    detalles.append(lista)
        #--------------------
        lista_titular=('Titular','','','','','','','','')
        detalles.append(lista_titular)
        lista_codeudor=('Codeudor','','','','','','','','')
        detalles.append(lista_codeudor)
        lista_garante=('Garante','','','','','','','','')
        detalles.append(lista_garante)
        lista_total=('Total Genral','','','','','','','','')
        detalles.append(lista_total)
        
        detalle_orden = Table([encabezado]+[encabezados] + detalles,
            colWidths=[2*cm,0.6*cm,2*cm,0.6*cm,2*cm,0.6*cm,2*cm,0.6*cm,2*cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                #('ALIGN', (0,-1), (-1,-1), 'LEFT'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                ('FONTSIZE', (0, 2), (-1, -1),8),
                ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                ('BOX',(0,0),(-1,-1),1,colors.black),
                ('GRID', (-1, -1), (0, 1), 0, colors.white),
                ('SPAN',(0,0),(1,1)),
                ('SPAN',(0,-1),(-1,-1)),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 1*cm,1.5*cm)           
                                        
        
    def num_documento(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = [Paragraph('123456789012',style = style)]
        detalle_orden = Table([celda],colWidths=2.7*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.3 * cm, 26.7 * cm)
    def observacion(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = [Paragraph('Bloqueado por mora reiterativa Bloqueado por mora reiterativa ',style = style)]
        detalle_orden = Table([celda],colWidths=16.4*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.6 * cm, 26 * cm)
    def estado(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = [Paragraph('Desbloqueado',style = style)]
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17.5 * cm, 26.7 * cm)
    def nombre_cliente(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda=[Paragraph('Juan Carlos Mamani Choquecallata',style = style)]
        detalle_orden = Table([celda],colWidths=6*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.9 * cm, 26.7 * cm)
    def total(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=11)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.3 * cm, 10.2 * cm)
    def condonado(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=11)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 9.3 * cm, 10.2 * cm)
    def total_pagar(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=11)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 16 * cm, 10.2 * cm)
    def condonacion_c(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=11)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 12.3 * cm, 12.4 * cm)
    def diferi_d(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=11)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 12.3 * cm, 11.9 * cm)
    def rever_r(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=11)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 12.3 * cm, 11.4 * cm)
    def total_t(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=11)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 12.3 * cm, 10.9 * cm)
    def actividad_cliente(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = ['']
        detalle_orden = Table([celda],colWidths=15.9*cm,rowHeights=13)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4.1 * cm, 5.4 * cm)
    def mora_liquidacion(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = [Paragraph(' cliente texto largo para la prueba la pruevainsertando un texto largo para ',style = style)]
        detalle_orden = Table([celda],colWidths=14.8*cm)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 5.2 * cm, 4.1 * cm)
    def reversion(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        
        celda = [Paragraph(' la pruevainsertando un texto largo para la prueba la',style = style)]
        detalle_orden = Table([celda],colWidths=17.8*cm,)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 2.2 * cm, 2.9 * cm)
    def firma(self,pdf,style):
        firma_blanco = ['','','','']
        #'Asesor Comercial','Gerente de Agencia','Gerente Operativo','Sistemas'
        firma_letra=['Asesor Comercial','Gerente de Agencia','Gerente Operativo','Sistemas']
        detalle_orden = Table([firma_blanco]+[firma_letra],colWidths=[4.75*cm],rowHeights=[1.8*cm,12])
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(firma_blanco) va a estar centrada
                ('ALIGN',(0,1),(-1,-1),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('LINEBELOW', (1, 1), (-1, 0), 2, colors.darkblue),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('FONT', (0,-1), (-1,-1), 'VeraBd',9  ),
                #('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 1*cm,1*cm)
    
        
    

    