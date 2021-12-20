# Paquete Codavi
Codavi es una libreria de Python que te facilita la obtención de datos sobre el COVID-19 de toda Argentina.

## Instalación
```
pip install codavi
```

## Uso
```py
from codavi import Codavi

# instanciamos el objeto de Codavi
cod = Codavi()

# especificamos la dosis y si es acumulado o no
data = cod.aplicadas(dosis='primera', acumulado=True)

print(data) # salida: ['fecha', 'cantidad']
```

### Parámetros requeridos
- **dosis**: primera, segunda o total.
- **fecha**: en formato 'año-mes-día' ejemplo: '2021-12-12'
- **acumulado**: True o False.
