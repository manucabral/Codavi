from codavi import Codavi

codavi = Codavi()
total_fallecidos = codavis.fallecidos()
fallecidos_masculinos = codavi.fallecidos(sexo='m')
fallecidos_femeninos = codavi.fallecidos(sexo='f')
print(total_fallecidos, fallecidos_masculinos, fallecidos_femeninos)