# Paquete Codavi
Codavi es una libreria de Python que te facilita la obtención de datos sobre el COVID-19 de toda Argentina.

- [Instalación](#instalacion)
- [Información de uso](#info-vacuna)
  - [Vacunas](#info-vacuna)
  - [Dosis](#dosis)
  - [Llamadas 107](#llamadas107)
  - [Confirmados](#confirmados)
  - [Fallecidos](#fallecidos)
- [Fuente de datos](#fuente)
- [Contribuciones](#contribucion)

<a name="instalacion"></a>
# Instalación
La última versión de Codavi solamente esta disponible en [Python Packege Index (PyPI)](https://pypi.org/project/codavi/)
```
pip install codavi
```

## Dependencias
- [pandas](https://github.com/pandas-dev/pandas)
- [requests](https://github.com/psf/requests)

# Información de uso
<a name="info-vacuna"></a>
## vacuna(nombre:str, dosis:str) -> []
Devuelve la cantidad de dosis aplicadas por tipo de vacuna, es obligatorio especificar el tipo de vacuna que quieres obtener, la dosis es opcional y por defecto te devuelve la suma de todas.

Vacunas disponibles: ***Covishield, AstraZeneca, Sputnik, Sinopharm, Moderna y Pfizer***

Dosis disponibles: ***primera, segunda, refuerzo, unica y adicional***
### Parámetros requeridos
- `nombre`: tipo de vacuna a obtener
- `dosis`: tipo de dosis a obtener (opcional)

### Ejemplo de uso
```py
>>> from codavi import Codavi
>>> codavi = Codavi()
>>> codavi.vacuna(nombre='covishield', dosis='primera')
['2021-12-26', 'COVISHIELD ChAdOx1nCoV COVID 19', 'primera_dosis_cantidad', 647949]
```

<a name="dosis"></a>
## dosis(numero:str, acumulado:bool, fecha:str) -> []
Devuelve la cantidad de dosis aplicadas nacionalmente, por defecto si no le pasas ningún parámetro devuelve la última actualización de todas las dosis y de manera acumulada.

Dosis disponibles: ***primera, segunda y total***

### Parámetros requeridos
- `numero`: numero de dosis a obtener
- `acumulado`: True o False.
- `fecha`: en formato 'año-mes-día' ejemplo: '2021-12-12'

### Ejemplo de uso
```py
>>> from codavi import Codavi
>>> codavi = Codavi()
>>> codavi.dosis(numero='primera', acumulado=False)
['2021-12-24', '1943']
```

<a name="llamadas107"></a>
## llamadas_107(acumulado:bool, fecha:str) -> []
Devuelve la cantidad de llamadas 107 hechas de COVID-19, si no le pasas ningún parámetro devuelve la última actualización y de manera diaria (no acumulada).
### Parámetros requeridos
- `acumulado`: True o False.
- `fecha`: en formato 'DIAMESAÑO' ejemplo: '12MAY2021'
### Ejemplo de uso
```py
>>> from codavi import Codavi
>>> codavi = Codavi()
>>> codavi.llamadas_107(fecha='15MAY2021')
['15MAY2021', '429']
```

<a name="confirmados"></a>
## confirmados(sexo:str, fecha:str) -> []
Devuelve la cantidad de casos confirmados de COVID-19 en toda la Argentina, si no le pasas ningún parámetro devuelve la última actualización de casos confirmados de manera acumulada sin filtro por sexo. Esta función utiliza los reportes de Codavi que puedes obtenerlos desde [aquí](https://github.com/manucabral/Codavi/tree/main/reportes).
### Parámetros requeridos
- `sexo`: filtro por sexo, ejemplo: 'm'
- `fecha`: en formato 'año-mes-día' ejemplo: '2021-12-12'
### Ejemplo de uso
```py
>>> from codavi import Codavi
>>> codavi = Codavi()
>>> codavi.confirmados(fecha='2021-12-24', sexo='f')
['2021-12-24', '48362']
```

<a name="fallecidos"></a>
## fallecidos(sexo:str, fecha:str) -> []
Devuelve la cantidad de fallecidos por COVID-19 en toda la Argentina, si no le pasas ningún parámetro devuelve la última actualización de fallecidos de manera acumulada sin filtro por sexo. Esta función utiliza los reportes de Codavi que puedes obtenerlos desde [aquí](https://github.com/manucabral/Codavi/tree/main/reportes).
### Parámetros requeridos
- `sexo`: filtro por sexo, ejemplo: 'm'
- `fecha`: en formato 'año-mes-día' ejemplo: '2021-12-12'
### Ejemplo de uso
```py
>>> from codavi import Codavi
>>> codavi = Codavi()
>>> codavi.fallecidos(fecha='2021-12-24', sexo='m')
['2021-12-24', '66424']
```

<a name="fuente"></a>
## Fuente de datos
Todos los análisis y comparativas estan basados de los datos que provee el gobierno Argentino sobre el virus, estos datos lo puedes descargar [aquí](https://datos.gob.ar/dataset/salud-vacunas-contra-covid-19-dosis-aplicadas-republica-argentina---registro-desagregado).
Los datos son actualizados diariamente o semanalmente por el mismo gobierno del país.

<a name="contribucion"></a>
## Contribuciones
Si tienes alguna contribución, reporte o arreglo de bugs, mejoras en la documentación o en el código fuente eres bienvenido y aceptado para colaborar con Codavi.
