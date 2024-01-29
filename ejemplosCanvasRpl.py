from reportlab.pdfgen import canvas


auxiliar = canvas.Canvas("primerDocumento.pdf")

auxiliar.drawString(0,0, "Posicion origen (X,Y) = (0,0)")
auxiliar.drawString(50,100, "Posicion (X,Y) = (50,100)")
auxiliar.drawString(150,20, "Posicion (X,Y) = (150,20)")
auxiliar.drawImage("check.png", 300, 700, 100, 100)# Esto es para que se inserte una imagen en el documento pdf
auxiliar.drawImage("JorgeAmestoy.jpg", 200, 700, 100, 100)

auxiliar.showPage()# Esto es para que se cree una nueva pagina pdf
auxiliar.save()# Esto es para que se guarde el documento
