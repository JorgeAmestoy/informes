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
import sys
import typing

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                             QWidget, QListView, QHBoxLayout, QLineEdit)
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage

tickImage = QImage('check.png')

from PyQt6.QtCore import QAbstractListModel, Qt

from PyQt6.QtCore import QAbstractListModel, Qt

from conexionBD import ConexionBD


class TareasModelo(QAbstractListModel):  # Define una clase llamada TareasModelo que hereda de QAbstractListModel

    def __init__(self, tareas=None):
        super().__init__()  # Llama al inicializador de la clase base (QAbstractListModel).
        self.tareas = tareas or []  # Inicializa el atributo 'tareas' con el valor del argumento tareas, si se proporciona. Si no se proporciona ningún valor para tareas, se asigna una lista vacía [].

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:  # Verifica si el rol es para mostrar datos.
            tarea = self.tareas[indice.row()]  # Obtiene la tarea en el índice dado.
            return ", ".join(map(str,
                                 tarea))  # Concatena todos los elementos de la tupla en una cadena separada por comas y la devuelve como representación de la tarea.

        if rol == Qt.ItemDataRole.DecorationRole:  # Verifica si el rol es para mostrar la decoración de la tarea.
            return None  # Devuelve None para indicar que no hay decoración asociada.

    def setData(self, indice, valor, rol=Qt.ItemDataRole.EditRole):
        if rol == Qt.ItemDataRole.EditRole:  # Verifica si el rol es para editar datos.
            # Actualiza la tupla de la tarea en el índice dado dividiendo el valor en una lista y convirtiéndola en una tupla.
            self.tareas[indice.row()] = tuple(valor.split(", "))

            # Notifica a las vistas que los datos han cambiado.
            self.dataChanged.emit(indice, indice)
            return True  # Devuelve True para indicar que la operación fue exitosa.

        return False  # Devuelve False si el rol no es para editar datos.

    def rowCount(self, indice):
        return len(self.tareas)  # Devuelve el número de tareas en la lista.


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Facturas List Model")

        # BASE DE DATOS
        ruta_bd = "modelosClasicos.dat"
        self.conexion_bd = ConexionBD(ruta_bd)
        self.conexion_bd.conectaBD()
        self.conexion_bd.creaCursor()

        self.lista_data = []  # Creo lista vacía

        self.modelo = TareasModelo(self.lista_data)  # Creación del modelo de datos personalizado para las tareas
        cajav = QVBoxLayout()  # Creación de un layout vertical para organizar los widgets verticalmente
        self.lstTareas = QListView()  # Creación de un QListView para mostrar la lista de tareas
        self.lstTareas.setModel(self.modelo)  # Establecimiento del modelo de datos para el QListView
        self.lstTareas.setSelectionMode(
            QListView.SelectionMode.MultiSelection)  # Configuración del QListView para permitir la selección múltiple de tareas
        cajav.addWidget(self.lstTareas)  # Agregado del QListView al layout vertical

        # BOTONES Y TXT
        direccion = QLabel("Direccion")
        cajav.addWidget(direccion)
        self.txtdireccion = QLineEdit()
        cajav.addWidget(self.txtdireccion)
        ciudad = QLabel("Ciudad")
        cajav.addWidget(ciudad)
        self.txtciudad = QLineEdit()
        cajav.addWidget(self.txtciudad)
        cif_nif = QLabel("CIF/NIF")
        cajav.addWidget(cif_nif)
        self.txtnif = QLineEdit()
        cajav.addWidget(self.txtnif)
        telefono = QLabel("Teléfono")
        cajav.addWidget(telefono)
        self.txttelefono = QLineEdit()
        cajav.addWidget(self.txttelefono)
        mail = QLabel("Mail")
        cajav.addWidget(mail)
        self.textemail = QLineEdit()
        cajav.addWidget(self.textemail)
        fecha_emision = QLabel("Fecha de Emisión")
        cajav.addWidget(fecha_emision)
        self.txtfecha = QLineEdit()
        cajav.addWidget(self.txtfecha)
        num_factura = QLabel("Número de Factura")
        cajav.addWidget(num_factura)
        self.txtnumfactura = QLineEdit()
        cajav.addWidget(self.txtnumfactura)

        # BOTÓN GENERAR FACTURA
        self.botonGenerarFactura = QPushButton("Generar Factura")
        self.botonGenerarFactura.clicked.connect(self.on_botonGenerarFactura_clicked)
        cajav.addWidget(self.botonGenerarFactura)

        container = QWidget()
        container.setLayout(cajav)  # Añadir layout principal
        self.setCentralWidget(container)
        self.setFixedSize(500, 700)
        self.show()

        self.on_cargarDatos()

    def on_cargarDatos(self):
        # Ejecuta una consulta SQL para obtener los datos de la base de datos
        consulta = "SELECT * FROM ventas"
        datos_bd = self.conexion_bd.consultaSenParametros(consulta)

        self.lista_data = datos_bd
        self.modelo = TareasModelo(self.lista_data)
        self.lstTareas.setModel(self.modelo)
        self.lstTareas.show()

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
            c = canvas.Canvas("PDFfacturaListSql.pdf", pagesize=A4)
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

            # Crear la lista de datos de la factura
            datos_factura = [["ID", "Fecha1", "Fecha2", "Número"]]  # inicializa una lista con la primera fila con esos datos. Se utilizará para almacenar los datos de la factura en un formato que sea fácil de usar al generar el PDF.
            for tarea in self.modelo.tareas:  # Esto comienza un bucle for que recorre cada tarea en la lista de tareas del modelo. Con la variable modelo, que contiene el QAbstractListModel, accedo a dicha clase y cojo "tareas". En la variable modelo está también la lista/tupla con los datos de la lista.
                id,fecha1,fecha2,numero = tarea  # Aquí, descripcion, importe, cantidad y total son variables que se desempaquetan de cada tupla tarea en la lista de tareas. Por ejemplo, para la primera tarea ('Producto 1', '3,2', '5', '16,00'), descripcion sería 'Producto 1', importe sería '3,2', cantidad sería '5' y total sería '16,00'.
                datos_factura.append([id,fecha1,fecha2,numero])  # Luego, se agrega una lista que contiene estos datos (descripcion, importe, cantidad y total) a la lista datos_factura.

            # Configurar el estilo de la tabla
            estilo = TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.darkgreen),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 7),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTSIZE', (0, 0), (-1, -1), 15),
                ('LEADING', (0, 0), (-1, -1), 20),
                ('GRID', (0, 0), (-1, -1), 1, colors.white),
            ])

            # Crear y dibujar la tabla en el lienzo
            tabla = Table(data=datos_factura, colWidths=[100, 100, 100, 100])
            tabla.setStyle(estilo)
            tabla.wrapOn(c, 0, 0)
            tabla.drawOn(c, 100, 300)

            # Línea divisoria
            c.line(100, 200, 575, 200)

            # Mensaje de agradecimiento
            c.setFont("Helvetica-Bold", 16)
            c.drawRightString(450, 150, "GRACIAS POR SU CONFIANZA")

            # Guardar y cerrar el archivo PDF
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