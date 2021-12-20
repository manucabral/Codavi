from csv import reader
from requests import get
from datetime import datetime
from .constantes import *

class Codavi:
    def __fecha_actual(self) -> str:
        """
        Obtiene la fecha actual del sistema.

        :retorna: Fecha actual en formato 'año-mes-día'.
        :tiporetorno: str.
        """
        return datetime.now().strftime('%Y-%m-%d')

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

    def aplicadas(self, dosis='total', acumulado=True, fecha=None) -> ['fecha', 'total']:
        """
        Cantidad de dosis aplicadas acumuladas nacionalmente.

        :parámetro dosis: Dosis a obtener, por predeterminado 'total'.
        :parámetro acumulado: True para valores acumulados, False para valores diarios.
        :parámetro fecha: (opcional) fecha especifica a obtener.
        :retorna: fecha y cantidad aplicada acumulada.
        :tiporetorno: ['fecha', 'total']
        """
        if not fecha:
            fecha = self.__fecha_actual()
        url = URL_DOSIS_ACUMULADOS[dosis] if acumulado else URL_DOSIS_DIARIAS[dosis]
        res = self.__request(url)
        csv = reader(res.splitlines())
        lista = list(csv)
        if not fecha in res:
            return lista[-1]
        else:
            for linea in lista:
                if fecha in linea:
                    return linea