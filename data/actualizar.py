from datetime import datetime
import pandas as pd
import mysql.connector
import os

FECHA_ACTUAL = datetime.now().date().isoformat()
URL_DATASET = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/'
VACUNACION_ARCHIVO = 'datos_nomivac_covid19'

def existeArchivo(nombreArchivo):
    return os.path.isfile('./' + nombreArchivo + '.csv')

def actualizarDatosGenero():
    masculinos = [0, 0]
    femeninos = [0, 0]

    try:
        data = pd.read_csv('datos_nomivac_covid19.csv', usecols=[
                           'orden_dosis', 'sexo'], skipinitialspace=True)
    except Exception as Error:
        return Error

    for i in range(2):
        femeninos[i] = data.query(
            f'orden_dosis == {i+1} and sexo == "F"').sexo.count()
        masculinos[i] = data.query(
            f'orden_dosis == {i+1} and sexo == "M"').sexo.count()

    cnx = mysql.connector.connect(
        host="unknown",
        port=3306,
        user="unknown",
        password="unknown",
        db="unknown"
    )
    cursor = cnx.cursor()

    for i in range(2):
        query = (
            f"INSERT INTO `unknown`.`generos` (`masculino`, `femenino`, `dosis`, `fecha`) VALUES ({masculinos[i]}, '{femeninos[i]}', '{i+1}', '{FECHA_ACTUAL}');")
        cursor.execute(query)
    
    cursor.close()
    cnx.commit()
    cnx.close()
    return "Datos de generos actualizados correctamente"

if __name__ == "__main__":
    if(existeArchivo(VACUNACION_ARCHIVO)):
        actualizarDatosGenero()
    else:
        print(f'No se encontro el archivo {VACUNACION_ARCHIVO}')