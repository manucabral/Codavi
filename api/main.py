import pandas as pd
from flask import Flask
app= Flask(__name__)

def obtenerDatos():
    data = None
    try:
        url = 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19VacunasAgrupadas.csv.zip'
        data = pd.read_csv(url)
    except Exception as Error:
        print('Hubo un error al leer el dataset', Error)
    return data


@app.route('/covid', methods=['GET'])
def home():
    data = obtenerDatos()
    sputnik = data.query('vacuna_nombre.str.contains("Sputnik")').primera_dosis_cantidad.sum()
    astrazeneca = data.query('vacuna_nombre.str.contains("AstraZeneca")').primera_dosis_cantidad.sum()
    sinopharm = data.query('vacuna_nombre.str.contains("Sinopharm")').primera_dosis_cantidad.sum()
    covishield = data.query('vacuna_nombre.str.contains("COVISHIELD")').primera_dosis_cantidad.sum()
    moderna = data.query('vacuna_nombre.str.contains("Moderna")').primera_dosis_cantidad.sum()

    return {
        "comparativaVacunas": {
            "Sputnik":{
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