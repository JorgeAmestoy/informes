from PyQt6.QtCore import QAbstractTableModel, Qt

from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QTableView, QVBoxLayout, QHBoxLayout, QWidget,
                             QComboBox, QGroupBox, QGridLayout, QLabel, QPushButton, QMessageBox)

from conexionBD import ConexionBD

import sys
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

class ModeloTaboa(QAbstractTableModel):
    def __init__(self, datos):
        super().__init__()
        self.datos = datos

    def rowCount(self, index):
        return len(self.datos)

    def columnCount(self, index):
        if self.datos:
            # Devuelve el número de columnas basado en la longitud de la primera fila de datos
            return len(self.datos[0])
        return 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                value = self.datos[index.row()][index.column()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            self.datos[index.row()][index.column()] = value
            return True
        return False


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 20-02-2024")

        # BASE DE DATOS
        ruta_bd = "modelosClasicos.dat"
        self.conexion_bd = ConexionBD(ruta_bd)
        self.conexion_bd.conectaBD()
        self.conexion_bd.creaCursor()

        self.tabla_data = []# Creo lista vacía

        # LAYOUT y WIDGETS
        cajav = QVBoxLayout()
        groupBox = QGroupBox("Albarán")
        cajav.addWidget(groupBox)
        grid = QGridLayout()
        groupBox.setLayout(grid)
        lblNumeroAlbaran = QLabel("Número Albarán")
        grid.addWidget(lblNumeroAlbaran, 0, 0)
        self.cmbNumeroAlbaran = QComboBox()
        #self.cmbNumeroAlbaran.addItems(("1","2","3","4","5"))

        grid.addWidget(self.cmbNumeroAlbaran, 0, 1, 1, 1)
        lblDataAlbaran = QLabel("Data")
        grid.addWidget(lblDataAlbaran, 0, 2, 1, 1)
        self.txtDataAlbaran = QLineEdit()
        grid.addWidget(self.txtDataAlbaran, 0, 3, 1, 1)
        lblDataEntrega = QLabel("Data entrega")
        grid.addWidget(lblDataEntrega, 1, 0)
        self.txtDataEntrega = QLineEdit()
        grid.addWidget(self.txtDataEntrega, 1, 1, 1, 3)
        lblNumeroCliente = QLabel("Número cliente")
        grid.addWidget(lblNumeroCliente, 2, 0)
        self.txtNumeroCliente = QLineEdit()
        grid.addWidget(self.txtNumeroCliente, 2, 1, 1, 3)
        cajah = QHBoxLayout()
        cajav.addLayout(cajah)



        # QTABLE VIEW
        self.tabla = QTableView()
        cajah.addWidget(self.tabla)
        self.modelo = ModeloTaboa(self.tabla_data)
        self.tabla.setModel(self.modelo)


        # CAJA VERTICAL DERECHA QTABLE
        cajahder = QHBoxLayout()
        cajah.addLayout(cajahder)
        cajahder.setAlignment(Qt.AlignmentFlag.AlignTop)
        botonengadir = QPushButton("Engadir")
        cajahder.addWidget(botonengadir)
        botoneditar = QPushButton("Editar")
        cajahder.addWidget(botoneditar)
        botonborrar = QPushButton("Borrar")
        #botonborrar.clicked.connect(self.on_botonborrar_clicked)
        cajahder.addWidget(botonborrar)
        self.labelExito = QLabel()
        cajav.addWidget(self.labelExito)


        # CAJA HORIZONTAL FINAL
        cajah2 = QHBoxLayout()
        cajah2.addStretch()
        cajah2.setContentsMargins(100, 0, 0, 0)
        cajav.addLayout(cajah2)
        botoncancelar = QPushButton("Cancelar")
        cajah2.addWidget(botoncancelar)
        botonaceptar = QPushButton("Aceptar")
        #botonaceptar.clicked.connect(self.on_botonaceptar_clicked)
        cajah2.addWidget(botonaceptar)

        # BOTÓN GENERAR FACTURA
        self.botonCargarDatos = QPushButton("Generar Factura")
        self.botonCargarDatos.clicked.connect(self.on_botonGenerarFactura_clicked)
        cajav.addWidget(self.botonCargarDatos)

        # Llenar el ComboBox con los datos de la base de datos
        self.cargar_combobox()
        # Conectar la señal de cambio de texto del ComboBox a la función cargar_datos
        self.cmbNumeroAlbaran.currentTextChanged.connect(self.cargar_datos)



        container = QWidget()
        container.setLayout(cajav)  # Añadir layout principal
        self.setCentralWidget(container)
        #self.setFixedSize(400,400)
        #self.show()

    def cargar_combobox(self):
        """Carga los números de albarán disponibles en el QComboBox.

        Realiza una consulta a la base de datos para obtener los números de albarán únicos y los agrega al QComboBox.

        """
        # Consulta SQL para obtener los números de albarán disponibles
        consulta_sql = "SELECT DISTINCT numeroAlbaran FROM ventas"
        datos_albaran = self.conexion_bd.consultaSenParametros(consulta_sql)

        # Verificar si se obtuvieron datos de la consulta
        if datos_albaran:
            # Limpiar los elementos actuales del QComboBox
            self.cmbNumeroAlbaran.clear()

            # Itera sobre cada dato obtenido de la consulta
            for dato in datos_albaran:
                # Agrega el primer elemento de cada dato al QComboBox
                # El primer elemento generalmente corresponde al número de albarán
                self.cmbNumeroAlbaran.addItem(str(dato[0]))

    def cargar_datos(self, albaran):
        fila_seleccionada = self.cmbNumeroAlbaran.currentIndex()

        # COnsulta SQL para obtener los dato
        consulta_sql = "SELECT * FROM ventas WHERE numeroAlbaran = ?"

        # Guardar en variables lo del select
        datos_albaran = self.conexion_bd.consultaConParametros(consulta_sql, (albaran))


        if datos_albaran:
            self.txtDataAlbaran.setText(str(datos_albaran[0][1]))
            self.txtDataEntrega.setText(str(datos_albaran[0][2]))
            self.txtNumeroCliente.setText(str(datos_albaran[0][3]))

        consulta_sql2 = "SELECT * FROM detalleVentas WHERE numeroAlbaran = ?"

        # Guardar en variables lo del select
        datos_albaran = self.conexion_bd.consultaConParametros(consulta_sql2, (albaran))

        self.columna1 = []
        self.columna2 = []
        self.columna3 = []
        self.columna4 = []

        for fila in datos_albaran:
            self.columna1.append(fila[0])  # Suponiendo que la primera columna es la columna 1
            self.columna2.append(fila[1])  # Suponiendo que la segunda columna es la columna 2
            self.columna3.append(fila[2])  # Suponiendo que la tercera columna es la columna 3
            self.columna4.append(fila[3])


        self.tabla_data = datos_albaran
        self.modelo = ModeloTaboa(self.tabla_data)
        self.tabla.setModel(self.modelo)
        self.tabla.show()




    def on_botonGenerarFactura_clicked(self):
        try:
            print("Generando factura...")
            # Recoger los datos de los campos de texto
            numeroAlbaran = self.cmbNumeroAlbaran.currentText()
            dataAlbaran = self.txtDataAlbaran.text()
            dataEntrega = self.txtDataEntrega.text()
            numeroCliente = self.txtNumeroCliente.text()


            # Crear el archivo PDF
            c = canvas.Canvas("PDFpracticaExamenCasa.pdf", pagesize=A4)
            c.setFont("Helvetica", 20)
            c.drawString(340, 750, "FACTURA SIMPLIFICADA")

            c.setFont("Helvetica", 20)
            c.drawString(100, 700, "Nombre de tu Empresa")

            c.drawImage("check.png", 500, 700, 40, 40)

            c.setFont("Helvetica", 14)
            c.drawString(100, 680, "Numero Albarán: ")
            c.setFillColor("grey")
            numeroAlbaran_texto = c.beginText(230, 680)
            numeroAlbaran_texto.textLine(str(self.columna1))
            c.drawText(numeroAlbaran_texto)

            c.setFillColor("black")
            c.setFont("Helvetica", 14)
            c.drawString(100, 660, "Data: ")
            c.setFillColor("grey")
            dataAlbaran_texto = c.beginText(150, 660)
            dataAlbaran_texto.textLine(str(self.columna2))
            c.drawText(dataAlbaran_texto)

            c.setFillColor("black")
            c.setFont("Helvetica", 14)
            c.drawString(100, 640, "Data entrega: ")
            c.setFillColor("grey")
            dataEntrega_texto = c.beginText(200, 640)
            dataEntrega_texto.textLine(str(self.columna3))
            c.drawText(dataEntrega_texto)

            c.setFillColor("black")
            c.setFont("Helvetica", 14)
            c.drawString(100, 620, "Número Cliente: ")
            c.setFillColor("grey")
            numeroCliente_texto = c.beginText(220, 620)
            numeroCliente_texto.textLine(str(self.columna4))
            c.drawText(numeroCliente_texto)


            # Crear datos para la tabla
            encabezadoTabla = ['1', '2', '3', '4','5']
            infoTabla = self.tabla_data

            # Configurar el estilo de la tabla
            estilo = TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.darkgreen),
                # Establece un fondo verde oscuro para la primera fila de la tabla (fila 0). Esto proporciona un fondo distintivo para el encabezado de la tabla.
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                # Establece el color del texto en blanco para la primera fila de la tabla. Esto asegura que el texto en el encabezado sea visible sobre el fondo verde oscuro.
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                # Aplica la fuente "Helvetica-Bold" al texto en la primera fila de la tabla. Esto hace que el texto en el encabezado sea más grueso y destacado.
                ('BOTTOMPADDING', (0, 0), (-1, 0), 7),
                # Agrega un espacio adicional en la parte inferior de la primera fila. Esto proporciona un espacio visualmente agradable entre el encabezado y el resto de la tabla.
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
                # Establece un fondo verde claro para las filas de datos (a partir de la segunda fila hasta la penúltima fila, ya que empieza desde la fila 1). Esto ayuda a diferenciar visualmente las filas de datos del encabezado.
                # ('BACKGROUND', (0, -1), (-1, -1), colors.darkgreen), # Establece un fondo verde oscuro para la última fila
                # ('TEXTCOLOR', (0, -1), (-1, -1), colors.white),# Establece el color del texto en blanco para la última fila
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
                # Aplica la fuente "Helvetica-Bold" al texto en la última fila
                # ('BACKGROUND', (0, -1), (1, -1), colors.white),# Establece un fondo blanco para la última fila que no tiene datos
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                # Alinea el contenido de la tabla al centro. Especifica que tanto el texto como los números en la tabla se alineen al centro.
                ('FONTSIZE', (0, 0), (-1, -1), 15),  # Ajusta el tamaño de la fuente
                ('LEADING', (0, 0), (-1, -1), 20),  # Ajusta el espaciado entre las líneas
                ('GRID', (0, 0), (-1, -1), 1, colors.white),  # Agrega bordes a todas las celdas
            ])

            # TAMAÑO TABLA
            tabla = Table(data=[encabezadoTabla] + infoTabla, colWidths=[50, 50, 50, 100, 50])
            tabla.setStyle(estilo)

            # POSICION TABLA EN LIENZO
            tabla.wrapOn(c, 0, 0)
            tabla.drawOn(c, 150, 400)  # Ajusta las coordenadas

            """
            Si quisiera crear tabla con los datos que obtengo de los txt
             # Crear datos para la tabla
        encabezadoTabla = ['Campo', 'Valor']
        datosTabla = [
            ['Numero Albarán', numeroAlbaran],
            ['Data', dataAlbaran],
            ['Data entrega', dataEntrega],
            ['Número Cliente', numeroCliente]
        ]
            """

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
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    aplicacion.exec()