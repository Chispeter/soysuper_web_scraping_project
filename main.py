from config import get_configuration
from web_scraping import get_dictionaries

# Extraer la información de la configuración del proyecto
[hostname, data_dirname] = get_configuration()

# Extraer la información de la página web y guardarla en archivos JSON
get_dictionaries(hostname=hostname, data_dirname=data_dirname)

