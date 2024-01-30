## INFORMES

Cristal Reports: Programa que se instala en el ordenador y que permite crear informes. Es de pago. <br>
BIRT: Programa que se instala en el ordenador y que permite crear informes. Es gratuito. <br>
JASPER REPORTS: Programa que se instala en el ordenador y que permite crear informes. Es gratuito. <br>
REPORT LABL: Librería de python que permite crear informes. Es gratuita. <br>

**Instalamos librería reportlab** <br>

## ejemploCanvasRpl.py

## APUNTES PROFE ( ver ESemtia) 

https://danielcastelao.esemtia.net/moodle/pluginfile.php/12135/mod_resource/content/1/reportlab-userguide.pdf

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
https://elviajedelnavegante.blogspot.com/2010/04/crear-documentos-pdf-en-python-y-3.html
**Doc Template**<br>
**Page Template**<br>
**FRAMES**<br>
**Flowables**

**PAG 77 -> XML**


