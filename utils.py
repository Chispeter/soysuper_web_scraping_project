import json
import os


## Esta función se utiliza para crear una serie de directorios donde se van a guardar los datos
def create_directory(data_dirname: str, current_dir: str = "", current_category_name: str = "") -> str:

    # Obtener la ruta del directorio donde se ubica este archivo de python
    project_dir = os.path.dirname(__file__)
    
    if len(current_category_name) == 0:
        # Guardar la ruta de la carpeta donde van a almacenarse todos los datos
        current_dir = os.path.join(project_dir, data_dirname)
        
    else:
        # Guardar la ruta de la carpeta donde van a almacenarse los datos de las categorías
        current_dir = os.path.join(current_dir, get_cleaned_str(current_category_name))
    
    # Crear la carpeta de los datos (si existe)
    if not os.path.exists(current_dir):
        os.mkdir(current_dir)
    
    return current_dir


## Esta función se utiliza para guardar toda la información obtenida en un archivo JSON
def write_json(data_input: any, current_dir: str, data_dirname: str, indent: int = 3) -> str:
    
    # Obtener la ruta del directorio donde se ubica este archivo de python
    project_dir = os.path.dirname(__file__)
    
    # Unir la ruta con el nombre de la carpeta y el archivo
    file_path = os.path.join(project_dir, data_dirname, current_dir, get_cleaned_str(data_input['nombre_de_categoría']) + ".json")
    
    # Escribir los datos en un archivo JSON
    with open(file_path, "w", encoding="utf-8") as file:
        
        # Usar la función dump para convertir el diccionario en JSON y escribirlo en el archivo
        json.dump(obj=data_input, fp=file, ensure_ascii=False, indent=indent)

    # Cerrar el archivo
    file.close()
    

## Esta función se utiliza para limpiar un string y eliminar caracteres que generan problemas
def get_cleaned_str(str_input: str) -> str:
    return str_input.replace(" \ ", " - ").replace(" / ", " - ")


## Esta función se utiliza para comprobar si ya se habían extraído los datos de los productos anteriormente
def is_data_extracted(current_dir: str, current_category_name: str) -> bool:
    
    # Limpiar el nombre de la categoría
    cleaned_current_category_name = get_cleaned_str(current_category_name)
    
    # Obtener la ruta absoluta a comprobar
    abs_path_to_check = os.path.join(current_dir, cleaned_current_category_name+".json")
    
    return os.path.exists(abs_path_to_check)
