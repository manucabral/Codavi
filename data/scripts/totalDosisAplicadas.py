def totalDosisAplicadas():
    import pandas as pd
    data = pd.read_csv('https://sisa.msal.gov.ar/datos/descargas/covid-19/files/Covid19VacunasAgrupadas.csv.zip')

    sputnik = data.query('vacuna_nombre.str.contains("Sputnik")')
    sputnik_total = sputnik['primera_dosis_cantidad'].sum() + sputnik['segunda_dosis_cantidad'].sum()
    astrazeneca = data.query('vacuna_nombre.str.contains("AstraZeneca")')
    astrazeneca_total = astrazeneca['primera_dosis_cantidad'].sum() + astrazeneca['segunda_dosis_cantidad'].sum()
    sinopharm = data.query('vacuna_nombre.str.contains("Sinopharm")')
    sinopharm_total = sinopharm['primera_dosis_cantidad'].sum() + sinopharm['segunda_dosis_cantidad'].sum()
    covishield = data.query('vacuna_nombre.str.contains("COVISHIELD")')
    covishield_total = covishield['primera_dosis_cantidad'].sum() + covishield['segunda_dosis_cantidad'].sum()
    moderna = data.query('vacuna_nombre.str.contains("Moderna")')
    moderna_total = moderna['primera_dosis_cantidad'].sum() + moderna['segunda_dosis_cantidad'].sum()

    total = sputnik_total + astrazeneca_total + sinopharm_total + covishield_total + moderna_total
    print(f'Total de dosis suministradas: {total:,}')