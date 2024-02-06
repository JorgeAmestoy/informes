from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing

hojaEstilo = getSampleStyleSheet() # Obtener una hoja de estilo

# Crear un objeto de tipo lista que almacenará los objetos Platypus
elementosDoc = []

# Crear datos de temperaturas
temperaturas = [
               ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
               [15, 16, 20, 28, 30, 32, 35, 36, 34, 30, 20, 18],
               [-3, -4, -1, 18, 20, 22, 25, 26, 24, 20, 2, -2]
               ]

dibujo = Drawing(400, 200) # Crear un objeto de tipo Drawing
grafica = VerticalBarChart() # Crear un objeto de tipo VerticalBarChart
grafica.x = 50 # Posición en x de la gráfica
grafica.y = 50 # Posición en y de la gráfica
grafica.height = 125 # Altura de la gráfica
grafica.width = 300 # Ancho de la gráfica
grafica.data = temperaturas[1:] # Datos de la gráfica donde 1: es para omitir la primera fila de la tabla
grafica.strokeColor = colors.black # Color del borde de la gráfica
grafica.valueAxis.valueMin = -5 # Valor mínimo del eje vertical de la gráfica
grafica.valueAxis.valueMax = 40 # Valor máximo del eje vertical de la gráfica
grafica.valueAxis.valueStep = 5 # Paso del eje vertical de la gráfica
grafica.categoryAxis.labels.boxAnchor = 'ne' # Posición de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.dx = 8 # Distancia en x de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.dy = -10 # Distancia en y de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.labels.angle = 30 # Ángulo de las etiquetas del eje horizontal de la gráfica
grafica.categoryAxis.categoryNames = temperaturas[0] # Nombres de las categorías del eje horizontal de la gráfica
grafica.groupSpacing = 10 # Espacio entre grupos de barras de la gráfica
grafica.barSpacing = 2 # Espacio entre barras de la gráfica


dibujo.add(grafica) # Agregar la gráfica al dibujo
elementosDoc.append(dibujo) # Agregar el dibujo a la lista de elementos

documento = SimpleDocTemplate("ejemploGraficasRpl.pdf", pagesize=A4) # Crear un objeto de tipo SimpleDocTemplate
documento.build(elementosDoc) # Construir el documento a partir de la lista de elementos