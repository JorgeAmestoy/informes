from reportlab.pdfgen import canvas

frase = ["Esto es una bonita frase", "para tener distintas partes",
         "en las que incluir en nuestro", "texto de ejemplo."]

auxiliar = canvas.Canvas("ejemploTextoRpl.pdf")# Esto es para que se cree un documento pdf con el nombre "ejemploTextoRpl.pdf"
objetoTexto = auxiliar.beginText()# Esto es para que se cree un objeto de texto
objetoTexto.setTextOrigin(30,500)# Esto es para que se establezca la posicion de origen del texto en (100,500)
objetoTexto.setFont("Courier", 16)# Esto es para que se cambie la fuente del texto a Courier y el tamaño a 16
for linea in frase: # Recorro la lista de frases
    objetoTexto.textLine(linea)# Añado la frase al objeto de texto

objetoTexto.setFillGray(0.5)# Esto es para que se cambie el color del texto a gris

parrafo = '''Esto es un párrafo de ejemplo para ver cómo se puede
incluir un párrafo en el documento pdf. 
Se puede dividir en varias
líneas, las cuáles se pueden alinear a la izquierda, 
derecha o centradas. También se puede cambiar el tamaño
y el tipo.'''

objetoTexto.textLines(parrafo)# Diferenciar textLine en singular y en plural. Esto es para que se añada el parrafo al objeto de texto
auxiliar.drawText(objetoTexto)# Esto es para que se añada el objeto de texto al documento pdf
auxiliar.showPage()
auxiliar.save()