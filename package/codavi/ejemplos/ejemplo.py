from codavi import Codavi

cod = Codavi()
vacunas = cod.vacunas_aplicadas(acumulado=True)
llamadas = cod.llamadas_107(acumulado=True)
print(vacunas, llamadas)