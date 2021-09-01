<div align="center">
  <h1>Codavi :bar_chart:</h1>
</div>

[![](https://img.shields.io/badge/License-Apache_2.0-red.svg)](https://github.com/manucabral/COVID-19-Davi/blob/main/LICENSE)
[![nbviewer](https://img.shields.io/badge/jupyter_notebook-nbviewer-black.svg?style=flat-square)](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/Vacunación/DOSIS1-MasculineAndFeminineComparative.ipynb)
[![Python 3.6](https://img.shields.io/badge/python-3.9.1-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![React](https://img.shields.io/badge/React-16.8.6-blue)](https://es.reactjs.org/)
[![Node](https://img.shields.io/badge/Node-14.15.3-00610d.svg)](https://nodejs.org/es/)

![issues](https://img.shields.io/github/issues/manucabral/Codavi)
![activity](https://img.shields.io/github/commit-activity/m/manucabral/Codavi)
![contributors](https://img.shields.io/github/contributors/manucabral/Codavi)

Visualización y estadísticas sobre el COVID-19 en toda la Argentina.

## Contiene
- Vacunación
  - Comparación entre hombres y mujeres vacunados
    - [Primera dosis](https://github.com/manucabral/Codavi/blob/main/data/Primera%20dosis/DOSIS1-MasculineAndFeminineComparative.ipynb) / [Segunda dosis](https://github.com/manucabral/Codavi/blob/main/data/Segunda%20dosis/DOSIS2-MasculineAndFeminineComparative.ipynb)
  
  - Cantidad de vacunados por grupo etario
    - [Primera dosis](https://github.com/manucabral/Codavi/blob/main/data/Primera%20dosis/DOSIS1-GrupoEtarioComparativa.ipynb) / [Segunda dosis](https://github.com/manucabral/Codavi/blob/main/data/Segunda%20dosis/DOSIS2-GrupoEtarioComparativa.ipynb)
  
  - Cantidad de vacunas aplicadas por marca
    - [Primera dosis](https://github.com/manucabral/Codavi/blob/main/data/Primera%20dosis/DOSIS1-VacunasAplicadas.ipynb) / [Segunda dosis](https://github.com/manucabral/Codavi/blob/main/data/Segunda%20dosis/DOSIS2-VacunasAplicadas.ipynb)
- Casos
  - Comparativa de casos por género

## Fuente de datos
Todos los análisis y comparativas estan basados de los datos que provee el gobierno Argentino sobre el virus, estos datos lo puedes descargar [aquí](https://datos.gob.ar/dataset/salud-vacunas-contra-covid-19-dosis-aplicadas-republica-argentina---registro-desagregado).
Los datos son actualizados diariamente o semanalmente por el mismo gobierno del país.

## Requerimientos
- Python 3.9.1 (o una versión más reciente)
- Pandas
- Matplotlib
- Flask

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
