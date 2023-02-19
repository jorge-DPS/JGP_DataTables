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
    


class ReporteCondonaciones(View):

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
        pdf.drawString(7.5 * cm, 28 * cm , "Solicitud de Reversión")
        pdf.setFont("VeraBd", 9)
        pdf.drawString(1 * cm, 26.8 * cm , "Nombre de Grupo y/o Cliente:")
        pdf.drawString(14.9 * cm, 26.8 * cm , "Operación:")
        pdf.drawString(1 * cm, 26.1 * cm , "Transacción:")
        pdf.drawString(12 * cm, 26.1 * cm , "Fecha de solicitud:")
###************************CELDAS DATOS PERSONALES ******************************************************
        dato=''
        self.nombre_cliente(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.transaccion(pdf,style,dato_estilo,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.fecha_solicitud(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.num_operacion(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)

#*************************DATOS TOTALES ***************************************************
    def datos_totales(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        #************************************pie de pagina***********************************************************************************************
        #****************TEXTOS EN NEGRILLLAS
        pdf.setFont("VeraBd", 8)
        pdf.setFillColorRGB(0,0,0) 
        pdf.drawString(2 * cm, 10.3 * cm , "TOTAL")
        pdf.drawString(7 * cm, 10.3 * cm , "CONDONADO")
        pdf.drawString(13.3 * cm, 10.3 * cm , "TOTAL A PAGAR")
        #pdf.drawString(1 * cm, 9.5 * cm , "Justificación o motivo")
        pdf.setFont("Vera", 8)
        pdf.drawString(5.5 * cm, 12.5 * cm , "(C)  Condonación")
        pdf.drawString(5.5 * cm, 12 * cm , "(D)  Diferimiento solicitado a la ultima cuota")
        pdf.drawString(5.5 * cm, 11.5 * cm , "(R)  Reversión por pago adelantado")
        pdf.drawString(8.8 * cm, 11 * cm , "TOTAL CONDONADO")
        #pdf.drawString(1 * cm, 10.5 * cm , "Actividad de Cliente:")
        #pdf.drawString(1 * cm, 10 * cm , "Causa Mora y/o Liquidación:")
        
        #dato_t.append(Paragraph("Whatever printed with yourStyle", style2))
        #pdf.drawOn(1 * cm, 3.5 * cm , dato_t)
        style_subtitulo = ParagraphStyle(
            name='Normal',
            fontName='VeraBd',
            fontSize=8,
            spaceAfter = 6,
            spaceBefore = 6,
            spaceShrinkage = 0.05,
            borderPadding = 5
        )
        celda_titulo=[Paragraph('Justificación o motivo',style = style_subtitulo)]
        celda_espacio=[""]
        celda_actividad = [Paragraph('Actividad de Cliente:',style = style),Paragraph('Actividad del cliente pruevainsertando ',style = style)]
        celda_causa = [Paragraph('Causa Mora y/o Liquidación:',style = style),Paragraph('La pruevainsertando un texto dddd ggggggggg tttttttt ttttttttt largo  ',style = style)]
        celda_motivo = [Paragraph('Motivo:',style = style),Paragraph('rrLa pruevainsertando un texto dddd gggggggggttttttttttttttttt largo para la prueba lala largo para la prueba lala largo para la prueba lala largo para la prueba lala largo para la prueba lala largo para la prueba lala largo para la prueba lala largo para la prueba lala largo para la prueba lala ',style = style)]
        detalle_orden = Table([celda_titulo]+[celda_espacio]+[celda_actividad]+[celda_causa]+[celda_motivo],colWidths=[2.7*cm,16.5*cm],)
        detalle_orden.setStyle(TableStyle([
            ('FONT', (0,0), (1,1), 'Helvetica-Bold', 4 ),
            ('GRID', (0, 0), (-1, -1), 1, colors.white),
            ('LINEABOVE',(0,0),(-1,-1),1,colors.gray),
            ('SPAN',(0,0),(1,1)),
            #('FONT', (0,0), (-1,1), 'VeraBd',3),
            (fontsize),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 0.8 * cm, 3.6 * cm)
        
        
        #pdf.drawString(19.5 * cm,0.7 * cm," ACESOR COMERCIAL" )
        self.total(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.condonado(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.total_pagar(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.condonacion_c(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.diferi_d(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.rever_r(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.total_t(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        #self.actividad_cliente(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        #self.mora_liquidacion(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        #self.reversion(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        self.firma(pdf,style)
    
        
#************************DATOS PERSONALES************************************************
    def get(self, request):
        datos_JSON =  """
        {
            "total":"99999.12",
            "datos": [
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                },
                {
                    "fecha": "03/11/2022",
                    "capital": "123.2",
                    "tratamiento": "Rh2"
                }
                
                
                
                   



                
                     
            ]
        }
        """
        
        datos_solicitud = json.loads(datos_JSON)
        
        datos_tabla=datos_solicitud["datos"]
        
        suma=0
        for item in datos_tabla:
            suma=suma+float(item["capital"])
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
        self.tabla(pdf,style,datos_tabla,total_final,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
        
       
        
####################################################################################
        
        #pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self,pdf,style,datos_tabla,total_final,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        #caja_impreso=Caja.objects.all()
        encabezados = ('Nro De\nCuota','Fecha de\nVencimiento' , 'Capital', 'Interes Corriente','', 'Gastos Operativos','','Interes Moratorio','','Interes Moratorio','','Transacción')
        encabezados_2 = ('','' , '', 'Total','a Condonar', 'Total','a Condonar','Total','a Condonar','Total','a Condonar','')
        totales=('','TOTAL',total_final,'0','0','0','0','0','0','0','0','')
        #Creamos una lista de tuplas que van a contener a las personas
        #cuentas_cobrar=CuentasPorCobrar.objects.filter(caja_id=caja_pk).filter(eliminado_en = None)
        detalles=[]
        cont=0
        for item in datos_tabla:
            cont+=1
            lista= (cont,item['fecha'],item['capital'],'','','','','','','','',item['tratamiento'])
            detalles.append(lista)
        #--------------------
        if(cont <=20):
            while cont < 20 :
                cont+=1
                lista=(cont,'-','-','-','-','-','-','-','-','-','-','')
                detalles.append(lista)
            detalles.append(totales)
            
            detalle_orden = Table([encabezados]+[encabezados_2] + detalles, colWidths=[1*cm,2*cm,1.6*cm],rowHeights=15)
            detalle_orden.setStyle(TableStyle(
                [
                    ('ALIGN',(0,0),(-1,-1),'CENTER'),
                    ('ALIGN', (2,2), (10,-1), 'RIGHT'),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                    ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                    ('FONTSIZE', (0, 2), (-1, -1), 8),
                    ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                    ('BACKGROUND', (4, 2), (4, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                    ('BACKGROUND', (6, 2), (6, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                    ('BACKGROUND', (8, 2), (8, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                    ('BACKGROUND', (10, 2), (10, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                    ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                    ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                    ('BOX',(0,0),(-1,-1),1,colors.black),
                    ('GRID', (-1, -1), (0, 1), 0, colors.white),
                    ('SPAN',(0,0),(0,1)),
                    ('SPAN',(1,0),(1,1)),
                    ('SPAN',(2,0),(2,1)),
                    ('SPAN',(3,0),(4,0)),
                    ('SPAN',(5,0),(6,0)),
                    ('SPAN',(7,0),(8,0)),
                    ('SPAN',(9,0),(10,0)),
                    ('SPAN',(11,0),(11,1)),
                ]
            ))
            detalle_orden.wrapOn(pdf, 800, 600)
            detalle_orden.drawOn(pdf, 1*cm,13*cm)
            #************************************totales y resultados de pagina***********************************************************************************************
            self.datos_totales(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
            pdf.setFont("Vera", 8)
            pdf.drawString(10.2 * cm, 0.5 * cm , "1/1")
            
        else:
            if(cont <=40):
                pag=0
                while (pag<2):
                    pag+=1
                    if(pag!=2):
                        while cont < 40 :
                            cont+=1
                            lista=(cont,'-','-','-','-','-','-','-','-','-','-','-')
                            detalles.append(lista)
                        #detalles.append(totales)
                        
                        detalle_orden = Table([encabezados]+[encabezados_2] + detalles, colWidths=[1*cm,2*cm,1.6*cm],rowHeights=15)
                        detalle_orden.setStyle(TableStyle(
                            [
                                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                ('ALIGN', (2,2), (10,-1), 'RIGHT'),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                                ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                                ('FONTSIZE', (0, 2), (-1, -1), 7),
                                ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                                ('BACKGROUND', (4, 2), (4, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                ('BACKGROUND', (6, 2), (6, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                ('BACKGROUND', (8, 2), (8, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                ('BACKGROUND', (10, 2), (10, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                                ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                                ('BOX',(0,0),(-1,-1),1,colors.black),
                                ('GRID', (-1, -1), (0, 1), 0, colors.white),
                                ('SPAN',(0,0),(0,1)),
                                ('SPAN',(1,0),(1,1)),
                                ('SPAN',(2,0),(2,1)),
                                ('SPAN',(3,0),(4,0)),
                                ('SPAN',(5,0),(6,0)),
                                ('SPAN',(7,0),(8,0)),
                                ('SPAN',(9,0),(10,0)),
                                ('SPAN',(11,0),(11,1)),
                            ]
                        ))
                        detalle_orden.wrapOn(pdf, 800, 600)
                        detalle_orden.drawOn(pdf, 1*cm,2.8*cm)
                        pdf.setFont("Vera", 8)
                        pdf.drawString(10.2 * cm, 1.3 * cm , "1/2")
                    else:
                        pdf.setStrokeColorRGB(23.0/255,25.0/255,50.0/255)
                        pdf.setFillColorRGB(23.0/255,25.0/255,50.0/255)
                        pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
                        self.cabecera_logo(pdf)
                        self.cabecera_datos(pdf)
                        detalle_2=[]
                        while cont < 60 :
                            cont+=1
                            lista=(cont,'-','-','-','-','-','-','-','-','-','-','-')
                            detalle_2.append(lista)
                        detalle_2.append(totales)
                        
                        detalle_orden = Table([encabezados]+[encabezados_2] + detalle_2, colWidths=[1*cm,2*cm,1.6*cm],rowHeights=15)
                        detalle_orden.setStyle(TableStyle(
                            [
                                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                ('ALIGN', (2,2), (10,-1), 'RIGHT'),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                                ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                                ('FONTSIZE', (0, 2), (-1, -1), 7),
                                ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                                ('BACKGROUND', (4, 2), (4, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                ('BACKGROUND', (6, 2), (6, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                ('BACKGROUND', (8, 2), (8, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                ('BACKGROUND', (10, 2), (10, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                                ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                                ('BOX',(0,0),(-1,-1),1,colors.black),
                                ('GRID', (-1, -1), (0, 1), 0, colors.white),
                                ('SPAN',(0,0),(0,1)),
                                ('SPAN',(1,0),(1,1)),
                                ('SPAN',(2,0),(2,1)),
                                ('SPAN',(3,0),(4,0)),
                                ('SPAN',(5,0),(6,0)),
                                ('SPAN',(7,0),(8,0)),
                                ('SPAN',(9,0),(10,0)),
                                ('SPAN',(11,0),(11,1)),
                            ]
                        ))
                        detalle_orden.wrapOn(pdf, 800, 600)
                        detalle_orden.drawOn(pdf, 1*cm,13*cm)
                       #************************************totales y resultados de pagina***********************************************************************************************
                        self.datos_totales(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
                        pdf.setFont("Vera", 8)
                        pdf.drawString(10.2 * cm, 0.5 * cm , "2/2")
                    pdf.showPage()
                    
            else:
                #*************detalle mas de 40y menor a 60**************
                #print("//////////////////**********",cont)
                if(cont <=60):
                    pag=0
                    while (pag<2):
                        pag+=1
                        if(pag!=2):
                            hoja_1=[]
                            cont=0
                            for item in datos_tabla:
                                cont+=1
                                if(cont<=40):
                                    lista= (cont,item['fecha'],item['capital'],'','','','','','','','',item['tratamiento'])
                                    hoja_1.append(lista)
                            #hoja_1.append(totales)
                            detalle_orden = Table([encabezados]+[encabezados_2] + hoja_1, colWidths=[1*cm,2*cm,1.6*cm],rowHeights=15)
                            detalle_orden.setStyle(TableStyle(
                                [
                                    ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                    ('ALIGN', (2,2), (10,-1), 'RIGHT'),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                                    ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                                    ('FONTSIZE', (0, 2), (-1, -1), 7),
                                    ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                                    ('BACKGROUND', (4, 2), (4, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (6, 2), (6, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (8, 2), (8, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (10, 2), (10, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                                    ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                                    ('BOX',(0,0),(-1,-1),1,colors.black),
                                    ('GRID', (-1, -1), (0, 1), 0, colors.white),
                                    ('SPAN',(0,0),(0,1)),
                                    ('SPAN',(1,0),(1,1)),
                                    ('SPAN',(2,0),(2,1)),
                                    ('SPAN',(3,0),(4,0)),
                                    ('SPAN',(5,0),(6,0)),
                                    ('SPAN',(7,0),(8,0)),
                                    ('SPAN',(9,0),(10,0)),
                                    ('SPAN',(11,0),(11,1)),
                                ]
                            ))
                            detalle_orden.wrapOn(pdf, 800, 600)
                            detalle_orden.drawOn(pdf, 1*cm,2.8*cm)
                            pdf.setFont("Vera", 8)
                            pdf.drawString(10.2 * cm, 1.3 * cm , "1/2")
                        else:
                            pdf.setStrokeColorRGB(23.0/255,25.0/255,50.0/255)
                            pdf.setFillColorRGB(23.0/255,25.0/255,50.0/255)
                            pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
                            self.cabecera_logo(pdf)
                            self.cabecera_datos(pdf)
                            hoja_2=[]
                            cont_hoja_2=0
                            cont-=1
                            for item in datos_tabla:
                                cont_hoja_2+=1
                                if(cont_hoja_2>40):
                                    lista= (cont_hoja_2,item['fecha'],item['capital'],'','','','','','','','',item['tratamiento'])
                                    hoja_2.append(lista)
                            while cont_hoja_2 < 60 :
                                cont_hoja_2+=1
                                lista=(cont_hoja_2,'-','-','','-','-','-','-','-','-','-','')
                                hoja_2.append(lista)
                            hoja_2.append(totales)
                            
                            detalle_orden = Table([encabezados]+[encabezados_2] + hoja_2, colWidths=[1*cm,2*cm,1.6*cm],rowHeights=15)
                            detalle_orden.setStyle(TableStyle(
                                [
                                    ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                    ('ALIGN', (2,2), (10,-1), 'RIGHT'),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                                    ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                                    ('FONTSIZE', (0, 2), (-1, -1), 7),
                                    ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                                    ('BACKGROUND', (4, 2), (4, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (6, 2), (6, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (8, 2), (8, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (10, 2), (10, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                                    ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                                    ('BOX',(0,0),(-1,-1),1,colors.black),
                                    ('GRID', (-1, -1), (0, 1), 0, colors.white),
                                    ('SPAN',(0,0),(0,1)),
                                    ('SPAN',(1,0),(1,1)),
                                    ('SPAN',(2,0),(2,1)),
                                    ('SPAN',(3,0),(4,0)),
                                    ('SPAN',(5,0),(6,0)),
                                    ('SPAN',(7,0),(8,0)),
                                    ('SPAN',(9,0),(10,0)),
                                    ('SPAN',(11,0),(11,1)),
                                ]
                            ))
                            detalle_orden.wrapOn(pdf, 800, 600)
                            detalle_orden.drawOn(pdf, 1*cm,13*cm)
                            #************************************totales y resultados de pagina***********************************************************************************************
                            self.datos_totales(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
                            pdf.setFont("Vera", 8)
                            pdf.drawString(10.2 * cm, 0.5 * cm , "2/2")
                        pdf.showPage()
                else:
                    #----------------------------para 3 paginas--------------
                    pag=0
                    while (pag<3):
                        pag+=1
                        if(pag==1):
                            hoja_1=[]
                            cont=0
                            for item in datos_tabla:
                                cont+=1
                                if(cont<=40):
                                    lista= (cont,item['fecha'],item['capital'],'','','','','','','','',item['tratamiento'])
                                    hoja_1.append(lista)
                            #hoja_1.append(totales)
                            
                            detalle_orden = Table([encabezados]+[encabezados_2] + hoja_1, colWidths=[1*cm,2*cm,1.6*cm],rowHeights=15)
                            detalle_orden.setStyle(TableStyle(
                                [
                                    ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                    ('ALIGN', (2,2), (10,-1), 'RIGHT'),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                                    ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                                    ('FONTSIZE', (0, 2), (-1, -1), 7),
                                    ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                                    ('BACKGROUND', (4, 2), (4, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (6, 2), (6, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (8, 2), (8, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('BACKGROUND', (10, 2), (10, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                    ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                                    ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                                    ('BOX',(0,0),(-1,-1),1,colors.black),
                                    ('GRID', (-1, -1), (0, 1), 0, colors.white),
                                    ('SPAN',(0,0),(0,1)),
                                    ('SPAN',(1,0),(1,1)),
                                    ('SPAN',(2,0),(2,1)),
                                    ('SPAN',(3,0),(4,0)),
                                    ('SPAN',(5,0),(6,0)),
                                    ('SPAN',(7,0),(8,0)),
                                    ('SPAN',(9,0),(10,0)),
                                    ('SPAN',(11,0),(11,1)),
                                ]
                            ))
                            detalle_orden.wrapOn(pdf, 800, 600)
                            detalle_orden.drawOn(pdf, 1*cm,2.8*cm)
                            pdf.setFont("Vera", 8)
                            pdf.drawString(10.2 * cm, 1.3 * cm , "1/3")
                            
                            pdf.showPage()
                        else:
                            if(pag==2):
                                pdf.setStrokeColorRGB(23.0/255,25.0/255,50.0/255)
                                pdf.setFillColorRGB(23.0/255,25.0/255,50.0/255)
                                pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
                                self.cabecera_logo(pdf)
                                self.cabecera_datos(pdf)
                                hoja_2=[]
                                cont_hoja_2=0
                                for item in datos_tabla:
                                    cont_hoja_2+=1
                                    if(cont_hoja_2>=41 and cont_hoja_2<=80):
                                        lista= (cont_hoja_2,item['fecha'],item['capital'],'','','','','','','','',item['tratamiento'])
                                        hoja_2.append(lista)
                                if(cont_hoja_2<=80):
                                    while cont_hoja_2 < 80 :
                                        cont_hoja_2+=1
                                        lista=(cont_hoja_2,'-','-','-','-','-','-','-','-','-','-','')
                                        hoja_2.append(lista)
                                        
                                #hoja_2.append(totales)
                                
                                detalle_orden = Table([encabezados]+[encabezados_2] + hoja_2, colWidths=[1*cm,2*cm,1.6*cm],rowHeights=15)
                                detalle_orden.setStyle(TableStyle(
                                    [
                                        ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                        ('ALIGN', (2,2), (10,-1), 'RIGHT'),
                                        ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                                        ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                                        ('FONTSIZE', (0, 2), (-1, -1), 7),
                                        ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                                        ('BACKGROUND', (4, 2), (4, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                        ('BACKGROUND', (6, 2), (6, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                        ('BACKGROUND', (8, 2), (8, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                        ('BACKGROUND', (10, 2), (10, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                        ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                                        ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                                        ('BOX',(0,0),(-1,-1),1,colors.black),
                                        ('GRID', (-1, -1), (0, 1), 0, colors.white),
                                        ('SPAN',(0,0),(0,1)),
                                        ('SPAN',(1,0),(1,1)),
                                        ('SPAN',(2,0),(2,1)),
                                        ('SPAN',(3,0),(4,0)),
                                        ('SPAN',(5,0),(6,0)),
                                        ('SPAN',(7,0),(8,0)),
                                        ('SPAN',(9,0),(10,0)),
                                        ('SPAN',(11,0),(11,1)),
                                    ]
                                ))
                                detalle_orden.wrapOn(pdf, 800, 600)
                                detalle_orden.drawOn(pdf, 1*cm,2.8*cm)
                                pdf.setFont("Vera", 8)
                                pdf.drawString(10.2 * cm, 1.3 * cm , "2/3")
                                #pdf.showPage()
                            else:
                                if(pag==3):
                                    pdf.setStrokeColorRGB(23.0/255,25.0/255,50.0/255)
                                    pdf.setFillColorRGB(23.0/255,25.0/255,50.0/255)
                                    pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
                                    self.cabecera_logo(pdf)
                                    self.cabecera_datos(pdf)
                                    hoja_3=[]
                                    cont_hoja_3=0
                                    resto=0
                                    suma=0
                                    for item in datos_tabla:
                                        cont_hoja_3+=1
                                        if(cont_hoja_3>80):
                                            resto+=1
                                            lista= (cont_hoja_3,item['fecha'],item['capital'],'','','','','','','','',item['tratamiento'])
                                            hoja_3.append(lista)
                                        
                                    res=80-cont_hoja_3
                                    if(res>0):
                                        cont_hoja_3=cont_hoja_3+res
                                    if(cont_hoja_3<=100):
                                        while cont_hoja_3 < 100 :
                                            cont_hoja_3+=1
                                            lista=(cont_hoja_3,'-','-','-','-','-','-','-','-','-','-','')
                                            hoja_3.append(lista)
                                            
                                    hoja_3.append(totales)
                                    
                                    detalle_orden = Table([encabezados]+[encabezados_2] + hoja_3, colWidths=[1*cm,2*cm,1.6*cm],rowHeights=15)
                                    detalle_orden.setStyle(TableStyle(
                                        [
                                            ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                            ('ALIGN', (2,2), (10,-1), 'RIGHT'),
                                            ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                                            ('FONT', (0,0), (-1,1), 'Helvetica', 8 ),
                                            ('FONTSIZE', (0, 2), (-1, -1), 7),
                                            ('BACKGROUND', (0, 0), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                                            ('BACKGROUND', (4, 2), (4, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                            ('BACKGROUND', (6, 2), (6, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                            ('BACKGROUND', (8, 2), (8, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                            ('BACKGROUND', (10, 2), (10, -1), colors.Color(red=(240.0/255),green=(240.0/255),blue=(240.0/255))),
                                            ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                                            ('GRID', (0, 0), (-1, -1), 0, colors.gray),
                                            ('BOX',(0,0),(-1,-1),1,colors.black),
                                            ('GRID', (-1, -1), (0, 1), 0, colors.white),
                                            ('SPAN',(0,0),(0,1)),
                                            ('SPAN',(1,0),(1,1)),
                                            ('SPAN',(2,0),(2,1)),
                                            ('SPAN',(3,0),(4,0)),
                                            ('SPAN',(5,0),(6,0)),
                                            ('SPAN',(7,0),(8,0)),
                                            ('SPAN',(9,0),(10,0)),
                                            ('SPAN',(11,0),(11,1)),
                                        ]
                                    ))
                                    detalle_orden.wrapOn(pdf, 800, 600)
                                    detalle_orden.drawOn(pdf, 1*cm,13*cm)
                                    
                                   #************************************totales y resultados de pagina***********************************************************************************************
                                    self.datos_totales(pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente)
                                    pdf.setFont("Vera", 8)
                                    pdf.drawString(10.2 * cm, 0.5 * cm , "3/3")
                            pdf.showPage()
                                
        
    def transaccion(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda = [Paragraph('LIQUIUDACION DE PRESTAMO cliente',style = style)]
        detalle_orden = Table([celda],colWidths=8*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.4 * cm, 26 * cm)
    def fecha_solicitud(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        dia=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        mes=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Nomviembre","Diciembre"]
        fecha_actual=datetime.now().strftime('%d-%m-%Y')
        d = datetime.strptime(fecha_actual, "%d-%m-%Y")
        fecha_convertido=datetime.now().strftime('%d-%m-%Y')
        print("fechaaaaaaadddddaaaa",dia[d.weekday()])
        celda = [Paragraph(dia[d.weekday()]+" "+fecha_actual,style = style)]
        detalle_orden = Table([celda],colWidths=4.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 15.5 * cm, 26 * cm)
    def num_operacion(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        
        celda = [Paragraph('123456789124',style = style)]
        detalle_orden = Table([celda],colWidths=3*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17 * cm, 26.7 * cm)
    def nombre_cliente(self,pdf,style,dato,row_celda,grid,fontsize,backgroud,valig,fuente):
        celda=[Paragraph(' Nombre de cliente empresa',style = style)]
        detalle_orden = Table([celda],colWidths=8*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),(fuente)]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 6.4 * cm, 26.7 * cm)
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
    
        
    

    