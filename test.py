
from project_functions import get_main_soup
            


# Obtener la sopa de la url introducida
soup = get_main_soup(pathname="/c/pasta-arroz-y-legumbres/pasta/espaguetis")
# Encontrar la sección donde se encuentran los productos
main_section = soup.find("section", id="main")
# Obtener el número total de páginas
pager_section = main_section.find("section", id="pager")

if pager_section is None:
    total_number_of_pages = "1"
else:
    total_number_of_pages = pager_section.find_all("a")[-2].text.strip()
    # Obtener los datos de todos los productos por cada página
    for page in range(2, int(total_number_of_pages)+1):
        # Obtener la nueva sopa en cada página
        print(page)
        soup = get_main_soup(pathname="/c/pasta-arroz-y-legumbres/pasta/espaguetis"+"?page="+str(page))
        # Encontrar la sección donde se encuentran los productos
        main_section = soup.find("section", id="main")
        # Obtener el número total de páginas
        pager_section = soup.find("section", id="pager")
        
        # Obtener los datos de todos los productos en cada página
        product_list = main_section.find("ul", class_="basiclist productlist grid clearfix")
        all_products = product_list.find_all("li", itemtype="http://schema.org/Product")
        #Obtener los datos de cada producto en cada página
        for product in all_products:
            main_info = product.find("a", class_="btn btn-primary newproduct btn-block")
            # Extraer el id del producto
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
            # Extraer el precio del producto
            product_price = product.find("span", class_="price").text.strip()
            print('product_price:', product_price)
            # Extraer el precio unitario del producto
            product_unitprice = product.find("span", class_="unitprice").text.strip()
            print('product_unitprice:', product_unitprice)

# Falta ver otros productos que no sean de alimentación
# falta entrar a las páginas de cada producto
# Poner todo en funcion de un diccionario mejor para tener menos parámetros
