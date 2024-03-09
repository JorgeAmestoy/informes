REPORTLAB:

https://danielcastelao.esemtia.net/moodle/pluginfile.php/12135/mod_resource/content/1/reportlab-userguide.pdf

CANVAS:<br>
https://elviajedelnavegante.blogspot.com/2010/03/crear-documentos-pdf-en-python-y-1.html

TEXTO: <br>
https://elviajedelnavegante.blogspot.com/2010/03/crear-documentos-pdf-en-python-y-2.html

OCTOPUS:<br>
https://elviajedelnavegante.blogspot.com/2010/04/crear-documentos-pdf-en-python-y-3.html

TABLAS:<br>
http://menteleal.blogspot.com/2014/02/reportlab-platypus-sobre-las-tablas.html

GRÁFICAS: <br>
http://menteleal.blogspot.com/2014/02/reportlab-graficos-16.html

EJEMPLOS FACTURAS: <br>
https://danielcastelao.esemtia.net/moodle/mod/resource/view.php?id=20634 <br>
https://danielcastelao.esemtia.net/moodle/mod/resource/view.php?id=20635


-----------------------------------------------------------

### GENERAL

**reportlab.graphics:** Este módulo se centra en la creación de gráficos vectoriales y figuras, como líneas, rectángulos, círculos, y también permite la inserción de imágenes en un documento PDF. Es útil cuando necesitas crear gráficos personalizados o añadir elementos visuales complejos a tu documento.<br>
**reportlab.pdfgen(canvas):** Este módulo proporciona las herramientas para generar documentos PDF mediante la especificación de contenido de bajo nivel, como texto, imágenes, formas básicas, etc., directamente en un lienzo de dibujo. Es útil para situaciones en las que deseas un control fino sobre el diseño y la disposición de los elementos en el PDF.<br>
**reportlab.platypus:** Este módulo se enfoca en la generación de documentos PDF de alto nivel utilizando una interfaz más abstracta y fácil de usar. Ofrece clases como Paragraph, Image, Spacer, etc., que te permiten definir el contenido del documento de manera más estructurada y menos orientada a la programación de bajo nivel. Es útil para la creación rápida de documentos con texto, imágenes y otros elementos comunes.<br>

### DUDAS
- objetoTexto.setFillColorRGB() ¿? - Qué pongo para que sea azul? rjo? amarillo?
- Por qué en ejemploImageRpl creo varias instancias de Drawing() en vez
de ir añadiendo todo en el mismo?
- En ejemploTextoRpl.pu, cómo diferencia el parrafo del otrosi lo añado
al mismo objeto?


### ejemploDocPlatypus.py

Heading1 (Encabezado 1): Este estilo suele ser el más prominente y se utiliza para los títulos principales del documento. Por lo general, es el título más grande y llamativo, y puede establecer la estructura general del documento.<BR>
Heading2 (Encabezado 2): Es un nivel de encabezado subordinado al Heading1. Se utiliza para subtítulos importantes o secciones principales dentro de las secciones principales. Suele ser más pequeño que Heading1 pero aún así resaltar respecto al texto normal.<br>
Heading3 (Encabezado 3): Es un nivel de encabezado subordinado al Heading2 y se utiliza para subdivisiones dentro de las secciones principales. Es más pequeño y menos prominente que Heading2, pero aún así resalta respecto al texto normal.<br>
Heading4 (Encabezado 4): Es un nivel de encabezado subordinado al Heading3 y se utiliza para subdivisiones más específicas o detalles dentro de las secciones principales. Es el menos prominente de los cuatro estilos de encabezado mencionados, pero aún así sirve para organizar y estructurar el contenido del documento.<br>

**keepWithNext** es 0: Esto significa que el elemento puede separarse del siguiente elemento si es necesario para la paginación del documento. Es decir, no se garantiza que el elemento actual permanezca junto al siguiente en el flujo del documento. Puede haber un salto de página entre el elemento actual y el siguiente.<br>
**keepWithNext** es 1: Esto indica que se desea que el elemento actual permanezca junto al siguiente elemento. En otras palabras, se asegura que el elemento actual no se separe del siguiente en el flujo del documento. Si es posible, se evita un salto de página entre el elemento actual y el siguiente.

## TABLAS

#### ESTILO
```
estilo = TableStyle([
                ('BACKGROUND',(0,0),(-1,0),colors.darkgreen), # Establece un fondo verde oscuro para la primera fila de la tabla (fila 0). Esto proporciona un fondo distintivo para el encabezado de la tabla.
                ('TEXTCOLOR',(0,0),(-1,0),colors.white), # Establece el color del texto en blanco para la primera fila de la tabla. Esto asegura que el texto en el encabezado sea visible sobre el fondo verde oscuro.
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), # Aplica la fuente "Helvetica-Bold" al texto en la primera fila de la tabla. Esto hace que el texto en el encabezado sea más grueso y destacado.
                ('BOTTOMPADDING', (0, 0), (-1, 0), 7), # Agrega un espacio adicional en la parte inferior de la primera fila. Esto proporciona un espacio visualmente agradable entre el encabezado y el resto de la tabla.
                ('BACKGROUND',(0,1),(-1,-2),colors.lightgreen), # Establece un fondo verde claro para las filas de datos (a partir de la segunda fila hasta la penúltima fila, ya que empieza desde la fila 1). Esto ayuda a diferenciar visualmente las filas de datos del encabezado.
                ('BACKGROUND',(0,-1),(-1,-1),colors.darkgreen), # Establece un fondo verde oscuro para la última fila
                ('TEXTCOLOR',(0,-1),(-1,-1),colors.white), # Establece el color del texto en blanco para la última fila
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),# Aplica la fuente "Helvetica-Bold" al texto en la última fila
                ('BACKGROUND',(0,-1),(1,-1),colors.white), # Establece un fondo blanco para la última fila que no tiene datos
                ('ALIGN',(0,0),(-1,-1),'CENTER'), # Alinea el contenido de la tabla al centro. Especifica que tanto el texto como los números en la tabla se alineen al centro.
                ('FONTSIZE', (0, 0), (-1, -1), 15),  # Ajusta el tamaño de la fuente
                ('LEADING', (0, 0), (-1, -1), 20),   # Ajusta el espaciado entre las líneas
                ('GRID', (0, 0), (-1, -1), 1, colors.white),  # Agrega bordes a todas las celdas
                    ])
```                    
#### Para VALIGN (alineación vertical):

- `'BOTTOM'`: Alinea el texto en la parte inferior de la celda.
- `'MIDDLE'`: Alinea el texto en el centro vertical de la celda.
- `'TOP'`: Alinea el texto en la parte superior de la celda.

#### Para ALIGN (alineación horizontal):

- `'LEFT'`: Alinea el texto a la izquierda de la celda.
- `'CENTER'`: Alinea el texto en el centro horizontal de la celda.
- `'RIGHT'`: Alinea el texto a la derecha de la celda.
<br>

#### COLORES

**('TEXTCOLOR', (0, 0), (0, -1), colors.pink):**<BR>
El primer (0, 0) indica la posición de inicio, que es la celda en la esquina superior izquierda de la tabla. El primer 0 representa la columna y el segundo 0 representa la fila. Entonces, este es el primer elemento de la primera fila de la tabla.<BR>
El segundo (0, -1) indica la posición de fin. El 0 nuevamente representa la columna, pero el -1 representa la última fila de la tabla.<br>
Por lo tanto, esta expresión establece el color del texto en todas las celdas de la primera columna de la tabla a rosa. El estilo se aplica desde la celda en la esquina superior izquierda hasta la celda en la esquina inferior izquierda de la primera columna.<br>
**('TEXTCOLOR',(1,0),(-1,0), colors.blueviolet):** Esto cambia el color del texto de la primera fila de la tabla a violeta. Desde la columna1 pero en la fila cero pintame de bluviolet todas las columnas pero en la misma fila (la cero)<br>
**('TEXTCOLOR',(1,1),(-1,-1), colors.grey):**<br>
Pintame de gris desde la columa 1 y fila 1 hasta la ultima columna y ultima fila<br>
**POSICIONES NEGATIVAS**<br>
**('TEXTCOLOR',(0,0),(-1,0), colors.grey),**# Darle color desde la columna 0 hasta la ultima co0luma (-1, **penultima seria -2**) de la fila 0<br>
**('BACKGROUND', (-2, -2), (-1, -1), colors.lavenderblush):** (-2, -2) se refiere a la penúltima fila y columna, mientras que (-1, -1) se refiere a la última fila y columna. Por lo tanto, esta línea de código establece un fondo de color lavanda claro (lavenderblush) para todas las celdas desde la penúltima fila y columna hasta la última fila y columna de la tabla.<br>
**('BOX',(1,1),(-1,-1), 1.25, colors.grey):** Esto dibuja un borde alrededor de todas las celdas de la tabla (excepto la primera fila y la primera columna) con un grosor de 1.25 y un color gris.<br>
**('INNERGRID',(1,1),(-1,-1), 1.25, colors.lightgrey):** Esto dibuja una cuadrícula interna dentro de todas las celdas de la tabla (excepto la primera fila y la primera columna) con un grosor de 1.25 y un color gris claro.<br>
**('VALING',(0,0),(-1,-1), 1.25, 'MIDDLE'):** Esto alinea verticalmente el texto de todas las celdas de la tabla al centro.<br>
**('BACKGROUND',(-2,-1),(-1,-1), colors.lightgrey)**: se debe pintar el fondo de las celdas desde la penúltima columna de la última fila hasta la última columna de la última fila de la tabla con un color gris claro.<br>


### DATOS A DESTACAR
imagen = Image("check.png")# SI fuese jppg tendria que poner el width y el height para que runnease

### MÉTODOS
```
for i,fila in enumerate(temperaturas):
   for j,temperatura in enumerate(fila): #Para saber el indice de la columna de la lista temperaturas
       if type(temperatura) == int:
           if temperatura>0:# Aqui se trabaja columna, fila y no fila, columna. POr eso j,i.
            estilo.append(('TEXTCOLOR',(j,i),(j,i), colors.black))# La j,i es la posicion de la fila y columna. Significa que va a cambiar el color del texto de la fila y columna entera¿?
            if temperatura > 30:
                estilo.append(('BACKGROUND', (j,i), (j,i), colors.fidred))
            elif temperatura<=30 and temperatura>20:
                estilo.append(('BACKGROUND', (j,i), (j,i), colors.orange))
            elif temperatura<=20 and temperatura>10:
                estilo.append(('BACKGROUND', (j,i), (j,i), colors.lightpink))
            elif temperatura<=10 and temperatura>0:
                estilo.append(('BACKGROUND', (j,i), (j,i), colors.lightblue))
       else:
        estilo.append(('TEXTCOLOR',(j,i),(j,i), colors.blue))
        estilo.append(('BACKGROUND',(j,i),(j,i),colors.lightgrey))
```
Este método trabaja con la variable estilo, que es una lista de tuplas que contienen instrucciones para dar estilo a la tabla.<br>
**El bucle for i, fila in enumerate(temperaturas):** itera sobre cada fila de la lista temperaturas. enumerate() devuelve tanto el índice i
como el contenido fila de la fila actual.<br>
Dentro del bucle exterior, hay otro **bucle for j, temperatura in enumerate(fila)**: que itera sobre cada elemento 
de la fila actual. Aquí, j representa el índice de la columna actual y temperatura representa el contenido de la celda.<br>
Se verifica si el contenido de la celda es un número entero mediante **if type(temperatura) == int:**.
Si lo es, se procede a aplicar estilos basados en el valor de la temperatura.<br>
Si la temperatura es mayor que cero (**if temperatura > 0:**), se cambia el color del texto a negro y se
establece un color de fondo dependiendo del rango de la temperatura
utilizando la función **estilo.append(('BACKGROUND', (j,i), (j,i), color))**,
donde (j,i) representa la posición de la celda y color es el color correspondiente al rango de la temperatura.<br>
Así, cuando (j, i) y (j, i) están iguales en una tupla (j, i), (j, i), eso significa que se está refiriendo a 
una sola celda específica en la tabla, ubicada en la fila i y columna j.<br>
Entonces, en el contexto de **('BACKGROUND', (j,i), (j,i), colors.fidred)**, la tupla (j,i) especifica la esquina superior
izquierda del rango de celdas, y (j,i) especifica la esquina inferior derecha del rango. 
Pero dado que son las mismas coordenadas (j,i) en ambas partes de la tupla, se está aplicando el estilo a una única celda.<br>
Si el contenido de la celda no es un número entero, se asume que es un texto (nombre del mes o tipo de temperatura) 
y se cambia el color del texto a azul y se le aplica un fondo gris claro. Esto se realiza para resaltar las etiquetas 
de los meses y los tipos de temperatura.<br>
En resumen, este método utiliza bucles para recorrer los datos de la tabla de temperaturas y aplica estilos de forma dinámica dependiendo del contenido de cada celda.<br>

```
total = sum(Decimal(row[3].replace(',', '.')) for row in self.table_data)
total_row = ['', '', 'TOTAL', f'{total:.2f} €']
```
La línea `sum(Decimal(row[3].replace(',', '.')) for row in self.table_data)` calcula el total sumando el valor de la columna 3 en cada fila de `self.table_data`. Utiliza una comprensión de lista para iterar sobre cada fila en `self.table_data`. Dentro de la comprensión de lista, `Decimal(row[3].replace(',', '.'))` convierte el valor de la columna 3 en un objeto Decimal para asegurar una precisión adecuada en cálculos financieros. Además, `replace(',', '.')` reemplaza las comas (`,`) con puntos (`.`) en el valor para que pueda ser interpretado correctamente como un número decimal.

La línea `total_row = ['', '', 'TOTAL', f'{total:.2f} €']` crea una nueva fila para representar el total en la factura. La lista `['', '', 'TOTAL', f'{total:.2f} €']` contiene cuatro elementos:

- `''`: Un espacio en blanco para la primera columna.
- `''`: Otro espacio en blanco para la segunda columna.
- `'TOTAL'`: La palabra "TOTAL" para la tercera columna, indicando que esta fila representa el total de la factura.
- `f'{total:.2f} €'`: Utiliza una cadena formateada (f-string) para convertir el valor de `total` en una cadena con dos decimales (`:.2f`) seguidos del símbolo del euro (`€`). Esto muestra el total con dos decimales y el símbolo del euro al final.
