![Logo](/logoHex.png)

<p align="center">
<img src="https://img.shields.io/github/issues/llactalab/sisurbano" alt="Issues"></img>
<img src="https://img.shields.io/github/forks/llactalab/sisurbano" alt="Forks"></img>
<img src="https://img.shields.io/github/stars/llactalab/sisurbano" alt="Stars"></img>
<img src="https://img.shields.io/github/license/llactalab/sisurbano" alt="Licence"></img>
</p>

<br>
<img src="https://github.com/anahicalderon/sisurbano/blob/fbfdcdd48d0519ea9f562d8652eb8d0f24ecaa25/img_uso1.PNG?raw=true" alt="img_uso1" width=50%></img>
<img src="https://github.com/anahicalderon/sisurbano/blob/master/img_uso2.PNG?raw=true" alt="img_uso2" width=50%></img>

<br>
<br>
<br>

* [SISURBANO](#sisurbano)
* [Requisitos](#requisitos)
* [Instalación](#instalación)
* [Lista de indicadores](#lista-de-indicadores)
* [Contribuyendo](#🤝-contribuyendo)
* [Contactos](#contactos)
<br>
<br>
<br>


# SISURBANO - Evaluación de sustentabilidad en tejidos urbanos: Sistema de indicadores y herramienta de análisis espacial.

Esta herramienta basada en sistemas de información geográfica permite integrar datos urbanos desagregados en un sistema de indicadores para evaluar diferentes componentes de la sustentabilidad. La herramienta es open-source y puede ser utilizada de forma libre por investigadores, técnicos, estudiantes, planificadores y ciudadanía en general.

SISURBANO parte de la necesidad de conocer la forma urbana y su relación con la sustentabilidad como clave para comprender los retos actuales de nuestras ciudades. Así, luego del desarrollo de una batería de indicadores de sustentabilidad urbana, adaptada a la localidad de una ciudad andina intermedia, como es el caso de Cuenca, la investigación se enfoca en la creación y aplicación de una herramienta informática automatizada que permita medir los diferentes indicadores de sustentabilidad en los tejidos urbanos de Cuenca. Seguido, el proyecto explora la variabilidad de los valores de estos indicadores entre las diferentes tipologías de tejidos, con el fin de mostrar evidencia cuantitativa de la correlación entre sustentabilidad y morfología urbana. Los resultados permiten además una evaluación diferenciada de las condiciones de sustentabilidad presentes en cada tejido. Esto último posibilita la discusión de políticas públicas que mejoren la calidad de vida de los sectores menos beneficiados (sustentables).

# Requisitos 
- QGIS 3.10.2 o superior. [Sitio para descargar](https://www.qgis.org/es/site/forusers/download.html)

# Instalación
Descargue el complemento SISURBANO haciendo click [aquí](https://github.com/llactalab/sisurbano/raw/master/sisurbano.zip), luego agregue a sus complementos de QGIS. El complemento se agregará a la "Caja de herramientas de procesos". 

![Plugin](/pluginSisurbano.png)

Existe una diferencia importante entre QGIS en Windows y QGIS en Linux o Mac. Mientras que la versión de Windows instala su propio intérprete de Python, los de Linux y Mac dependen del Python del sistema operativo.

El plugin de SISUrbano utiliza una librería externa llamada ```pandas```, en caso de que exista un error en la instalación debido a esta librería, ```pandas``` se deberá instalar manualmente.

### Windows 
<!-- - pip install pandas. [Más información de como instalar pandas en Windows](https://stackoverflow.com/questions/42907331/how-to-install-pandas-from-pip-on-windows-cmd) -->
- Debería haber una instalación OSGeo4W Shell en su sistema Windows. Ejecútelo como administrador y use el paquete de instalación de pip. Si no tiene pip instalado, primero [descárguelo](https://bootstrap.pypa.io/get-pip.py). 
- Luego ejecute `python get-pip.py`. Ahora debería poder instalar y usar nuevas bibliotecas de Python de QGIS.
- ```pip install pandas```

### Ubuntu 
- Abra la consola de comandos y escriba ```pip install pandas```.

# Lista de indicadores
- Ambiente construido
    + A01 Densidad neta de habitantes
    + A02 Densidad neta de viviendas
    + A03 Compacidad absoluta
    + A04 Eficiencia en el uso del territorio
    + A05 Área de predios vacíos
    + A06 Proporción de la calle
    + A07 Proximidad a servicios urbanos básicos
    + A08 Proximidad al espacio público abierto
    + A08 Proximidad al espacio público abierto
    + A09 Cobertura de actividades comerciales cotinianas
    + A10 Relación entre actividad y residencia
    + A11 Complejidad urbana
    + A12 Densidad de intersecciones peatonales
    + A13 Sinergia
- Ambiente biofísico
    + B01 Calidad del aire
    + B02 Luminación nocturna del viario público
    + B03 Confort acústico
    + B04 Proximidad al espacio verde público más cercano
    + B05 Superficie verde por habitante
    + B06 Superficie de área agrícola/huertos
    + B07 Permeabilidad del suelo
- Movilidad urbana
    + C01 Reparto del viario público peatonal
    + C03 Vías públicas por habitante'
    + C04 Proximidad a redes de transporte alternativo
    + C05 Espacio público ocupado por vehículos parqueados
    + C09 Consumo de energía eléctrica en la vivienda
    + C13 Cobertura del sistema de servicio de alcantarillado
- Dinámicas socio-espaciales
    + D01 Viviendas con cobertura total de servicios básicos
    + D02 Viviendas con carencias constructivas
    + D03 Viviendas emplazadas en zonas vulnerables y de riesgo
    + D04 Espacios públicos abiertos que necesitan mejoras
    + D05 Acceso a internet
    + D06 Uso del tiempo
    + D07 Indice de calidad de vida
    + D08 Cercanía y asequibilidad a alimentos
    + D09 Robos por número de habitantes
    + D10 Seguridad de tenencia de la vivienda
    + D11 Tasa de desempleo
    + D12 Mujeres en la fuerza de trabajo remunerado
    + D13 Población activa con estudios universitarios
    + D14 Estabilidad de la comunidad
    + D15 Percepción de inseguridad
    + D16 Índice de envejecimiento
    + D17 Segregación Espacial


# 🤝 Contribuyendo

Como la mayoría de los proyectos que trabajan con datos abiertos y software libre, la retroalimentación de los usuarios es una herramienta fundamental para la mejora de los datos y su tratamiento, por lo que agradecemos e incentivamos la recepción de ideas, sugerencias o correcciones. Puedes escribirnos a llactalab@ucuenca.edu.ec en caso que te interese colaborar de otra forma.

<br>


# Contactos

LlactaLAB – Ciudades Sustentables es un Grupo de Investigación de la Universidad de Cuenca, parte del Departamento Interdisciplinario de Espacio y Población.

llactalab@ucuenca.edu.ec


