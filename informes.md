## INFORMES

Cristal Reports: Programa que se instala en el ordenador y que permite crear informes. Es de pago. <br>
BIRT: Programa que se instala en el ordenador y que permite crear informes. Es gratuito. <br>
JASPER REPORTS: Programa que se instala en el ordenador y que permite crear informes. Es gratuito. <br>
REPORT LABL: Librería de python que permite crear informes. Es gratuita. <br>

**Instalamos librería reportlab** <br>

## ejemploCanvasRpl.py

## APUNTES PROFE ( ver ESemtia) 

https://danielcastelao.esemtia.net/moodle/pluginfile.php/12135/mod_resource/content/1/reportlab-userguide.pdf
Pag 16¿?
PAg 27: colores... Antes edicion...
Pag 29: lo de que salgan desplzadas las frases
```
auxiliar = canvas.Canvas("primerDocumento.pdf")

auxiliar.drawString(0,0)
```
Distintas opciones con auxiliar.(auxiliar.image, auxiliar.drawString, auxiliar.line, auxiliar.rect, auxiliar.setFillColor, auxiliar.setFont, auxiliar.drawString...)<br>
El **punto de origen** es (X,Y) ,(0,0), siendo la x horizontal
y la Y vertical, en la esquina inferior izquierda de la página. <br>

## ejemplosImageRpl.py
```
from reportlab.graphics.shapes import Image, Drawing # Esto es para que se pueda insertar una imagen en el documento pdf
from reportlab.graphics import renderPDF # Esto es para que se pueda renderizar el documento pdf (mostrarlo en el navegador)
from reportlab.lib.pagesizes import A4 # Esto es para que se pueda usar el tamaño A4
```

**Page Layout And Typography Using Scripts** es una página
que nos permite ver los distintos tipos de letra q
que podemos usar en reportlab. <br>

## ejemploDocPlatypus (ESEMTIA)<br>
https://elviajedelnavegante.blogspot.com/2010/04/crear-documentos-pdf-en-python-y-3.html<br>
**Doc Template**<br>
**Page Template**<br>
**FRAMES**<br>
**Flowables**

**PAG 77 -> XML**

**Manual Reportlab**
https://danielcastelao.esemtia.net/moodle/pluginfile.php/12135/mod_resource/content/1/reportlab-userguide.pdf

# 1-2-2024
Libro ReportLab.pdf
Capitulo 3: Fuentes y tipos de letra
Capitulo 7: Tablasy TableStyles (pag 83)


# 5-2-2024

ES COLUMNA, FILA NO FILA, COLUMNA

MODULO ejemplotablaTemperatura.py

**estilo.append(('TEXTCOLOR',(i,j),(i,j), colors.blue))**: Fijarme que no cierro con
parentesis TEXTCOLOR. Diferencia entre esto y 
 estilo.append(('TEXTCOLOR'),(i,j),(i,j), colors.blue)) ¿? EJecuta¿?

 **if temperatura>0:
            estilo.append(('TEXTCOLOR',(j,i),(j,i), colors.black))**:
que es la (j,i)

----------------------------------

MODULO ejemploTablasCombinadas.py

## EXAMEN FACTURA

Dominar los PÁRRAFOS

EJEMPLO DE PARRAFO, la cabecera hay que meterla en una tabla para que salga bien
el color dentro de esta.

Por qué algunso tiene save y los que no tienen tablas no?

