import json

# Esta función se encarga de obtener los parámetros del proyecto de un archivo de configuración en formato JSON
def get_configuration():
    
    with open("config.json", "r") as file:
        data = json.load(file)
    
    return [data["hostname"], data["data_dirname"]]
