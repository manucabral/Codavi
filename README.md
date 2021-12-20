![codavi-logo](https://i.imgur.com/r92Bj5n.png)
<div align="center">
  <a href="https://github.com/manucabral/COVID-19-Davi/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-red.svg" alt="licence"> </a>
  <a href="https://www.python.org/downloads/release/python-360/"><img src="https://img.shields.io/badge/python-3.9.1-blue.svg" alt="Python"> </a>
  <a href="https://es.reactjs.org/"><img src="https://img.shields.io/badge/React-16.8.6-blue.svg" alt="React"> </a>
  <a href="https://nodejs.org/es/"><img src="https://img.shields.io/badge/Node-14.15.3-00610d.svg" alt="Node"> </a>

  <a href="https://vercel.com"><img src="https://vercelbadge.vercel.app/api/andrewmanu/codavi-web" alt="Vercel"> </a>
  <a href="#"><img src="https://img.shields.io/github/issues/manucabral/Codavi" alt="issues"> </a>
  <a href="#"><img src="https://img.shields.io/github/commit-activity/m/manucabral/Codavi" alt="activity"> </a>
  <a href="#"><img src="https://img.shields.io/github/contributors/manucabral/Codavi" alt="contributors"> </a>
</div>

**Codavi** es un servicio de código abierto que trata sobre la visualización y obtención de datos sobre el COVID-19 en toda la Argentina.
## Contiene
- Vacunación
  - Dosis aplicadas: [Primera dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Primera_Dosis/DOSIS1-TotalVacunasAplicadas.ipynb) / [Segunda Dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Segunda_Dosis/DOSIS2-TotalVacunasAplicadas.ipynb) / [Total de Dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/TotalDosisAplicadas.ipynb)
   - Comparación de vacunas aplicadas: [Primera Dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Primera_Dosis/DOSIS1-ComparativaVacunasAplicadas.ipynb) / [Segunda Dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Segunda_Dosis/DOSIS2-ComparativaVacunasAplicadas.ipynb)

  - Comparación entre mujeres y hombres: [Primera Dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Primera_Dosis/DOSIS1-ComparativaGenero.ipynb) / [Segunda Dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Segunda_Dosis/DOSIS2-ComparativaGenero.ipynb)
  
  - Comparación por grupo etario: [Primera Dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Primera_Dosis/DOSIS1-ComparativaGrupoEtario.ipynb) / [Segunda Dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Segunda_Dosis/DOSIS2-ComparativaGrupoEtario.ipynb)
  
# Paquete
Codavi puede ser instalado mediante PyPI, tener en cuenta que este paquete todavía está en desarrollo.
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

# Fuente de datos
Todos los análisis y comparativas estan basados de los datos que provee el gobierno Argentino sobre el virus, estos datos lo puedes descargar [aquí](https://datos.gob.ar/dataset/salud-vacunas-contra-covid-19-dosis-aplicadas-republica-argentina---registro-desagregado).
Los datos son actualizados diariamente o semanalmente por el mismo gobierno del país.
# Codavi en otros paises
Codavi se extiende en otros países los cuales son
  - [Codavi Chile](https://github.com/leo1q/Codavi-CL)
  - [Codavi Uruguay](https://github.com/nyashi/CODAVI-UY)
# API
Otra forma de obtener los datos es usando la API de Codavi, en ella encontraras las siguientes rutas
- /vacunas/[dosis]
- /genero/[dosis]

Estas mismas las puedes consultar con la versión de prueba yendo [aquí](http://codavi.herokuapp.com)

## Desplegar localmente
Clonar y ejecutar el archivo **api/wsgi.py**
```
git clone --recursive https://github.com/manucabral/Codavi.git
cd Codavi/api
python wsgi.py
```
Finalizando estos pasos habrás desplegado correctamente la API de Codavi localmente en la siguiente dirección [localhost:5000](http://localhost:5000).

# Bot de discord
Invita a Codavi desde [aquí](https://discord.com/oauth2/authorize?client_id=884893298551037983&permissions=8&scope=bot) a tu servidor de discord para estar a tanto sobre las vacunaciones.

