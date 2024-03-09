from reportlab.graphics.shapes import Image, Drawing # Esto es para que se pueda insertar una imagen en el documento pdf
from reportlab.graphics import renderPDF # Esto es para que se pueda renderizar el documento pdf (mostrarlo en el navegador)
from reportlab.lib.pagesizes import A4 # Esto es para que se pueda usar el tamaño A4

imagenes =[]
imagen = Image(0,0,300,281, "JorgeAmestoy.jpg")# # Crea una instancia de la clase Image con las coordenadas (0,0), un ancho de 300 y un alto de 281, y la imagen "JorgeAmestoy.jpg"
dibujo = Drawing()# Instancio clase Drawing, es como un lienzo. (Puedo darle el temaño dentro de los parentesis)
dibujo.add(imagen)# Agregar la imagen al dibujo
dibujo.translate(50,100)# Mover el dibujo a la posicion (0,700)
imagenes.append(dibujo)# Agregar el dibujo a la lista de imagenes

dibujo = Drawing()
dibujo.add(imagen)
dibujo.rotate(45)
dibujo.scale(1.5,0.5 )# Esto cambia de tamaño (escala) la imagen en el eje X a 1.5 y en el eje Y a 0.5
dibujo.translate(250,250)
imagenes.append(dibujo)

dibujo = Drawing(A4[0],A4[1])# Esto es para que el dibujo (la hoja del pdf) tenga el tamaño de la hoja A4 siendo 0 el ancho y 1 el alto. Si es 0,0 la hoja del pdf es un cuadrdado
for aux in imagenes:# Recorro la lista de imagenes
    dibujo.add(aux)# Las añado a este ultimo dibujo

renderPDF.drawToFile(dibujo, "ejemplosImageRpl.pdf", "Imagenes")# Esto es para que se renderize el documento pdf y se guarde con el nombre "ejemplosImageRpl.pdf" y el titulo "Imagenes"