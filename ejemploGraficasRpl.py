from reportlab.graphics.charts.legends import LineLegend, Legend
from reportlab.graphics.charts.piecharts import Pie, Pie3d
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker

hojaEstilo = getSampleStyleSheet() # Creo una hoja de estilo

elementosDoc = []# Creo una lista de elementos vacía

# TABLA
temperaturas = [
               ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
               [15, 16, 20, 28, 30, 32, 35, 36, 34, 30, 20, 18],
               [-3, -4, -1, 18, 20, 22, 25, 26, 24, 20, 2, -2]
               ]

# GRÁFICA DE BARRAS
dibujo = Drawing(400, 200) # Crear un objeto de tipo Drawing
graficaBarras = VerticalBarChart() # Crear un objeto de tipo VerticalBarChart

graficaBarras.x = 50 # Posición en x de la gráfica
graficaBarras.y = 50 # Posición en y de la gráfica
graficaBarras.height = 125 # Altura de la gráfica
graficaBarras.width = 300 # Ancho de la gráfica
graficaBarras.data = temperaturas[1:] # Datos de la gráfica donde 1: es para omitir la primera fila de la tabla
graficaBarras.strokeColor = colors.black # Color del borde de la gráfica
graficaBarras.valueAxis.valueMin = -5 # Valor mínimo del eje vertical de la gráfica
graficaBarras.valueAxis.valueMax = 40 # Valor máximo del eje vertical de la gráfica
graficaBarras.valueAxis.valueStep = 5 # 5 unidades de división verticalmente
graficaBarras.categoryAxis.labels.boxAnchor = 'ne' # Posición de las etiquetas del eje horizontal de la gráfica. Noreste.
graficaBarras.categoryAxis.labels.dx = 8 # Distancia en x de las etiquetas del eje horizontal de la gráfica
graficaBarras.categoryAxis.labels.dy = -10 # Distancia en y de las etiquetas del eje horizontal de la gráfica
graficaBarras.categoryAxis.labels.angle = 30 # Ángulo de las etiquetas del eje horizontal de la gráfica
graficaBarras.categoryAxis.categoryNames = temperaturas[0] # Nombres de las categorías del eje horizontal de la gráfica
graficaBarras.groupSpacing = 10 # Espacio entre grupos de barras de la gráfica
graficaBarras.barSpacing = 5 # Espacio entre barras de la gráfica


dibujo.add(graficaBarras) # Agregar la gráfica al dibujo
elementosDoc.append(dibujo) # Agregar el dibujo a la lista de elementos
elementosDoc.append(Spacer(1, 100)) # Agregar un espacio  1 pulgada de ancho y 12 puntos de alto entre la gráfica de barras y la gráfica de líneas

# GRÁFICA DE LÍNEAS
dibujo = Drawing(400, 200) # Crear un objeto de tipo Drawing
graficaLineas = HorizontalLineChart() # Crear un objeto de tipo HorizontalLineChart
graficaLineas.x = 30
graficaLineas.y =50
graficaLineas.height = 125
graficaLineas.width = 350
# graficaLineas.data = [temperaturas[1]]# Así solo sale una linea. Si quiero que refleje las dos series debo colocar: graficaLineas.data = temperaturas[1:]. SIn los dos corchetes da error¿ probar
graficaLineas.data = temperaturas[1:]
graficaLineas.categoryAxis.categoryNames = temperaturas[0]# Nombres de las categorías del eje horizontal de la gráfica. Quiero que las etiquetas sean la primera fila de la lista temperaturas que son los meses.
graficaLineas.categoryAxis.labels.angle = 20 # Ángulo de las etiquetas del eje horizontal de la gráfica
graficaLineas.categoryAxis.labels.dx = 10# Distancia en x de las etiquetas del eje horizontal de la gráfica
graficaLineas.categoryAxis.labels.dy = -10# Distancia en y de las etiquetas del eje horizontal de la gráfica
graficaLineas.categoryAxis.labels.boxAnchor = 'n'# Posición de las etiquetas del eje horizontal de la gráfica donde n es norte. Para oeste sería w, para sur s y para este e.
graficaLineas.valueAxis.valueMin = 0# Valor mínimo del eje vertical de la gráfica
graficaLineas.valueAxis.valueMax = 40# Valor máximo del eje vertical de la gráfica
graficaLineas.valueAxis.valueStep = 10# Paso del eje vertical de la gráfica. Esto es para que se ponga una etiqueta cada 10 unidades.
graficaLineas.lines[0].strokeWidth = 1# Grosor de la línea (roja)
graficaLineas.lines[0].symbol = makeMarker('FilledCircle')# Tipo de marcador. ESto es para que se ponga un punto en cada punto de la línea.
graficaLineas.lines[1].strokeWidth = 5# Grosor de la línea ( verde)
dibujo.add(graficaLineas)# Agregar la gráfica al dibujo

leyenda = LineLegend()
leyenda.fontSize = 8# Tamaño de la fuente de la leyenda
leyenda.fontName = "Helvetica"# Tipo de fuente de la leyenda
leyenda.alignment = 'right'# Alineación de la leyenda
leyenda.x =0# Horizontal
leyenda.y = 0# Vertical
leyenda.columnMaximum = 2# Número máximo de columnas de la leyenda
series = ['Maximas','Minimas']# Nombres de las series de la leyenda
leyenda.colorNamePairs = [(graficaLineas.lines[i].strokeColor, series[i]) for i in range(len (graficaLineas.data))]# Esto es para que se ponga el color de la serie y el nombre de la serie en la leyenda. Uso una lista por comprensión para que se ponga el color y el nombre de la serie en la leyenda.
# [('red','Maximas'),('blue','Minimas')]# Esta creando una tupla con el color y el nombre de la serie. Esto es para que se ponga el color de la serie y el nombre de la serie en la leyenda.
dibujo.add(leyenda)# Agregar la leyenda al dibujo
elementosDoc.append(dibujo)# Agregar el dibujo a la lista de elementos


# GRAFICA EN FORMA DE TARTA 3D
elementosDoc.append(Spacer(30, 30)) # Agregar un espacio de 20 puntos entre la gráfica de barras y la gráfica de líneas
dibujo = Drawing(300, 200) # Crear un objeto de tipo Drawing
tarta = Pie3d() # Crear un objeto de tipo Pie
tarta.x = 65# Posición en x de la gráfica
tarta.y = 15# Posición en y de la gráfica
tarta.data = [10,5,20,25,40]# Datos de la gráfica
tarta.labels = ['Edge', 'Brave', 'Firefox', 'Safari', 'Chrome']# Etiquetas de la gráfica
tarta.slices.strokeWidth=0.5# Grosor del borde de las porciones de la gráfica
tarta.slices[3].popout = 10# Esto es para que se separe la porción de la gráfica de la tarta en 10 puntos
tarta.slices[3].strokeWidth = 2# Grosor del borde de la porción de la gráfica
tarta.slices[3].strokeDashArray = [2,2]# Tipo de línea del borde de la porción de la gráfica. Es en forma de guión.
tarta.slices[3].labelRadius = 2# Radio de la etiqueta de la porción de la gráfica. ESto es para que se ponga la etiqueta fuera de la porción de la gráfica.
tarta.slices[3].fontColor = colors.red# Color de la fuente de la etiqueta de la porción de la gráfica
# tarta.slices[3].fillColor = colors.pink# Color de relleno de la porción de la gráfica
tarta.sideLabels = 1# Esto es para que se pongan las etiquetas fuera de la gráfica
dibujo.add(tarta)# Agregar la gráfica al dibujo
elementosDoc.append(dibujo)# Agregar el dibujo a la lista de elementos

# GRAFICA EN FORMA DE TARTA
elementosDoc.append(Spacer(30, 30)) # Agregar un espacio de 20 puntos entre la gráfica de barras y la gráfica de líneas
dibujo = Drawing(300, 200) # Crear un objeto de tipo Drawing
tarta = Pie() # Crear un objeto de tipo Pie
tarta.x = 65# Posición en x de la gráfica
tarta.y = 15# Posición en y de la gráfica
tarta.data = [10,5,20,25,40]# Datos de la gráfica
tarta.labels = ['Edge', 'Brave', 'Firefox', 'Safari', 'Chrome']# Etiquetas de la gráfica
tarta.slices.strokeWidth=0.5# Grosor del borde de las porciones de la gráfica
tarta.slices[3].popout = 10# Esto es para que se separe la porción de la gráfica de la tarta en 10 puntos
tarta.slices[3].strokeWidth = 2# Grosor del borde de la porción de la gráfica
tarta.slices[3].strokeDashArray = [2,2]# Tipo de línea del borde de la porción de la gráfica. Es en forma de guión.
tarta.slices[3].labelRadius = 2# Radio de la etiqueta de la porción de la gráfica. ESto es para que se ponga la etiqueta fuera de la porción de la gráfica.
tarta.slices[3].fontColor = colors.blue# Color de la fuente de la etiqueta de la porción de la gráfica
# tarta.slices[3].fillColor = colors.pink# Color de relleno de la porción de la gráfica
tarta.sideLabels = 1# Esto es para que se pongan las etiquetas fuera de la gráfica
dibujo.add(tarta)# Agregar la gráfica al dibujo


leyenda = Legend()# Crear un objeto de tipo Legend
leyenda.x=300# Posición en horizontal de la leyenda
leyenda.y = 120# Posición vertical de la leyenda
leyenda.dx = 10# Distancia en x de la leyenda
leyenda.dy =10  # Distancia en y de la leyenda
leyenda.fontName = 'Helvetica'# Tipo de fuente de la leyenda
leyenda.fontSize = 8# Tamaño de la fuente de la leyenda
leyenda.boxAnchor = 'n'# Posición de la caja de la leyenda donde n es norte. Para oeste sería w, para sur s y para este e.
leyenda.columnMaximum = 15# Número máximo de columnas de la leyenda
leyenda.strokeWidth = 0.5# Grosor del borde de la leyenda
leyenda.strokeColor = colors.grey# Color del borde de la leyenda
leyenda.autoXPadding = 5# Espacio horizontal entre la leyenda y la gráfica
leyenda.yGap = 0# Espacio vertical entre las etiquetas de la leyenda
leyenda.dxTextSpace = 3# Distancia en x entre las etiquetas de la leyenda
leyenda.alignment = 'right'# Alineación de la leyenda
leyenda.dividerLines = 1|3|4# Líneas divisorias de la leyenda. ESto es para que se pongan las líneas divisorias en la leyenda. LOs numeros son los códigos de las líneas divisorias. 1 es para que se ponga la línea divisoria arriba, 2 es para que se ponga la línea divisoria abajo y 4 es para que se ponga la línea divisoria en el medio.
leyenda.dividerOffsY = 4.5# Distancia en y de las líneas divisorias de la leyenda
leyenda.subCols.rpad = 30# Distancia en x entre las columnas de la leyenda

paresColorLeyenda = list()# Crear una lista de pares de color y leyenda
colores = [colors.red, colors.blue, colors.green, colors.yellow, colors.pink]# Colores de las porciones de la gráfica
for i, color in enumerate(colores):# Recorro la lista de colores
    tarta.slices[i].fillColor = color# Esto es para que se ponga el color de la porción de la gráfica
    paresColorLeyenda.append((color,tarta.labels[i]))

leyenda.colorNamePairs = paresColorLeyenda# Esto es para que se ponga el color de la serie y el nombre de la serie en la leyenda

dibujo.add(leyenda)# Agregar la leyenda al dibujo
elementosDoc.append(dibujo)# Agregar el dibujo a la lista de elementos






documento = SimpleDocTemplate("ejemploGraficasRpl.pdf", pagesize=A4) # Crear un objeto de tipo SimpleDocTemplate
documento.build(elementosDoc) # Construir el documento a partir de la lista de elementos