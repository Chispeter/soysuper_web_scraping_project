test = {'Aperitivos': {'nombre_de_categoria': 'Aperitivos', 'nombre_de_ruta': '/c/aperitivos', 'numero_de_productos': '6.377', 'subcategorias': [{'nombre_de_subcategoria': 'Snacks', 'nombre_de_ruta': '/c/aperitivos/snacks#products', 'numero_de_productos': '1.270'}, {'nombre_de_subcategoria': 'Pepito', 'nombre_de_ruta': '/pepito', 'numero_de_productos': '1'}]}}

for value in test.values():
    for dict in value['subcategorias']:
        print(dict)

print(len({'1': '3'}))