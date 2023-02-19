import json
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
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, landscape, portrait
from reportlab.lib.enums import TA_CENTER,TA_LEFT



class FichaDatos(View):
    import io  
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle  
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet  
    from reportlab.lib import colors  
    from reportlab.lib.pagesizes import letter  
    from reportlab.platypus import Table

    def cabecera_logo(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = ImageReader('web/static/assets/media/Logos_JDGP/logomediano.jpg')
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen,1 * cm, 26 *cm,width=50*mm,height=50*mm,preserveAspectRatio=True)                

    def get(self, request, *args, **kwargs):
        fecha_actual=datetime.now().strftime('%d/%m/%Y')
        user_actual=User.objects.get(id=self.request.user.pk)
#*****************VARIABLES GLOBALES****************************
        color_oscuro_R= 0.23
        color_oscuro_G=0.26
        color_oscuro_B=0.50
        color_plomo_RGB= 221
        tamano_letra=8
#************estilos de las celdas
        grid='GRID', (0, 0), (-1, -1), 1, colors.gray
        fontsize='FONTSIZE', (0, 0), (-1, -1), tamano_letra
        backgroud='BACKGROUND', (0, 0), (-1, 0), colors.Color(red=(221.0/255),green=(221.0/255),blue=(221.0/255))
        valig='VALIGN', (0,0), (-1, -1), 'MIDDLE'

        row_celda=11
#*********************************************************************        
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #filename = f'caja-{caja_pk}-fecha-{fecha}.pdf'
        #response['Content-Disposition'] = f'attachment; filename={filename}'
        #pdf = canvas.Canvas("apps/reports/arqueo_caja.pdf")
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        w,h=A4
        pdf = canvas.Canvas(buffer)
   
        #pdf = canvas.Canvas(buffer,pagesize=landscape(letter))
#************************************ENCABEZADO***********************************************************************************************
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera_logo(pdf)
       #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica-Bold", 12)
        pdf.setFillColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B) 
        pdf.drawString(8.5 * cm, 28.3 * cm , "FICHA DE DATOS")
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.setFont("Helvetica", 8)
        pdf.setFillColorRGB(0,0,0) 
        pdf.drawString(17.5 * cm,28.4 * cm,"Fecha: "+fecha_actual)
        pdf.drawString(17.5 * cm,28 * cm,"Usuario: "+user_actual.username)
#******************************LINEAS GRUESAS*****************************
        pdf.setStrokeColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
        pdf.setFillColorRGB(color_oscuro_R,color_oscuro_G,color_oscuro_B)
        pdf.roundRect(1*cm, 27.5*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
        pdf.roundRect(1*cm, 20*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
        pdf.roundRect(1*cm, 17.7*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
        pdf.roundRect(1*cm, 9.2*cm, 19*cm, 0.05*cm, 0, stroke = 1, fill = 1)
        pdf.line(1*cm,22.4*cm,20*cm,22.4*cm)
        pdf.line(1*cm,13.2*cm,20*cm,13.2*cm)
        pdf.line(1*cm,7.3*cm,20*cm,7.3*cm)
#****************************TEXTO LABEL*************************************************************************************        
#****************TEXTOS EN NEGRILLLAS
        pdf.setFont("Helvetica-Bold", 9)
        pdf.drawString(1 * cm, 27 * cm , "DATOS PERSONALES")
        pdf.drawString(1 * cm,22 * cm,"DATOS DEL CONYUGE")
        pdf.drawString(1 * cm,19.6 * cm,"DOMICILIO")
        pdf.drawString(1 * cm,17.2 * cm,"ACTIVIDAD")
        pdf.drawString(1 * cm,8.8 * cm,"REFERENCIA")
#****************TEXTOS NORMAL (DATOS PERSONAL)
        pdf.setFont("Helvetica", tamano_letra)
        pdf.setFillColorRGB(0,0,0) 
        pdf.drawString(1 * cm,26.5 * cm , "Primer Nombre:")
        pdf.drawString(1 * cm,26  * cm , "Segundo Nombre:")
        pdf.drawString(1 * cm,25.5 * cm,"Apellido Paterno:")
        pdf.drawString(1 * cm,25 * cm,"Apellido Materno:")
        pdf.drawString(1 * cm,24.5 * cm,"Apellido de Casada:")
        pdf.drawString(1 * cm,24 * cm,"Conocido Por:")
        pdf.drawString(1 * cm,23.5 * cm,"Género:")
        pdf.drawString(4 * cm,23.5 * cm,"Femenino")
        pdf.drawString(6.5 * cm,23.5 * cm,"Masculino")
        pdf.drawString(1 * cm,23 * cm,"Nro. Celular(WhatsApp):")
        #**************LADO DERECHO
        pdf.drawString(10.5 * cm,26.5 * cm , "No.C.I.:")
        pdf.drawString(16.5 * cm,26.5 * cm , "-")
        pdf.drawString(18.2 * cm,26.5 * cm , "Ext.:")
        pdf.drawString(10.5 * cm,26  * cm , "Fecha Nacimiento :")
        pdf.drawString(10.5 * cm,25.5 * cm,"Lugar Nacimiento:")
        pdf.drawString(10.5 * cm,25 * cm,"Nacionalidad:")
        pdf.drawString(10.5 * cm,24.5 * cm,"Estado civil (Ci):")
        pdf.drawString(10.5 * cm,24 * cm,"Estado civil según Visita:")
        pdf.drawString(10.5 * cm,23.5 * cm,"Dependientes:")
        pdf.drawString(10.5 * cm,23 * cm,"Correo electrónico:")
#****************TEXTOS NORMAL (DATOS DEL CONYUGE)
        pdf.drawString(1 * cm,21.5 * cm,"Apellido Paterno:")
        pdf.drawString(6.5 * cm,21.5 * cm,"Apellido Materno:")
        pdf.drawString(12.2 * cm,21.5 * cm,"Nombres:")
        pdf.drawString(1 * cm,21 * cm,"Actividad Principal:")
        pdf.drawString(14.5 * cm,21 * cm,"Nro. Celular(WhatsApp):")
        pdf.drawString(1 * cm,20.5 * cm,"Lugar de trabajo:")
        pdf.drawString(12.8 * cm,20.5 * cm,"No.C.I.:")
        pdf.drawString(16.5 * cm,20.5 * cm,"-")
        pdf.drawString(18.2 * cm,20.5 * cm,"Ext.:")
#****************TEXTO DE DOMICILIO
        pdf.drawString(1 * cm,19.1 * cm,"Dirección Domicilio:")
        pdf.drawString(11.5 * cm,19.1 * cm,"Nro. Puerta:")
        pdf.drawString(15 * cm,19.1 * cm,"Zona:")
        pdf.drawString(1 * cm,18.6 * cm,"Tenencia Vivienda:")
        pdf.drawString(3.5 * cm,18.6 * cm,"Propio")
        pdf.drawString(5.5 * cm,18.6 * cm,"Alquiler")
        pdf.drawString(7.5 * cm,18.6 * cm,"Anticrético")
        pdf.drawString(9.8 * cm,18.6 * cm,"Prestamo")
        pdf.drawString(12 * cm,18.6 * cm,"Familiar")
        pdf.drawString(14 * cm,18.6 * cm,"Otros")
        pdf.drawString(15.5 * cm,18.6 * cm,"Comentario:")
        pdf.drawString(1 * cm,18.1 * cm,"Referencia:")
        pdf.drawString(17 * cm,18.1 * cm,"Años Residencia:")
#***************TEXTO ACTIVIDAD***************
        pdf.drawString(1 * cm,16.7 * cm , "Actividad Principal:")
        pdf.drawString(12.5 * cm,16.7 * cm , "Años en el Rubro:")
        pdf.drawString(16.3 * cm,16.7 * cm , "Años en el Negocio:")
        pdf.drawString(1 * cm,16.2 * cm,"CAEDEC Act. Ppal:")
        pdf.drawString(1 * cm,15.7 * cm,"Dirección Act. Ppal:")
        pdf.drawString(14 * cm,15.7 * cm,"Zona:")
        pdf.drawString(1 * cm,15.2 * cm,"Referencia:")
        pdf.drawString(16.5 * cm,15.2 * cm,"Teléfono:")
        pdf.drawString(1 * cm,14.7 * cm,"Dias Laborales:")
        pdf.drawString(3.5 * cm,14.7 * cm,"LU")
        pdf.drawString(5 * cm,14.7 * cm,"MA")
        pdf.drawString(6.5 * cm,14.7 * cm,"MI")
        pdf.drawString(8 * cm,14.7 * cm,"JU")
        pdf.drawString(9.5 * cm,14.7 * cm,"VI")
        pdf.drawString(11 * cm,14.7 * cm,"SA")
        pdf.drawString(12.5 * cm,14.7 * cm,"DO")
        pdf.drawString(14.5 * cm,14.7 * cm,"Horario: desde")
        pdf.drawString(17.8 * cm,14.7 * cm,"hasta")
        pdf.drawString(1 * cm,14.2 * cm,"Tendencia Negocio:")
        pdf.drawString(3.6 * cm,14.2 * cm,"Propio")
        pdf.drawString(5.5 * cm,14.2 * cm,"Alquiler")
        pdf.drawString(7.5 * cm,14.2 * cm,"Anticrético")
        pdf.drawString(9.8 * cm,14.2 * cm,"Prestamo")
        pdf.drawString(12 * cm,14.2 * cm,"Familiar")
        pdf.drawString(14 * cm,14.2 * cm,"Otros")
        pdf.drawString(15.5 * cm,14.2 * cm,"Comentario:")
        pdf.drawString(1 * cm,13.7 * cm,"Tipo de negocio:")
        pdf.drawString(3.5 * cm,13.7 * cm,"Fijo")
        pdf.drawString(5 * cm,13.7 * cm,"Ambulante")
        pdf.drawString(7.5 * cm,13.7 * cm,"Tipo de ingreso:Dependiente")
        pdf.drawString(12.5 * cm,13.7 * cm,"Independiente")
        pdf.drawString(15.3 * cm,13.7 * cm,"Ingreso Mensual Aprox.:")

        pdf.drawString(1 * cm,12.7 * cm , "Actividad Secundaria:")
        pdf.drawString(12.5 * cm,12.7 * cm , "Años en el Rubro:")
        pdf.drawString(16.3 * cm,12.7 * cm , "Años en el Negocio:")
        pdf.drawString(1 * cm,12.2 * cm,"CAEDEC Act. Sec:")
        pdf.drawString(1 * cm,11.7 * cm,"Dirección Act. Sec:")
        pdf.drawString(14 * cm,11.7 * cm,"Zona:")
        pdf.drawString(1 * cm,11.2 * cm,"Referencia:")
        pdf.drawString(16.5 * cm,11.2 * cm,"Teléfono:")
        pdf.drawString(1 * cm,10.7 * cm,"Dias Laborales:")
        pdf.drawString(3.5 * cm,10.7 * cm,"LU")
        pdf.drawString(5 * cm,10.7 * cm,"MA")
        pdf.drawString(6.5 * cm,10.7 * cm,"MI")
        pdf.drawString(8 * cm,10.7 * cm,"JU")
        pdf.drawString(9.5 * cm,10.7 * cm,"VI")
        pdf.drawString(11 * cm,10.7 * cm,"SA")
        pdf.drawString(12.5 * cm,10.7 * cm,"DO")
        pdf.drawString(14.5 * cm,10.7 * cm,"Horario: desde")
        pdf.drawString(17.8 * cm,10.7 * cm,"hasta")
        pdf.drawString(1 * cm,10.2 * cm,"Tendencia Negocio:")
        pdf.drawString(3.6 * cm,10.2 * cm,"Propio")
        pdf.drawString(5.5 * cm,10.2 * cm,"Alquiler")
        pdf.drawString(7.5 * cm,10.2 * cm,"Anticrético")
        pdf.drawString(9.8 * cm,10.2 * cm,"Prestamo")
        pdf.drawString(12 * cm,10.2 * cm,"Familiar")
        pdf.drawString(14 * cm,10.2 * cm,"Otros")
        pdf.drawString(15.5 * cm,10.2 * cm,"Comentario:")
        pdf.drawString(1 * cm,9.7 * cm,"Tipo de negocio:")
        pdf.drawString(3.5 * cm,9.7 * cm,"Fijo")
        pdf.drawString(5 * cm,9.7 * cm,"Ambulante")
        pdf.drawString(7.5 * cm,9.7 * cm,"Tipo de ingreso:Dependiente")
        pdf.drawString(12.5 * cm,9.7 * cm,"Independiente")
        pdf.drawString(15.3 * cm,9.7 * cm,"Ingreso Mensual Aprox.:")
#*************TEXTOT REFERENCIA*****************************
        pdf.drawString(1 * cm,8.2 * cm,"Referencia Familiar:")
        pdf.drawString(12 * cm,8.2 * cm,"Celular:")
        pdf.drawString(15.4 * cm,8.2 * cm,"Parentesco:")
        pdf.drawString(1 * cm,7.7 * cm,"Dirección:")                
        pdf.drawString(1 * cm,6.7 * cm,"Referencia Personal:")
        pdf.drawString(12 * cm,6.7 * cm,"Celular:")
        pdf.drawString(15.4 * cm,6.7 * cm,"Parentesco:")
        pdf.drawString(1 * cm,6.2 * cm,"Dirección:")  

##************************CELDAS DATOS PERSONALES ******************************************************
# dato de prueba
        dato='prueba'       
        self.primer_nombre(pdf,dato,row_celda,grid,fontsize,backgroud,valig)
        self.segundo_nombre(pdf,dato,row_celda,grid,fontsize,backgroud,valig)
        self.apell_paterno(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.apell_materno(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.apell_casada(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.conocido(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.genero_femenino(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.genero_masculino(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.num_celular(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.num_celular_2(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.num_ci(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.num_ci_2(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.ext(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.fecha_nac(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.lugar_nac(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.nacionalidad(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.estado_civil(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.estado_civil_2(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.dependiente(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.correo(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        #---------------DATOS DEL CONYUGE-----------------------------
        self.apell_pater_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.apell_mater_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.nombre_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.activ_princ_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.num_celu_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.lugar_trabj_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.num_ci_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.num_ci_2_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.ext_conyuge(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        #---------------DATOS DEL DOMICILIO-----------------------------
        self.domicilio_direccion(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_num_puerta(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_zona(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_propio(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_alquiler(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_anticretico(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_prestamo(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_familiar(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_otros(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_comentario(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_referencia(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.domicilio_ano_residencia(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        #-------------------ACTIVIDAD 1----------------------------
        self.actividad_activ_principal(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_ano_rubro(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_ano_negocio(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_caedec(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_caedec_2(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_direcc_actpal(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_zona(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_referencia(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_telefono(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_LU(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_MA(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_MI(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_JU(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_VI(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_SA(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_DO(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_hora(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_hasta(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_propio(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_alquiler(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_anticretico(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_prestamo(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_familiar(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_otros(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_comentario(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_fijo(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_ambulante(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_dependiente(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_independiente(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_ingreso_mensual(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        #---------------------ACTIVIDAD SECUNDARIO---------------
        self.actividad_2_activ_secundario(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_ano_rubro(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_ano_negocio(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_caedec(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_caedec_2(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_direcc_actpal(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_zona(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_referencia(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_telefono(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_LU(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_MA(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_MI(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_JU(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_VI(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_SA(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_DO(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_hora(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_hasta(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_propio(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_alquiler(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_anticretico(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_prestamo(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_familiar(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_otros(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_comentario(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_fijo(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_ambulante(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_dependiente(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_independiente(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.actividad_2_ingreso_mensual(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        #----------------------REFERENCIA----------------------------------
        self.referencia_familiar(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.referencia_celular(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.referencia_parentesco(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.referencia_direccion(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        #--------------------referencia 2-----------------
        self.referencia_2_personal(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.referencia_2_celular(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.referencia_2_parentesco(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        self.referencia_2_direccion(pdf ,dato,row_celda,grid,fontsize,backgroud,valig)
        #------------------texto final y firma-------------------------
        self.texto_final(pdf,dato,grid,fontsize,backgroud,valig)
        self.firma(pdf,tamano_letra)
#------_2------------------------------------
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
#/////////////////////////////METODOS DE LOS DATOS EN CELDA************************************************
#************************DATOS PERSONALES************************************************
    
    def primer_nombre(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=6*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4*cm,26.4*cm)
        
    def segundo_nombre(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [dato,]
        detalle_orden = Table([celda],colWidths=6*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 25.9 * cm)

    def apell_paterno(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['Mamani']
        detalle_orden = Table([celda],colWidths=6*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 25.4 * cm)
    
    def apell_materno(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=6*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 24.9 * cm)

    def apell_casada(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=6*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 24.4 * cm)

    def conocido(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = [dato]
        detalle_orden = Table([celda],colWidths=6*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 23.9 * cm)
    
    def genero_femenino(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 5.5 * cm, 23.4 * cm)
    
    def genero_masculino(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 8 * cm, 23.4 * cm)

    def num_celular(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4.5 * cm, 22.9 * cm)

    def num_celular_2(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 7.5 * cm, 22.9 * cm)
    
    def num_ci(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 26.4 * cm)

    def num_ci_2(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=0.9*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 16.8 * cm, 26.4 * cm)

    def ext(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=1*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 19 * cm, 26.4 * cm)

    def fecha_nac(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=6.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 25.9 * cm)

    def lugar_nac(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=6.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 25.4 * cm)
    
    def nacionalidad(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=6.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 24.9 * cm)
    
    def estado_civil(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=6.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 24.4 * cm)
    
    def estado_civil_2(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=6.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 23.9 * cm)

    def dependiente(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=6.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 23.4 * cm)
    
    def correo(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=6.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 22.9 * cm)
#-------------------DATOS CONYUGE---------------------------
    def apell_pater_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=3*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.2 * cm, 21.4 * cm)
    
    def apell_mater_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=3*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 8.8 * cm, 21.4 * cm)
    
    def nombre_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=6.2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 21.4 * cm)

    def activ_princ_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=10.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.5 * cm, 20.9 * cm)

    def num_celu_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 18 * cm, 20.9 * cm)
    
    def lugar_trabj_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=9*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.5 * cm, 20.4 * cm)
    
    def num_ci_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.8 * cm, 20.4 * cm)

    def num_ci_2_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=0.9*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 16.8 * cm, 20.4 * cm)

    def ext_conyuge(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=1*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 19 * cm, 20.4 * cm)
    
    def domicilio_direccion(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=7.5*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.7 * cm, 19 * cm)

    def domicilio_num_puerta(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=1.6 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.1 * cm, 19 * cm)
    
    def domicilio_zona(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=4*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 16 * cm, 19 * cm)

    def domicilio_propio(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4.5 * cm, 18.5 * cm)

    def domicilio_alquiler(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 6.5 * cm, 18.5 * cm)
    
    def domicilio_anticretico(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 9 * cm, 18.5 * cm)
    
    def domicilio_prestamo(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 11.1 * cm, 18.5 * cm)

    def domicilio_familiar(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.2 * cm, 18.5 * cm)

    def domicilio_otros(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 14.8 * cm, 18.5 * cm)
    
    def domicilio_comentario(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=2.9*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17.1 * cm, 18.5 * cm)
    
    def domicilio_referencia(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=14*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 2.5 * cm, 18 * cm)

    def domicilio_ano_residencia(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 0.67 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 19.3 * cm, 18 * cm)
    
    def actividad_activ_principal(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 8.5 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.5 * cm, 16.6 * cm)
    
    def actividad_ano_rubro(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 1 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 14.8 * cm, 16.6 * cm)
    
    def actividad_ano_negocio(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 1 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 19 * cm, 16.6 * cm)
    
    def actividad_caedec(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 3 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.8 * cm, 16.1 * cm)

    def actividad_caedec_2(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 13 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 7 * cm, 16.1 * cm)

    def actividad_direcc_actpal(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 9.5 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.8 * cm, 15.6  * cm)

    def actividad_zona(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 5 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 15 * cm, 15.6 * cm)
    
    def actividad_referencia(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 13.5 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 2.5 * cm, 15.1 * cm)
    
    def actividad_telefono(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['12345678123']
        detalle_orden = Table([celda],colWidths= 2.3 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17.7 * cm, 15.1 * cm)
    
    def actividad_LU(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 14.6 * cm)

    def actividad_MA(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 5.5 * cm, 14.6 * cm)

    def actividad_MI(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 7 * cm, 14.6 * cm)

    def actividad_JU(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 8.5 * cm, 14.6 * cm)
    def actividad_VI(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 10 * cm, 14.6 * cm)
    def actividad_SA(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 11.5 * cm, 14.6 * cm)
    def actividad_DO(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13 * cm, 14.6 * cm)

    def actividad_hora(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['08:49']
        detalle_orden = Table([celda],colWidths= 1.3 * cm ,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 16.4 * cm, 14.6 * cm)
    def actividad_hasta(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['18:30']
        detalle_orden = Table([celda],colWidths= 1.3 * cm ,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 18.7 * cm, 14.6 * cm)
    def actividad_propio(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4.5 * cm, 14.1 * cm)

    def actividad_alquiler(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 6.5 * cm, 14.1 * cm)
    
    def actividad_anticretico(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 9 * cm, 14.1 * cm)
    
    def actividad_prestamo(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 11.1 * cm, 14.1 * cm)

    def actividad_familiar(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.2 * cm, 14.1 * cm)

    def actividad_otros(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 14.8 * cm, 14.1 * cm)
    
    def actividad_comentario(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['COMENTARIO']
        detalle_orden = Table([celda],colWidths=2.9*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17.1 * cm, 14.1 * cm)

    def actividad_fijo(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 13.6 * cm)
    def actividad_ambulante(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 6.5 * cm, 13.6 * cm)
    def actividad_dependiente(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 11.2 * cm, 13.6 * cm)
    def actividad_independiente(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 14.5 * cm, 13.6 * cm)
    def actividad_ingreso_mensual(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['12500']
        detalle_orden = Table([celda],colWidths= 1.5 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 18.5 * cm, 13.6 * cm)
    
    def actividad_2_activ_secundario(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 8.5 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.5 * cm, 12.6 * cm)
    
    def actividad_2_ano_rubro(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 1 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 14.8 * cm, 12.6 * cm)
    
    def actividad_2_ano_negocio(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 1 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 19 * cm, 12.6 * cm)
    
    def actividad_2_caedec(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 3 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.8 * cm, 12.1 * cm)

    def actividad_2_caedec_2(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 13 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 7 * cm, 12.1 * cm)

    def actividad_2_direcc_actpal(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 9.5 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.8 * cm, 11.6  * cm)

    def actividad_2_zona(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 5 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 15 * cm, 11.6 * cm)
    
    def actividad_2_referencia(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 13.5 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 2.5 * cm, 11.1 * cm)
    
    def actividad_2_telefono(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['12345678123']
        detalle_orden = Table([celda],colWidths= 2.3 *cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17.7 * cm, 11.1 * cm)
    
    def actividad_2_LU(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 10.6 * cm)

    def actividad_2_MA(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 5.5 * cm, 10.6 * cm)

    def actividad_2_MI(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 7 * cm, 10.6 * cm)

    def actividad_2_JU(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 8.5 * cm, 10.6 * cm)
    def actividad_2_VI(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 10 * cm, 10.6 * cm)
    def actividad_2_SA(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 11.5 * cm, 10.6 * cm)
    def actividad_2_DO(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13 * cm, 10.6 * cm)

    def actividad_2_hora(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['08:49']
        detalle_orden = Table([celda],colWidths= 1.3 * cm ,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 16.4 * cm, 10.6 * cm)
    def actividad_2_hasta(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['18:30']
        detalle_orden = Table([celda],colWidths= 1.3 * cm ,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 18.7 * cm, 10.6 * cm)
    def actividad_2_propio(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4.5 * cm, 10.1 * cm)

    def actividad_2_alquiler(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 6.5 * cm, 10.1 * cm)
    
    def actividad_2_anticretico(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 9 * cm, 10.1 * cm)
    
    def actividad_2_prestamo(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 11.1 * cm, 10.1 * cm)

    def actividad_2_familiar(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13.2 * cm, 10.1 * cm)

    def actividad_2_otros(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 14.8 * cm, 10.1 * cm)
    
    def actividad_2_comentario(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['COMENTARIO']
        detalle_orden = Table([celda],colWidths=2.9*cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17.1 * cm, 10.1 * cm)

    def actividad_2_fijo(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 4 * cm, 9.6 * cm)
    def actividad_2_ambulante(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 6.5 * cm, 9.6 * cm)
    def actividad_2_dependiente(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 11.2 * cm, 9.6 * cm)
    def actividad_2_independiente(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths=row_celda,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 14.5 * cm, 9.6 * cm)
    def actividad_2_ingreso_mensual(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['12500']
        detalle_orden = Table([celda],colWidths= 1.5 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 18.5 * cm, 9.6 * cm)
    #-------------------referencia 
    def referencia_familiar(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 8 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.8 * cm, 8.1 * cm)
    def referencia_celular(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 2 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13 * cm, 8.1 * cm)
    def referencia_parentesco(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 3 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17 * cm, 8.1 * cm)
    def referencia_direccion(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 17.5 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 2.5 * cm, 7.6 * cm)
    def referencia_2_personal(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 8 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 3.8 * cm, 6.6 * cm)
    def referencia_2_celular(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 2 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 13 * cm, 6.6 * cm)
    def referencia_2_parentesco(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 3 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 17 * cm, 6.6 * cm)
    def referencia_2_direccion(self,pdf,dato,row_celda,grid,fontsize,backgroud,valig):
        celda = ['']
        detalle_orden = Table([celda],colWidths= 17.5 * cm,rowHeights=row_celda)
        detalle_orden.setStyle(TableStyle([(grid),(fontsize),(backgroud),(valig),]))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 2.5 * cm, 6.1 * cm)
#**************************TEXTO FINAL*******************
    def texto_final(self,pdf,dato,grid,fontsize,backgroud,valig):
        var='JUAN CARLOS MAMANI MAMANIR'
        var2=' ReportLab incluye una API de bajo nivel para generar documentos PDF directamente desde Python, y un lenguaje de plantillas de más alto nivel similar a HTML y a los sistemas de plantilla que se emplean en el desarrollo web llamado RML. Generalmente la segunda opción suele ser más conveniente para aquellos que deban hacer un uso exhaustivo de las capacidades de la librería al momento de generar documentos. Para el resto de los casos, será suficiente con la API de bajo nivel que describiremos en este artículo. Como sea, puedes encontrar la documentación oficial del paquete en su totalidad en este enlace'
        styles=getSampleStyleSheet()
        #Estilos de la tabla para cabeceras y datos
        thead = styles["Normal"]
        thead.alignment=TA_LEFT
        thead.fontSize=8
        tbody = styles["BodyText"]
        tbody.alignment=TA_LEFT
        tbody.fontSize=6



        celda = []
        parafo=Paragraph('YO, '+var+'ReportLab incluye una API de bajo nivel para generar documentos PDF directamente desde Python, y un lenguaje de plantillas de más alto nivel similar a HTML y a los sistemas de plantilla que se emplean en el desarrollo web llamado RML. Generalmente la segunda opción suele ser más conveniente para aquellos que deban hacer un uso exhaustivo de las capacidades de la librería al momento de generar documentos. Para el resto de los casos, será suficiente con la API de bajo nivel que describiremos en este artículo. Como sea, puedes encontrar la documentación oficial del paquete en su totalidad en este enlace.',
                    styles['Heading6']
                    )
        dat=[Paragraph(str(var),thead),Paragraph(var2,tbody)]
        celda.append(dat)
        detalle_orden = Table([celda],colWidths= 19.5*cm)
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 0.8* cm, 3.8 * cm)
#********************************FIRMAS *********************************   
   
    def firma(self,pdf,tamano_letra):
        firma_blanco = ['','','']
        
        firma_letra=['FIRMA DEL CLIENTE','FIRMA Y SELLO DE ASESOR COMERCIAL','FIRMA Y SELLO PLATAFORMA']
        detalle_orden = Table([firma_blanco]+[firma_letra],colWidths=[6.5*cm,6.5*cm,6.5*cm,0],rowHeights=[2*cm,15])
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(firma_blanco) va a estar centrada
                ('ALIGN',(0,1),(-1,-1),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('LINEBELOW', (1, 1), (-1, 0), 2, colors.darkblue),
                ('FONTSIZE', (0, 0), (-1, -1), tamano_letra),
                ('FONT', (0,-1), (-1,-1), 'Helvetica-Bold',8  ),
                #('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                ('VALIGN', (0,0), (-1, -1), 'MIDDLE'),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 1*cm,1*cm)
    