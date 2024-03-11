from PyQt6.QtCore import QAbstractTableModel, Qt
import sys
from decimal import Decimal
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLabel, QLineEdit, \
    QInputDialog
from PyQt6.QtCore import Qt, QAbstractTableModel
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class ModeloTaboa(QAbstractTableModel):
    def __init__(self, datos):
        """
        Inicializa el modelo con los datos proporcionados.

        :param datos: Los datos para inicializar el modelo.
        :type datos: list
        """
        super().__init__()  # Llama al inicializador de la clase base (QAbstractTableModel).
        self.datos = datos  # Inicializa el atributo 'datos' con los datos proporcionados.

    def rowCount(self, index):
        """
        Devuelve el número de filas en los datos.

        :param index: El índice.
        :type index: QModelIndex
        :return: El número de filas en los datos.
        :rtype: int
        """
        return len(self.datos)

    def columnCount(self, index):
        """
        Devuelve el número de columnas en los datos.

        Se asume que todas las filas tienen la misma cantidad de columnas.

        :param index: El índice.
        :type index: QModelIndex
        :return: El número de columnas en los datos.
        :rtype: int
        """
        return len(self.datos[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """
        Devuelve los datos en el índice dado con el rol especificado.

        :param index: El índice.
        :type index: QModelIndex
        :param role: El rol de los datos.
        :type role: Qt.ItemDataRole
        :return: Los datos en el índice dado.
        :rtype: str
        """
        if index.isValid():  # Verifica si el índice es válido.
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:  # Verifica si el rol es para mostrar o editar datos.
                value = self.datos[index.row()][index.column()]  # Obtiene el valor en la posición del índice.
                return str(value)  # Devuelve el valor convertido a cadena.

    def setData(self, index, value, role):
        """
        Establece los datos en el índice dado con el valor especificado.

        :param index: El índice.
        :type index: QModelIndex
        :param value: El valor a establecer.
        :type value: str
        :param role: El rol de los datos.
        :type role: Qt.ItemDataRole
        :return: True si la operación fue exitosa, False de lo contrario.
        :rtype: bool
        """
        if role == Qt.ItemDataRole.EditRole:  # Verifica si el rol es para editar datos.
            self.datos[index.row()][index.column()] = value  # Actualiza el valor en la posición del índice con el nuevo valor.
            return True  # Devuelve True para indicar que la operación fue exitosa.
        return False  # Devuelve False si el rol no es para editar datos.

    def flags(self, index):
        """
        Devuelve las banderas para el índice dado.

        Esto permite que los datos sean editables, seleccionables y habilitados.

        :param index: El índice.
        :type index: QModelIndex
        :return: Las banderas para el índice dado.
        :rtype: Qt.ItemFlag
        """
        return Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Facturas")

        cajav = QVBoxLayout()

        # LISTA CON CONTENIDO DE TABLA
        self.tabla_data = [
            ['Producto 1', '3,2', '5', '16,00'],
            ['Producto 2', '2,1', '3', '6,30'],
            ['Producto 3', '2,9', '76', '220,40'],
            ['Producto 4', '5', '23', '115,00'],
            ['Producto 5', '4,95', '3', '14,85'],
            ['Producto 6', '6', '2', '12,00']
        ]

        # BOTONES Y TXT
        direccion = QLabel("Direccion")
        cajav.addWidget(direccion)
        self.txtdireccion = QLineEdit()  # Agregar self
        cajav.addWidget(self.txtdireccion)
        ciudad = QLabel("Ciudad")
        cajav.addWidget(ciudad)
        self.txtciudad = QLineEdit()  # Agregar self
        cajav.addWidget(self.txtciudad)
        cif_nif = QLabel("CIF/NIF")
        cajav.addWidget(cif_nif)
        self.txtnif = QLineEdit()  # Agregar self
        cajav.addWidget(self.txtnif)
        telefono = QLabel("Teléfono")
        cajav.addWidget(telefono)
        self.txttelefono = QLineEdit()  # Agregar self
        cajav.addWidget(self.txttelefono)
        mail = QLabel("Mail")
        cajav.addWidget(mail)
        self.textemail = QLineEdit()  # Agregar self
        cajav.addWidget(self.textemail)
        fecha_emision = QLabel("Fecha de Emisión")
        cajav.addWidget(fecha_emision)
        self.txtfecha = QLineEdit()  # Agregar self
        cajav.addWidget(self.txtfecha)
        num_factura = QLabel("Número de Factura")
        cajav.addWidget(num_factura)
        self.txtnumfactura = QLineEdit()  # Agregar self
        cajav.addWidget(self.txtnumfactura)


        # TABLA
        self.table_view = QTableView()
        self.table_view.setModel(ModeloTaboa(self.tabla_data))
        self.table_view.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.table_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.table_view.setEditTriggers(QTableView.EditTrigger.AllEditTriggers)
        cajav.addWidget(self.table_view)


        # BOTÓN AGREGAR PRODUCTO
        self.botonAnhadir = QPushButton("Agregar Producto")
        self.botonAnhadir.clicked.connect(self.on_botonAnhadir_clicked)
        cajav.addWidget(self.botonAnhadir)

        # BOTÓN GENERAR FACTURA
        self.botonGenerarFactura = QPushButton("Generar Factura")
        self.botonGenerarFactura.clicked.connect(self.on_botonGenerarFactura_clicked)
        cajav.addWidget(self.botonGenerarFactura)

        container = QWidget()
        container.setLayout(cajav)  # Añadir layout principal
        self.setCentralWidget(container)
        self.setFixedSize(500,700)
        self.show()

    def on_botonAnhadir_clicked(self):
        # Método para agregar un nuevo producto a la tabla
        nombreProducto, ok_name = QInputDialog.getText(self, "Agregar Producto", "Nombre del Producto:")
        precioProducto, ok_price = QInputDialog.getDouble(self, "Agregar Producto", "Precio del Producto:")
        cantidadProducto, ok_quantity = QInputDialog.getInt(self, "Agregar Producto", "Cantidad del Producto:")
        total, ok_total = QInputDialog.getDouble(self, "Total Producto", "Total del producto:")

        # Agregar los datos a la lista de datos
        nuevaFila = [nombreProducto, precioProducto, cantidadProducto, total]
        self.tabla_data.append(nuevaFila)

        # Actualizar la vista de la tabla
        self.table_view.model().layoutChanged.emit()


    def on_botonGenerarFactura_clicked(self):
        try:
            print("Generando factura...")
            # Recoger los datos de los campos de texto
            direccion = self.txtdireccion.text()
            ciudad = self.txtciudad.text()
            nif = self.txtnif.text()
            telefono = self.txttelefono.text()
            email = self.textemail.text()
            fecha = self.txtfecha.text()
            numeroFactura = self.txtnumfactura.text()

            # Crear el archivo PDF
            c = canvas.Canvas("PDFfacturaTable.pdf", pagesize=A4)
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
            encabezadoTabla = ['Descripción', 'Importe', 'Cantidad', 'Total']
            infoTabla = self.tabla_data

            # Configurar el estilo de la tabla
            estilo = TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.darkgreen), # Establece un fondo verde oscuro para la primera fila de la tabla (fila 0). Esto proporciona un fondo distintivo para el encabezado de la tabla.
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), # Establece el color del texto en blanco para la primera fila de la tabla. Esto asegura que el texto en el encabezado sea visible sobre el fondo verde oscuro.
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la primera fila de la tabla. Esto hace que el texto en el encabezado sea más grueso y destacado.
                ('BOTTOMPADDING', (0, 0), (-1, 0), 7), # Agrega un espacio adicional en la parte inferior de la primera fila. Esto proporciona un espacio visualmente agradable entre el encabezado y el resto de la tabla.
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),# Establece un fondo verde claro para las filas de datos (a partir de la segunda fila hasta la penúltima fila, ya que empieza desde la fila 1). Esto ayuda a diferenciar visualmente las filas de datos del encabezado.
                #('BACKGROUND', (0, -1), (-1, -1), colors.darkgreen), # Establece un fondo verde oscuro para la última fila
                #('TEXTCOLOR', (0, -1), (-1, -1), colors.white),# Establece el color del texto en blanco para la última fila
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la última fila
                #('BACKGROUND', (0, -1), (1, -1), colors.white),# Establece un fondo blanco para la última fila que no tiene datos
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # Alinea el contenido de la tabla al centro. Especifica que tanto el texto como los números en la tabla se alineen al centro.
                ('FONTSIZE', (0, 0), (-1, -1), 15),  # Ajusta el tamaño de la fuente
                ('LEADING', (0, 0), (-1, -1), 20),  # Ajusta el espaciado entre las líneas
                ('GRID', (0, 0), (-1, -1), 1, colors.white), # Agrega bordes a todas las celdas
            ])

            # TAMAÑO TABLA
            tabla = Table(data=[encabezadoTabla] + infoTabla, colWidths=[200, 70, 70, 70])
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

            # TAMAÑO TABLA 2
            tabla2 = Table(data=tabla_data2, colWidths=[20], rowHeights=[600])
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
