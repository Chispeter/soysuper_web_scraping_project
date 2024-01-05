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

            # Preparar la búsqueda de los datos
            if len(categories_list) == 0:
                for cat in li:
                    # Buscar el elemento <a> que contiene la información de la categoría
                    category = cat.find("a")
                    # Extraer el title, number y path de la categoría y guardar en los diccionarios y las listas
                    categories_list[category["title"]] = {}
                    categories_list[category["title"]]["nombre_de_categoría"] = category["title"]
                    categories_list[category["title"]]["nombre_de_ruta"] = category["href"]
                    categories_list[category["title"]]["numero_de_productos"] = category.find("span", class_="number").text
            else:
                for value in categories_list.values():
                    new_url = url + value['nombre_de_ruta']
                    response = requests.get(new_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, "html.parser")
                        try:
                            section = soup.find_all("section", class_="product-nav")[1]
                            ul = section.find_all("ul")[0]
                            li = ul.find_all("li")

                            value["subcategorías"] = []

                            # Subcategoría inicial
                            for subcat in li:
                                subcategory = subcat.find("a")
                                value["subcategorías"].append({"nombre_de_subcategoría": subcategory["title"],
                                                            "nombre_de_ruta": subcategory["href"],
                                                            "numero_de_productos": subcategory.find("span", class_="number").text})

                            # Subcategorías posteriores
                            #for subcat in value["subcategorías"]:
                                


                        except:
                            print(f"Error al realizar el web scraping de la categoría {value['nombre_de_categoría']} (no existen más subcategorías)")
                    else:
                        print(f"Error al acceder al enlace de la categoría {value['nombre_de_categoría']}")

        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print("Error al realizar el web scraping (la estructura del código HTML ha cambiado)")

    else:
        # Mostrar un mensaje de error si la respuesta no es exitosa
        print("Error al acceder a la página web")

# Definir la URL de la página web
url = "https://soysuper.com"

# Extraer categorías y subcategorías
extract_categories(url)


