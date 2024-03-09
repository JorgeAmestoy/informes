from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# CREACIÓN CANVA
c = canvas.Canvas("Factura2canva.pdf", pagesize=A4)

# LADO IZQUIERDO
c.setFont("Helvetica-Bold",20)
c.setFillColor("green")
c.drawString(50,750,"Nombre de tu Empresa")# 50 de horizontal y 750 de vertical


c.setFont("Helvetica",12)
c.drawString(50,730,"Dirección:")
c.setFont("Helvetica",10)
c.setFillGray(0.25)
direccion = c.beginText(115, 730)
direccion.textLine("Lepanto, 1")
c.drawText(direccion)

c.setFillColor("green")
c.setFont("Helvetica",12)
c.drawString(50,710,"Ciudad y País:")
c.setFont("Helvetica",10)
c.setFillGray(0.25)
ciudad = c.beginText(130, 710)
ciudad.textLine("Pontevedra, España")
c.drawText(ciudad)

c.setFillColor("green")
c.setFont("Helvetica",12)
c.drawString(50,690,"CIF/NIF: ")
c.setFont("Helvetica",10)
c.setFillGray(0.25)
nif = c.beginText(100, 690)
nif.textLine("7654321C")
c.drawText(nif)

c.setFillColor("green")
c.setFont("Helvetica",12)
c.drawString(50,670,"Teléfono")
c.setFont("Helvetica",10)
telefono = c.beginText(100, 670)
c.setFillGray(0.25)
telefono.textLine("669 83 83 83")
c.drawText(telefono)

c.setFillColor("green")
c.setFont("Helvetica", 12)
c.drawString(50,650,"Mail: ")
c.setFont("Helvetica",10)
fecha = c.beginText(80, 650)
c.setFillGray(0.25)
fecha.textLine("jorge.amestoy@gmail.com")
c.drawText(fecha)

# LADO DERECHO
c.setFillColor("green")
c.setFont("Helvetica-Bold",20)
c.drawString(330,800,"FACTURA SIMPLIFICADA")
c.drawImage("check.png", 400, 700, 90, 70)

c.setFillColor("green")
c.setFont("Helvetica",12)
c.drawString(350,670,"Fecha de emisión")
c.setFont("Helvetica",10)
fecha = c.beginText(450, 670)
c.setFillGray(0.25)
fecha.textLine("DD/MM/AAAA")
c.drawText(fecha)

c.setFillColor("green")
c.setFont("Helvetica",12)
c.drawString(350,650,"Número de factura")
c.setFont("Helvetica",10)
num = c.beginText(460, 650)
c.setFillGray(0.25)
num.textLine("A0001")
c.drawText(num)

# TABLA
tabla_data = [['Descripción','Importe','Cantidad','Total'],
              ['Producto1','3,2','5','16,00'],
              ['Producto2', '2,5', '4', '10,00'],
              ['Producto3', '1,8', '3', '5,40'],
              ['Producto4', '2,7', '6', '16,20'],
              ['Producto5', '2,0', '8', '16,00'],
              ['Producto6', '3,3', '7', '23,10'],
              ]

estilo = [('TEXTCOLOR',(0,0),(-1,0), colors.white),# Establece el color del texto de la primera fila de la tabla como blanco.
('TEXTCOLOR',(0,1),(-1,-1), colors.black),# Establece el color de texto en negro desde la primera columna y segunda fila hasta el final de la tabla
('BACKGROUND',(0,0),(-1,0), colors.darkgreen),# Establece el color de fondo de la primera fila de la tabla como verde oscuro
('BACKGROUND',(0,1),(-1,-1), colors.lightgreen),# Estbalece color de fondo desde la primera columna y segunda fila hasta final de la tabla
('BOX',(0,0),(-1,-1), 0.5, colors.black),
('INNERGRID',(0,0),(-1,-1), 1, colors.black),
('VALIGN',(0,0),(-1,-1), 'TOP'), # Alinea verticalmente el texto de todas las celdas de la tabla al centro.
('ALIGN', (0, 0), (-1, -1), 'CENTER') # Alinea horizontalmente el texto de todas las celdas de la tabla al centro.
]

# TAMAÑO TABLA
tabla = Table(data=tabla_data, colWidths=[180, 100, 100, 100])
tabla.setStyle(estilo)

# POSICION TABLA EN LIENZO
tabla.wrapOn(c, 0, 0)
tabla.drawOn(c, 50, 500)

# TABLA 2
tabla_data2 = [['TOTAL','385€']
              ]

estilo2 = [('TEXTCOLOR',(0,0),(-1,-1), colors.white),# Establece el color del texto de la primera fila de la tabla como blanco.
('BACKGROUND',(0,0),(-1,-1), colors.darkgreen),# Establece el color de fondo de la primera fila de la tabla como verde oscuro
('BOX',(0,0),(-1,-1), 0.5, colors.black),
('INNERGRID',(0,0),(-1,-1), 1, colors.black),
('VALIGN',(0,0),(-1,-1), 'MIDDLE'), # Alinea verticalmente el texto de todas las celdas de la tabla al centro.
('ALIGN', (0, 0), (-1, -1), 'CENTER') # Alinea horizontalmente el texto de todas las celdas de la tabla al centro.
]

# TAMAÑO TABLA 2
tabla2 = Table(data=tabla_data2, colWidths=[100,100], rowHeights=[50])
tabla2.setStyle(estilo2)

# POSICION TABLA EN LIENZO
tabla2.wrapOn(c, 0, 0)
tabla2.drawOn(c, 330, 430)

# LINEA
c.line(50, 400, 575, 400)# Coordenadas de punto incial hasta el final

c.setFillColor("black")
c.setFont("Helvetica-Bold", 16)
c.drawRightString(420,350, "GRACIAS POR SU CONFIANZA")


# TABLA 3
tabla_data3 = [[''],
               ['']
              ]

estilo3 = [('BACKGROUND',(0,0),(0,0), colors.darkgreen),
('BACKGROUND',(0,1),(0,-1), colors.lightgreen)
]

# TAMAÑO TABLA 3
tabla3 = Table(data=tabla_data3, colWidths=[20], rowHeights=[50,600])
tabla3.setStyle(estilo3)

# POSICION TABLA EN LIENZO
tabla3.wrapOn(c, 0, 0)
tabla3.drawOn(c, 5, 170)

# TABLA 4
tabla_data4 = [['']
              ]

estilo4 = [('BACKGROUND',(0,0),(-1,-1), colors.lightgreen)
]

# TAMAÑO TABLA 4
tabla4 = Table(data=tabla_data4, colWidths=[20], rowHeights=[140])
tabla4.setStyle(estilo4)

# POSICION TABLA EN LIENZO
tabla4.wrapOn(c, 0, 0)
tabla4.drawOn(c, 5, 5)


c.showPage()# Esto es para que se cree una nueva pagina pdf
c.save()# Esto es para que se guarde el documento