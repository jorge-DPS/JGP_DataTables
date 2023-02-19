import json

import requests
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView
from apps.cajas.models import (Caja)
from apps.accounts.models import User
from apps.empresa.models.sucursal import Sucursal

#***************
#from io import BytesIO
from django.views import View
from django.http import HttpResponse
# reportlab imports
from reportlab.platypus import *
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
#from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import (Image, Table, Frame,BaseDocTemplate, Frame, Paragraph, 
                    NextPageTemplate, PageBreak, PageTemplate)
from reportlab.lib.units import inch,mm,cm
from reportlab.lib.utils import ImageReader
from PIL import Image
from reportlab.lib.pagesizes import A4
#from PyPDF2 import PdfFileWriter, PdfFileReader
#from reportlab.lib.pagesizes import letter, landscape
#Importamos settings para poder tener a la mano la ruta de la carpeta media
from django.conf import settings
from io import BytesIO
from django.views.generic import View
from reportlab.lib.pagesizes import letter, landscape
#librerias
from datetime import datetime,timedelta
from rest_framework.response import Response
from rest_framework import status
import io  
#import pandas as pd

from apps.contrib.api.viewsets import ModelCreateListViewSet
#import pandas as pd
class LiquidacionPrestamo_datos(ModelCreateListViewSet):
    def datos(self, request, *args, **kwargs):
        global datos 
        try: 
            #cuenta_cobrar = CuentasPorCobrar.objects.get(id=kwargs["id"])
            codigo=0
            data=self.request.data
            codigo=data['codigo']
            fecha=data['fecha']
            if(codigo>0):
                datos={"codigo":codigo,"fecha":fecha}
                #reporte=LiquidacionPrestamo()
                #reporte.get()
                return Response(datos,status=status.HTTP_200_OK)
            
            else:
                return Response({"message":"Ingrese el codigo mayor a 0"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        except KeyError:
            return Response({'message':'Ingrrese los datos en el campo codigo y la fecha'},status=status.HTTP_406_NOT_ACCEPTABLE)      


class ReporteLiquidacionPrestamo(View):

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
        tamano_letra=8
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        #self.cabecera_logo(pdf)
       #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("VeraBd", 16)
        pdf.setFillColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B) 
        pdf.drawString(7.3 * cm, 28.2 * cm , "LIQUIDACIÓN DE PRÉSTAMO")
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.setFont("Vera", 7)
        pdf.setFillColorRGB(0,0,0) 
        pdf.drawString(17.7 * cm,28.4 * cm,"Fecha: "+fecha_actual)
        pdf.drawString(17.7 * cm,28 * cm,"Usuario: "+user_actual.username)

    def get(self, request, *args, **kwargs):
        fecha_actual=datetime.now().strftime('%d/%m/%Y')
        user_actual=User.objects.get(id=self.request.user.pk)
#*****************VARIABLES GLOBALES****************************
        color_oscuro_R= 23.0/255
        color_oscuro_G= 25.0/255
        color_oscuro_B= 50.0/255
        color_plomo_RGB= 221
        tamano_letra=8
#************estilos de las celdas
        grid='GRID', (0, 0), (-1, -1), 1, colors.gray
        fontsize='FONTSIZE', (0, 0), (-1, -1), tamano_letra
        backgroud='BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))
        valig='VALIGN', (0,0), (-1, -1), 'MIDDLE'
        row_celda=14
#*********************************************************************        
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        w,h=A4
        pdf = canvas.Canvas(buffer)
        #pdf = canvas.Canvas(buffer,pagesize=landscape(letter))

#DATOS  JSON RECICIENDO
        #501211301353
        #2023-01-03
        ###codigo=kwargs["codigo"]
        codigo='1234423423'
        #fecha = datetime.strptime(kwargs["fecha"], '%Y-%m-%d' ).date()
        ###fecha=kwargs["fecha"]
        
        ###datos_json = requests.get("http://192.168.100.30:8003/api/v1/cre/rep/liquidacion-prestamo?operacion="+codigo+"&fecha="+fecha).text
        datos_json = """
        {
"success": true,
"data": {
"codigo_operacion": 101011012249,
"monto_desembolsado": 9500,
"fecha_inicio": "2016-02-05",
"tasa_interes": 3,
"numero_cuotas": 3,
"frecuencia": "Mensual",
"estado": "V",
"grupo_solidario": "el grupo maroyu",
"ultima_cuota_pagada": "Cuota 1 con vencimiento el 2016-03-07 pagado en fecha 2016-03-08",
"numero_cuota": "1",
"fecha_vencimiento_cuota": "2016-03-07",
"fecha_pago_cuota": "2016-03-08",
"cuotas_impagas": "desde 2 a 3",
"titulares": [
{
"nombre": "Quinteros Cristina Rosaicela",
"documento_identificacion": "5950265LP"
},
{
"nombre": "Vargas Quispe Carlos",
"documento_identificacion": "9868009LP"
},
{
"nombre": "Ramos Daza Elizabeth Sandra",
"documento_identificacion": "4806740LP"
},
{
"nombre": "Chambi Amos Tania",
"documento_identificacion": "6996198LP"
},
{
"nombre": "Quispe Ramos Rene Juan",
"documento_identificacion": "6949082LP"
}
],
"codeudores": [],
"garantes": [
{
"nombre": "Quinteros Cristina Rosaicela",
"documento_identificacion": "5950265LP"
},
{
"nombre": "Vargas Quispe Carlos",
"documento_identificacion": "9868009LP"
},
{
"nombre": "Ramos Daza Elizabeth Sandra",
"documento_identificacion": "4806740LP"
},
{
"nombre": "Chambi Amos Tania",
"documento_identificacion": "6996198LP"
},
{
"nombre": "Quispe Ramos Rene Juan",
"documento_identificacion": "6949082LP"
}
],
"capital": {
"capital_desembolsado": 9500,
"capital_cancelado": 6218.9,
"saldo_capital": 3281.1,
"fecha_ultimo_pago": "2016-03-08"
},
"interes": {
"interes": 8179.78,
"pago_acuenta": 290.9,
"saldo_interes": 7888.88,
"fecha_ultimo_pago": "2016-03-08",
"fecha_calculo": "2023-01-03",
"dias_transcurridos": 2493
},
"penal": {
"penalidad": 1346.89,
"pago_acuenta": 0,
"saldo_penal": 1346.89,
"fecha_incumplimiento": "2016-04-06",
"fecha_calculo": "2023-01-03",
"dias_transcurridos": 2463
},
"cargos": [
{
"descripcion_cargo": "Precio diferido",
"monto_cargo": "65.28"
}
]
},
"message": "ok"
}
        """
        objeto_json = json.loads(datos_json)
        estado=objeto_json["success"]
        estado_data=objeto_json["data"]
        if(estado is True):
            datos_label=objeto_json["data"]
            codigo_operacion=datos_label['codigo_operacion']
            ultima_cuota_pagada='Cuota '+datos_label['numero_cuota']+' con vencimiento el '+datos_label['fecha_vencimiento_cuota']+' pagado en fecha '+datos_label['fecha_pago_cuota']
            grupo_solidario=datos_label['grupo_solidario']
            titulares=[]
            if(len(datos_label['titulares'])>0):
                for item in datos_label['titulares']:
                    lista=(item['nombre']+'-'+item['documento_identificacion'])
                    titulares.append(lista)
                texto_titular=""
                for grupo in titulares:
                    lista= (grupo)
                    texto_titular=texto_titular+", "+lista
            else:
                texto_titular="--"
            
            codeudores=[]
            if(len(datos_label['codeudores'])>0):
                for item in datos_label['codeudores']:
                    lista=(item['nombre']+'-'+item['documento_identificacion'])
                    codeudores.append(lista)
                texto_codeudores=""
                for grupo in codeudores:
                    lista= (grupo)
                    texto_codeudores=texto_codeudores+", "+lista
            else:
                texto_codeudores="*-"
                
            garantes=[]
            if(len(datos_label['garantes'])>0):
                for item in datos_label['garantes']:
                    lista=(item['nombre']+'-'+item['documento_identificacion'])
                    garantes.append(lista)
                texto_garantes=""
                for grupo in garantes:
                    lista= (grupo)
                    texto_garantes=texto_garantes+", "+lista
            else:
                texto_garantes="--"
               
            importe_inicial=datos_label['monto_desembolsado']
            fecha_inicio=datos_label['fecha_inicio']    
            tasa_interes=(str(datos_label['tasa_interes'])+' % mensual')
            plazo=str(datos_label['numero_cuotas'])+' '+datos_label['frecuencia']
            estado=datos_label['estado']
#************************************ENCABEZADO***********************************************************************************************
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
            self.cabecera_logo(pdf)
    #*********************************controlador de grupos pa la cordenada de y
            if(grupo_solidario=='-'):
                y_pos=2.3*cm 
            else:
                y_pos=1*cm   
    #******************************LINEAS GRUESAS*****************************
            pdf.setStrokeColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
            pdf.setFillColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
            pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
            pdf.roundRect(1*cm, 16.7*cm+y_pos, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
            #---------------------LINEAS DELGADAS
            pdf.line(1*cm,19.3*cm+y_pos,20*cm,19.3*cm+y_pos)
            
    #****************************TEXTO LABEL*************************************************************************************        
    #****************TEXTOS EN NEGRILLLAS
            pdf.setFont("Helvetica-Bold", 9)
            pdf.drawString(1 * cm, 27 * cm , "Datos de la operación ")
            pdf.drawString(1 * cm, 26.3 * cm , "Operación: ")
            pdf.drawString(10 * cm, 26.3 * cm , "Grupo solidario: ")
            pdf.drawString(1 * cm,18.7 * cm+y_pos,"Ultimos pagos efectuados")
    #****************TEXTOS NORMAL (DATOS DE LA OPERARCION
            pdf.setFont("Helvetica-Bold", tamano_letra)
            pdf.setFillColorRGB(0,0,0) 
            #pdf.drawString(1 * cm,24.9  * cm , "Titular(es):")
            #pdf.drawString(1 * cm,23.2 * cm,"Codeudor(es):")
            #pdf.drawString(1 * cm,21.5 * cm,"Garantes:")
            pdf.drawString(1 * cm,20.5 * cm+y_pos,"Importe inicial:")
            pdf.drawString(6 * cm,20.5 * cm+y_pos,"Fecha de inicio:")
            pdf.drawString(11 * cm,20.5 * cm+y_pos,"Tasa interés:")
            pdf.drawString(17 * cm,20.5 * cm+y_pos,"Plazo:")
            pdf.drawString(1 * cm,19.8 * cm+y_pos,"Estado:")
            style_subtitulo = ParagraphStyle(
                name='Normal',
                fontName='Helvetica-Bold',
                fontSize=8,
                borderColor=colors.black
                
            )
            style = ParagraphStyle(
                name='Normal',
                fontName='Helvetica',
                fontSize=8,
                textColor='black',
                borderPadding = 10,
                borderColor=colors.black
                #spaceAfter=spaceAfter + 2 * borderPadding
                #leading=9,
                #borderColor=gray,
                
            )
            celda_titulo=[Paragraph('Justificación o motivo',style = style_subtitulo)]
            espacio_ariba=['']
            titulares = [Paragraph('Titular(es):',style = style_subtitulo),'',Paragraph(texto_titular[1:],style = style),'']
            codeudor = [Paragraph('Codeudor(es):',style = style_subtitulo),'',Paragraph(texto_codeudores[1:],style = style),'']
            garantes = [Paragraph('Garantes:',style = style_subtitulo),'',Paragraph(texto_garantes[1:],style = style),'']
            detalle_orden = Table([titulares]+[codeudor]+[garantes],colWidths=[2.4*cm,0.1*cm,16.8*cm,0.1*cm])
            detalle_orden.setStyle(TableStyle([
                #('FONT', (0,0), (1,1), 'Helvetica-Bold', 4 ),
                #('LINEABOVE',(0,0),(-1,-1),1,colors.gray),
                #('SPAN',(0,0),(1,1)),
                #('GRID', (1, 0), (-1, -1), 1, colors.gray),
                ('BACKGROUND', (1, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('BACKGROUND', (1, 1), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('BACKGROUND', (1, 2), (-1, 2), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                #('FONT', (0,0), (-1,1), 'VeraBd',3),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
                ('FONT', (0,0), (-1,-1), 'Helvetica',8),
                ('BOX', (2,0), (2,0), 5.5, colors.gray),
                ('BOX', (2,1), (2,1), 5.5, colors.gray),
                ('BOX', (2,2), (2,2), 5.5, colors.gray),
                
                #('BOX', (1,0), (-1,-1), 6, colors.gray),
                #('BOX',(0,0),(1,-1),4.5,colors.yellow),
                ('GRID', (1, 0), (-1, -1), 4, colors.white),
                ('BOX', (1,0), (3,-1), 6, colors.white),
                #('LINEABOVE',(2,0),(2,0),1,colors.gray),
                #('LINEABOVE',(2,3),(2,3),1,colors.gray),
                #('LINEABOVE',(2,3),(2,3),3,colors.blue),
                ]))
            detalle_orden.wrapOn(pdf, 800, 600)
            detalle_orden.drawOn(pdf, 0.8 * cm, 21.5 * cm+y_pos)
            
    #****************TEXTOS NORMAL (DATOS ULTIMOS PAGOS EFECTUADOS)
            pdf.drawString(1 * cm,18  * cm +y_pos, "Ultima cuota pagada completa:")
            pdf.drawString(1 * cm,17.3 * cm+y_pos,"Cuota(s) impaga(s):")
    ###************************CELDAS DATOS PERSONALES ******************************************************
    ## dato de prueba
            dato="prueba"
            self.operacion(pdf,codigo_operacion,row_celda,grid,fontsize,backgroud,valig)
            self.grupo(pdf,grupo_solidario,row_celda,grid,fontsize,backgroud,valig)
            #self.titulares(pdf,titulares,style,row_celda,grid,fontsize,backgroud,valig)
            #self.codeudor(pdf ,codeudores,style,row_celda,grid,fontsize,backgroud,valig)
            #self.garantes(pdf ,garantes,style,row_celda,grid,fontsize,backgroud,valig)
            self.importe_inicial(pdf ,importe_inicial,row_celda,grid,fontsize,backgroud,valig,y_pos)
            self.fecha_inicio(pdf ,fecha_inicio,row_celda,grid,fontsize,backgroud,valig,y_pos)
            self.taza_interes(pdf ,tasa_interes,row_celda,grid,fontsize,backgroud,valig,y_pos)
            self.plazo(pdf ,plazo,row_celda,grid,fontsize,backgroud,valig,y_pos)
            self.estado(pdf ,estado,row_celda,grid,fontsize,backgroud,valig,y_pos)
            #-------------Ultimos pagos efectuados
            self.ultima_cuota(pdf ,ultima_cuota_pagada,row_celda,grid,fontsize,backgroud,valig,y_pos)
            self.cuota_impage(pdf ,dato,row_celda,grid,fontsize,backgroud,valig,y_pos)
            self.tabla_liquidacion_prestamo(pdf,datos_label,row_celda,grid,fontsize,backgroud,valig,y_pos)
            
            pdf.setFont("Helvetica", 9)
            pdf.drawString(10.2 * cm, 0.5 * cm , "1/1")
            

            pdf.showPage()
            #********************
            
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
        else:
            if(estado is False):
                self.cabecera_logo(pdf)
                pdf.setStrokeColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
                pdf.setFillColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
                
                pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
                pdf.setFont("Helvetica-Bold", 18)
                pdf.drawString(1 * cm, 24.5 * cm , "La operacion "+codigo+" no existe o No admite liquidacion")
                pdf.showPage()
                #********************
                pdf.save()
                pdf = buffer.getvalue()
                buffer.close()
                response.write(pdf)
                return response
                #return Response({'message':'La operacion no existe o No admite liquidacion '},status=status.HTTP_406_NOT_ACCEPTABLE)      

#/////////////////////////////METODOS DE LOS DATOS EN CELDA************************************************
#************************DATOS PERSONALES************************************************
    def operacion(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=5.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.1 * cm, 26.2 * cm)
    def grupo(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=5.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 12.7 * cm, 26.2 * cm)
    def titulares(self,pdf,dato,style,row_celda,grid,fontsize,backgroud,valig):
        texto=""
        for grupo in dato:
            lista= (grupo)
            texto=texto+", "+lista
        celda=[Paragraph(texto[1:],style = style)]
        detalle_orden = Table([celda],colWidths=16.9*cm)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.1 * cm, 24.5 * cm)
    def codeudor(self,pdf,dato,style,row_celda,grid,fontsize,backgroud,valig):
        texto=""
        detalle=[]
        for grupo in dato:
            lista= (grupo)
            texto=texto+", "+lista
            detalle.append(texto)
        celda=[Paragraph(texto[1:],style = style)]
        detalle_orden = Table([celda],colWidths=16.9*cm)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.1 * cm, 22.8 * cm)
    
    def garantes(self,pdf,dato,style,row_celda,grid,fontsize,backgroud,valig):
        texto=""
        detalle=[]
        for grupo in dato:
            lista= (grupo)
            texto=texto+", "+lista
            detalle.append(texto)
        celda=[Paragraph(texto[1:],style = style)]
        detalle_orden = Table([celda],colWidths=16.9*cm)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.1 * cm, 21.1 * cm)

    def importe_inicial(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig,y_pos):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=2.1*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.1 * cm, 20.4 * cm+y_pos)
    def fecha_inicio(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig,y_pos):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 8.2 * cm, 20.4 * cm+y_pos)
    def taza_interes(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig,y_pos):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=3*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13 * cm, 20.4 * cm+y_pos)
    def plazo(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig,y_pos):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 18 * cm, 20.4 * cm+y_pos)
    def estado(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig,y_pos):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=3.9*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.1 * cm, 19.7 * cm+y_pos)
    
    def ultima_cuota(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig,y_pos):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=14.7*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 5.3 * cm, 17.9 * cm+y_pos)
    def cuota_impage(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig,y_pos):
        celda = ['falta probar']
        detalle_orden = Table([celda],colWidths=16.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.8 * cm, 17.2 * cm +y_pos)
    #-----------------------Tabla de liquidacion-----------------------------------------
    def tabla_liquidacion_prestamo(self,pdf,datos,row_celda,grid,fontsize,backgroud,valig,y_pos):
        #-----datos de capital
        capital_desembolso=datos['capital']['capital_desembolsado']
        capital_cancelado=datos['capital']['capital_cancelado']
        saldo_capital=datos['capital']['saldo_capital']
        fecha_ultimo_pago=datos['capital']['fecha_ultimo_pago']
        encabezados = ['Concepto', 'Descripción', 'Importe desembolsado','Amortización','Saldo']
        capital=[]
        lista_capital=('Capital','Fecha ultimo pago: '+fecha_ultimo_pago,capital_desembolso,capital_cancelado,saldo_capital)
        capital.append(lista_capital)
        #------datos de iteres-------------------------------
        interes_dato=datos['interes']['interes']
        pago_acuenta=datos['interes']['pago_acuenta']
        saldo_interes=datos['interes']['saldo_interes']
        fecha_ultimo_pago=datos['interes']['fecha_ultimo_pago']
        fecha_calculo=datos['interes']['fecha_calculo']
        dias_transcurridos=str(datos['interes']['dias_transcurridos'])
        encabezados_interes = ['Interés', '', 'Interes a la fecha','Pago a cuenta','Saldo']
        interes=[]
        lista_interes=('','Intereses pagado al: '+fecha_ultimo_pago+'\nFecha de calculo: '+fecha_calculo+'\nDías trancuridos: '+dias_transcurridos+' días',interes_dato,pago_acuenta,saldo_interes)
        interes.append(lista_interes)
        #-------datos interes penal------------------------
        penalidad=datos['penal']['penalidad']
        pago_acuenta_penal=datos['penal']['pago_acuenta']
        saldo_penal=datos['penal']['saldo_penal']
        fecha_incumplimiento=str(datos['penal']['fecha_incumplimiento'])
        fecha_calculo_penal=datos['penal']['fecha_calculo']
        dias_transcurridos_penal=str(datos['penal']['dias_transcurridos'])
        
        encabezado_interes_penal=['Interés penal','','Penalidad a la fecha','Pago a cuenta','Saldo']
        interes_penal=[]
        lista_interes_penal=('','Fecha de incumplimiento: '+fecha_incumplimiento+'\nFecha de calculo: '+fecha_calculo_penal+'\nDías trancuridos: '+dias_transcurridos_penal+' días',penalidad,pago_acuenta_penal,saldo_penal)
        interes_penal.append(lista_interes_penal)
        #--------datos gastos y costos--------------------------------
        gastos_costos=[]
        lista_gastos=['Gastos, costos legales y honorarios profesionales','','Importe','Pago a cuenta','Saldo']
        gastos_costos.append(lista_gastos)
        suma_monto_cargo=0.0
        gastos_costos=[]
        for item in datos['cargos']:
            suma_monto_cargo=suma_monto_cargo+float(item['monto_cargo'])
            lista=('',item['descripcion_cargo'],item['monto_cargo'],'0.00',item['monto_cargo'])
            gastos_costos.append(lista)
        
        detalle=[]
        cont=0
        for grupo in gastos_costos:
            cont+=1
            lista= (grupo)
            detalle.append(lista)
        #el numero 6 representa el alto de la celda
        espaciolibre=(14-cont)*6
        y_n=(espaciolibre+20)*mm
        detalle_orden = Table([encabezados] + capital+
                              [encabezados_interes]+interes+
                              [encabezado_interes_penal]+interes_penal+
                              [lista_gastos]+detalle, 
                        #colWidths=[59, 160, 60 , 60,60,100],rowHeights=[15,20,15,50,15,50,15,15])
                        colWidths=[2.5*cm, 6*cm, 3.5*cm , 3.5*cm,3.5 *cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(1,0),'CENTER'),
                #('ALIGN',(1,1),(0,0),'LEFT')
                ('ALIGN', (2,0), (-1,-1), 'RIGHT'),
                ('ALIGN', (2,1), (-1,-1), 'RIGHT'),
                
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (5, 0), (-1, -1), 0, colors.white),
                ('BOX',(0,0),(-1,-1),1,colors.gray),
                #saldos con linea negros 
                #('GRID', (0, 3), (7, 2), 0, colors.black), 
                #borde sin celda
                #('GRID', (0, 1), (-1, -1), 0, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONT', (0,0), (-1,0), 'Helvetica-Bold',8  ),
                #item isquierdos en negrillas
                ('FONT', (0,1), (0,-1), 'Helvetica-Bold',8  ),
                #subtotales en negrillas
                ('FONT', (0,2), (-1,2), 'Helvetica-Bold',8  ),
                ('FONT', (0,4), (-1,4), 'Helvetica-Bold',8  ),
                ('FONT', (0,6), (-1,6), 'Helvetica-Bold',8  ),
                #('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),
                
                ('LINEABOVE',(0,2),(-1,2),1,colors.gray),
                ('LINEABOVE',(0,4),(-1,4),1,colors.gray),
                ('LINEABOVE',(0,6),(-1,6),1,colors.gray),
                #('LINEABOVE',(0,7),(-1,7),1,colors.black),
                
                ('FONTSIZE', (0, 1), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ##span para el gasos
                #('SPAN',(0,6),(1,)),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 400, 300)
        
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 1*cm,y_n+y_pos)
        #pdf.line(1*cm,(y_n+6.15*mm),20*cm,(y_n+6.15*mm))
        pdf.setFont("Helvetica-Bold", 8)
        pdf.setFillColorRGB(0,0,0) 
        pdf.drawString(12.5 * cm,y_n-10*mm +y_pos, "Total deuda con la empresa:")
        pdf.drawString(12.5 * cm,y_n-17*mm +y_pos, "Honorarios Profesionales:")
        pdf.drawString(12.5 * cm,y_n-24*mm +y_pos, "Total general:")
        suma=0
        suma=float(suma+saldo_capital+saldo_interes+saldo_penal+suma_monto_cargo)
        total_suma=round(suma,2)
        celda_deuda = [total_suma]
        total_profesional=0.00
        celda_profesional = [total_profesional]
        total_general=float(total_suma+total_profesional)
        total_general=round(total_general,2)
        celda_general = [total_general]
        detalle_orden = Table([celda_deuda],colWidths=3*cm,rowHeights=15)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),('ALIGN',(0,0),(-1,0),'RIGHT'),('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17 * cm, (y_n-11*mm)+y_pos)
        #----------------------------------------------------------
        detalle_orden = Table([celda_profesional],colWidths=3*cm,rowHeights=15)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),('ALIGN',(0,0),(-1,0),'RIGHT'),('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17 * cm, (y_n-18*mm)+y_pos)
        #----------------------------------------------------------
        detalle_orden = Table([celda_general],colWidths=3*cm,rowHeights=15)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),('ALIGN',(0,0),(-1,0),'RIGHT'),('FONT', (-1,-1), (-1,-1), 'Helvetica-Bold',8  ),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17 * cm, (y_n-25*mm)+y_pos)
        
    