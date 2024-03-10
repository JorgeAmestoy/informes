import sys
from decimal import Decimal
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLabel, QLineEdit, \
    QInputDialog
from PyQt6.QtCore import Qt, QAbstractTableModel
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class InvoiceModel(QAbstractTableModel):  # Define una clase llamada InvoiceModel que hereda de QAbstractTableModel.

    def __init__(self, data):
        super().__init__()  # Llama al inicializador de la clase base (QAbstractTableModel).
        self._data = data  # Inicializa el atributo '_data' con los datos proporcionados.

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:  # Verifica si el rol es para mostrar datos.
            return self._data[index.row()][index.column()]  # Devuelve el dato en la posición del índice.

    def rowCount(self, parent):
        return len(self._data)  # Devuelve el número de filas en los datos.

    def columnCount(self, parent):
        return len(self._data[0])  # Devuelve el número de columnas en los datos, asumiendo que todas las filas tienen la misma longitud.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Facturas")



        self.tabla_data = [
            ['Producto 1', '3,2', '5', '16,00'],
            ['Producto 2', '2,1', '3', '6,30'],
            ['Producto 3', '2,9', '76', '220,40'],
            ['Producto 4', '5', '23', '115,00'],
            ['Producto 5', '4,95', '3', '14,85'],
            ['Producto 6', '6', '2', '12,00']
        ]

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Campos de texto
        self.text_fields = [QLineEdit() for _ in range(7)]

        # Diseño de etiquetas y campos de texto
        label_layout = QVBoxLayout()
        labels = ["Dirección", "Ciudad", "CIF/NIF", "Teléfono", "Mail", "Fecha de Emisión", "Número de Factura"]

        for label, field in zip(labels, self.text_fields):
            label_layout.addWidget(QLabel(label))
            label_layout.addWidget(field)

        # Agregar el diseño de etiquetas y campos de texto al diseño general
        layout.addLayout(label_layout)

        # Agregar la tabla al diseño general
        self.table_view = QTableView()
        self.table_view.setModel(InvoiceModel(self.tabla_data))
        layout.addWidget(self.table_view)

        # Botón para agregar un nuevo producto
        self.add_product_button = QPushButton("Agregar Producto")
        self.add_product_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_product_button)

        # Botón de generación de factura
        self.generate_button = QPushButton("Generar Factura")
        self.generate_button.clicked.connect(self.generarFactura)
        layout.addWidget(self.generate_button)

    def add_product(self):
        # Método para agregar un nuevo producto a la tabla
        nombreProducto, ok_name = QInputDialog.getText(self, "Agregar Producto", "Nombre del Producto:")
        precioProducto, ok_price = QInputDialog.getDouble(self, "Agregar Producto", "Precio del Producto:")
        cantidadProducto, ok_quantity = QInputDialog.getInt(self, "Agregar Producto", "Cantidad del Producto:")

        if ok_name and ok_price and ok_quantity:
            # Calcular el total
            product_total = precioProducto * cantidadProducto

            # Agregar el producto a la lista de datos de la tabla
            self.tabla_data.append(
                [nombreProducto, f'{precioProducto:.2f}', str(cantidadProducto), f'{product_total:.2f}'])

            # Actualizar el modelo de la tabla
            self.table_view.model().layoutChanged.emit()

    def update_table_data(self, product_data):
        # Método para actualizar los datos de la tabla de productos
        # product_data debe ser una lista con la información del producto
        self.tabla_data.append(product_data)
        self.table_view.model().layoutChanged.emit()

    def generarFactura(self):
        try:
            # Aquí iría la lógica para generar la factura en PDF usando ReportLab
            print("Generando factura...")
            # Recoger los datos de los campos de texto
            direccion = self.text_fields[0].text()
            ciudad = self.text_fields[1].text()
            nif = self.text_fields[2].text()
            telefono = self.text_fields[3].text()
            email = self.text_fields[4].text()
            fecha = self.text_fields[5].text()
            numeroFactura = self.text_fields[6].text()

            # Crear el archivo PDF
            c = canvas.Canvas("PDFfacturaAngi.pdf", pagesize=A4)
            c.setFont("Helvetica", 20)
            c.drawString(340, 750, "FACTURA SIMPLIFICADA")

            c.setFont("Helvetica", 20)
            c.drawString(100, 700, "Nombre de tu Empresa")

            c.drawImage("check.png", 500, 700, 40, 40)

            c.setFont("Helvetica", 14)
            c.drawString(100, 680, "Dirección: ")
            direccion_texto = c.beginText(200, 680)
            direccion_texto.textLine(direccion)
            c.drawText(direccion_texto)

            c.setFont("Helvetica", 14)
            c.drawString(100, 660, "Ciudad y País: ")
            ciudadPais = c.beginText(200, 660)
            ciudadPais.textLine(ciudad)
            c.drawText(ciudadPais)

            c.setFont("Helvetica", 14)
            c.drawString(100, 640, "CIF/NIF: ")
            cifNif = c.beginText(200, 640)
            cifNif.textLine(nif)
            c.drawText(cifNif)

            c.setFont("Helvetica", 14)
            c.drawString(100, 620, "Teléfono: ")
            telefono_texto = c.beginText(200, 620)
            telefono_texto.textLine(telefono)
            c.drawText(telefono_texto)

            c.setFont("Helvetica", 14)
            c.drawString(100, 600, "Mail: ")
            mail = c.beginText(200, 600)
            mail.textLine(email)
            c.drawText(mail)

            c.setFont("Helvetica", 14)
            c.drawRightString(500, 650, "Fecha Emisión: ")
            fechaEmision = c.beginText(500, 650)
            fechaEmision.textLine(fecha)
            c.drawText(fechaEmision)

            c.setFont("Helvetica", 14)
            c.drawRightString(500, 630, "Número de Factura: ")
            numeroFactura_texto = c.beginText(500, 630)
            numeroFactura_texto.textLine(numeroFactura)
            c.drawText(numeroFactura_texto)

            # Crear datos para la tabla
            table_header = ['Descripción', 'Importe', 'Cantidad', 'Total']
            table_data = self.tabla_data

            # Calcular el total
            total = sum(Decimal(row[3].replace(',', '.')) for row in self.tabla_data)
            total_row = ['', '', 'TOTAL', f'{total:.2f} €']

            # Agregar el total a la tabla
            table_data.append(total_row)

            # Configurar el estilo de la tabla
            estilo = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen), # Establece un fondo verde oscuro para la primera fila de la tabla (fila 0). Esto proporciona un fondo distintivo para el encabezado de la tabla.
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), # Establece el color del texto en blanco para la primera fila de la tabla. Esto asegura que el texto en el encabezado sea visible sobre el fondo verde oscuro.
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la primera fila de la tabla. Esto hace que el texto en el encabezado sea más grueso y destacado.
                ('BOTTOMPADDING', (0, 0), (-1, 0), 7), # Agrega un espacio adicional en la parte inferior de la primera fila. Esto proporciona un espacio visualmente agradable entre el encabezado y el resto de la tabla.
                ('BACKGROUND', (0, 1), (-1, -2), colors.lightgreen),# Establece un fondo verde claro para las filas de datos (a partir de la segunda fila hasta la penúltima fila, ya que empieza desde la fila 1). Esto ayuda a diferenciar visualmente las filas de datos del encabezado.
                ('BACKGROUND', (0, -1), (-1, -1), colors.darkgreen), # Establece un fondo verde oscuro para la última fila
                ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),# Establece el color del texto en blanco para la última fila
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la última fila
                ('BACKGROUND', (0, -1), (1, -1), colors.white),# Establece un fondo blanco para la última fila que no tiene datos
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # Alinea el contenido de la tabla al centro. Especifica que tanto el texto como los números en la tabla se alineen al centro.
                ('FONTSIZE', (0, 0), (-1, -1), 15),  # Ajusta el tamaño de la fuente
                ('LEADING', (0, 0), (-1, -1), 20),  # Ajusta el espaciado entre las líneas
                ('GRID', (0, 0), (-1, -1), 1, colors.white), # Agrega bordes a todas las celdas
            ])

            # TAMAÑO TABLA
            tabla = Table(data=[table_header] + table_data, colWidths=[200, 70, 70, 70])
            tabla.setStyle(estilo)

            # POSICION TABLA EN LIENZO
            tabla.wrapOn(c, 0, 0)
            tabla.drawOn(c, 100, 300)  # Ajusta las coordenadas

            c.line(100, 200, 575, 200)

            c.setFont("Helvetica-Bold", 16)
            c.drawRightString(450, 150, "GRACIAS POR SU CONFIANZA")

            # TABLA 2
            tabla_data2 = [['']]
            estilo2 = [('BACKGROUND', (0, 0), (-1, -1), colors.lightgreen)]

            # TAMAÑO TABLA 4
            tabla2 = Table(data=tabla_data2, colWidths=[20], rowHeights=[140])
            tabla2.setStyle(estilo2)

            # POSICION TABLA EN LIENZO
            tabla2.wrapOn(c, 0, 0)
            tabla2.drawOn(c, 5, 5)

            c.showPage()
            c.save()

            print("Factura generada.")
        except Exception as e:
            print(f"Error al generar la factura: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
