import json
import os

# Esta función se encarga de obtener los parámetros del proyecto de un archivo de configuración en formato JSON
def get_configuration():
    
    project_dir = os.path.dirname(__file__)
    
    config_dir = os.path.join(project_dir, "config.json")
    
    with open(config_dir, "r") as file:
        data = json.load(file)
    
    file.close()
    
    return [data["hostname"], data["data_dirname"]]
