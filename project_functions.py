### LIBRARIES
import json
import requests
import os
from bs4 import BeautifulSoup

### FUNCTIONS
## Función para obtener la sopa principal del nombre de ruta introducido
def get_main_soup(
    hostname: str = "https://soysuper.com",
    pathname: str = "",
    parser: str = "html.parser",
) -> BeautifulSoup:

    # Control de excepciones
    try:
        # Enviar una petición GET
        response = requests.get(url=hostname + pathname)

        # Comprobar el estado de la respuesta
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup con el contenido de la respuesta
            main_soup = BeautifulSoup(markup=response.content, features=parser)

        else:
            # Mostrar un mensaje de error si la respuesta no es exitosa
            print(
                f"Error en la función get_main_soup(). No se puede acceder a la página debido a que el código de estado de la respuesta HTTP es {str(response.status_code)}"
            )

        return main_soup

    except:
        # Mostrar un mensaje de error si el código anterior no se ejecuta por completo
        print(
            "Error en la función get_main_soup(). No se puede acceder a la página web debido a un error tipográfico"
        )


## Función para obtener los diccionarios con los datos de la página web (función principal)
def get_dictionaries(
    pathname: str = "",
    actual_list: list = [],
    actual_dictionary: dict = {},
    init: bool = False,
) -> list:

    # Obtener la sopa principal del nombre de ruta introducido
    main_soup = get_main_soup(pathname=pathname)

    # Obtener la sopa específica para cada categoría
    categories_soup_array = get_soup_array(
        main_soup=main_soup, extract_mode="categories", init=init
    )

    # Preparar la búsqueda de los datos para cada categoría
    for obj in categories_soup_array:
        # Buscar el elemento <a> que contiene la información de la categoría
        category = obj.find("a")

        # Extraer los datos de las categorías, excepto la última, que no tendrá más categorías posteriores
        if category != (-1):
            extract_categories(actual_list=actual_list, soup_category=category)

        # Extraer los datos de los productos en cada categoría final (la última contendrá los datos de los productos)
        else:
            # Obtener el array de la sopa para las categorías (por defecto)
            extract_products(
                actual_dictionary=actual_dictionary,
                main_soup=main_soup,
                pathname=pathname,
            )

    return actual_list


## Función para obtener el array de la sopa introducida
def get_soup_array(
    main_soup: BeautifulSoup,
    extract_mode: str = "categories" or "products" or "supermarkets",
    init: bool = False,
) -> any:

    # Extraer los datos de la categorías
    if extract_mode == "categories":
        # Control de excepciones
        try:
            # Buscar los elementos que contienen las categorías de los productos
            product_nav = main_soup.find_all("section", class_="product-nav")[1]
            categories_section = product_nav.find("div", class_="hidden-t")

            # Arreglar un problema ocasional relacionado con la estructura del código HTML
            if (categories_section.find("h4") is None) and (init is False):
                soup_array = [" "]

            else:
                all_categories = categories_section.find("ul")
                soup_array = all_categories.find_all("li")

        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print(
                "Error en la función get_soup.array(). No se puede realizar el web scraping de categorías a través de: section(class=product-nav) -> ul -> li"
            )

    # Extraer los datos de los productos de cada categoría final
    elif extract_mode == "products":
        try:
            # Encontrar la sección donde se encuentran los productos
            products_section = main_soup.find("section", id="main")

            # Obtener los datos de todos los productos en cada página
            products_list = products_section.find(
                "ul", class_="basiclist productlist grid clearfix"
            )
            soup_array = products_list.find_all(
                "li", itemtype="http://schema.org/Product"
            )

        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print(
                "Error en la función get_soup_array(). No se puede realizar el web scraping de productos a través de: section(class=main) -> ul(class=basiclist productlist grid clearfix) -> li(itemtype=http://schema.org/Product)"
            )

    # Extraer los datos de los supermercados de cada producto
    elif extract_mode == "supermarkets":
        try:
            # Obtener los datos de todos los supermercados que incluyen un producto
            soup_array = main_soup.find("section", class_="superstable")

        except:
            # Mostrar un mensaje de error si no se pueden extraer los datos de la web según el procedimiento anterior
            print(
                "Error en la función get_soup_array(). No se puede realizar el web scraping de supermercados a través de: section(class=superstable) -> tr"
            )

    return soup_array


## Función para registrar los datos de las categorías en el diccionario
def extract_categories(actual_list: list, soup_category: any):

    # Extraer el nombre de la categoría, el nombre de la ruta y el número de productos; y guardarlos en un diccionario
    actual_list.append(
        {
            "nombre_de_categoría": soup_category["title"].strip(),
            "nombre_de_ruta": soup_category["href"].replace("#products", "").strip(),
            "numero_de_productos": soup_category.find(
                "span", class_="number"
            ).text.strip(),
            "subcategorías": [],
        }
    )

    # Realizar el web scraping de las categorías aguas abajo
    get_dictionaries(
        pathname=actual_list[-1]["nombre_de_ruta"],
        actual_list=actual_list[-1]["subcategorías"],
        actual_dictionary=actual_list[-1],
    )

    # Mostrar mensaje de éxito
    print(f"Categoría {actual_list[-1]['nombre_de_categoría']} extraída con éxito!")


## Función para registrar los datos de los productos de una categoría para la primera página
def extract_products(actual_dictionary: dict, main_soup: any, pathname: str):

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

    # Obtener la sopa específica para los productos
    products_soup_array = get_soup_array(main_soup=main_soup, extract_mode="products")

    # Registrar en el diccionario todos los productos de la primera página (siempre va a haber una primera página)
    extract_products_from_page(
        products_soup_array=products_soup_array, actual_dictionary=actual_dictionary
    )

    # Registrar en el diccionario todos los productos del resto de páginas (si existen)
    if total_number_of_pages != "1":
        for number_of_page in range(2, int(total_number_of_pages) + 1):
            # Extraer la sopa principal en cada página
            new_soup = get_main_soup(
                pathname=pathname + "?page=" + str(number_of_page) + "#products"
            )

            # Extraer la sopa específica para los productos
            new_soup_array = get_soup_array(main_soup=new_soup, extract_mode="products")

            # Extraer
            extract_products_from_page(
                products_soup_array=new_soup_array, actual_dictionary=actual_dictionary
            )

    print(
        f"Subcategoría {actual_dictionary['nombre_de_categoría']} extraída con éxito!"
    )


## Función para registrar los datos de todos los productos por cada página de productos
def extract_products_from_page(products_soup_array: any, actual_dictionary: dict):

    # Obtener los datos de los productos en cada página
    for product in products_soup_array:
        # Extraer una parte de la sopa en la que se va a encontrar ciertos valores
        main_info = product.find("a", class_="btn btn-primary newproduct btn-block")

        # Extraer el id del producto
        product_id = main_info["data-product_id"].strip()
        if len(product_id) == 0:
            product_id = None

        # Extraer el nombre del producto
        product_name = main_info["data-name"].strip()
        if len(product_name) == 0:
            product_name = None

        # Extraer la marca del producto
        try:
            product_brand = main_info["data-brand"].strip()
            if len(product_brand) == 0:
                product_brand = None

        except:
            try:
                product_brand = product.find("a", class_="brand").text.strip()
            except:
                product_brand = None

        # Extraer la variante del producto
        product_variant = main_info["data-variant"].strip()
        if len(product_variant) == 0:
            product_variant = None

        # Extraer el nombre de la ruta del producto
        product_pathname = product.find("a")["href"].strip()
        if len(product_pathname) == 0:
            product_pathname = None

        # Extraer el nombre de la ruta de la imagen del producto
        try:
            product_image_url = product.find("img")["src"].strip()
        except:
            product_image_url = None

        # Extraer el precio medio del producto (en relación a los supermercados en los que aparece el producto)
        try:
            product_average_price = product.find("meta", itemprop="price")[
                "content"
            ].strip()
        except:
            product_average_price = None

        # Extraer la moneda (divisa) del precio del producto
        try:
            product_price_currency = product.find("meta", itemprop="priceCurrency")[
                "content"
            ].strip()
        except:
            product_price_currency = None

        # Extraer el precio del producto por variante del producto
        try:
            product_price_per_variant = product.find(
                "span", class_="price"
            ).text.strip()
        except:
            product_price_per_variant = None

        # Extraer el precio del producto por variante estándar (precio unitario)
        try:
            product_unitprice = product.find("span", class_="unitprice").text.strip()
        except:
            product_unitprice = None

        # Registrar los datos del producto en el diccionario
        actual_dictionary["productos"].append(
            {
                "product_id": product_id,
                "product_name": product_name,
                "product_brand": product_brand,
                "product_variant": product_variant,
                "product_pathname": product_pathname,
                "product_image_url": product_image_url,
                "product_average_price": product_average_price,
                "product_price_currency": product_price_currency,
                "product_price_per_variant": product_price_per_variant,
                "product_unitprice": product_unitprice,
            }
        )

        # Registrar los supermercados del producto en cada página
        extract_supermarkets_from_product_page(
            actual_dictionary=actual_dictionary["productos"][-1]
        )


# Función para registrar los datos de los supermercados de un producto en cada página
def extract_supermarkets_from_product_page(actual_dictionary: dict):

    # Extraer la sopa principal de los supermercados
    supermarket_main_soup = get_main_soup(
        pathname=actual_dictionary["product_pathname"]
    )

    # Extraer la sopa específica de los supermercados del producto
    supermarket_soup_array = get_soup_array(
        main_soup=supermarket_main_soup, extract_mode="supermarkets"
    )

    # Inicializar clave donde se van a guardar los datos de los supermercados
    actual_dictionary["product_in_supermarkets"] = []

    # Controlar el caso de que algún producto, por alguna razón, no aparezca en ningún supermercado
    try:
        # Extraer la sopa donde se encuentran los datos de los supermercados
        supermarket_list = supermarket_soup_array.find_all("tr")

        # Registrar los datos de los supermercados en el diccionario
        for supermarket in supermarket_list:
            # Extraer el nombre del supermercado en el que aparece el producto
            supermarket_name = supermarket.find("i")["title"].strip()

            # Extraer el precio del producto en ese supermercado
            supermarket_product_price = supermarket.find("td").text.strip()

            # Registrar los datos en el diccionario
            actual_dictionary["product_in_supermarkets"].append(
                {
                    "supermarket_name": supermarket_name,
                    "supermarket_product_price": supermarket_product_price,
                }
            )

    except:
        actual_dictionary["product_in_supermarkets"].append(None)


## Función para guardar toda la información obtenida en un archivo JSON
def write_json(input: any, indent: int = 3):

    # Obtener la ruta del directorio actual
    current_dir = os.path.dirname(__file__)

    # Guardar la ruta de la carpeta donde van a almacenarse los datos
    data_dir = os.path.join(current_dir, "data")

    # Crear la carpeta de los datos (si existe)
    if not os.path.exists(data_dir):
        os.mkdir("data")

    # Unir la ruta con el nombre de la carpeta y el archivo
    file_path = os.path.join(
        data_dir,
        input["nombre_de_categoría"].lower().replace(" ", "_").replace(",", "")
        + ".json",
    )

    # Escribir los datos en un archivo JSON
    with open(file_path, "w", encoding="utf-8") as file:

        # Usar la función dump para convertir el diccionario en JSON y escribirlo en el archivo
        json.dump(obj=input, fp=file, ensure_ascii=False, indent=indent)

    # Cerrar el archivo
    file.close()
