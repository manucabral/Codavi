"""
    Este simple programa descarga el archivo de casos sobre el COVID-19 ortogado por la Dirección Nacional de Epidemiología y Análisis de Situación de Salud.
    Referencia: https://datos.gob.ar/dataset/salud-covid-19-casos-registrados-republica-argentina
"""

from urllib.request import urlopen
from shutil import copyfileobj

URL_DATASET = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19Casos.zip'
ARCHIVO = 'Covid19Casos.zip'

print('> Iniciando descarga del archivo', ARCHIVO)
try:
    with urlopen(URL_DATASET) as respuesta, open(ARCHIVO, 'wb') as salida:
        print('>> Copiando en el directorio..')
        copyfileobj(respuesta, salida)
except Exception as e:
    print('> Ocurrio un error al descargar el archivo.', e)

print(f'> {ARCHIVO} descargado correctamente en el directorio')
