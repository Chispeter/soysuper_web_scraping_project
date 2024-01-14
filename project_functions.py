### LIBRARIES
import json
import requests
from bs4 import BeautifulSoup

### FUNCTIONS
## Función para obtener la sopa del nombre de ruta introducido
def get_main_soup(hostname: str = "https://soysuper.com", pathname: str = "", parser: str = "html.parser") -> BeautifulSoup:
    # Control de excepciones
    try:
        # Enviar la petición GET
        response = requests.get(url=hostname+pathname)
        # Comprobar el estado de la respuesta
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup con el contenido de la respuesta
            main_soup = BeautifulSoup(markup=response.content, features=parser)
        else:
            # Mostrar un mensaje de error si la respuesta no es exitosa
            print(f"Error en la función get_main_soup(). No se puede acceder a la página debido a que el código de estado de la respuesta HTTP es {str(response.status_code)}")
        return main_soup
    except:
        # Mostrar un mensaje de error si el código anterior no se ejecuta
            print("Error en la función get_main_soup(). No se puede acceder a la página web debido a un error tipográfico")

## Función para obtener la lista de diccionarios (json) con los datos de la página web "soysuper" (función principal)
def get_list_of_dictionaries(pathname: str = "", actual_list: list = [], actual_dictionary: dict = {}) -> list:
    try:
        # Obtener la sopa de la url introducida
        main_soup = get_main_soup(pathname=pathname)
        
        # Obtener el array de la sopa para las categorías (por defecto)
        categories_soup_array = get_soup_array(main_soup=main_soup, extract_mode="categories")

        # Preparar la búsqueda de los datos por categorías y subcategorías
        for index, obj in enumerate(categories_soup_array):
            # Buscar el elemento <a> que contiene la información de la categoría
            category = obj.find("a")
            # Extraer las categorías y subcategorías, excepto la última (que no podrá ser iterada más veces -> NoneType)
            if category is not None:
                extract_categories(actual_list=actual_list, soup_category=category, index=index)
            # Extraer los datos de los productos en cada categoría final
            else:
                # Obtener el array de la sopa para las categorías (por defecto)
                extract_products(actual_dictionary=actual_dictionary, main_soup=main_soup, pathname=pathname)

    except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print("Error en la función get_list_of_dictionaries(). No se puede registrar la categoría o los productos")

    return actual_list  

## Función para obtener el array de la sopa introducida
def get_soup_array(main_soup: BeautifulSoup, extract_mode: str = "categories" or "products" or "supermarkets") -> any:
    if extract_mode == "categories":
        # Control de excepciones
        try:
            # Buscar los elementos que contienen las categorías de los productos
            categories_section = main_soup.find_all("section", class_="product-nav")[1]
            ul = categories_section.find_all("ul")[0]
            soup_array = ul.find_all("li")
         
        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print("Error en la función get_soup.array(). No se puede realizar el web scraping de categorías a través de section(class=product-nav) -> ul -> li")

    elif extract_mode == "products":
        try:
            # Encontrar la sección donde se encuentran los productos
            products_section = main_soup.find("section", id="main")
            # Obtener los datos de todos los productos en cada página
            products_list = products_section.find("ul", class_="basiclist productlist grid clearfix")
            soup_array = products_list.find_all("li", itemtype="http://schema.org/Product")

        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print("Error en la función get_soup_array(). No se puede realizar el web scraping de productos a través de section(class=main) -> ul(class=basiclist productlist grid clearfix) -> li(itemtype=http://schema.org/Product)")

    elif extract_mode == "supermarkets":
        try:
            # Obtener los datos de todos los supermercados que incluyen un producto
            supermarkets_section = main_soup.find("section", class_="superstable")
            soup_array = supermarkets_section.find_all("tr")

        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print("Error en la función get_soup_array(). No se puede realizar el web scraping de supermercados a través de ul (class=basiclist productlist grid clearfix)")
    else:
        soup_array = []
    return soup_array

## Función para extraer los datos de las categorías
def extract_categories(actual_list: list, soup_category: any, index: int):
    # Control de excepciones
    try:
        # Extraer el nombre de la categoría, el nombre de la ruta y el número de productos; y guardarlos como un diccionario en cada elemento de la lista
        actual_list.append({"nombre_de_categoría": soup_category["title"].strip(),
                            "nombre_de_ruta": soup_category["href"].replace("#products", "").strip(),
                            "numero_de_productos": soup_category.find("span", class_="number").text.strip(),
                            "subcategorías": []})
        # Activar el web scraping de todas las categorías posteriores (recursividad)
        get_list_of_dictionaries(pathname=actual_list[index]["nombre_de_ruta"], actual_list=actual_list[index]["subcategorías"], actual_dictionary=actual_list[index])
    
    except:
        # Mostrar un mensaje de error si no se pueden extraer los datos de las categorías
        print(f"Error en la función extract_categories(). No se puede realizar el web scraping de los datos de la categoría {soup_category["title"].strip()}")

## Función para extraer los datos de todos los productos de una categoría para la primera página 
def extract_products(actual_dictionary: dict, main_soup: any, pathname: str):
    # Control de excepciones
    try:
        # Cambiar la clave "subcategorías" por "productos"
        actual_dictionary["productos"] = []
        del actual_dictionary["subcategorías"]
        # Encontrar la sección donde se encuentran los productos
        main_section = main_soup.find("section", id="main")
        # Definir el número total de páginas
        pager_section = main_section.find("section", id="pager")
        if pager_section is None:
            total_number_of_pages = "1"
        else:
            total_number_of_pages = pager_section.find_all("a")[-2].text.strip()
        # Obtener el array de la sopa para los productos
        products_soup_array = get_soup_array(main_soup=main_soup, extract_mode="products")
        
        # Registrar en el diccionario todos los productos de la primera página (siempre va a haber una primera página)
        extract_products_from_page(products_soup_array=products_soup_array, actual_dictionary=actual_dictionary)
        
        # Registrar en el diccionario todos los productos del resto de páginas (si existen)
        if total_number_of_pages != "1":
            for number_of_page in range(2, int(total_number_of_pages)+1):
                # Obtener la nueva sopa en cada página
                new_soup = get_main_soup(pathname=pathname+"?page="+str(number_of_page)+"#products")
                new_soup_array = get_soup_array(main_soup=new_soup, extract_mode="products")
                extract_products_from_page(products_soup_array=new_soup_array, actual_dictionary=actual_dictionary)

    except:
        # Mostrar un mensaje de error si no se pueden extraer los datos de los productos de la categoría
        print(f"Error en la función extract_products(). No se puede realizar el web scraping de los datos de los productos de la categoría {actual_dictionary["nombre_de_categoría"]}")


## Función para extraer los datos de todos los productos por cada página de productos
def extract_products_from_page(products_soup_array: any, actual_dictionary: dict):
    # Control de excepciones
    try:
        # Obtener los datos de cada producto en una página
        for product in products_soup_array:
            main_info = product.find("a", class_="btn btn-primary newproduct btn-block")
            # Extraer el id del producto
            product_id = main_info["data-product_id"].strip()
            # Extraer el nombre del producto
            product_name = main_info["data-name"].strip()
            # Extraer la marca del producto
            product_brand = main_info["data-brand"].strip()
            if len(product_brand) == 0:
                product_brand = None
            # Extraer la variante del producto
            product_variant = main_info["data-variant"].strip()
            if len(product_variant) == 0:
                product_variant = None
            # Extraer el nombre de la ruta del producto
            product_pathname = product.find("a")["href"].strip()
            # Extraer el nombre de la ruta de la imagen del producto
            try:
                product_image_url = product.find("img")["src"].strip()
            except:
                product_image_url = None
            # Extraer el precio medio del producto (en relación a los supermercados en los que aparece el producto)
            product_average_price = product.find("meta", itemprop="price")["content"].strip()
            # Extraer la moneda (divisa) del precio del producto
            product_price_currency = product.find("meta", itemprop="priceCurrency")["content"].strip()
            # Extraer el precio del producto por variante del producto
            product_price_per_variant = product.find("span", class_="price").text.strip()
            # Extraer el precio del producto por variante estándar (precio unitario)
            product_unitprice = product.find("span", class_="unitprice").text.strip()
            # Registrar los datos en el diccionario
            actual_dictionary["productos"].append({"product_id": product_id,
                                                    "product_name": product_name,
                                                    "product_brand": product_brand,
                                                    "product_variant": product_variant,
                                                    "product_pathname": product_pathname,
                                                    "product_image_url": product_image_url,
                                                    "product_average_price": product_average_price,
                                                    "product_price_currency": product_price_currency,
                                                    "product_price_per_variant": product_price_per_variant,
                                                    "product_unitprice": product_unitprice,
                                                    "product_in_supermarkets": []})
            extract_supermarkets_from_product_page(actual_dictionary=actual_dictionary["productos"][-1])
    except:
        # Mostrar un mensaje de error si no se pueden extraer los datos de los productos de cada página
        print(f"Error en la función extract_products_from_page(). No se puede realizar el web scraping de los datos del producto {product_name} de la categoría {actual_dictionary["nombre_de_categoría"]}")


def extract_supermarkets_from_product_page(actual_dictionary: dict):
    try:
        supermarket_main_soup = get_main_soup(pathname=actual_dictionary["product_pathname"])
        supermarket_soup_array = get_soup_array(main_soup=supermarket_main_soup, extract_mode="supermarkets")
        for supermarket in supermarket_soup_array:
            # Extraer el nombre del supermercado en el que aparece el producto
            supermarket_name = supermarket.find("i")["title"].strip()
            # Extraer el precio del producto en ese supermercado
            supermarket_product_price = supermarket.find("td").text.strip()
            # Registrar los datos en el diccionario
            actual_dictionary["product_in_supermarkets"].append({"supermarket_name": supermarket_name,
                                                                "supermarket_product_price": supermarket_product_price})

    except:
        # Mostrar un mensaje de error si no se pueden extraer los datos de los supermercados de cada producto
        print(f"Error en la función extract_supermarkets_from_product_page(). No se puede realizar el web scraping de los datos de los supemercados en los que aparece el producto {actual_dictionary["product_name"]} de la marca {actual_dictionary["product_brand"]}")

    
## Función para guardar toda la información obtenida en un archivo JSON
def write_json(input: any, filename: str = "soysuper_data", indent: int = 3):
    # Escribir los datos en un archivo JSON
    with open(filename+".json", "w", encoding="utf-8") as file:
        # Usar la función dump para convertir el diccionario en JSON y escribirlo en el archivo
        json.dump(obj=input, fp=file, ensure_ascii=False, indent=indent)
    # Cerrar el archivo
    file.close()