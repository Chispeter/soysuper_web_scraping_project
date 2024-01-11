# Importar las bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Función para obtener la sopa del nombre de ruta introducido
def get_bs_soysuper(hostname="https://soysuper.com", pathname="") -> BeautifulSoup:
    # Control de excepciones
    try:
        # Enviar la petición GET
        response = requests.get(url=hostname+pathname)
        # Comprobar el estado de la respuesta
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup con el contenido de la respuesta
            soup = BeautifulSoup(markup=response.content, features="html.parser")
        else:
            # Mostrar un mensaje de error si la respuesta no es exitosa
            print(f"ConnectionError: No se puede acceder a la página debido a que el código de estado de la respuesta HTTP es {str(response.status_code)}")
        return soup
    except:
        # Mostrar un mensaje de error si el código anterior no se ejecuta
            print("ConnectionError: No se puede acceder a la página web debido a un error tipográfico")

def extract_categories(categories_list, url="") -> list:
    # Obtener la sopa de la url introducida
    soup = get_bs_soysuper(pathname=url)
    try:
        # Buscar los elementos que contienen las categorías de los productos
        section = soup.find_all("section", class_="product-nav")[1]
        ul = section.find_all("ul")[0]
        li = ul.find_all("li")
    except:
        # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
        print("Error al realizar el web scraping")

    # Preparar la búsqueda de los datos por categorias y subcategorías
    for index, cat in enumerate(li):
        # Buscar el elemento <a> que contiene la información de la categoría
        category = cat.find("a")
        # Primera extracción de categorías
        if len(categories_list) == 0:
            try:
                # Extraer el nombre de la categoría, el nombre de la ruta (remodelado, ya que se añade #products y no queremos que pase esto) y el número de productos y guardarlos como un diccionario en cada elemento de la lista
                categories_list.append({"nombre_de_categoría": category["title"],
                                        "nombre_de_ruta": category["href"].replace("#products", ""),
                                        "numero_de_productos": category.find("span", class_="number").text,
                                        "subcategorías": []})

            except:
                # Mostrar un mensaje de error si no se pueden extraer los datos de las categorías principales
                print(f"Error al realizar el web scraping de las categoría principal {categories_list[index]['nombre_de_categoría']}")

        else:
            try:
                # Extraer el nombre de la subcategoría, el nombre de la ruta (remodelado, ya que se añade #products y no queremos que pase esto) y el número de productos y guardarlos como un diccionario en cada elemento de la lista
                categories_list["subcategorías"].append({"nombre_de_subcategoría": category["title"],
                                                        "nombre_de_ruta": category["href"].replace("#products", ""),
                                                        "numero_de_productos": category.find("span", class_="number").text,
                                                            "subcategorías": []})

            except:
                # Mostrar un mensaje de error si no se pueden más datos de las subcategorías
                print(f"Error al realizar el web scraping de la subcategoría {categories_list[index]['subcategorías']['nombre_de_subcategoría']}")

    return categories_list

# Primera extracción de categorías

first_categories_list = extract_categories()
for category in first_categories_list:
    first_subcategories_list = extract_categories(categories_list=category, url=category['nombre_de_ruta'])
    print(first_subcategories_list)
