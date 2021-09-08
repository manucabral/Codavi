import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
import base64
import io
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

    sputnik = data.query('vacuna_nombre.str.contains("Sputnik")')
    astrazeneca = data.query('vacuna_nombre.str.contains("AstraZeneca")')
    sinopharm = data.query('vacuna_nombre.str.contains("Sinopharm")')
    covishield = data.query('vacuna_nombre.str.contains("COVISHIELD")')
    moderna = data.query('vacuna_nombre.str.contains("Moderna")')

    return sputnik, astrazeneca, sinopharm, covishield, moderna


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


@app.route('/vacunas/<dosis>', methods=['GET'])
def vacunas(dosis):
    titulo = None
    descripcion = None
    objetivo_dosis = None
    sputnik, astrazeneca, sinopharm, covishield, moderna = obtenerDatosVacuna()

    if int(dosis) == 1:
        titulo = 'Vacunas aplicadas en la primera dosis'
        descripcion = "Cantidad de vacunas aplicadas por marca en la primera dosis"
        objetivo_dosis = 'primera_dosis_cantidad'
    elif int(dosis) == 2:
        titulo = 'Vacunas aplicadas en la segunda dosis'
        descripcion = "Cantidad de vacunas aplicadas por marca en la segunda dosis"
        objetivo_dosis = 'segunda_dosis_cantidad'

    sputnik_total = sputnik[objetivo_dosis].sum()
    astrazeneca_total = astrazeneca[objetivo_dosis].sum()
    sinopharm_total = sinopharm[objetivo_dosis].sum()
    covishield_total = covishield[objetivo_dosis].sum()
    moderna_total = moderna[objetivo_dosis].sum()
    total = sputnik_total + astrazeneca_total + \
        sinopharm_total + covishield_total + moderna_total

    x = ['Sputnik', 'AstraZeneca', 'Sinopharm', 'Covishield', 'Moderna']
    y = [sputnik_total, astrazeneca_total,
         sinopharm_total, covishield_total, moderna_total]
    plt.bar(x, y, color='green')
    plt.ylabel('Cantidad')
    plt.xlabel('Marca')
    plt.title(titulo)

    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches="tight")
    plt.close()
    img = base64.b64encode(img.getvalue()).decode("utf-8").replace("\n", "")
    return {
        "status": 200,
        "titulo": titulo,
        "descripcion": descripcion,
        "total": int(total),
        "grafico": img,
        "data": {
            "Sputnik": {
                "nombre": "Sputnik",
                "total": int(sputnik_total)
            },
            "AstraZeneca": {
                "nombre": "AstraZeneca",
                "total": int(astrazeneca_total)
            },
            "Sinopharm": {
                "nombre": "Sinopharm",
                "total": int(sinopharm_total)
            },
            "Covishield": {
                "nombre": "Covishield",
                "total": int(covishield_total)
            },
            "Moderna": {
                "nombre": "Moderna",
                "total": int(moderna_total)
            }
        }
    }

@app.route('/genero/<dosis>', methods=['GET'])
def genero(dosis=0):
    return obtenerDatosGenero(dosis)
