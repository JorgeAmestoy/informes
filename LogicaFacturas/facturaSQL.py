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
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sqlite3
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLineEdit, QLabel, QMessageBox, QComboBox
from PyQt6.uic.properties import QtGui



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Facturas SQL")

        cajav = QVBoxLayout()
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

        # ComboBox
        self.combo = QComboBox()
        self.combo.addItems(("Enero","Febrero","Marzo"))
        cajav.addWidget(self.combo)


        # BASE DE DATOS
        self.baseDatos = QSqlDatabase("QSQLITE")# Crear una instancia de la base de datos SQLite en PyQt
        self.baseDatos.setDatabaseName("baseDatosCasa.dat")  # Establecer el nombre de la base de datos a la que se va a conectar
        self.baseDatos.open()# Abrir la conexión con la base de datos
        self.bbdd = sqlite3.connect("baseDatosCasa.dat")  # Establecer una conexión directa con la base de datos utilizando sqlite3 (sin usar PyQt)
        self.c = self.bbdd.cursor()# Crear un cursor para ejecutar consultas en la base de datos

        # QTABLE VIEW
        self.tabla = QTableView()  # Creo objeto QTableView para visualizar los datos de la base de datos en una tabla
        cajav.addWidget(self.tabla)  # Lo añado al layout vertical
        self.modelo = QSqlTableModel(db=self.baseDatos)  # Creo el modelo que va a usar el objeto TableView. En este caso, el modelo a usar es QSqlTableModel, que sirve para trabajar con bases de datos.
        self.tabla.setModel(self.modelo)  # Añado el modelo al objeto QTableView (tabla)
        self.modelo.setTable("listaPersonas")  # Añado al modelo la tabla listaPersonas creada en la base de datos
        self.modelo.select()  # Para amosar los datos de dicha tabla. Sin esto no se ve ná.
        #self.tabla.clicked.connect(self.on_tabla_clicked)  # EVENTO TABLA AL HACER CLICK SOBRE ELLA
        self.tabla.setSelectionMode(QTableView.SelectionMode.NoSelection)


        # BOTÓN GENERAR FACTURA
        self.botonCargarDatos = QPushButton("Generar Factura")
        self.botonCargarDatos.clicked.connect(self.on_botonGenerarFactura_clicked)
        cajav.addWidget(self.botonCargarDatos)

        container = QWidget()
        container.setLayout(cajav)  # Añadir layout principal
        self.setCentralWidget(container)
        self.setFixedSize(500,700)
        self.show()



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
            mes = self.combo.currentText()#currentIndex() para obtener el índice seleccionado

            # Crear el archivo PDF
            c = canvas.Canvas("PDFfacturaSQL.pdf", pagesize=A4)
            c.setFont("Helvetica", 20)
            c.drawString(340, 750, "FACTURA SIMPLIFICADA")

            c.setFont("Helvetica", 20)
            c.drawString(100, 700, "Nombre de tu Empresa")

            c.drawImage("check.png", 500, 700, 40, 40)

            # LADO IZQUIERDO
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

            # LADO DERECHO
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

            c.setFont("Helvetica", 14)
            c.drawRightString(500, 610, "Mes: ")
            numeroFactura_texto = c.beginText(500, 610)
            numeroFactura_texto.textLine(numeroFactura)
            c.drawText(numeroFactura_texto)

            # Obtener los datos de la tabla de la interfaz de usuario
            datos_tabla = []  # Lista que almacenará los datos de la tabla para la factura
            for fila in range(self.modelo.rowCount()):  # Iterar a través de las filas del modelo de la tabla. Con el range consigo el indice de cada fila que itera
                datos_fila = []  # Lista que almacenará los datos de una fila específica
                for columna in range(self.modelo.columnCount()):  # Iterar a través de las columnas del modelo de la tabla. Con el range consigo el indice de cada columna que itera
                    indice = self.modelo.index(fila,columna)  # Obtener el índice del elemento en la posición (fila, columna)
                    valor = self.modelo.data(indice)  # Obtener el valor en la posición especificada por el índice
                    datos_fila.append(valor)  # Agregar el valor a la lista de datos de la fila actual
                datos_tabla.append(datos_fila)  # Agregar los datos de la fila actual a la lista de datos de la tabla

            encabezadoTabla = ['DNI', 'Nombre', 'Género', 'Edad', 'Fallecido']
            datos_tabla.insert(0, encabezadoTabla)  # Insertar el encabezado al principio, en la fila cero.



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
            tabla = Table(datos_tabla)
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