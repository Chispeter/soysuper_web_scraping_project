# Proyecto de Web Scraping de Soysuper
## ¿En qué consiste?
Este proyecto consiste en hacer web scraping de la página web Soysuper, un supermercado online que te permite comparar precios de diferentes productos en distintos supermercados.

## ¿Cuál es la motivación?
La motivación de este proyecto es explorar y manejar distintas librerías como forma de crecimiento profesional. Además, ¿a quién no le va a gustar extraer buenos datos?

## ¿Cuál es el objetivo?
El objetivo es extraer los datos de los productos (como el nombre, la marca o el precio) que aparecen en la web y guardarlos en archivos JSON.

## ¿Cómo funciona?
El proyecto usa la librería requests para hacer peticiones HTTP a la web de Soysuper, y la librería BeautifulSoup para parsear el HTML y extraer los datos de interés. El proyecto está dividido en varios módulos:
- **soysuper.py:** Contiene la clase Soysuper, que es la encargada de hacer el web scraping. Tiene métodos para obtener las categorías, subcategorías y productos de la web, y para guardar los datos en archivos JSON. También, contiene funciones auxiliares para limpiar y formatear los datos, y para crear un directorio donde guardar los archivos JSON.
- **main.py:** Contiene el código principal que ejecuta el web scraping. Se puede modificar el número de categorías y subcategorías que se quieren obtener.
'''eee'''
```aaa```


<!--
soysuper.py: contiene la clase Soysuper, que es la encargada de hacer el web scraping. Tiene métodos para obtener las categorías, subcategorías y productos de la web, y para guardar los datos en archivos JSON.
utils.py: contiene funciones auxiliares para limpiar y formatear los datos, y para crear un directorio donde guardar los archivos JSON.
main.py: contiene el código principal que ejecuta el web scraping. Se puede modificar el número de categorías y subcategorías que se quieren obtener, y el tiempo de espera entre cada petición
-->
