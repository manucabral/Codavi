from urllib.request import urlopen
import zipfile
import shutil
import os

# Ubicación de los datasets oficiales del gobierno.
URL_DATASET = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/'

# Archivo que contiene las vacunaciones.
VACUNACION_ARCHIVO = 'datos_nomivac_covid19'

# Archivo que contiene los casos.
CASOS_ARCHIVO = 'Covid19Casos'

def existeArchivo(nombreArchivo):
    return os.path.isfile('./' + nombreArchivo + '.csv')

def descargarArchivo(nombreArchivo):

    comprimido = nombreArchivo + '.zip'
    csv = nombreArchivo + '.csv'

    print('Iniciando descarga del archivo', comprimido)
    with urlopen(URL_DATASET + comprimido) as respuesta, open(comprimido, 'wb') as salida:

        print('Copiando', comprimido, 'en el directorio..')
        shutil.copyfileobj(respuesta, salida)

        print('Extrayendo', csv, 'del archivo comprimido..')
        with zipfile.ZipFile(comprimido) as archivoComprimido:
            archivoComprimido.extract(csv)

    print('Eliminado', comprimido, 'del directorio..')
    os.remove(comprimido)

    return print('Archivo', csv, 'descargado correctamente en el directorio.')


if __name__ == "__main__":

    try:
        if not existeArchivo(VACUNACION_ARCHIVO):
            descargarArchivo(VACUNACION_ARCHIVO)
        else:
            print('Archivo encontrado:', VACUNACION_ARCHIVO)

        if not existeArchivo(CASOS_ARCHIVO):
            descargarArchivo(CASOS_ARCHIVO)
        else:
            print('Archivo encontrado:', CASOS_ARCHIVO)

    except ValueError:
        print('Ocurrio un error al descargar los archivos: ', ValueError)