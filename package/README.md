# Paquete Codavi
Codavi es una libreria de Python que te facilita la obtención de datos sobre el COVID-19 de toda Argentina.

## Instalación
```
pip install codavi
```
## Ejemplo de uso
```py
from codavi import Codavi

# instanciamos el objeto de Codavi
cod = Codavi()

# especificamos la dosis y si es acumulado o no
data = cod.vacunas_aplicadas(dosis='primera', acumulado=True)

print(data) # salida: ['fecha', 'cantidad']
```

## **vacunas_aplicadas(dosis:str, acumulado:bool, fecha:str) -> []**
Devuelve la cantidad de vacunas aplicadas por determinada dosis, por defecto si no le pasas ningún parámetro devuelve la última actualización de todas las dosis y de manera acumulada.     
### Parámetros requeridos
- `dosis`: primera, segunda o total
- `fecha`: en formato 'año-mes-día' ejemplo: '2021-12-12'
- `acumulado`: True o False.

## **llamadas_107(acumulado:bool, fecha:str) -> []**
Devuelve la cantidad de llamadas 107 hechas de COVID-19, si no le pasas ningún parámetro devuelve la última actualización y de manera diaria (no acumulada).
### Parámetros requeridos
- `acumulado`: True o False.
- `fecha`: en formato 'DIAMESAÑO' ejemplo: '12MAY2021'

## **confirmados(sexo:str, fecha:str) -> []**
Devuelve la cantidad de casos confirmados de COVID-19 en toda la Argentina, si no le pasas ningún parámetro devuelve la última actualización de casos confirmados de manera acumulada sin filtro por sexo. Esta función utiliza los reportes de Codavi que puedes obtenerlos desde [aquí](https://github.com/manucabral/Codavi/tree/main/reportes).
### Parámetros requeridos
- `sexo`: filtro por sexo, ejemplo: 'm'
- `fecha`: en formato 'año-mes-día' ejemplo: '2021-12-12'

## **fallecidos(sexo:str, fecha:str) -> []**
Devuelve la cantidad de fallecidos por COVID-19 en toda la Argentina, si no le pasas ningún parámetro devuelve la última actualización de fallecidos de manera acumulada sin filtro por sexo. Esta función utiliza los reportes de Codavi que puedes obtenerlos desde [aquí](https://github.com/manucabral/Codavi/tree/main/reportes).
### Parámetros requeridos
- `sexo`: filtro por sexo, ejemplo: 'm'
- `fecha`: en formato 'año-mes-día' ejemplo: '2021-12-12'

## Fuente de datos
Todos los análisis y comparativas estan basados de los datos que provee el gobierno Argentino sobre el virus, estos datos lo puedes descargar [aquí](https://datos.gob.ar/dataset/salud-vacunas-contra-covid-19-dosis-aplicadas-republica-argentina---registro-desagregado).
Los datos son actualizados diariamente o semanalmente por el mismo gobierno del país.