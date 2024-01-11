# Importar las bibliotecas
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Función para obtener la sopa del nombre de ruta introducido
def get_bs_soysuper(hostname="https://soysuper.com", pathname="") -> BeautifulSoup:
    # Control de excepciones
    try:
        # Enviar la petición GET
        response = requests.get(url=hostname+pathname)
        # Comprobar el estado de la respuesta
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup con el contenido de la respuesta
            soup = BeautifulSoup(markup=response.content, features="html.parser")
        else:
            # Mostrar un mensaje de error si la respuesta no es exitosa
            print(f"ConnectionError: No se puede acceder a la página debido a que el código de estado de la respuesta HTTP es {str(response.status_code)}")
        return soup
    except:
        # Mostrar un mensaje de error si el código anterior no se ejecuta
            print("ConnectionError: No se puede acceder a la página web debido a un error tipográfico")
            
            
print(get_bs_soysuper())