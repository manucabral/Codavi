"""
    Este programa analiza el archivo de casos sobre el COVID-19 ortogado por la Dirección Nacional de Epidemiología y Análisis de Situación de Salud.
    Referencia: https://datos.gob.ar/dataset/salud-covid-19-casos-registrados-republica-argentina
"""

from datetime import datetime
import os, pandas as pd

class CodaviReporte:

    def obtener_fecha(self) -> str:
        self.hoy = datetime.now().strftime('%Y-%m-%d')
        return self.hoy
    
    def leer_dataset(self, archivo: str, columnas: list) -> bool:
        try:
            print(f'> Leyendo el archivo {archivo.split(".")[0]}...')
            self.data = pd.read_csv(archivo, usecols=columnas)
            print('>> Lectura terminada')
        except Exception as e:
            print('Ocurrio un error al leer el dataset', e)
            return False
    
    def filtrar(self) -> bool:
        try:
            print('> Filtrando los datos...')
            self.data = self.data.query('clasificacion_resumen == "Confirmado"')
            print('>> Filtrado terminado')
            return True
        except Exception as e:
            print('Ocurrio un error al filrar el dataset', e)
            return False

    def generar_casos(self) -> None:
        total_confirmados = self.data.count()[0]
        confirmados_masculinos = self.data.query('sexo == "M"').count()[0]
        confirmados_femeninos = self.data.query('sexo == "F"').count()[0]

        print('> Generando reporte de casos...')
        try:
            with open('confirmados.csv', 'a') as f:
                f.write(f'{self.hoy},{total_confirmados},{confirmados_masculinos},{confirmados_femeninos}\n')
                f.close()
            print('>> Reporte de casos finalizado')
        except Exception as e:
            print('Ocurrio un error al generar el reporte', e)
    
    def generar_fallecidos(self) -> None:
        total = self.data.query('fallecido == "SI"').count()[0]
        masculinos = self.data.query('fallecido == "SI" and sexo == "M"').count()[0]
        femeninos = self.data.query('fallecido == "SI" and sexo == "F"').count()[0]

        print('> Generando reporte de fallecidos...')
        try:
            with open('fallecidos.csv', 'a') as f:
                f.write(f'{self.hoy},{total},{masculinos},{femeninos}\n')
                f.close()
            print('>> Reporte de fallecidos finalizado')
        except Exception as e:
            print('Ocurrio un error al generar el reporte', e)

if __name__ == "__main__":
    reporte = CodaviReporte()
    reporte.obtener_fecha()
    reporte.leer_dataset('Covid19Casos.csv', ['clasificacion_resumen', 'fallecido', 'sexo'])
    reporte.filtrar()
    reporte.generar_casos()
    reporte.generar_fallecidos()
