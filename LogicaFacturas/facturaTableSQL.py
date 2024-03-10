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
from conexionBD import ConexionBD



class ModeloTaboa(QAbstractTableModel):  # Define una clase llamada ModeloTaboa que hereda de QAbstractTableModel.

    def __init__(self, datos):
        super().__init__()  # Llama al inicializador de la clase base (QAbstractTableModel).
        self.datos = datos  # Inicializa el atributo 'datos' con los datos proporcionados.

    def rowCount(self, index):
        return len(self.datos)  # Devuelve el número de filas en los datos.

    def columnCount(self, index):
        if self.datos:
            # Devuelve el número de columnas basado en la longitud de la primera fila de datos.
            return len(self.datos[0])
        return 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():  # Verifica si el índice es válido.
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                # Obtiene el valor de los datos en la posición del índice y lo devuelve como una cadena.
                value = self.datos[index.row()][index.column()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:  # Verifica si el rol es para editar datos.
            # Actualiza el valor de los datos en la posición del índice con el nuevo valor proporcionado.
            self.datos[index.row()][index.column()] = value
            return True  # Devuelve True para indicar que la operación fue exitosa.
        return False  # Devuelve False si el rol no es para editar datos.

    def flags(self, index):
        # Devuelve las banderas que especifican cómo se comportan los elementos en la vista, como si son editables, seleccionables, etc.
        return Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Facturas Abstract SQL")

        cajav = QVBoxLayout()

        # BASE DE DATOS
        ruta_bd = "modelosClasicos.dat"
        self.conexion_bd = ConexionBD(ruta_bd)
        self.conexion_bd.conectaBD()
        self.conexion_bd.creaCursor()

        self.tabla_data = []  # Creo lista vacía

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
        self.tabla = QTableView()
        cajav.addWidget(self.tabla)
        self.modelo = ModeloTaboa(self.tabla_data)
        self.tabla.setModel(self.modelo)

        # TRIGGERS
        self.tabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.tabla.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.tabla.setEditTriggers(QTableView.EditTrigger.AllEditTriggers)

        # BOTÓN GENERAR FACTURA
        self.botonCargarDatos = QPushButton("Generar Factura")
        self.botonCargarDatos.clicked.connect(self.on_botonGenerarFactura_clicked)
        cajav.addWidget(self.botonCargarDatos)

        container = QWidget()
        container.setLayout(cajav)  # Añadir layout principal
        self.setCentralWidget(container)
        self.setFixedSize(500,700)
        self.show()

        self.on_cargarTabla()

    def on_cargarTabla(self):
        # Consulta SQL para obtener los datos de ventas
        consulta_sql = "SELECT * FROM ventas"

        # Guardar en variables los datos de la consulta
        datosBD = self.conexion_bd.consultaSenParametros(consulta_sql)

        self.tabla_data = datosBD
        self.modelo = ModeloTaboa(self.tabla_data)
        self.tabla.setModel(self.modelo)
        self.tabla.show()

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
            c = canvas.Canvas("PDFfacturaTableSQL.pdf", pagesize=A4)
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
            encabezadoTabla = ['ID', 'Fecha1', 'Fecha2', 'Numero']
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
            tabla = Table(data=[encabezadoTabla] + infoTabla, colWidths=[200, 100, 100, 100])
            tabla.setStyle(estilo)

            # POSICION TABLA EN LIENZO
            tabla.wrapOn(c, 0, 0)
            tabla.drawOn(c, 80, 400)  # Ajusta las coordenadas

            c.line(100, 250, 575, 250)

            c.setFont("Helvetica-Bold", 16)
            c.drawRightString(450, 200, "GRACIAS POR SU CONFIANZA")

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