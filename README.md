![Logo](/logoHex.png)

# SISURBANO - Plugin para el cálculo de indicadores de sustetabilidad urbana
Herramienta de Sistemas de Información Geográfica para QGIS para el cálculo de indicadores de sustentabildiad urbana en ciudades intermedias.

## Requisitos 
- QGIS 3.10.2 o superior. [Sitio para descargar](https://www.qgis.org/es/site/forusers/download.html)

## Instalación
Descargue o clone el repositorio, luego comprima la carpeta y agregue a sus complementos de QGIS. El complemento se agregará a la "Caja de herramientas de procesos". 

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

## Lista de indicadores
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



