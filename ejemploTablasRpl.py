import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Color

hojaEstilo = getSampleStyleSheet()# Creo hoja de estilo

elementosDoc = []# Creo lista de elementos del documento vacía

imagen = Image("check.png")# Creo imagen con formato png
imagen2 = Image("JorgeAmestoy.jpg",50,100)# Creo imagen con formato jpg(al ser jpg tengo que establecer ancho y alto)
estiloCuerpoTexto = hojaEstilo['Heading4']# Configuro el estilo del cuerpo del texto ('Heading4').
estiloCuerpoTexto2 = hojaEstilo['BodyText']# Configuro el estilo del cuerpo del texto ('BodyText').
#estiloCuerpoTexto.textColor = colors.greenyellow# Otra forma de cambiar el color del texto
estiloCuerpoTexto2.textColor = Color(0, 0, 150, 0.5)# Color azul oscuro
parrafo = Paragraph("Optare", estiloCuerpoTexto)# Creo párrafo con texto "Optare" y le aplico estilo creado anteriormente
parrafo2 = Paragraph("<a backColor = 'green' fontSize = 15>Optare</a>", estiloCuerpoTexto2)# Creo párrafo con texto "Optare" y le aplico estilo creado anteriormente


# TABLA
datos = [['Empresas', 'Candidato 1', 'Candidato 2', 'Especificaciones'],
         ['Ayco', 'Marcos', 'Rubén',' Desarrollado web con PHP'],
         ['Iterat', 'Borja','Juan', 'Reconocimiento de imágenes con OpenCV'],
         [[parrafo2, parrafo], 'Lidier', 'Lucas', 'Aplicaciones para las Telecomunicaciones'],
         [[parrafo2, imagen]]
         ]


# ESTILO ( COLUMNA, FILA NO FILA, COLUMA!!!!!!!!!!)
estilo = [('TEXTCOLOR',(0,0),(0,-1), colors.pink), #  Esto cambia el color del texto de la primera columna de la tabla a rosa.
         ('TEXTCOLOR',(1,0),(-1,0), colors.blueviolet),#Esto cambia el color del texto de la primera fila de la tabla a violeta.
         ('TEXTCOLOR',(1,1),(-1,-1), colors.grey),
         ('BOX',(1,1),(-1,-1), 1.25, colors.grey),# dibuja un borde alrededor de todas las celdas de la tabla (excepto la primera fila y la primera columna) con un grosor de 1.25 y un color gris.
         ('INNERGRID',(1,1),(-1,-1), 1.25, colors.lightgrey),# dibuja una cuadrícula interna dentro de todas las celdas de la tabla (excepto la primera fila y la primera columna) con un grosor de 1.25 y un color gris claro.
         ('VALING',(0,0),(-1,-1), 1.25, 'MIDDLE'),# Esto alinea verticalmente el texto de todas las celdas de la tabla al centro.
          ]

# CREACIÓN TABLA
tabla = Table(data=datos, style=estilo)# colWidths=100, rowHeights=30 Esto dentro de los parentesis para determinar el tamaño de la tabla. SI no lo pongo se ajusta al tamaño de la pagina
#tabla.setStyle(estilo). Otra forma de hacerlo.
elementosDoc.append(tabla)# Añado la tabla a la lista de documentos

# CREACIÓN PDF
documento = SimpleDocTemplate("ejemploTablas.pdf", pagesize=A4, showBoundary=0)# Esto es para que se cree un documento pdf con el nombre "ejemploDocPlatypus.pdf" y el tamaño A4. ShowBoundary es para que se muestre el borde de la hoja. Si es 0 no se muestra.
documento.build(elementosDoc)# Esto es para que se cree el documento pdf con los elementos de la lista de elementos del documento