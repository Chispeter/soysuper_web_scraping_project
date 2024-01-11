## LIBRARIES
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

## FUNCTIONS
# Función para obtener la sopa del nombre de ruta introducido
def get_bs_soysuper(hostname: str = "https://soysuper.com", pathname: str = "", parser: str = "html.parser") -> BeautifulSoup:
    # Control de excepciones
    try:
        # Enviar la petición GET
        response = requests.get(url=hostname+pathname)
        # Comprobar el estado de la respuesta
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup con el contenido de la respuesta
            soup = BeautifulSoup(markup=response.content, features=parser)
        else:
            # Mostrar un mensaje de error si la respuesta no es exitosa
            print(f"ConnectionError: No se puede acceder a la página debido a que el código de estado de la respuesta HTTP es {str(response.status_code)}")
        return soup
    except:
        # Mostrar un mensaje de error si el código anterior no se ejecuta
            print("ConnectionError: No se puede acceder a la página web debido a un error tipográfico")

# Función para obtener la lista de diccionarios con los datos de la página web "soysuper" (función principal)
def get_list_soysuper(url: str = "", categories_list: list = [], categories_dict: dict = {}) -> list:
    # Obtener la sopa de la url introducida
    soup = get_bs_soysuper(pathname=url)
    
    # Obtener el array de la sopa
    soup_array = get_soup_array(soup=soup, extract_mode="categories")

    # Preparar la búsqueda de los datos por categorias y subcategorías
    for index, cat in enumerate(soup_array):
        # Buscar el elemento <a> que contiene la información de la categoría
        category = cat.find("a")
        # Extraer las categorías y subcategorías, excepto la última (que no podrá ser iterada más veces -> NoneType)
        if category is not None:
            extract_categories(categories_list=categories_list, category=category)
        # Extraer los productos en cada categoría final
        else:
            extract_products(categories_dict=categories_dict, category=category)
    
    return categories_list

# Función para obtener el array de la sopa introducida
def get_soup_array(soup: BeautifulSoup, extract_mode: str = "categories" or "products") -> any:
    if extract_mode == "categories":
        try:
            # Buscar los elementos que contienen las categorías de los productos
            section = soup.find_all("section", class_="product-nav")[1]
            ul = section.find_all("ul")[0]
            soup_array = ul.find_all("li")
        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print("Error al realizar el web scraping a través de section (class=product-nav) -> ul -> li")
    elif extract_mode == "products":
        try:
            # Buscar los elementos que contienen los datos de los productos
            soup_array = soup.find_all("ul", class_="basiclist productlist grid clearfix")
        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print("Error al realizar el web scraping a través de section -> ul -> li")
    else:
        soup_array = []
    return soup_array
    
# Función para extraer los datos de las categorías
def extract_categories(categories_list: list, category: any):
    try:
        # Extraer el nombre de la categoría, el nombre de la ruta (remodelado, ya que se añade #products y no queremos que pase esto) y el número de productos; y guardarlos como un diccionario en cada elemento de la lista
        categories_list.append({"nombre_de_categoría": category["title"],
                                "nombre_de_ruta": category["href"].replace("#products", ""),
                                "numero_de_productos": category.find("span", class_="number").text,
                                "subcategorías": []})
        # Activar para hacer scraping de todas las categorías
        #extract_categories(categories_list=categories_list[index]["subcategorías"], url=categories_list[index]["nombre_de_ruta"], categories_dict=categories_list[index])
    except:
        # Mostrar un mensaje de error si no se pueden extraer los datos de las categorías
        print(f"Error al realizar el web scraping de los datos de la categoría {category["title"]}")

# Función para extraer los datos de los productos
def extract_products(categories_dict: dict, category: any):
    try:
        # Cambiar la clave "subcategorías" por "productos"
        categories_dict["productos"] = []
        del categories_dict["subcategorías"]
    except:
        # Mostrar un mensaje de error si no se pueden extraer los datos de los productos de la categoría
        print(f"Error al realizar el web scraping de los datos de los productos de la categoría {category["title"]}")


## MAIN CODE
start_time = time.time()

# Insertar código

end_time = time.time()
print(f"Tiempo de ejecución: {(end_time-start_time)/60} minutos")