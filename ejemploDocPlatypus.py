import os

from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

hojaEstilo = getSampleStyleSheet()# Esto es para que se cree un objeto de estilo
elementosDoc = []# Esto es para que se cree una lista de elementos del documento
cabecera = hojaEstilo['Heading4']# Definimos cómo queremos que sea el estilo de la PageTemplate.
cabecera.pageBreakBefore = 0#No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).
cabecera.keepWithNext = 1# Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.
# cabecera.fontSize = 20# Esto es para que se cambie el tamaño de la fuente a 20. TAmbien puedo cambiarlo poniendolo en la etiqueta.
cabecera.backColor = colors.dimgray# Esto es para que se cambie el color de fondo de la cabecera a gris oscuro

parrafo = Paragraph("<a backColor = 'green' fontSize = 15>Cabecera del documento</a>", cabecera)# Esto es para que se cree un parrafo con la cabecera. El segundo parametro es el estilo de la cabecera que he hecho antes.
elementosDoc.append(parrafo)# Añadimos el parrafo a la lista de elementos del documento

contenidoDocumento = "Este es el contenido del documento, el cual va a ocupar múltiples líneas "*100 # Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.
estiloCuerpoTexto = hojaEstilo['BodyText']# Damos un estilo BodyText al segundo párrafo, que será el texto a escribir.
parrafo = Paragraph(contenidoDocumento, estiloCuerpoTexto)# Esto es para que se cree un parrafo con el contenido del documento y el estilo del cuerpo del texto
# Tengo dos variables que se llaman párrafos, pero son distintas. Una es el estilo de la cabecera y otra es el contenido del documento. Se sobrescriben.
elementosDoc.append(parrafo)# Añadimos el parrafo a la lista de elementos del documento
elementosDoc.append(Spacer(0, 20))# Esto es para que se añada un espacio de 20 puntos entre el parrafo y la imagen

imagen = Image("JorgeAmestoy.jpg",50,400)# Esto es para que se cree una imagen
elementosDoc.append(imagen)# Añadimos la imagen a la lista de elementos del documento

documento = SimpleDocTemplate("ejemploDocPlatypus.pdf", pagesize=A4, showBoundary=0)# Esto es para que se cree un documento pdf con el nombre "ejemploDocPlatypus.pdf" y el tamaño A4. ShowBoundary es para que se muestre el borde de la hoja. Si es 0 no se muestra.
documento.build(elementosDoc)# Esto es para que se cree el documento pdf con los elementos de la lista de elementos del documento