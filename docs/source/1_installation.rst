=================================
Primeros pasos
=================================

Requisitos
------------------------------

Sisurbano es un complemento que se instala el programa de sistemas de información geográfico QGIS 3.10.2 o superior. `Sitio para descargar <https://www.qgis.org/es/site/forusers/download.html>`_

Instalación
------------------------------

Descargue el complemento SISURBANO haciendo click `aquí <https://github.com/llactalab/sisurbano/raw/master/sisurbano.zip>`_, luego agregue a sus complementos de QGIS. El complemento se agregará a la "Caja de herramientas de procesos".

.. image:: img/pluginSisurbano.png
   :width: 200

Existe una diferencia importante entre QGIS en Windows y QGIS en Linux o Mac. Mientras que la versión de Windows instala su propio intérprete de Python, los de Linux y Mac dependen del Python del sistema operativo.

El plugin de SISUrbano utiliza una librería externa llamada pandas, en caso de que exista un error en la instalación debido a esta librería, pandas se deberá instalar manualmente.

Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Debería haber una instalación OSGeo4W Shell en su sistema Windows. Ejecútelo como administrador y use el paquete de instalación de pip. Si no tiene pip instalado, primero [descárguelo](https://bootstrap.pypa.io/get-pip.py). 
- Luego ejecute `python get-pip.py`. Ahora debería poder instalar y usar nuevas bibliotecas de Python de QGIS.
- ``pip install pandas``


Ubuntu 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Abra la consola de comandos y escriba ```pip install pandas```.
