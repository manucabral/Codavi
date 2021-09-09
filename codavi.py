
from data.descargar import descargarArchivo, existeArchivo, CASOS_ARCHIVO, VACUNACION_ARCHIVO
from data.scripts import totalDosisAplicadas

if __name__ == "__main__":
    try:
        if not existeArchivo(VACUNACION_ARCHIVO):
            descargarArchivo(VACUNACION_ARCHIVO)
        else:
            print('Archivo encontrado:', VACUNACION_ARCHIVO)

        #if not existeArchivo(CASOS_ARCHIVO):
        #    descargarArchivo(CASOS_ARCHIVO)
        #else:
        #    print('Archivo encontrado:', CASOS_ARCHIVO)

    except ValueError:
        print('Ocurrio un error al descargar los archivos: ', ValueError)

    totalDosisAplicadas()