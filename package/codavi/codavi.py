from csv import reader
from requests import get, exceptions
from datetime import datetime

# Todo import
from .constantes import *
from .excepciones import *
class Codavi:
    """
    Codavi ofrece datos sobre el COVID-19 en toda la Argentina.
    """

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

        :param url: URL para hacer la petición.
        :param decodificar: Codec a decodificar, por predeterminado 'utf-8'.
        :return: str decodificado.
        :treturn: str.
        """
        try:
            res = get(url)
            res.raise_for_status()
        except exceptions.HTTPError as err:
            raise DatosNoActualizados()
        return res.content.decode(decodificar)
    
    def fallecidos(self, sexo='todos', fecha=None):
        """
        Cantidad de fallecidos por COVID-19 en Argentina de manera acumulada.
        
        :param sexo: Filtro por sexo, por defecto 'todos'.
        :param fecha: Fecha a obtener en formato 'año-mes-día'.
        :return: Fecha y cantidad.
        :treturn: ['fecha', 'cantidad']
        """
        if not sexo.lower() in FILTROS['fallecidos'].keys():
            raise SexoDesconocido()
        if not fecha:
            fecha = self.__fecha_actual()
        try:
            res = self.__request(URLS['ar']['casos'] + fecha + '.csv')
        except DatosNoActualizados as err:
            print(err)
            return
        datos = res.splitlines()[1].split(',')
        fecha = datos[0]
        cantidad = datos[FILTROS['fallecidos'][sexo.lower()]]
        return [fecha, cantidad]

    def confirmados(self, sexo='todos', fecha=None):
        """
        Cantidad de casos confirmados en Argentina de manera acumulada.

        :param sexo: Filtro por sexo, por defecto 'todos'.
        :param fecha: Fecha a obtener en formato 'año-mes-día'.
        :return: Fecha y cantidad.
        :treturn: ['fecha', 'cantidad']
        """
        if not sexo.lower() in FILTROS['confirmados'].keys():
            raise SexoDesconocido()
        if not fecha:
            fecha = self.__fecha_actual()
        try:
            res = self.__request(URLS['ar']['casos'] + fecha + '.csv')
        except DatosNoActualizados as err:
            print(err)
            return
        datos = res.splitlines()[1].split(',')
        fecha = datos[0]
        cantidad = datos[FILTROS['confirmados'][sexo.lower()]]
        return [fecha, cantidad]

    def llamadas_107(self, acumulado=False, fecha=None) -> ['fecha', 'cantidad']:
        """
        Cantidad de llamadas 107 hechas de COVID-19.

        :param acumulado: True para obtener el valor acumulado, False para obtener valor diario.
        :param fecha: Fecha especifica a obtener en formato '12MAY2021'.
        :return: Fecha y cantidad.
        :treturn: ['fecha', 'cantidad']
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

        :param dosis: Dosis a obtener, por predeterminado 'total'.
        :param acumulado: True para valores acumulados, False para valores diarios.
        :param fecha: Fecha especifica a obtener en formato 'año-mes-día'.
        :return: Fecha y cantidad aplicada acumulada/diaria.
        :treturn: ['fecha', 'cantidad']
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