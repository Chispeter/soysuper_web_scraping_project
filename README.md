# Proyecto de Web Scraping de Soysuper 🛒
## ¿En qué consiste? 📝
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Este proyecto consiste en hacer web scraping de la página web [Soysuper](https://soysuper.com/), un supermercado online que te permite comparar precios de diferentes productos en distintos supermercados.

## ¿Cuál es la motivación? 💪
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; La motivación de este proyecto es (1) explorar y manejar distintas librerías como modo de entretenimiento y (2) conocer y poner en práctica una pequeña parte de la etapa de extracción en los procesos ETL y ELT como forma de crecimiento profesional.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Además, ¿a quién no le va a gustar una buena extracción de datos?

## ¿Cuál es el objetivo? 🎯
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; El objetivo es extraer los datos de los productos (como el nombre, la marca y el precio) que aparecen en la web y guardarlos en archivos JSON.

## ¿Cómo funciona? 🛠️
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; El proyecto usa la librería [requests](https://pypi.org/project/requests/) para hacer peticiones HTTP a la página web de [Soysuper](https://soysuper.com/), y la librería [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) para parsear el HTML y extraer los datos de interés para, posteriormente, guardarlos en archivos JSON en diferentes directorios con ayuda de las librerías json y os. El proyecto está dividido en varios módulos:

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; • **`config.py:`** Contiene una función que lee el archivo de configuración `config.json` y devuelve los parámetros del proyecto, como el nombre del host de la página web y el nombre del directorio en el que se van a guardar los datos.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; • **`web_scraping.py`:** Contiene diferentes funciones que extraen los datos de categorías, subcategorías, productos y supermercados de la página web. Los datos extraídos se guardan en archivos JSON con ayuda del módulo auxiliar `utils.py`.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; • **`utils.py`:** Contiene funciones auxiliares para (1) crear una serie de directorios por cada categoría, (2) escribir los achivos JSON, (3) limpiar cadenas de caracteres y (4) comprobar los últimos datos extraídos.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; • **`main.py`:** Contiene el código principal que ejecuta el web scraping.

## ¿Cómo se utiza? ⚙️
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Para usar este proyecto, se necesita tener instalado [Python 3](https://www.python.org/downloads/) y las librerías [requests](https://pypi.org/project/requests/) y [BeautifulSoup](https://pypi.org/project/beautifulsoup4/). Los pasos son los siguientes:

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **1.** Clonar o descargar este repositorio.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **2.** Crear y activar un entorno virtual (opcional). Se recomienda usar un entorno virtual para instalar las dependencias.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **3.** Instalar las dependencias con `pip install -r requirements.txt`.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **4.** Ejecutar el archivo `main.py` con `python main.py`.

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; **5.** Esperar a que termine el web scraping y revisar los archivos JSON generados en el directorio `data`, creado por defecto.

🔥**NOVEDAD**🔥En caso de detener la ejecución de `main.py`, la próxima vez que se vuelva a ejecutar, el módulo `web_scraping.py` comprobará los últimos datos extraídos y continuará por la última categoría registrada en el directorio `data`.

## Advertencia ⚠️
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Este proyecto tiene fines educativos y de entretenimiento. No se pretende violar los términos y condiciones de Soysuper, ni hacer un uso indebido de sus datos. Se recomienda hacer un uso responsable y moderado de este proyecto, respetando los derechos de autor y la privacidad de Soysuper y de los supermercados que compara. El autor no se hace responsable de las consecuencias que pueda tener el uso de este proyecto.

## Agradecimientos 🫶
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Quiero agradecer a Soysuper por ofrecer un servicio tan útil y práctico para los consumidores online, y por tener una página web tan bien estructurada y fácil de hacer web scraping. También quiero agradecer a Bing por ayudarme a redactar este README.md, y por ser un buscador tan inteligente y amigable. Y por último, quiero agradecer a ti, por leer este README.md y por interesarte por este proyecto. Espero que te haya gustado y que lo disfrutes. ¡Hasta pronto! 🙌

