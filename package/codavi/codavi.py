from csv import reader
from requests import get
from datetime import datetime

# Todo import
from .constantes import *
from .excepciones import *

class Codavi:
    def __fecha_actual(self, formato: str ='%Y-%m-%d') -> str:
        """
        Obtiene la fecha actual del sistema.

        :retorna: Fecha actual, por defecto en formato 'año-mes-día'.
        :tiporetorno: str.
        """
        return datetime.now().strftime(formato)

    def __request(self, url: str, decodificar: str = 'utf-8') -> str:
        """
        Hace una petición HTTP tipo GET hacia determinado URL.

        :parámetro url: URL para hacer la petición.
        :parámetro decodificar: Codec a decodificar, por predeterminado 'utf-8'.
        :retorna: str.
        :tiporetorno: str decodificado.
        """
        try:
            res = get(url)
            res.raise_for_status()
        except rexceptions.HTTPError as err:
            raise err
        return res.content.decode(decodificar)

    def llamadas_107(self, acumulado=False, fecha=None) -> ['fecha', 'cantidad']:
        """
        Cantidad de llamadas 107 hechas de COVID-19.

        :parámetro acumulado: True para obtener el valor acumulado, False para obtener valor diario.
        :parámetro fecha: (opcional) fecha especifica a obtener en formato '12MAY2021'.
        :retorna: fecha y cantidad aplicada.
        :tiporetorno: ['fecha', 'cantidad']
        """
        res = self.__request(URLS['ar']['llamadas_107'])
        csv = reader(res.splitlines())
        lista = list(csv)
        lista.pop(0)

        if not fecha:
            fecha = lista[-1][0][:-9]
            if acumulado:
                sumatoria = 0
                for linea in lista:
                    sumatoria += int(linea[1])
                cantidad = sumatoria
            else:
                cantidad = lista[-1][1]
            return [fecha, cantidad]
        
        if not fecha in res:
            raise FechaNoEncontrada()
        
        if acumulado:
            sumatoria = 0
            for linea in lista:
                sumatoria += int(linea[1])
                if fecha in linea[0]:
                    break
            cantidad = sumatoria
        else:
            for linea in lista:
                if fecha in linea[0]:
                    cantidad = linea[1]
                    break
        return [fecha, cantidad]

    def vacunas_aplicadas(self, dosis='total', acumulado=True, fecha=None) -> ['fecha', 'cantidad']:
        """
        Cantidad de dosis aplicadas nacionalmente.

        :parámetro dosis: Dosis a obtener, por predeterminado 'total'.
        :parámetro acumulado: True para valores acumulados, False para valores diarios.
        :parámetro fecha: (opcional) fecha especifica a obtener.
        :retorna: fecha y cantidad aplicada acumulada/diaria.
        :tiporetorno: ['fecha', 'cantidad']
        """
        url = URLS['ar']['vacunas_aplicadas']['acumulado'][dosis] if acumulado else URLS['ar']['vacunas_aplicadas']['diario'][dosis]
        res = self.__request(url)
        csv = reader(res.splitlines())
        lista = list(csv)
        
        if not fecha:
            return lista[-1]

        if not fecha in res:
            raise FechaNoEncontrada()
        else:
            for linea in lista:
                if fecha in linea:
                    return linea