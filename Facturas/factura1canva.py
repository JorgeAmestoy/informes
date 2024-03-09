from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

c = canvas.Canvas("Factura1canva.pdf", pagesize=A4)
c.setFont("Helvetica-Bold",20)
c.drawString(50,750,"Factura Proforma")# 50 de horizontal y 750 de vertical

c.drawImage("check.png", 400, 750, 90, 70)

# LADO IZQUIERDO
c.setFont("Helvetica",15)
c.drawString(50,700,"FACTURA A:")

c.setFont("Helvetica",15)
c.drawString(50,650,"Cliente:")
c.setFont("Helvetica",12)
cliente = c.beginText(120,650)
cliente.textLine("Jorge Amestoy")
c.drawText(cliente)

c.setFont("Helvetica",15)
c.drawString(50,630,"Domicilio:")
c.setFont("Helvetica",12)
calle = c.beginText(120,630,)
calle.textLine("Eduardo Pondal")
c.drawText(calle)

c.setFont("Helvetica",15)
c.drawString(50,610,"Código postal/ciudad: ")
c.setFont("Helvetica",12)
cp = c.beginText(200,610)
cp.textLine("36001, Pontevedra")
c.drawText(cp)

c.setFont("Helvetica",15)
c.drawString(50,590,"(NIF)")
c.setFont("Helvetica",12)
cp = c.beginText(120,590)
cp.textLine("77777777C")
c.drawText(cp)

# LADO DERECHO
c.setFont("Helvetica", 20)
nFactura = c.beginText(350,700)
nFactura.textLine("Nº DE FACTURA")
c.drawText(nFactura)

c.setFont("Helvetica", 14)
c.drawString(350,680,"Fecha: ")
c.setFont("Helvetica",12)
fecha = c.beginText(400, 680)
c.setFillGray(0.5)
fecha.textLine("23/08/1997")
c.drawText(fecha)

c.setFillColor("Black")
c.setFont("Helvetica", 14)
c.drawString(350,660,"Nº de pedido: ")
c.setFont("Helvetica",12)
c.setFillGray(0.5)
nPedido = c.beginText(440, 660)
nPedido.textLine("12345")
c.drawText(nPedido)

c.setFillColor("Black")
c.setFont("Helvetica", 14)
c.drawString(350,640,"Fecha de vencimiento: ")
c.setFont("Helvetica",12)
c.setFillGray(0.5)
vencimiento = c.beginText(500, 640)
vencimiento.textLine("08/08/2028")
c.drawText(vencimiento)

c.setFillColor("Black")
c.setFont("Helvetica", 14)
c.drawString(350,620,"Condiciones de pago: ")
c.setFont("Helvetica",12)
c.setFillGray(0.5)
pago = c.beginText(500, 620)
pago.textLine("Cash")
c.drawText(pago)

# TABLA
tabla_data = [['Pos.', ' Concepto/Descripción', 'Cantidad', 'Unidad','Precio\nUnitario', 'Importe'],
         ['1','','','','',''],
         ['1','','','','','']]

estilo = [('TEXTCOLOR',(0,0),(-1,0), colors.black),# Establece el color del texto de la primera fila de la tabla como negro.
('BACKGROUND',(0,0),(-1,0), colors.lightgrey), # Establece el color de fondo de la primera fila de la tabla como gris claro.
('BOX',(0,0),(-1,-1), 1.25, colors.black), # Dibuja un borde alrededor de todas las celdas de la tabla (excepto la primera fila y la primera columna) con un grosor de 1.25 y un color negro.
('INNERGRID',(0,0),(-1,-1), 1, colors.black), # Dibuja una cuadrícula interna dentro de todas las celdas de la tabla (excepto la primera fila y la primera columna) con un grosor de 1.25 y un color negro.
('VALIGN',(0,0),(-1,-1), 'TOP'), # Alinea verticalmente el texto de todas las celdas de la tabla al centro.
('ALIGN', (0, 0), (-1, -1), 'CENTER') # Alinea horizontalmente el texto de todas las celdas de la tabla al centro.
]

# TAMAÑO TABLA
tabla = Table(data=tabla_data, colWidths=[40, 180, 60, 60, 80, 80])
tabla.setStyle(estilo)

# POSICION TABLA EN LIENZO
tabla.wrapOn(c, 0, 0)
tabla.drawOn(c, 50, 500)

# TABLA 2
tabla_data2=[['Método de pago:']]

estilo2 = [('FONTSIZE',(0,0),(-1,-1),8),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('ALIGN',(0,0),(-1,-1),'LEFT'),
    ('VALIGN',(0,0),(-1,-1),'TOP')]

# TAMAÑO TABLA 2
tabla2 = Table(data=tabla_data2, colWidths=[250], rowHeights=[100])
tabla2.setStyle(estilo2)

# POSICION TABLA 2 EN LIENZO
tabla2.wrapOn(c, 0, 0)
tabla2.drawOn(c, 50, 300)


# TABLA 3
tabla_data3 = [['Importe neto',''],
               ['+ IVA de ___%',''],
               ['- IRPF de __ %',''],
               ['IMPORTE BRUTO','']
               ]

estilo3 = [('FONTSIZE',(0,0),(-1,-1),8),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('BACKGROUND',(-2,-1),(-1,-1), colors.lightgrey), # Establece el color de fondo de la última fila de la tabla.
           ]

# TAMAÑO TABLA 3
tabla3 = Table(data=tabla_data3, colWidths=[100,70])
tabla3.setStyle(estilo3)

# POSICION TABLA 3 EN LIENZO
tabla3.wrapOn(c, 0, 0)
tabla3.drawOn(c, 400, 300)


c.showPage()# Esto es para que se cree una nueva pagina pdf
c.save()# Esto es para que se guarde el documento

