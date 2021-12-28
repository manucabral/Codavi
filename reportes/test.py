
"""
    Este programa analiza el archivo de casos sobre el COVID-19 ortogado por la Dirección Nacional de Epidemiología y Análisis de Situación de Salud.
    Referencia: https://datos.gob.ar/dataset/salud-covid-19-casos-registrados-republica-argentina
"""

from datetime import datetime
import os, pandas as pd

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