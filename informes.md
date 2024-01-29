## INFORMES

Cristal Reports: Programa que se instala en el ordenador y que permite crear informes. Es de pago. <br>
BIRT: Programa que se instala en el ordenador y que permite crear informes. Es gratuito. <br>
JASPER REPORTS: Programa que se instala en el ordenador y que permite crear informes. Es gratuito. <br>
REPORT LABL: Librería de python que permite crear informes. Es gratuita. <br>

**Instalamos librería reportlab** <br>

## ejemploCanvasRpl.py

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

