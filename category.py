# Importar las bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_categories(url: str, categories_list=[]):
    # Hacer una solicitud HTTP a la página web
    response = requests.get(url)

    # Comprobar el estado de la respuesta
    if response.status_code == 200:
        # Crear un objeto BeautifulSoup con el contenido de la respuesta
        soup = BeautifulSoup(response.content, "html.parser")

        try:
            # Buscar los elementos que contienen las categorías de los productos
            section = soup.find_all("section", class_="product-nav")[1]
            ul = section.find_all("ul")[0]
            li = ul.find_all("li")

            if len(categories_list) == 0:

                # Preparar la búsqueda de los datos por categoria
                for cat in li:
                    # Buscar el elemento <a> que contiene la información de la categoría
                    category = cat.find("a")
                    # Extraer el title, number y path de la categoría y guardar en cada elemento de la lista de diccionarios
                    categories_list.append({"nombre_de_categoría": category["title"],
                                            "nombre_de_ruta": category["href"],
                                            "numero_de_productos": category.find("span", class_="number").text,
                                            "subcategorías": []})
                    # Extraccion de subcategorías (primera)
                    new_url = hostname + categories_list['nombre_de_ruta']
                    extract_categories(url=new_url, categories_list=categories_list)

            else:
                for subcat in li:
                    subcategory = subcat.find("a")
                    categories_list["subcategorías"].append({"nombre_de_subcategoría": subcategory["title"],
                                                             "nombre_de_ruta": subcategory["href"],
                                                             "numero_de_productos": subcategory.find("span", class_="number").text,
                                                             "subcategorías": []})
                    # Extracción de subcategorías (de la segunda hasta el final)
                    new_url = hostname + categories_list['nombre_de_ruta']
                    extract_categories(url=new_url, categories_list=categories_list)
        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print("Error al realizar el web scraping (la estructura del código HTML ha cambiado)")

    else:
        # Mostrar un mensaje de error si la respuesta no es exitosa
        print("Error al acceder a la página web")


# Definir el hostname de la página web
hostname = "https://soysuper.com"

# Extraer categorías
extract_categories(url=hostname)