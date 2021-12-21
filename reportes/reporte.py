import pandas as pd
from urllib.request import urlopen
from datetime import datetime
import zipfile
import shutil
import os

URL_DATASET = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/'
CASOS_ARCHIVO = 'Covid19Casos'

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

def extraer(archivo_zip):
    print(f'> Comenzando extracción del archivo {archivo_zip.filename} ...')
    with archivo_zip as zf:
        try:
            zf.extractall('.')
        except zerror as e:
            pass
    print('> Extracción terminada correctamente')
        

descargarArchivo(CASOS_ARCHIVO)
hoy = datetime.now().strftime('%Y-%m-%d')
data = pd.read_csv('./Covid19Casos.csv', usecols = ['clasificacion_resumen', 'fallecido'])
confirmados = data.query('clasificacion_resumen == "Confirmado"').count()[0]
fallecidos = data.query('fallecido == "SI" and clasificacion_resumen == "Confirmado"').count()[0]             

with open(f'{hoy}.csv', 'w') as f:
    f.write(f'fecha,confirmados,fallecidos\n{hoy},{confirmados},{fallecidos}')
    f.close()