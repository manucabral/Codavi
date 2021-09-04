import pandas as pd
import mysql.connector
from flask import Flask
from datetime import datetime

app = Flask(__name__)
FECHA_ACTUAL = datetime.now().date().isoformat()


def obtenerDatosVacuna():
    try:
        url = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19VacunasAgrupadas.csv.zip'
        data = pd.read_csv(url)
    except Exception as Error:
        print('Hubo un error al leer el dataset', Error)
    return data


def obtenerDatosGenero(dosis):
    try:
        cnx = mysql.connector.connect(
            host="desconocido",
            port=3306,
            user="desconocido",
            password="desconocido",
            db="desconocido"
        )
        cursor = cnx.cursor()
    except Exception:
        return {
            "status": 204,
            "titulo": f"Comparativa por género dosis {dosis}",
            "data": "No hay datos"}

    query = (
        f"SELECT masculino, femenino, fecha FROM `x3lh5zri57nk7is6`.`generos` WHERE dosis = '{dosis}' and fecha = '{FECHA_ACTUAL}';")
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) == 0:
        return {
            "status": 204,
            "titulo": f"Comparativa por género dosis {dosis}",
            "data": "No hay datos actualizados para hoy."}
    
    cantidadMasculino, cantidadFemenino, fecha = result[0]
    cursor.close()
    cnx.close()
    
    return {
        "status": 200,
        "titulo": f"Comparativa por género dosis {dosis}",
        "descripcion": f'Cantidad de vacunados por género en la DOSIS {dosis}',
        "fecha": str(fecha),
        "dosis": f"{dosis}",
        "data": {
            "masculino": {
                "nombre": "Masculino",
                "total": int(cantidadMasculino),
            },
            "femenino": {
                "nombre": "Femenino",
                "total": int(cantidadFemenino)
            }
        }
    }


@app.errorhandler(404)
def page_not_found(e):
    return "La ruta que buscas no existe."


@app.route('/', methods=['GET'])
def index():
    return "Bienvenido a la API de Codavi."


@app.route('/vacunas', methods=['GET'])
def vacunas():
    data = obtenerDatosVacuna()
    sputnik = data.query(
        'vacuna_nombre.str.contains("Sputnik")').primera_dosis_cantidad.sum()
    astrazeneca = data.query(
        'vacuna_nombre.str.contains("AstraZeneca")').primera_dosis_cantidad.sum()
    sinopharm = data.query(
        'vacuna_nombre.str.contains("Sinopharm")').primera_dosis_cantidad.sum()
    covishield = data.query(
        'vacuna_nombre.str.contains("COVISHIELD")').primera_dosis_cantidad.sum()
    moderna = data.query(
        'vacuna_nombre.str.contains("Moderna")').primera_dosis_cantidad.sum()

    return {
        "status": 200,
        "titulo": "Comparativa vacunas",
        "descripcion": f'Cantidad de vacunas aplicadas por marca incluyendo la primera y segunda dosis.',
        "data": {
            "Sputnik": {
                "nombre": "Sputnik",
                "total": int(sputnik)
            },
            "AstraZeneca": {
                "nombre": "AstraZeneca",
                "total": int(astrazeneca)
            },
            "Sinopharm": {
                "nombre": "Sinopharm",
                "total": int(sinopharm)
            },
            "Covishield": {
                "nombre": "Covishield",
                "total": int(covishield)
            },
            "Moderna": {
                "nombre": "Moderna",
                "total": int(moderna)
            }
        }
    }


@app.route('/genero/<dosis>', methods=['GET'])
def genero(dosis=0):
    return obtenerDatosGenero(dosis)
