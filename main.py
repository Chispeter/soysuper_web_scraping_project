# Importar las bibliotecas
import pandas as pd
import time
from project_functions import get_json

start_time = time.time()

get_json(pathname="/c/solidaridad")

end_time = time.time()
print(f"Tiempo de ejecución: {(end_time-start_time)/60} minutos")