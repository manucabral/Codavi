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
            host="",
            port=3306,
            user="",
            password="",
            db=""
        )
        cursor = cnx.cursor()
    except Exception:
        return "No hay datos"

    query = (
        f"SELECT masculino, femenino, fecha FROM `alex`.`generos` WHERE dosis = '{dosis}' and fecha = '{FECHA_ACTUAL}';")
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) == 0:
        return "No hay datos"
    cantidadMasculino, cantidadFemenino, fecha = result[0]
    cursor.close()
    cnx.close()
    return {
        "masculino": int(cantidadMasculino),
        "femenino": int(cantidadFemenino),
        "dosis": f"{dosis}",
        "fecha": str(fecha),
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
        "comparativaVacunas": {
            "Sputnik": {
                "subtitle": "Sputnik",
                "total": int(sputnik)
            },
            "AstraZeneca": {
                "subtitle": "AstraZeneca",
                "total": int(astrazeneca)
            },
            "Sinopharm": {
                "subtitle": "Sinopharm",
                "total": int(sinopharm)
            },
            "Covishield": {
                "subtitle": "Covishield",
                "total": int(covishield)
            },
            "Moderna": {
                "subtitle": "Moderna",
                "total": int(moderna)
            }
        }
    }


@app.route('/genero/<dosis>', methods=['GET'])
def genero(dosis):
    return obtenerDatosGenero(dosis)
