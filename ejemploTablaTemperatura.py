import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()# Creo hoja de estilo

elementosDoc = []# Creo lista de elementos del documento vacío

# TABLA TEMPERATURAS
temperaturas = [['', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',# Dejo la primera celda vacia ya que corresponde a las etiquetas de las temperaturas max y min
                 'Julio', 'Agosto','Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
                ['Maximas', 15,16,20,25,27,31,35,38,30,25,20,18],
                ['Minimas',-3,-4,-1,4,6,9,12,16,12,8,2,-2]]

# ESTILO (Es columna, fila no fila,columna!!!!!!!!!!!)
estilo =[('TEXTCOLOR',(0,0),(-1,0), colors.grey),# Darle color desde la columna 0 hasta la ultima co0luma (-1, penultima seria -2) de la fila 0
         ('TEXTCOLOR',(0,1),(0,-1), colors.grey),#
         ('BOX',(1,1),(-1,-1), 1.50, colors.grey), #
         ('INNERGRID',(1,1),(-1,-1), 0.5, colors.lightgrey)]# INNERGRID es para que se cree una cuadricula en el interior de la tabla. El 1,1 es la posicion de la segunda fila y segunda columna y el -1,-1 es la posicion de la ultima fila y la ultima columna. El 0.25 es el grosor de la linea y el color es el gris claro
         # ('VALIGN',(0,0),(-1,-1), 'MIDDLE')]# VALIGN es para que se centre el texto. El 0,0 es la posicion de la primera fila y columna y el -1,-1 es la posicion de la ultima fila y la ultima columna. El 'MIDDLE' es para que se centre el texto. VALIGN significa Vertical Align

# Uso enumerate para saber el indice de la fila de la lista temperaturas.
for i,fila in enumerate(temperaturas):
   for j,temperatura in enumerate(fila): #Para saber el indice de la columna de la lista temperaturas
       if type(temperatura) == int:
           if temperatura>0:# Aqui se trabaja columna, fila y no fila, columna. POr eso j,i.
            estilo.append(('TEXTCOLOR',(j,i),(j,i), colors.black))# La j,i es la posicion de la fila y columna. Significa que va a cambiar el color del texto de la fila y columna entera¿?
            if temperatura > 30:
                estilo.append(('BACKGROUND', (j,i), (j,i), colors.fidred))
            elif temperatura<=30 and temperatura>20:
                estilo.append(('BACKGROUND', (j,i), (j,i), colors.orange))
            elif temperatura<=20 and temperatura>10:
                estilo.append(('BACKGROUND', (j,i), (j,i), colors.lightpink))
            elif temperatura<=10 and temperatura>0:
                estilo.append(('BACKGROUND', (j,i), (j,i), colors.lightblue))
       else:
        estilo.append(('TEXTCOLOR',(j,i),(j,i), colors.blue))
        estilo.append(('BACKGROUND',(j,i),(j,i),colors.lightgrey))
            
              


# CREACIÓN TABLA
tabla = Table(data=temperaturas)# colWidths=100, rowHeights=30 Esto dentro de los parentesis para determinar el tamaño de la tabla. SI no lo pongo se ajusta al tamaño de la pagina
tabla.setStyle(estilo)
elementosDoc.append(tabla)

# CREACIÓN PDF
documento = SimpleDocTemplate("ejemploTablaTemperatura.pdf", pagesize=A4, showBoundary=0)# Esto es para que se cree un documento pdf con el nombre "ejemploDocPlatypus.pdf" y el tamaño A4. ShowBoundary es para que se muestre el borde de la hoja. Si es 0 no se muestra.
documento.build(elementosDoc)# Esto es para que se cree el documento pdf con los elementos de la lista de elementos del documento