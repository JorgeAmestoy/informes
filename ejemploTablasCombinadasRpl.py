import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()  # Esto es para que se cree un objeto de estilo

elementosDoc = []  # Esto es para que se cree una lista de elementos del documento

datos = [['Arriba\nIzquierda','','02','03','04'],
         ['','','12','13','14'],
         ['20','21','22','Abajo\nDerecha',''],
         ['30','31','32','','']]


# Es columna, fila no fila,columna.
estilo = [('GRID', (0, 0), (-1, -1),1, colors.grey),
          ('BACKGROUND', (0, 0), (1, 1), colors.lavender),
          ('SPAN', (0,0), (1, 1)),  # Esto es para que se una la celda de la fila 0 y columna 0 con la fila 1 y columna 1
          ('BACKGROUND', (-2, -2), (-1, -1), colors.lavenderblush),
          ('SPAN', (-2,-2), (-1, -1))]



tabla = Table(data=datos)
tabla.setStyle(estilo)

elementosDoc.append(tabla)

documento = SimpleDocTemplate("ejemploTablasCombinadasRpl.pdf", pagesize=A4, showBoundary=0)  # Esto es para que se cree un documento pdf con el nombre "ejemploDocPlatypus.pdf" y el tamaño A4. ShowBoundary es para que se muestre el borde de la hoja. Si es 0 no se muestra.
documento.build(elementosDoc)  # Esto es para que se cree el documento pdf con los elementos de la lista de elementos del documento