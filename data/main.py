from descargar import descargarArchivo, existeArchivo, CASOS_ARCHIVO, VACUNACION_ARCHIVO
from scripts.totalDosisAplicadas import obtenerTotalDosis
from scripts.comparativaGenero import obtenerComparativaGenero

if __name__ == "__main__":
    try:
        if not existeArchivo(VACUNACION_ARCHIVO):
            descargarArchivo(VACUNACION_ARCHIVO)
        else:
            print('Archivo encontrado:', VACUNACION_ARCHIVO)

        # if not existeArchivo(CASOS_ARCHIVO):
        #    descargarArchivo(CASOS_ARCHIVO)
        # else:
        #    print('Archivo encontrado:', CASOS_ARCHIVO)

    except ValueError:
        print('Ocurrio un error al descargar los archivos: ', ValueError)

    total_dosis = obtenerTotalDosis()
    print(f'Total de dosis suministradas hasta hoy: {total_dosis:,}')
    total_masculinos, total_femeninos = obtenerComparativaGenero(1)
    print('> DOSIS 1')
    print(
        f'Personas masculinas vacunadas: {total_masculinos:,}\nPersonas femeninas vacunadas: {total_femeninos:,}')