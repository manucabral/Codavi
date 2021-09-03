<div align="center">
  <h1>Codavi :bar_chart:</h1>
  <a href="https://github.com/manucabral/COVID-19-Davi/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-red.svg" alt="licence"> </a>
  <a href="https://www.python.org/downloads/release/python-360/"><img src="https://img.shields.io/badge/python-3.9.1-blue.svg" alt="Python"> </a>
  <a href="https://es.reactjs.org/"><img src="https://img.shields.io/badge/React-16.8.6-blue.svg" alt="React"> </a>
  <a href="https://nodejs.org/es/"><img src="https://img.shields.io/badge/Node-14.15.3-00610d.svg" alt="Node"> </a>

  <a href="https://vercel.com"><img src="https://vercelbadge.vercel.app/api/manucabral/Codavi" alt="Vercel"> </a>
  <a href="#"><img src="https://img.shields.io/github/issues/manucabral/Codavi" alt="issues"> </a>
  <a href="#"><img src="https://img.shields.io/github/commit-activity/m/manucabral/Codavi" alt="activity"> </a>
  <a href="#"><img src="https://img.shields.io/github/contributors/manucabral/Codavi" alt="contributors"> </a>
</div>

**Codavi** es un servicio de código abierto que trata sobre la visualización y estadísticas de información oficial sobre el COVID-19 en toda la Argentina.

## Contiene
- Vacunación
  - Comparación entre hombres y mujeres vacunados
    - [Primera dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Primera%20dosis/DOSIS1-MasculineAndFeminineComparative.ipynb) / [Segunda dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data//Segunda%20dosis/DOSIS2-MasculineAndFeminineComparative.ipynb)
  
  - Cantidad de vacunados por grupo etario
    - [Primera dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Primera%20dosis/DOSIS1-GrupoEtarioComparativa.ipynb) / [Segunda dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Segunda%20dosis/DOSIS2-GrupoEtarioComparativa.ipynb)
  
  - Cantidad de vacunas aplicadas por marca
    - [Primera dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Primera%20dosis/DOSIS1-VacunasAplicadas.ipynb) / [Segunda dosis](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/data/Segunda%20dosis/DOSIS2-VacunasAplicadas.ipynb)
- Casos
  - Comparativa de casos por género

## Fuente de datos
Todos los análisis y comparativas estan basados de los datos que provee el gobierno Argentino sobre el virus, estos datos lo puedes descargar [aquí](https://datos.gob.ar/dataset/salud-vacunas-contra-covid-19-dosis-aplicadas-republica-argentina---registro-desagregado).
Los datos son actualizados diariamente o semanalmente por el mismo gobierno del país.

## Requerimientos
- Pandas
- Matplotlib
> Si requieres instalarlos.
```
pip install 'nombre'
```

## Uso para visualización
Clonar y ejecutar el archivo main.py, o también puedes usar Jupyter Notebook para la visualización de datos.
```
git clone --recursive https://github.com/manucabral/Codavi.git
cd Codavi
python main.py
```
> Ten en cuenta que Codavi descargará los datos y luego los eliminará, esto tomará poco tiempo.
