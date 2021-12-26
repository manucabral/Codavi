from codavi import Codavi

codavi = Codavi()
total_confirmados = codavis.confirmados()
confirmados_masculinos = codavi.confirmados(sexo='m')
confirmados_femeninos = codavi.confirmados(sexo='f')
print(total_confirmados, confirmados_masculinos, confirmados_femeninos)