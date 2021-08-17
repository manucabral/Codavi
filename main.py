from urllib.request import urlopen
import zipfile
import shutil
import os

url = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/datos_nomivac_covid19.zip'
zip = 'datos_nomivac_covid19.zip'

if not os.path.isfile('./datos_nomivac_covid19.csv'):

    print("Extrayendo archivo comprimido..")
    with urlopen(url) as response, open(zip, 'wb') as salida:
        shutil.copyfileobj(response, salida)

        # extrayendo del comprimido el archivo csv
        with zipfile.ZipFile(zip) as zf:
            zf.extract('datos_nomivac_covid19.csv')

    print("Eliminando archivo comprimido..")
    os.remove('datos_nomivac_covid19.zip')

print("Datos descargandos correctamente.")

#   columns ->

# 	sexo
#   grupo_etario
# 	jurisdiccion_residencia
# 	jurisdiccion_residencia_id
# 	depto_residencia
# 	depto_residencia_id
# 	jurisdiccion_aplicacion
# 	jurisdiccion_aplicacion_id
# 	depto_aplicacion
# 	depto_aplicacion_id	fecha_aplicacion
# 	vacuna
# 	condicion_aplicacion
# 	orden_dosis	lote_vacuna
