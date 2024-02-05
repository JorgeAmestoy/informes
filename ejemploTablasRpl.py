import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()# Esto es para que se cree un objeto de estilo

elementosDoc = []# Esto es para que se cree una lista de elementos del documento

imagen = Image("check.png")# SI fuese jppg tendria que poner el width y el height para que runnease
imagen2 = Image("JorgeAmestoy.jpg",50,100)# Esto es para que se cree una imagen
estiloCuerpoTexto = hojaEstilo['BodyText']# Damos un estilo BodyText al segundo párrafo, que será el texto a escribir.
estiloCuerpoTexto2 = hojaEstilo['Heading4']
#estiloCuerpoTexto.textColor = colors.pink# Esto es para que se cambie el color del texto a rojo
estiloCuerpoTexto.textColor = Color(0,0,150,0.5)
parrafo = Paragraph("<a backColor = 'green' fontSize = 15>Optare</a>", estiloCuerpoTexto)# Esto es para que se cree un parrafo con la cabecera. El segundo parametro es el estilo de la cabecera que he hecho antes.
parrafo2 = Paragraph("Optare", estiloCuerpoTexto2)# Esto es para que se cree un parrafo con la cabecera. El segundo parametro es el estilo de la cabecera que he hecho antes.


datos = [['Empresas', 'Candidato 1', 'Candidato 2', 'Especificaciones'],
         ['Ayco', 'Marcos', 'Rubén',' Desarrollado web con PHP'],
         ['Iterat', 'Borja','Juan', 'Reconocimiento de imágenes con OpenCV'],
         [[parrafo, parrafo2],'Lidier','Lucas','Aplicaciones para las Telecomunicaciones'],
         [[parrafo, imagen]]
         ]


# ES COLUMNA, FILA NO FILA, COLUMA
estilo = [('TEXTCOLOR',(0,0),(0,-1), colors.pink), # Esto significa que va a cambiar el color del texto de la fila y columna entera
         ('TEXTCOLOR',(1,0),(-1,0), colors.blueviolet),#
         ('TEXTCOLOR',(1,1),(-1,-1), colors.grey),
         ('BOX',(1,1),(-1,-1), 1.25, colors.grey),#  El 1.25 es el grosor de la linea y el color es el gris
         ('INNERGRID',(1,1),(-1,-1), 1.25, colors.lightgrey),# El 1.25 es el grosor de la linea y el color es el gris claro
         ('VALING',(0,0),(-1,-1), 1.25, 'MIDDLE'),# 'MIDDLE' es para que se centre el texto. VALING significa Vertical Align

          ]


tabla = Table(data=datos, style=estilo)# colWidths=100, rowHeights=30 Esto dentro de los parentesis para determinar el tamaño de la tabla. SI no lo pongo se ajusta al tamaño de la pagina
#tabla.setStyle(estilo). Otra forma de hacerlo.

elementosDoc.append(tabla)


documento = SimpleDocTemplate("ejemploTablas.pdf", pagesize=A4, showBoundary=0)# Esto es para que se cree un documento pdf con el nombre "ejemploDocPlatypus.pdf" y el tamaño A4. ShowBoundary es para que se muestre el borde de la hoja. Si es 0 no se muestra.
documento.build(elementosDoc)# Esto es para que se cree el documento pdf con los elementos de la lista de elementos del documento