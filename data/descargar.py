from urllib.request import urlopen
from datetime import datetime
import zipfile
import shutil
import os

URL_DATASET = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/'
VACUNACION_ARCHIVO = 'datos_nomivac_covid19'
CASOS_ARCHIVO = 'Covid19Casos'

def existeArchivo(nombreArchivo):
    return os.path.isfile('./' + nombreArchivo + '.csv')

def descargarArchivo(nombreArchivo):

    comprimido = nombreArchivo + '.zip'
    csv = nombreArchivo + '.csv'

    print('> Iniciando descarga del archivo', comprimido)
    with urlopen(URL_DATASET + comprimido) as respuesta, open(comprimido, 'wb') as salida:

        print('>> Copiando', comprimido, 'en el directorio..')
        shutil.copyfileobj(respuesta, salida)

        print('>> Extrayendo', csv, 'del archivo comprimido..')
        with zipfile.ZipFile(comprimido) as archivoComprimido:
            archivoComprimido.extract(csv)

    print('>> Eliminando', comprimido, 'del directorio..')
    os.remove(comprimido)

    return print('> Archivo', csv, 'descargado correctamente en el directorio.')
