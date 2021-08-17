import pandas as pd
import zipfile
import os

from urllib.request import urlopen
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

data = pd.read_csv('datos_nomivac_covid19.csv')
dosis = data.loc[(data['orden_dosis'] == 1), 'vacuna']