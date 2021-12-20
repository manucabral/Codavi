# Codavi API
Codavi ofrece una API para obtener los datos sobre las dosis aplicadas y casos registrados mediante generos.

## Instalación
Clonar y ejecutar el archivo **api/wsgi.py**
```
git clone --recursive https://github.com/manucabral/Codavi.git
cd Codavi/api
python wsgi.py
```
Finalizando estos pasos habrás desplegado correctamente la API de Codavi localmente en la siguiente dirección [localhost:5000](http://localhost:5000).

## Heroku
Codavi está desplegado de manera gratis y de prueba en Heroku, puedes acceder a ella yendo [aquí](http://codavi.herokuapp.com)

## Rutas disponibles
- /vacunas/[dosis]
- /genero/[dosis]
