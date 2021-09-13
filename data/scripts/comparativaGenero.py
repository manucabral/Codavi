import pandas as pd
import os

def obtenerComparativaGenero(dosis):
    data = pd.read_csv(os.getcwd() + '/datos_nomivac_covid19.csv', usecols = ['orden_dosis', 'sexo'])
    masculinos = data.query(f'orden_dosis == {dosis} and sexo == "M"').sexo.count()
    femeninos = data.query(f'orden_dosis == {dosis} and sexo == "F"').sexo.count()
    return masculinos, femeninos
