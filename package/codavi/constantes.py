"""
    ARGENTINA:
        Estos datos son públicos generados, guardados y publicados por organismos de gobierno de la República Argentina.
        Referencia: http://datos.salud.gob.ar/dataset
"""

URLS = {
    'ar': {
        'llamadas_107': 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/salud/llamados-107-covid/llamados_107_covid.csv',
        'dosis': {
            'acumulado': {
                'primera': 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/covid_1raDosis_acumulado.csv',
                'segunda': 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/covid_2daDosis_acumulado.csv',
                'total': 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/covid_total_acumulado.csv'
            },
            'diario': {
                'primera': 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/covid_1raDosis_diario.csv',
                'segunda': 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/covid_2daDosis_diario.csv',
                'total': 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/covid_total_diario.csv'
            }
        },
        'vacunas' : 'https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19VacunasAgrupadas.csv.zip',
        'casos': 'https://raw.githubusercontent.com/manucabral/Codavi/main/reportes/'
    },
    'chl': {
        'vacunas_aplicadas': 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto76/vacunacion_t.csv'
    }
}

FILTROS = {
    'fallecidos': {
        'm': 5,
        'f': 6,
        'todos': 4
    },
    'confirmados': {
        'm': 2,
        'f': 3,
        'todos': 1
    },
    'dosis': {
        'unica': 'dosis_unica_cantidad',
        'primera':  'primera_dosis_cantidad',
        'segunda': 'segunda_dosis_cantidad',
        'adicional': 'dosis_adicional_cantidad',
        'refuerzo': 'dosis_refuerzo_cantidad'
    }
}

MES = {
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC'
}
