import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

hojaEstilo = getSampleStyleSheet()# Creo una hoja de estilo
elementosDoc = []# Creo una lista vacía para contener los elementos del documento.

# CABECERA
cabecera = hojaEstilo['Heading4']# Configuro el estilo de la cabecera ('Heading4').
cabecera.pageBreakBefore = 0# No se insertará un salto de página antes de la cabecera.
cabecera.keepWithNext = 1# La cabecera permanecerá junto al siguiente elemento.
#cabecera.fontSize = 20# Esto es para que se cambie el tamaño de la fuente a 20. TAmbien puedo cambiarlo poniendolo en la etiqueta de Paragraph debajo.
cabecera.backColor = colors.beige# Configuro el color de fondo de la cabecera como beige.
parrafo = Paragraph("<a backColor = 'green' fontSize = 15>Cabecera del documento</a>", cabecera)# Creo un párrafo con el texto "Cabecera del documento" utilizando el estilo de cabecera definido anteriormente.
elementosDoc.append(parrafo)# Agrego el párrafo a la lista de elementos del documento.

# CONTENIDO DOCUMENTO
contenidoDocumento = "Este es el contenido del documento, el cual va a ocupar múltiples líneas "*100 # 100 lineas
estiloCuerpoTexto = hojaEstilo['BodyText']# Configuro el estilo del cuerpo del texto ('BodyText').
parrafo = Paragraph(contenidoDocumento, estiloCuerpoTexto)# Creo un párrafo con el contenido del documento y el estilo del cuerpo del texto
elementosDoc.append(parrafo)# Añado el parrafo a la lista de elementos del documento
elementosDoc.append(Spacer(0, 20))# Agrego un espacio vertical de 20 puntos entre el párrafo y la imagen.

# IMAGEN
imagen = Image("JorgeAmestoy.jpg",50,400)# Creo y establezco tamaño de la imagen
elementosDoc.append(imagen)# Añado la imagen a la lista de elementos del documetno

# CREACIÓN PDF
documento = SimpleDocTemplate("ejemploDocPlatypus.pdf", pagesize=A4, showBoundary=0)# Esto es para que se cree un documento pdf con el nombre "ejemploDocPlatypus.pdf" y el tamaño A4. ShowBoundary es para que se muestre el borde de la hoja. Si es 0 no se muestra.
documento.build(elementosDoc)# Esto es para que se cree el documento pdf con los elementos de la lista de elementos del documento