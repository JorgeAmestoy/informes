import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()# Crep hoja de estilo

elementosDoc = []# Creo lista de elementos del documento vacía

# TABLA
datos = [['Arriba\nIzquierda','','02','03','04'],
         ['','','12','13','14'],
         ['20','21','22','Abajo\nDerecha',''],
         ['30','31','32','','']]


# ESTILO ( COLUMNA, FILA NO FILA, COLUMA!!!!!!!!!!)
estilo = [('GRID', (0, 0), (-1, -1),1, colors.grey), #Añade una rejilla con grosor 1 y color gris a todas las celdas.
          ('BACKGROUND', (0, 0), (1, 1), colors.lavender),# Colorea el fondo de las celdas de la esquina superior izquierda con color lavanda.
          ('SPAN', (0,0), (1, 1)),  # Esto es para que se una la celda de la fila 0 y columna 0 con la fila 1 y columna 1. # Combina las celdas de la esquina superior izquierda para formar una sola celda grande.
          ('BACKGROUND', (-2, -2), (-1, -1), colors.lavenderblush), # (-2, -2) se refiere a la penúltima fila y columna, mientras que (-1, -1) se refiere a la última fila y columna. Por lo tanto, esta línea de código establece un fondo de color lavanda claro (lavenderblush) para todas las celdas desde la penúltima fila y columna hasta la última fila y columna de la tabla.
          ('SPAN', (-2,-2), (-1, -1))]# Combina las celdas de la esquina inferior derecha para formar una sola celda grande.


# CREACIÓN TABLA
tabla = Table(data=datos)
tabla.setStyle(estilo)
elementosDoc.append(tabla)

# CREACIÓN PDF
documento = SimpleDocTemplate("ejemploTablasCombinadasRpl.pdf", pagesize=A4, showBoundary=0)  # Esto es para que se cree un documento pdf con el nombre "ejemploDocPlatypus.pdf" y el tamaño A4. ShowBoundary es para que se muestre el borde de la hoja. Si es 0 no se muestra.
documento.build(elementosDoc)  # Esto es para que se cree el documento pdf con los elementos de la lista de elementos del documento