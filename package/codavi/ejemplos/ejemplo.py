from codavi import Codavi

cod = Codavi()
vacunas = cod.vacunas_aplicadas(acumulado=True)
llamadas = cod.llamadas_107(acumulado=True)
total_confirmados = cod.confirmados()
confirmados_masculinos = cod.confirmados(sexo='m')
confirmados_femeninos = cod.confirmados(sexo='f')
muertes = cod.fallecidos()
muertes_masculinas = cod.fallecidos(sexo='m')
muertes_femeninas = cod.fallecidos(sexo='f')

print(vacunas, llamadas, total_confirmados)