from PyQt6.QtCore import QAbstractTableModel, Qt

from PyQt6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QTableView, QVBoxLayout, QHBoxLayout, QWidget,
                             QComboBox, QGroupBox, QGridLayout, QLabel, QPushButton, QMessageBox)

from conexionBD import ConexionBD

import sys

class ModeloTaboa(QAbstractTableModel):
    def __init__(self, datos):
        """Inicializa el modelo con los datos proporcionados.

        :param datos: Los datos para el modelo.
        :type datos: list[list[str]]

        """
        super().__init__()
        self.datos = datos

    def rowCount(self, index):
        """Devuelve el número de filas en el modelo.

        :param index: Índice de la fila.
        :type index: QModelIndex
        :return: El número de filas en el modelo.
        :rtype: int

        """
        return len(self.datos)

    def columnCount(self, index):
        """Devuelve el número de columnas en el modelo.

        Si hay datos disponibles, devuelve el número de columnas basado en la longitud de la primera fila de datos.

        :param index: Índice de la columna.
        :type index: QModelIndex
        :return: El número de columnas en el modelo.
        :rtype: int

        """
        if self.datos:
            # Devuelve el número de columnas basado en la longitud de la primera fila de datos
            return len(self.datos[0])
        return 0

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        """Devuelve los datos en el índice especificado para el rol dado.

        Si el rol es DisplayRole o EditRole, devuelve los datos en el índice en forma de cadena.

        :param index: El índice de los datos.
        :type index: QModelIndex
        :param role: El rol para los datos.
        :type role: Qt.ItemDataRole
        :return: Los datos en el índice.
        :rtype: str or None

        """
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
                value = self.datos[index.row()][index.column()]
                return str(value)

    def setData(self, index, value, role):
        """Establece los datos en el índice especificado con el valor dado para el rol dado.

        Si el rol es EditRole, actualiza los datos en el índice con el nuevo valor proporcionado.

        :param index: El índice en el que se establecerán los datos.
        :type index: QModelIndex
        :param value: El nuevo valor para establecer en el índice.
        :type value: str
        :param role: El rol para el que se establecerán los datos.
        :type role: Qt.ItemDataRole
        :return: True si se establecieron los datos correctamente, False en caso contrario.
        :rtype: bool

        """
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

        self.datos_bd = []# Creo lista vacía

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
        self.modelo = ModeloTaboa(self.datos_bd)
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
        botonborrar.clicked.connect(self.on_botonborrar_clicked)
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

            # Agregar los números de albarán obtenidos al QComboBox
            for dato in datos_albaran:
                self.cmbNumeroAlbaran.addItem(str(dato[0]))

    def cargar_datos(self, albaran):
        """Carga los datos relacionados con el albarán seleccionado en la ventana.

        Realiza consultas a la base de datos para obtener los datos del albarán y los detalles de ventas asociados
        y actualiza los campos de texto y la tabla en la ventana con esta información.

        :param albaran: El número de albarán seleccionado.
        :type albaran: str

        """
        # Obtener el índice seleccionado del QComboBox de albarán
        fila_seleccionada = self.cmbNumeroAlbaran.currentIndex()

        # Consulta SQL para obtener los datos del albarán seleccionado
        consulta_sql = "SELECT * FROM ventas WHERE numeroAlbaran = ?"

        # Guardar en variables lo del select
        datos_albaran = self.conexion_bd.consultaConParametros(consulta_sql, (albaran))

        # Actualizar los campos de texto con los datos del albarán seleccionado
        if datos_albaran:
            self.txtDataAlbaran.setText(str(datos_albaran[0][1]))
            self.txtDataEntrega.setText(str(datos_albaran[0][2]))
            self.txtNumeroCliente.setText(str(datos_albaran[0][3]))

        # Consulta SQL para obtener los detalles de ventas del albarán seleccionado
        consulta_sql2 = "SELECT * FROM detalleVentas WHERE numeroAlbaran = ?"

        # Guardar en variables lo del select
        datos_albaran = self.conexion_bd.consultaConParametros(consulta_sql2, (albaran))

        # Actualizar los datos de la tabla con los detalles de ventas del albarán seleccionado
        self.datos_bd = datos_albaran
        self.modelo = ModeloTaboa(self.datos_bd)
        self.tabla.setModel(self.modelo)
        self.tabla.show()

    def on_botonborrar_clicked(self):
        """Maneja el evento de clic en el botón de borrar.

        Muestra un cuadro de diálogo de confirmación para confirmar la eliminación de los datos seleccionados.
        Si se confirma la eliminación, elimina la fila seleccionada de la tabla y de la base de datos.

        """
        # Obtener la fila seleccionada
        filas_seleccionadas = self.tabla.selectionModel().selectedRows()
        if filas_seleccionadas:
            # Mostrar un cuadro de diálogo de confirmación
            respuesta = QMessageBox.question(self, "Confirmación", "¿Estás seguro que quieres eliminar los datos?",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            # Si se confirma la eliminación
            if respuesta == QMessageBox.StandardButton.Yes:
                # Seleccionar la primera fila
                fila = filas_seleccionadas[0].row()

                # Obtener el número de albarán de la fila seleccionada
                numeroAlbaran = self.modelo.index(fila, 0).data()

                # Ocultar la fila en la tabla
                self.tabla.hideRow(filas_seleccionadas[0].row())

                # Eliminar la fila de la base de datos
                consulta_sql = "DELETE FROM ventas WHERE numeroAlbaran = ?"
                self.conexion_bd.eliminar_datos(consulta_sql, (numeroAlbaran,))

                # Mostrar un mensaje de éxito
                self.labelExito.setText(
                    "<html><b style='color: green;'>LOS DATOS SE HAN GUARDADO CORRECTAMENTE</b></html>")
            else:
                # Mostrar una advertencia si no se selecciona ninguna fila para eliminar
                QMessageBox.warning(self, "Advertencia", "Seleccione una fila para eliminar")

    def on_botonborrar_clicked(self):
        """
                Elimina la fila seleccionada tanto de la tabla como de la base de datos.

                :return: None
                """
        # Obtener la fila seleccionada
        filas_seleccionadas = self.tabla.selectionModel().selectedRows()
        if filas_seleccionadas:
            fila = filas_seleccionadas[0].row()  # Seleccionar la primera fila (asumiendo selección única)

            # Obtener el número de cliente de la fila seleccionada
            numeroCliente = self.modelo.index(fila, 0).data()

            # Eliminar la fila de la tabla
            #self.modelo.removeRow(fila)
            self.tabla.hideRow(filas_seleccionadas[0].row())

            # Eliminar la fila de la base de datos
            consulta_sql = "DELETE FROM clientes WHERE numeroCliente = ?"
            self.conexion_bd.eliminar_datos(consulta_sql, (numeroCliente,))

            self.limpiar_campos()

    def on_botoneditar_clicked(self):
        """
                Actualiza los datos de la fila seleccionada tanto en el modelo de tabla como en la base de datos.

                :return: None
                """

        # Obtener los nuevos valores de los campos de edición
        num_cliente = self.txtnum.text()
        nome = self.txtnome.text()
        apelidos = self.txtapelidos.text()
        direccion = self.txtdireccion.text()
        cidade = self.txtcidade.text()
        provincia = self.txtprovincia.text()
        cp = self.txtcp.text()
        telefono = self.txttelefono.text()

        # Obtener la fila seleccionada
        filas_seleccionadas = self.tabla.selectionModel().selectedRows()
        if filas_seleccionadas:
            fila = filas_seleccionadas[0].row()  # Seleccionar la primera fila (asumiendo selección única)

            # Actualizar los datos en el modelo de tabla
            self.modelo.datos[fila] = [num_cliente, nome, apelidos, telefono, direccion, cidade, provincia, cp]
            self.modelo.layoutChanged.emit()

            # Actualizar en la base de datos
            consulta_sql = "UPDATE clientes SET numerocliente=?, nomecliente=?, apelidoscliente=?, telefono=?, direccion=?, cidade=?, provinciaEstado=?, codigoPostal=? WHERE numerocliente=?"
            valores = (num_cliente, nome, apelidos, telefono, direccion, cidade, provincia, cp, num_cliente)
            self.conexion_bd.actualizar_datos(consulta_sql, valores)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    aplicacion.exec()