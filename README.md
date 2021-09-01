<div align="center">
  <h1>Codavi :bar_chart:</h1>
</div>

[![](https://img.shields.io/badge/License-GPLv3-red.svg)](https://github.com/manucabral/COVID-19-Davi/blob/main/LICENSE)
[![nbviewer](https://img.shields.io/badge/jupyter_notebook-nbviewer-black.svg?style=flat-square)](https://nbviewer.jupyter.org/github/manucabral/Codavi/blob/main/Vacunación/DOSIS1-MasculineAndFeminineComparative.ipynb)
[![Python 3.6](https://img.shields.io/badge/python-3.9.1-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![React](https://img.shields.io/badge/-React-black?style=for-the-badge&logo=React)](https://es.reactjs.org/)
[![SASS](https://img.shields.io/badge/-sass-white?style=for-the-badge&logo=sass)](https://sass-lang.com/)
[![CSS](https://img.shields.io/badge/-css-lightblue?style=for-the-badge&logo=css3)](https://developer.mozilla.org/es/docs/Web/CSS)
[![Html](https://img.shields.io/badge/-html-black?style=for-the-badge&logo=html5)](https://developer.mozilla.org/es/docs/Web/HTML)
[![Javascript](https://img.shields.io/badge/-Javascript-critical?style=for-the-badge&logo=Javascript)](https://developer.mozilla.org/es/docs/Web/JavaScript)
[![Express](https://img.shields.io/badge/-express-black?style=for-the-badge&logo=express)](https://expressjs.com/es/)
[![Node](https://img.shields.io/badge/-Node-black?style=for-the-badge&logo=Node.js)](https://nodejs.org/es/)
[![Figma](https://img.shields.io/badge/-Figma-white?style=for-the-badge&logo=figma)](https://figma.com/)
Visualización y estadísticas sobre el COVID-19 en toda la Argentina.

## Contiene
- [Vacunación](https://github.com/manucabral/Codavi/tree/main/Vacunación) :test_tube:
  - [Primera dosis](https://github.com/manucabral/Codavi/tree/main/Vacunación/Primera%20dosis)
    - [Comparación entre hombres y mujeres](https://github.com/manucabral/Codavi/blob/main/Vacunación/Primera%20dosis/DOSIS1-MasculineAndFeminineComparative.ipynb)
    - [Cantidad de vacunados por grupo etario](https://github.com/manucabral/Codavi/blob/main/Vacunación/Primera%20dosis/DOSIS1-GrupoEtarioComparativa.ipynb)
    - [Cantidad de vacunas aplicadas por marca](https://github.com/manucabral/Codavi/blob/main/Vacunación/Primera%20dosis/DOSIS1-VacunasAplicadas.ipynb)

## Fuente de datos
Todos los análisis y comparativas estan basados de los datos que provee el gobierno Argentino sobre el virus, estos datos lo puedes descargar [aquí](https://datos.gob.ar/dataset/salud-vacunas-contra-covid-19-dosis-aplicadas-republica-argentina---registro-desagregado).
Los datos son actualizados diariamente o semanalmente por el mismo gobierno del país.

## Requerimientos
- Python 3.9.1 (o una versión más reciente)
- Pandas
- Matplotlib
- Flask

Si requieres instalarlos.
```
pip install 'nombre'
```

## Uso
Clonar y ejecutar el archivo main.py, o también puedes usar Jupyter Notebook para la visualización de datos.
```
git clone --recursive https://github.com/manucabral/Codavi.git
cd Codavi
python main.py
```
Ten en cuenta que Codavi descargará los datos y luego los eliminará, esto tomará poco tiempo.

### API
También encontraras la API de Codavi.
```
cd Codavi/api
python wsgi.py
```
Una vez ejecutada está se alojará en [localhost:5000](http://localhot:5000)

### Desplegar en Heroku :rocket:
Para desplegarlo en heroku necesitas generar el archivo _requeriments.txt_ y _Procfile_.

Configuración de requeriments.
```
pandas==1.3.2
Flask==2.0.1
Flask-RESTful==0.3.9
gunicorn==20.1.0
```

Configuración de Procfile.
```
web: gunicorn -b :$PORT wsgi:app
```
