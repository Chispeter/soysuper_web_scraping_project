# LIBRARIES
import time
import os
from project_functions import get_dictionaries, create_directory, write_json


start_time = time.time()

# Crear el directorio inicial donde van a alojarse los datos
current_dir = create_directory()

# Extraer la información de la página web y guardarla en una lista de diccionarios
soysuper_list = get_dictionaries(current_dir=current_dir)




# Guardar toda la información obtenida en un archivo JSON
for category in soysuper_list:
    write_json(input=category)

end_time = time.time()

print(f"Tiempo de ejecución: {(end_time-start_time) // 60} minutos y {(end_time-start_time) % 60} segundos")
