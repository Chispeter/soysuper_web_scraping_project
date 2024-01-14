# Importar las bibliotecas
import time
from project_functions import get_list_of_dictionaries, write_json


start_time = time.time()

# Extraer la información de la página web y guardarla en una lista de diccionarios
soysuper_list = get_list_of_dictionaries()

# Guardar toda la información obtenida en un archivo JSON
write_json(input=soysuper_list)

end_time = time.time()
print(f"Tiempo de ejecución: {(end_time-start_time)/60} minutos")
