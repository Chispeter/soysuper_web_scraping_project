else:
    categories_list["subcategorías"].append({"nombre_de_subcategoría": category["title"],
                                                        "nombre_de_ruta": category["href"].replace("#products", ""),
                                                        "numero_de_productos": category.find("span", class_="number").text,
                                                        "subcategorías": []})

    # Extraccion de subcategorías (primera)
    actual_category = categories_list[index]
    new_url = hostname + actual_category["nombre_de_ruta"]
    categories_list = extract_categories(url=new_url, categories_list=actual_category)