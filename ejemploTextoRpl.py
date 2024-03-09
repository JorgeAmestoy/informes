from reportlab.pdfgen import canvas



auxiliar = canvas.Canvas("ejemploTextoRpl.pdf")# Creo documento pdf

frase = ["Esto es una bonita frase", "para tener distintas partes",
         "en las que incluir en nuestro", "texto de ejemplo."]

objetoTexto = auxiliar.beginText()# Creo objeto de texto
objetoTexto.setTextOrigin(30,500)# Establezco la posicion de origen del texto en (100,500)
objetoTexto.setFont("Courier", 16)# Establezco fuente del texto y tamaño
objetoTexto.setFillGray(0.5)# Establezco color del texto en gris
#objetoTexto.setFillColorRGB()
for linea in frase: # Recorro la lista de frases
    objetoTexto.textLine(linea)# Añado la frase al objeto de texto


objetoTexto.setTextOrigin(30,800)# (Si no pongo este origen, se pone automáticamente debajo del texto de arriba)
parrafo = '''Esto es un párrafo de ejemplo para ver cómo se puede
incluir un párrafo en el documento pdf. 
Se puede dividir en varias
líneas, las cuáles se pueden alinear a la izquierda, 
derecha o centradas. También se puede cambiar el tamaño
y el tipo.'''


objetoTexto.textLines(parrafo)# Añado párrafo al objetoTexto(Lines en plural para añadir un parrafo)
auxiliar.drawText(objetoTexto)# Añado el objeto de texto al pdf
auxiliar.showPage()
auxiliar.save()