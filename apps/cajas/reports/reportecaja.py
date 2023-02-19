
import json
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, CreateView
from apps.cajas.models import (Caja)
from apps.accounts.models import User
from apps.empresa.models.sucursal import Sucursal
from apps.cajas.models.arqueo import (CuentasPorCobrar,
                                        TransaccionInventario,
                                        EncabezadoArqueo,
                                        DetalleArqueo,
                                        CorteMoneda
                                        )
#***************
#from io import BytesIO
from django.views import View
from django.http import HttpResponse
# reportlab imports
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
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
class CajaReporte(View):
    import io  
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle  
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet  
    from reportlab.lib import colors  
    from reportlab.lib.pagesizes import letter  
    from reportlab.platypus import Table

    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = ImageReader('web/static/assets/media/Logos_JDGP/logomediano.jpg')
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen,0.5 * cm, 18 *cm,width=35*mm,height=45*mm,preserveAspectRatio=True)                

    def retrievefecha(self,data):
        global fecha_busqueda
        fecha_busqueda=data
        return fecha_busqueda

    def get(self, request, *args, **kwargs):
        caja_pk=kwargs["pk"]
        fecha_busqueda = datetime.strptime(kwargs["fecha"], '%d-%m-%Y' ).date()
        fecha_actual=datetime.now().strftime('%d/%m/%Y')
        user_actual=User.objects.get(id=self.request.user.pk)
        
        encabezado_arqueo=EncabezadoArqueo.objects.get(caja_id=caja_pk)
        fecha = encabezado_arqueo.fecha_arqueo.strftime('%d/%m/%Y')
        total_bs=encabezado_arqueo.total_arqueo_mn
        total_s=encabezado_arqueo.total_arqueo_me
        observacion=encabezado_arqueo.observaciones
        usuario=User.objects.get(id=encabezado_arqueo.usuario_id_id)
        datos_sucursal=Sucursal.objects.get(id=encabezado_arqueo.sucursal_creacion_id)
        sucursal=datos_sucursal.nombre
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #filename = f'caja-{caja_pk}-fecha-{fecha}.pdf'
        #response['Content-Disposition'] = f'attachment; filename={filename}'
        
        #pdf = canvas.Canvas("apps/reports/arqueo_caja.pdf")
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        w,h=A4
        pdf = canvas.Canvas(buffer,pagesize=landscape(letter))
       
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
       #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(11 * cm, 20 * cm , u"ARQUEO DE CAJA DEL DIA:"+fecha)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.setFont("Helvetica", 8)
        pdf.drawString(0.5 * cm, 0.5 * cm , "v2.0")
        pdf.drawString(27 * cm, 0.5 * cm , "1/1")
        pdf.drawString(0.5 * cm ,19.5 * cm ,"Sucursal: "+sucursal)
        pdf.drawString(25 * cm,19.9 * cm,"Fecha: "+fecha_actual)
        pdf.drawString(25 * cm,19.5 * cm,"Usuario: "+user_actual.username)
        y_titulos=18.9 *cm
        self.titulos1(pdf,y_titulos)
        self.titulos2(pdf,y_titulos)
        self.titulos3(pdf,y_titulos)
        #pdf.drawString(0.5 * cm,18.6 * cm,"Saldo Anterior: ")
        pdf.drawString(4.2 * cm,18.6 * cm,"Saldo Anterior: ")
        pdf.drawString(4.2 * cm,9.3 * cm,"Saldo Actual: ")
        #pdf.drawString(0.5 * cm,16.5 * cm,"Arqueo del dia:"+fecha)
        pdf.drawString(0.5 * cm,16 * cm,"Bolivianos ")
        pdf.drawString(1 * cm,5 * cm,"OBSERVACIONES: ")
        pdf.line(4*cm,h-800,9*cm,h-800)
        pdf.line(18*cm,h-800,23*cm,h-800)
        pdf.drawString(5 * cm,1 * cm,"JEFE DE SUCURSAL ")
        pdf.drawString(20 * cm,1 * cm,"CAJERO ")
        pdf.drawString(19.5 * cm,0.7 * cm,usuario.first_name+" "+usuario.last_name )
        
        y = 8 * cm 
        self.tabla_saldo_anterior(pdf, y,caja_pk,fecha_busqueda,total_bs,total_s)
        self.tabla_detalle_arqueo(pdf, y,caja_pk,fecha_busqueda,total_bs,total_s)
        self.tabla_resumen(pdf, y,caja_pk,fecha_busqueda,total_bs,total_s)
        self.tabla_inventario_saldo_anterior(pdf, y,caja_pk,fecha_busqueda)
        self.tabla_inventario(pdf, y,caja_pk,fecha_busqueda)
        self.tabla_inventario_saldo_actual(pdf, y,caja_pk,fecha_busqueda)
        self.tabla_cuentas_cobrar(pdf, y,caja_pk)
        y_ob=4*cm
        self.observacion(pdf,y_ob,observacion)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def titulos1(self,pdf,y2):
        encabezados = ['MATERIAL MONETARIO','','','']
        detalle_orden = Table([encabezados],colWidths=25,rowHeights=12)
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('SPAN',(0,0),(3,0)),
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 0.5*cm,y2)
    
    def titulos2(self,pdf,y):
        encabezados = ['INVENTARIO DE MERCADERIA','','','']
        detalle_orden = Table([encabezados],colWidths=82.5,rowHeights=12)
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('SPAN',(0,0),(3,0)),
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4.2*cm,y)
    def titulos3(self,pdf,y):
        encabezados = ['CUENTAS A RENDIR','','','']
        detalle_orden = Table([encabezados],colWidths=81.2,rowHeights=12)
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('SPAN',(0,0),(3,0)),
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 16*cm,y)
    
    def observacion(self,pdf,y,observacion):
        obs=[observacion,'','','']
        detalle_orden = Table([obs],colWidths=5.5*cm,rowHeights=50)
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'LEFT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('SPAN',(0,0),(3,0)),
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 4.2*cm,y)

    def tabla_saldo_anterior(self,pdf,y,caja_pk,fecha_busqueda,total_bs,total_s):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ['Saldo  Anterior:', '', '','']
        #Creamos una lista de tuplas que van a contener a las personas
        saldo=[]
        lista_t=('Efect.A','','','')
        saldo.append(lista_t)
        lista_t=('Efect.B','','','')
        saldo.append(lista_t)        
        lista_t=('Total','','','')
        saldo.append(lista_t)
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] +saldo, 
                        colWidths=[36,32,32,0],rowHeights=12)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                #('ALIGN',(0,0),(3,0),'CENTER'),
                ('ALIGN', (2,1), (-1,-1), 'LEFT'),
                ('SPAN',(0,0),(2,0)),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                #('SPAN',(0,0),(-1,-1)),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 0.5*cm,17*cm)
    def tabla_resumen(self,pdf,y,caja_pk,fecha_busqueda,total_bs,total_s):
        
        encabezado_arqueo=EncabezadoArqueo.objects.get(caja_id=caja_pk)
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ['Resumen:', '', '','']
        #Creamos una lista de tuplas que van a contener a las personas
        saldo=[]
        lista_t=('Mat. Monetario',encabezado_arqueo.total_arqueo_mn,'','')
        saldo.append(lista_t)
        lista_t=('Reporte "A"','','','')
        saldo.append(lista_t)
        lista_t=('Reporte "B"','','','')
        saldo.append(lista_t)
        lista_t=('Total Reporte','','','')
        saldo.append(lista_t)
        lista_t=('Diferencia','','','')
        saldo.append(lista_t)        
        lista_t=('Sobrante','','','')
        saldo.append(lista_t)
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] +saldo, 
                        colWidths=[60,40,0,0],rowHeights=12)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                ('ALIGN', (2,1), (-1,-1), 'LEFT'),
                ('ALIGN', (1,1), (-1,-1), 'RIGHT'),
                ('SPAN',(0,0),(1,0)),
                #fila span y aling final
                ('SPAN',(-4,-1),(1,-1)),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                #('SPAN',(0,0),(-1,-1)),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 0.5*cm,6.2*cm)
    def tabla_detalle_arqueo(self,pdf,y,caja_pk,fecha_busqueda,total_bs,total_s):
        fecha_inicio=fecha_busqueda
        fecha_fin=fecha_busqueda
        dia=1
        dt_obj_1=fecha_inicio-timedelta(dia,0)
        dt_obj_2=fecha_fin+timedelta(dia,0)
        
        # #Creamos una tupla de encabezados para neustra tabla
        encabezados = ['Corte', 'Cant.', 'Total','']
        #Creamos una lista de tuplas que van a contener a las personas
        total_boliviano=[]
        total_dolares=[]
        lista_bs=('Total Bs\nTotal $','',total_bs)
        total_boliviano.append(lista_bs)
        lista_s=('','',total_s)
        total_dolares.append(lista_s)
        detalles_p=[]
        detalle_arqueo=DetalleArqueo.objects.filter(arqueo_id=caja_pk).filter(creado_en__gte=dt_obj_1,creado_en__lte=dt_obj_2).filter(eliminado_en = None).order_by('corte_moneda_id_id')
        cont=0
        detalle2=[]
        cortes=['200','100','50','20','10','5','2','1','0.50','0.20','0.10','100']
        ide_corte=[2,4,6,8,10,22,24,26,28,30,32,52]
        pos=0
        sw=0
        for detalle in detalle_arqueo:
            sw=0
            while sw<1:
                if(ide_corte[cont]==detalle.corte_moneda_id_id):
                    print("pasa primer if ",ide_corte[cont],"el otro",detalle.corte_moneda_id_id)
                    lista=(cortes[pos],detalle.cantidad_corte_moneda,detalle.valor_corte_moneda,'')
                    lista2=(detalle.corte_moneda_id_id)
                    detalles_p.append(lista)
                    detalle2.append(lista2)
                    pos+=1
                    cont+=1
                    sw=1
                else:
                    print("pasa primer else ",ide_corte[cont],"el otro",detalle.corte_moneda_id_id)
                    
                    lista=(cortes[pos],'0','-','')
                    detalles_p.append(lista)
                    pos+=1
                    cont+=1
                    sw=0
        for i in range(len(ide_corte)):
            if(ide_corte[cont]==ide_corte[i]):
                print("datos finales",ide_corte[i])
                print("ultimo datos finales",ide_corte[-1])
                if(ide_corte[cont]==52):
                    print("-")
                else:
                    lista=(cortes[pos],'0','-','')
                    detalles_p.append(lista)
                cont=i+1
                pos+=1
        detalles_p.reverse()
        #################Calculando la posicion de la tabla
        espaciolibre=(21-cont)*4
        y_n=(espaciolibre+62)*mm
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles_p +total_boliviano+total_dolares, 
                        colWidths=[30,25,45,0],rowHeights=12)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                ('ALIGN', (2,1), (-1,-1), 'RIGHT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('SPAN',(-4,-2),(1,-1)),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 0.5*cm,y_n)
        #else:
        #    print(" *** no existe el id")
    
    def tabla_inventario_saldo_anterior(self,pdf,y,caja_pk,fecha_busqueda):
        fecha_inicio=fecha_busqueda
        fecha_fin=fecha_busqueda
        dia=1
        dt_obj_1=fecha_inicio-timedelta(dia,0)
        dt_obj_2=fecha_fin+timedelta(dia,0)
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ['Cod', 'Detalle', 'A','B','Total']
        #Creamos una lista de tuplas que van a contener a las personas
        saldo=[]
        lista_t=('51','Electrodomestico','','')
        saldo.append(lista_t)
        lista_t=('52','Viveres','','')
        saldo.append(lista_t)
        lista_t=('53','Temporada','','')
        saldo.append(lista_t)
        lista_t=('54','Art. del hogar','','')
        saldo.append(lista_t)
        lista_t=('55','Otros','','')
        saldo.append(lista_t) 
        lista_t=('Total','','res','res','res')
        saldo.append(lista_t) 
        #################Calculando la posicion de la tabla
        y_n=15.5*cm  
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + saldo, 
                        colWidths=[20, 110, 50 , 50,50],rowHeights=12)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(-1,-7),'CENTER'),
                ('ALIGN', (2,1), (-1,-1), 'RIGHT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('SPAN',(-4,-1),(0,-1)),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 400, 300)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 4.2*cm,y_n)
    def tabla_inventario_saldo_actual(self,pdf,y,caja_pk,fecha_busqueda):
        fecha_inicio=fecha_busqueda
        fecha_fin=fecha_busqueda
        dia=1
        dt_obj_1=fecha_inicio-timedelta(dia,0)
        dt_obj_2=fecha_fin+timedelta(dia,0)
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ['Cod', 'Detalle', 'A','B','Total']
        #Creamos una lista de tuplas que van a contener a las personas
        saldo=[]
        lista_t=('51','Electrodomestico','','')
        saldo.append(lista_t)
        lista_t=('52','Viveres','','')
        saldo.append(lista_t)
        lista_t=('53','Temporada','','')
        saldo.append(lista_t)
        lista_t=('54','Art. del hogar','','')
        saldo.append(lista_t)
        lista_t=('55','Otros','','')
        saldo.append(lista_t) 
        lista_t=('Total','','res','res','res')
        saldo.append(lista_t) 
        #################Calculando la posicion de la tabla
        y_n=6.2*cm  
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + saldo, 
                        colWidths=[20, 110, 50 , 50,50],rowHeights=12)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(-1,-7),'CENTER'),
                #('ALIGN',(1,1),(0,0),'LEFT')
                ('ALIGN', (2,1), (-1,-1), 'RIGHT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('SPAN',(-4,-1),(0,-1)),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 400, 300)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 4.2*cm,y_n)

    def tabla_inventario(self,pdf,y,caja_pk,fecha_busqueda):
        fecha_inicio=fecha_busqueda
        fecha_fin=fecha_busqueda
        dia=1
        dt_obj_1=fecha_inicio-timedelta(dia,0)
        dt_obj_2=fecha_fin+timedelta(dia,0)
        #Creamos una tupla de encabezados para neustra tabla
        encabezado = ('Movimiento del dia', '', 'A', '','B', '')
        encabezados = ('Cod', 'Detalle', 'Ingreso', 'Salida','Ingreso', 'Salida')
        #Creamos una lista de tuplas que van a contener a las personas
        transaccion=TransaccionInventario.objects.filter(caja_id=caja_pk).filter(eliminado_en = None).filter(creado_en__gte=dt_obj_1,creado_en__lte=dt_obj_2)
        detalle=[]
        cont=0
        for grupo in transaccion:
            cont+=1
            if(grupo.fondo=='A' and grupo.monto_ingreso > 0.00):
                lista= (grupo.producto_financiero_id,grupo.detalle,grupo.monto_ingreso,'-','-','-')
            if(grupo.fondo=='A' and grupo.monto_salida > 0.00):
                lista= (grupo.producto_financiero_id,grupo.detalle,'-',grupo.monto_salida,'-','-')
            if(grupo.fondo=='B' and grupo.monto_ingreso > 0.00):
                lista= (grupo.producto_financiero_id,grupo.detalle,'-','-',grupo.monto_ingreso,'-')
            if(grupo.fondo=='B' and grupo.monto_salida > 0.00):
                lista= (grupo.producto_financiero_id,grupo.detalle,'-','-','-',grupo.monto_salida)
            detalle.append(lista)
        espaciolibre=(20-cont)*4
        y_n=(espaciolibre+62)*mm
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezado] +[encabezados]+ detalle, colWidths=[20, 110, 50 , 50,50,50],rowHeights=12)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(4,0),'CENTER'),
                ('ALIGN',(0,1),(-1,-1),'CENTER'),
                ('ALIGN',(1,1),(-1,-1),'LEFT'),
                ('ALIGN', (2,2), (-1,-1), 'RIGHT'),
                ('SPAN',(0,0),(1,0)),
                ('SPAN',(2,0),(3,0)),
                ('SPAN',(4,0),(5,0)),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 1), (-1, 1), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 4.2*cm,y_n)
    
    def tabla_cuentas_cobrar(self,pdf,y,caja_pk):
        #Creamos una tupla de encabezados para neustra tabla
        #caja_impreso=Caja.objects.all()
        encabezados = ('N°', 'Fecha', 'Funcionario', 'Entrega','Devolucion', 'Saldo')
        #Creamos una lista de tuplas que van a contener a las personas
        cuentas_cobrar=CuentasPorCobrar.objects.filter(caja_id=caja_pk).filter(eliminado_en = None)
        detalles=[]
        cont=0
        for cuenta in cuentas_cobrar:
            cont+=1
            formato_fecha = cuenta.fecha_entrega.strftime('%d/%b/%Y')
            funcionario=User.objects.get(id=cuenta.funcionario_id_id)
            lista= (cont,formato_fecha,funcionario.first_name+' '+funcionario.last_name,cuenta.monto_entregado,cuenta.monto_devuelto,cuenta.monto_saldo)
            detalles.append(lista)
        while cont < 29:
            cont+=1
            lista=(cont,'','','','','')
            detalles.append(lista)
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[20, 55, 100 , 50,50,50],rowHeights=12)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(-1,-1),'CENTER'),
                ('ALIGN',(0,0),(-3,-1),'LEFT'),
                ('ALIGN', (3,1), (-1,-1), 'RIGHT'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 16*cm,6.2*cm)
