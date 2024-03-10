# PRUEBAS

### PREGUNTAS EXAMEN

1. **¿Qué se entiende por término prueba?**
El término "prueba" se refiere a procesos sistemáticos para evaluar un sistema o componente con el objetivo de detectar errores y verificar su funcionamiento correcto.
Las pruebas de software son invetsigaciones cuyo objetivo es proporcionar información objetiva e independeiente
sobre la calidad del producto.
2. **¿Qué son validación y verificación?**

**VERIFCACIÓN:**
Proceso de evaluación de un sistema o componente para determinar
si un producto de una **determinada fase** de desarrollo satisface las condiciones
impuestas al inicio de la fase.*¿Estamos elaborando correctamente el producto?*
- **Propósito**: Asegurar que los productos internos seleccionados cumplen con su especificación de requerimientos. Los métodos
pueden ser: inspecciones, repisiones por pares, auditorias, recorridas, análisis, demostraciones, simulaciones..<br>
**VALIDACIÓN:** 
Proceso de evaluación de un sistema o componente **durante o al final** del proceso
de desarrollo apra determinar cuando se satisfacen los requerminetos especificados.*¿Estamos
elaborando el producto correcto?*
- **Propósito**: Es demostrar que un producto o componente de un rpdocutto cumple
su uso previsto cuando es puesto en su ambiente previsto. Deben ser seleccionados los productos internos
que mejor indican cuanto de bien el producto y los productos internos deben satisfaces las
necesidades del usuario.<br>
3. **¿Por qué se realizan las pruebas?**
- Evitar pérdidas económicas
- Evitar incumplir plazos y presupuestos
- Evitar mala calidad del prdoucto
- Evitar nsatisfaces a los interesados
- Evitar perder confianza del cliente
- 
4. **¿Recuerdas algún principio de los mencionados?**

- **Pruebas muestran a presencia de defectoss**: Significa que las pruebas demustran que EXISTEN problemas, pero no
que los problemas NO EXISTEN. El objetivo es detectar defectos.
- **Las pruebas exhaustivas son imposibles**: Las ruebas exhaustivas tratan de cubrir todas las combinaciones
psobles de datos en el sofware, para garantir que ninguna situacion puede surgir. En aplicaciones muy ssimples
sí es posible.
- **Pruebas tempranas**: Un producto se puede probar tan pronto como se haya creado. Es lo recomendable. Al final son más diciles de resolver.
- **Agrupamietno de defectos**: Estudios dicen que los probelmas tienden a agruparse en torno a ubn conjutno limitado
de módulos oáreas. Una vez que hayan sido identificadas, se puede enfocar las pruebas en etas zonas sensibles, mientras
se sigue buscando errores en los módulos restantes.
- **Paradoja del Pesticida**: Si las pruebas se repiten una y otra vez, ya no se encunetran nuevos errores.Si los programadores
responden a las pruebas reduciendo o eliminadno los errores, se deduce que como el software meejora, la eficacia de las priebas anteriores se
daña, se desgastan las pruebas y hay que crear y aprender y usar nuevas. Estas deben ser escritas.
5. **¿Qué son los casos de prueba?**
Estos casos se utilizan para probar diferentes escenarios y asegurarse de que el software funcione correctamente en diversas situaciones.
Se recomienid **mínimo 2** casos de prueba para cada requisito del sistema.

### PUNTOS IMPORTANTES
- Las pruebas nos demuestran la presencia de errores en  un programa. No pueden demostrar que no existen más defectos.
- Se diseñan pruebas según el sistema a desarrollar.
- Todo el proceso de pruebas puede ser demasiado extenso para un grupo pequeño, por eso se ajustan las p`ruebas o se contratan terceras empresas.
- La automatización de las pruebas puede reducir el tiempo pero puede elvar el coste

### DEFINICIONES
**Pruebas**: Es una actividad realizada para evaluar la calidad del producto y mejorarla
identificando defectos y problemas. <br>
**Pruebas(IEEE)**: Es el proceso de operar un sistema o componente bajo condiciones
específicas, observar o registrar los resultados y realizar una evaluación 
de algún aspecto del sistema.<br>
**Pruebas de software**: Verificación dinámica del comportamiento de un programa
contra el comportamiento esperado,  usando un conjunto finito de casos
de prueba, seleccionados de manera adecuada desde el dominio infitio
de ejecución(SWEBOK):
- Dinámica: Implica que para realizar las pruebas hay que ejecutar el prirama
para los datos de entrada.
- Comportamiento esperado: Debe ser posible decidir cuando la salida observada
de la ejecución del programa es aceptable o no, de fotra forma el esfuerzo
de la prueba es inútil.


## Causa del mal funcionamiento
- **Error**: Equivocación realizada por una persona(Ej: escribir mal una instrucción de código)
- **Defecto o falta**: Error al realizar alguna actividad concerniente al software. Lo que debería hacer y lo que hace(Debido a un error
de programacion, un botón en una app no hace lo que se supone que debería)
- **Falla**: Desvío respecto al comportamiento requerido del sistema.(Ej: Si hago clic en un enlace de pag web, la página nos e carga como se espera)<br>
*La prueba puede revelar fallas, pero son las faltas las que pueden y deber ser removidas*

## INTRODUCCIÓN(definición)
Las pruebas de software son invetsigaciones cuyo objetivo es proporcionar información objetiva e independeiente
sobre la calidad del producto.<br>
Es una actividad más en el proceso de control de calidad.<br>
Dependiendo del tipo, pueden ser implementas en cualquier moento del proceso.<br>

### ¿POR QUÉ REALIZAR PRUEBAS?
- Evitar pérdidas económicas
- Evitar incumplir plazos y presupuestos
- Evitar mala calidad del prdoucto
- Evitar nsatisfaces a los interesados
- Evitar perder confianza del cliente

## OBJETIVOS
- Demostrar al desarrollados y cliente que el software satisface sus requerimientos
- Descubrir defectos en software, en el que comportamiento esté incorrecto,
no deseable o no cumple la especificacón. (caídas del sistema, cálculos incrrectos y corruopcion de datos x ej)
### CONCLUSIÓN OBJETIVOS
- Prueba es un proceso que intenta proporcionar confianza en software
- La salida de ls pruebas, solo pueden predecirse por personas que comprenden
el funcionamiento del sistema
- Las pruebas deben basarse en un subconjutno de posibles casos de prueba

## PRINCIPIOS
- **Pruebas muestran a presencia de defectoss**: Significa que las pruebas demustran que EXISTEN problemas, pero no
que los problemas NO EXISTEN. El objetivo es detectar defectos.
- **Las pruebas exhaustivas son imposibles**: Las ruebas exhaustivas tratan de cubrir todas las combinaciones
psobles de datos en el sofware, para garantir que ninguna situacion puede surgir. En aplicaciones muy ssimples
sí es posible.
- **Pruebas tempranas**: Un producto se puede probar tan pronto como se haya creado. Es lo recomendable. Al final son más diciles de resolver.
- **Agrupamietno de defectos**: Estudios dicen que los probelmas tienden a agruparse en torno a ubn conjutno limitado
de módulos oáreas. Una vez que hayan sido identificadas, se puede enfocar las pruebas en etas zonas sensibles, mientras
se sigue buscando errores en los módulos restantes.
- **Paradoja del Pesticida**: Si las pruebas se repiten una y otra vez, ya no se encunetran nuevos errores.Si los programadores
responden a las pruebas reduciendo o eliminadno los errores, se deduce que como el software meejora, la eficacia de las priebas anteriores se
daña, se desgastan las pruebas y hay que crear y aprender y usar nuevas. Estas deben ser escritas.
## CONSIDERACIONES RESPECTO A LAS PRUEBA
- El probelma principal es que no se puede probar completamente el sistema por lo que se diseñarán **casos de prueba**`
- La actitud de la persona frente a la prueba es muy importante.
## CASOS DE PRUEBA
Son un conjunto de condiciones bajo las cuales un analista determinará si un app, software es parcial o completamente satisfactoria.
Se recomienid **mínimo 2** casos de prueba para cada requisito del sistema.
## ESTRUCTURA DE CASOS DE PRUEBA
1. **Introducción**: Contiene info general sobre los casos de prueba (identifiacdor, creador, version, nombre, porpósito, etc)
2. **Actividades**: Se describen y documentan las acciones a realizar en los casos de prueba (ambiente de prueba, inicialziación, finalización..)
3. **Resultados**: Se describen y documentos los resultados de las pruebas realizadas sobee el sistema (slaida esperdada, slaida obetenido, resultados, severidad, estado..)
## ACTITUD FRENTE A LA PRUEBA
- Prueba debe verse como forma de encontrar arreores
- La persona que la hace no puede tener el propósito de  verificar que el sistema
funciona correcyamente, sino el de buscar fallas, teniendo por seguro que xisten.

-------------------------------------------------

## PROCESO ESTÁNDAR
**HAY CINCO ETAPAS**:
1. **Planificación de pruebas**: Se definen el plan, estrategias.. Que resusos se usarán, cianto tiempo va a tardar, esfuerzos queridos,
riesgos.. Debe actualizarse este plan segúnse avanza el proyecto.
2. **Análisis y diseño de priebas**: Se diseña cómo se va a probar el sistema, se desterminan las pruebas a ejecutarse,
la metodología... *No se necesita un rpdoucto finalizado. Se generan aquí los casos de preuba.*
3. **Ejecución de pruebas:** Aquí se hace uso de todos los diseños geneerados anteriormente. Se registran las indicdencias detectados documentados
en un reporte. *Se necesita producto para realizar la ejecución*
4. **Reporte de pruebas**: Se analizan los resultados de la etapa anterior y de las indicencias
y su impacto en el proyecto. Se busca hacer análisis para corregir errores/fallas, etc.
5. **Cierre de pruebas**: Se toman las lecciones aprendidas de las fases anteirores. Se deja documento los errores, indicencias que afectaron,
para ser más preventivo en el futuro.

## TIPOS DE PRUEBAS POR SU EJECUCIÓN
- **Pruebas manuales**: Las hace un tester como si fuese un usuario pero siguiendo unos pasos establecidos. Realiza las acciones
indicadas en cada paso del caso de prueba comprobando que se uc,ple resultado. Si es distinto al esperado, re seportan con todo fetalle.
- **Pruebas automáticas**: Uso de software especial para controlar la ejecucion de pruebas y comparar resultados obetenidos
y los esperadas.
- **Pruebas específicas**: Se hacen de forma independiente y se hacen finromes detallados de los resultados. Este equipo trabaja a partir de documentos
de requerimientos del sistema y del usuario para desarollas los planes de prueba del sistema

## TRATAMIENTO DE PRUEBAS
Normalemnte se empieza con pruebas de componentes y luego las del sistema, aunque también se ha invertido esto, ya que implica
integrar componentes reutilizables ya adaptar el software.

## PRUEBAS DEL SISTEMA
- Implica integrar dos o más componentes que realicen funcciones del sistema y luego se prueba esto.<br>
-  En un proceso iteractivo con el cliente, esta prueba buscan proibar un cinremento que se va entrar al cliente.
- En un proceso en cascada, se ocupande probar el sistema por completo.

# STUBS
Componentes de "mentira" que imitan comportamiento de componentes todavía no implementados.

##  PRUEBAS DE INTEGRACIÓN
Hay dos fases:
1. **PRUEBAS DE INTEGRACIÓN:** Aqui el tipo de pruebas tiene acceso al código fuente del sistema.
Se construye a partir de sus componentes y probar el sistema resultante para aencontrar probelmas surgidos a partir de estos. Se comprueba
que los componenten funcionan juntos correctamente.<br>
**Integración descendente**: Se desarrolla el esqueleto del sistema y se añade los componente. Desde programa
princiapl hasta abajo por jerarquía.
**Integraciónd descendente profunda**: Se hace por ramas. Cada una implementa una funcionalidad específica.
Hay componentes comerciales, reulkizables adaptos, nuevos.
**Integración ascendente**: Se integran primero los componentes de nfrasteustcura que porporcionan servicios comunes como acceso a la BD y luego las funcionales.
Una buena opción es usar mezcla de ambas. Descendente para niveles superiores de la etsutura y ascendente para los suordinados.


## RESUMEN INTEGRACIÓN
- Hay que decicir al principio el orden de integración de los componententes
- Buena practica e sinetgrear primero los componentes que se usan con frecuencia
- Los componentes más usados reciben la mayoria de pruebas
- Inetgrar un nuevio componente puede cambiar el patrón de interacion de las demas
- **PRUEBAS DE REGRESIÓN**: es cuando se vuelve a ejecutar pruebas existentes de pruebas.

## **PRUEBAS DE ENTREGAS**: 
- Proceso de probar una entrega del sistema que ddistribuirá a los clientes.
- Objetivo es incrementar la confianza. Si se cumplen requisitos, se entrega al cliente. Esto se sabe si se muetsra
que se ha entregado al funcionadlidad especificada, el rendimiento OK, confiablidad OK y no folla durante uso normal.

## TÉCNICA DE LA CAJA NEGRA
Estas pruebas permiten obtener un conjutno de condiciones de entrada quye ejerciten complentamente los requisitos funcioanes de un programa. Se ignora
la etstura de control, contrentándose en la funcionandlidad del sistema.<br>
se centran en asegurarse de que todas las diferentes formas en que alguien podría usar el software estén probadas.
(Ejemplo biblioteca¿?)
## PRUEBAS GENERADAS:
- Probar el login usando logins correctos e incorrectos para ver que los que pueden pueden y los que no no.
- Probar repsuestas corre¡o eletronico

## PRUEBAS DE RENDIMINETO
- Se diseñnan para asegurar que el sistema pueda procesar su carga de forma esperada
- Se debe construir perfil operiacional: conjutno de pruebas que relfejan la cominacion real del teabajo que deberia ser manjeada 
por el sistema
## PRUEBAS DE COMPONENTES
- Comprueba los comonentes individuales del sistema
- Hay tres tipos de componentes:
  - Funciones o indiivudales: Más simplnes. Se usan rutinas.
  - Clases de objetos con varios atributos y metodos
  - Componentes compuestos formadas por difenres objetos o funcionees(tienn interfaz)
  
## PRUEBAS DE INTERFACES
- Objeto probar que la interfaz se comprota de acuerdo a la especifcaicon
- Son impornteantes para desarrollado orientdado a objetos
- Hay interfaces de parametros, de momoria compartida, procedurales(un componente encapsula un conjunto
de procedimientos que puedn ser llamados por otros componentes), interfaces de paso de mensajes(un componetne solicita un servicio a otro comp mediante paso de un mensaje)

## ERRORES DE INTERFACES
- Mal uso de la interfaz: Un componente llama a otro y va mal.por parametros mal pasados, numero errones de parametros.
- No compresion de interfaz: el componente que hace llada no comprende la interfaz del comp al que llama y hace suposicones
- Errores temporales: esto pasa los uqe comparten memoria o en la interfaz de paso de mensajes.

## PRUEBAS BASADAS EN REQUERIMIENTOS
Son prubeas de validacion en lugar de por decto. El use rintenta demostrar que el sistema
se ha ejecutado bien haciendo un conjunto de pruebas.

## PRUEBAS DE PARTICIONES
Son conjutos de datos en donde todos los miembros de los conjutnos deberians er procesados de la misma forma.

## PRUEBAS ESTRUCTURALES
- Estas se derivan a partir del conocimiento a le estructura e implemetnacion del sofware. Son de CAJA BLANCA.
- Su diseño está ligado al codigo fuente

## PRUEBAS DE CAMINOS
- Son una etsratgeia de pruebas etructurales cuo objetivo e sprobar acda camino de ejecucion de un problema.
- El numero de caminos del programa es sproporcional al tamaño del mismo
- Se usan sobre todo en pruebas de componentes
- Cada camino debe ejecutarse al menos una vez

## GLOSARIO
1. Gestor de prueba: gestiona la ejecucion de las pruebas del prgrama, mantiene registros de los datos
2. Generador de datos: usa datos de la base de datos o genera paratrones aleaotrios para probar el sistema
3. Oráculo: Genera predicciones de resultados esperados
4. Comparador de ficheros: compara los resultados de pruebas al programa con resultados
anteriores
5. Generado de informes: Porporciona la definciion de informes y fcailidades de generacion 
para los resultados de las pruebas.
6. Analizados dinámico: Añade codigo de un programa para contar numeros de veces qyue se ha ejhecutado
cada sentencia, para generar un informe.
7. Simulador: simulan donde se ejecuta el prugrama.