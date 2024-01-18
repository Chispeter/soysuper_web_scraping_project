# Proyecto de Web Scraping de Soysuper
## ¿En qué consiste?
Este proyecto consiste en hacer web scraping de la página web Soysuper, un supermercado online que te permite comparar precios de diferentes productos en distintos supermercados.

## ¿Cuál es la motivación?
La motivación de este proyecto es explorar y manejar distintas librerías como forma de crecimiento profesional. Además, ¿a quién no le va a gustar extraer buenos datos?

## ¿Cuál es el objetivo?
El objetivo es extraer los datos de los productos (como el nombre, la marca o el precio) que aparecen en la web y guardarlos en archivos JSON.

## ¿Cómo funciona?
El proyecto usa la librería requests para hacer peticiones HTTP a la web de Soysuper, y la librería BeautifulSoup para parsear el HTML y extraer los datos de interés. El proyecto está dividido en varios módulos:
- **```project_functions.py```:** Tiene métodos para obtener las categorías, subcategorías y productos de la web, y para guardar los datos en archivos JSON. También, contiene funciones auxiliares para limpiar y formatear los datos, y para crear un directorio donde guardar los archivos JSON.
- **```main.py```:** Contiene el código principal que ejecuta el web scraping. Se puede modificar el número de categorías y subcategorías que se quieren obtener.

## ¿Cómo se utiza?
Para usar este proyecto, se necesita tener instalado python 3 y las librerías requests y BeautifulSoup. Los pasos son los siguientes:
1. Clonar o descargar este repositorio.
2. Crear y activar un entorno virtual (opcional). Se recomienda usar un entorno virtual para instalar las dependencias.
3. Instalar las dependencias con ```pip install -r requirements.txt```.
4. Ejecutar el archivo ```main.py``` con ```python main.py```.
5. Esperar a que termine el web scraping y revisar los archivos JSON generados en el directorio ```data```. En caso de detener la ejecución de ```main.py```, la próxima vez que se vuelva a ejecutar, el módulo ```project_functions.py``` comprobará los datos que han sido extraídos y continuará por la última categoría registrada en el directorio ```data```.

## Advertencia
Este proyecto tiene fines educativos y de entretenimiento. No se pretende violar los términos y condiciones de Soysuper, ni hacer un uso indebido de sus datos. Se recomienda hacer un uso responsable y moderado de este proyecto, respetando los derechos de autor y la privacidad de Soysuper y de los supermercados que compara. El autor no se hace responsable de las consecuencias que pueda tener el uso de este proyecto.

## Agradecimientos
Quiero agradecer a Soysuper por ofrecer un servicio tan útil y práctico para los consumidores online, y por tener una web tan bien estructurada y fácil de hacer web scraping. También quiero agradecer a Bing por ayudarme a redactar este readme.md, y por ser un buscador tan inteligente y amigable. Y por último, quiero agradecer a ti, por leer este readme.md y por interesarte por este proyecto. Espero que te haya gustado y que lo disfrutes. ¡Hasta pronto!


<!--
soysuper.py: contiene la clase Soysuper, que es la encargada de hacer el web scraping. Tiene métodos para obtener las categorías, subcategorías y productos de la web, y para guardar los datos en archivos JSON.
utils.py: contiene funciones auxiliares para limpiar y formatear los datos, y para crear un directorio donde guardar los archivos JSON.
main.py: contiene el código principal que ejecuta el web scraping. Se puede modificar el número de categorías y subcategorías que se quieren obtener, y el tiempo de espera entre cada petición
-->
