from urllib.request import urlopen
from datetime import datetime
import zipfile, shutil, os, pandas as pd

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

descargarArchivo(CASOS_ARCHIVO)
print('>> Analizando los datos..')
hoy = datetime.now().strftime('%Y-%m-%d')
data = pd.read_csv('./Covid19Casos.csv', usecols = ['clasificacion_resumen', 'fallecido', 'sexo'])

print('>> Filtrando a los casos confirmados..')
filtro = data.query('clasificacion_resumen == "Confirmado"')

print('>> Obteniendo los campos..')
total_confirmados = filtro.count()[0]
total_fallecidos = filtro.query('fallecido == "SI"').count()[0]
confirmados_masculinos = filtro.query('sexo == "M"').count()[0]
confirmados_femeninos = filtro.query('sexo == "F"').count()[0]
fallecidos_masculinos = filtro.query('fallecido == "SI" and sexo == "M"').count()[0]
fallecidos_femeninos = filtro.query('fallecido == "SI" and sexo == "F"').count()[0]

print('>> Generando el archivo de reporte..')
with open(f'{hoy}.csv', 'w') as f:
    f.write('fecha,total_confirmados,confirmados_masculinos,confirmados_femeninos,total_fallecidos,fallecidos_masculinos,fallecidos_femeninos\n')
    f.write(f'{hoy},{total_confirmados},{confirmados_masculinos},{confirmados_femeninos},{total_fallecidos},{fallecidos_masculinos},{fallecidos_femeninos}')
    f.close()
print('>> Reporte terminado.')