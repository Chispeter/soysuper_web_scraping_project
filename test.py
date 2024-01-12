import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

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
            


# Obtener la sopa de la url introducida
soup = get_bs_soysuper(pathname="/c/solidaridad")
# Obtener el array de la sopa
main_section = soup.find("section", id="main")
# Obtener el número total de páginas
pager_section = main_section.find("section", id="pager")
if pager_section is None:
    total_number_of_pages = "1"
else:
    total_number_of_pages = pager_section.find_all("a")[-2].text.strip()
for page in range(1, int(total_number_of_pages)+1):
    # Obtener los datos de todos los productos en una página
    product_list = main_section.find("ul", class_="basiclist productlist grid clearfix")
    all_products = product_list.find_all("li")
    
    #Obtener los datos de cada producto en cada página
    for product in all_products:
        main_info = product.find("a", class_="btn btn-primary newproduct btn-block")
        # Extaer el id del producto
        product_id = main_info["data-product_id"].strip()
        print('product_id:', product_id)
        # Extraer el nombre de la ruta del producto
        product_pathname = product.find("a")["href"]
        print('product_pathname:', product_pathname)
        # Extraer la marca del producto
        product_brand = main_info["data-brand"].strip()
        if len(product_brand) == 0:
            product_brand = None
        print('product_brand:', product_brand)
        # Extraer el nombre del producto
        product_name = main_info["data-name"].strip()
        print('product_name:', product_name)
        # Extraer la variante del producto
        product_variant = main_info["data-variant"].strip()
        if len(product_variant) == 0:
            product_variant = None
        print('product_variant:', product_variant)
        # Extraer el nombre de la ruta de la imagen del producto
        product_image_url = product.find("img")["src"].strip()
        print('product_image_url:', product_image_url)

# Falta ver otros productos que no sean de alimentación
# falta entrar a las páginas de cada producto
