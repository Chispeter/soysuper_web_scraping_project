from config import get_configuration
from web_scraping import get_dictionaries

# Extraer la información de la configuración del proyecto
config_data = get_configuration()

# Extraer la información de la página web y guardarla en archivos JSON
get_dictionaries(hostname=config_data["hostname"], data_dirname=config_data["data_dirname"])

