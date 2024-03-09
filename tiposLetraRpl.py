from reportlab.pdfgen import canvas


auxiliar = canvas.Canvas("tiposLetra.pdf")# Esto es para que se cree un documento pdf con el nombre "ejemploTextoRpl.pdf"

frase = "Esto es una bonita frase para ver los distintos tipos de letra"
objetoTexto = auxiliar.beginText()# Esto es para que se cree un objeto de texto
objetoTexto.setTextOrigin(20,500)# Esto es para que se establezca la posicion de origen del texto en (100,500)
#objetoTexto.setFillColor("pink")# Despues de for no funciona¿?. Esto es para que se cambie el color del texto.
espacioCaracteres =0
objetoTexto.setFillColorRGB(0.2,0,150)# Otra forma de cambiar el color del texto
for tipoLetra in auxiliar.getAvailableFonts(): # Recorro la lista de frases y tipos de letra
    objetoTexto.setCharSpace(espacioCaracteres)# Pongo cero en espacio entre caracteres
    objetoTexto.setFont(tipoLetra, 16)# Esto es para que se cambie la fuente del texto a Courier y el tamaño a 16
    objetoTexto.textLine(tipoLetra+ ": "+ frase)# Añado la frase al objeto de texto
    objetoTexto.moveCursor(15,10)# Esto es para que se mueva el cursor 15 espacios en el eje X y 10 en el eje Y
    espacioCaracteres = espacioCaracteres + 1# Esto es para que se incremente el espacio entre caracteres en 1


objetoTexto.setFillGray(0.5)# Esto es para que se cambie el color del texto a gris
objetoTexto.setFont("Helvetica",10)# Esto es para que se cambie la fuente del texto a Helvetica y el tamaño a 10
objetoTexto.setCharSpace(0)# Esto es para que se cambie el espacio entre caracteres
objetoTexto.setTextOrigin(30,800)# Esto es para que se establezca la posicion de origen del texto en (100,500) siendo x el ancho y y el alto
for i in range(10):# Esto es para que se repita 10 veces
    objetoTexto.setWordSpace(9)## Esto es para que se cambie el espacio entre palabras
    objetoTexto.textLine("Esto es una frase de ejemplo para ver como se puede cambiar el espacio entre palabras")

auxiliar.drawText(objetoTexto)# Añado el objeto de texto al documento pdf
auxiliar.showPage()
auxiliar.save()
