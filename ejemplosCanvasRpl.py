from reportlab.pdfgen import canvas


c = canvas.Canvas("ejemplosCanvasRpl.pdf")# Creo documento pdf con ese nombre

c.drawString(0, 0, "Posicion origen (X,Y) = (0,0)")
c.drawString(50, 100, "Posicion (X,Y) = (50,100)")
c.drawString(150, 20, "Posicion (X,Y) = (150,20)")
c.drawImage("check.png", 300, 700, 100, 100)# Esto es para que se inserte una imagen en el documento pdf
c.drawImage("JorgeAmestoy.jpg", 200, 700, 100, 100)

c.showPage()# Esto es para que se cree una nueva pagina pdf
c.save()# Esto es para que se guarde el documento
