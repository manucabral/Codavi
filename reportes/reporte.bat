py descargar.py
"C:\Program Files\7-Zip\7z.exe" e "Covid19Casos.zip"
py reporte.py
git pull
git add *.csv
git commit -m "Reporte para el dia de hoy"
git push
del /f Covid19Casos.csv
del /f Covid19Casos.zip
pause