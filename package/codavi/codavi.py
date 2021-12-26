from csv import reader
from requests import get, exceptions
from datetime import datetime
import pandas as pd

# Todo import
from .constantes import *
from .excepciones import *
class Codavi:
    """
    Codavi ofrece datos y estadísticas sobre el COVID-19 en toda la Argentina.
    """

    def __fecha_actual(self, formato: str = '%Y-%m-%d') -> str:
        """
        Obtiene la fecha actual del sistema.

        :retorna: Fecha actual, por defecto en formato 'año-mes-día'.
        :tiporetorno: str.
        """

        return datetime.now().strftime(formato)

    def __request(self, url: str, contenido: bool = False, decodificar: str = 'utf-8') -> str:
        """
        Hace una petición HTTP tipo GET hacia determinado URL.

        :param url: URL para hacer la petición.
        :param contenido: True para obtener el contenido crudo, false para decodificarlo.
        :param decodificar: Codec a decodificar, por predeterminado 'utf-8'.
        :return: str decodificado.
        :treturn: str.
        """

        try:
            res = get(url)
            res.raise_for_status()
        except exceptions.HTTPError as err:
            raise DatosNoActualizados()
        return res if contenido else res.content.decode(decodificar)
    
    def fallecidos(self, sexo: str = 'todos', fecha: str = None):
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

    def confirmados(self, sexo: str = 'todos', fecha: str = None):
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

    def llamadas_107(self, acumulado: bool = False, fecha: str = None) -> ['fecha', 'cantidad']:
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
                if fecha    in linea[0]:
                    cantidad = linea[1]
                    break
        return [fecha, cantidad]
    
    def vacuna(self, nombre: str = None, dosis: str = 'total') -> ['fecha', 'nombre', 'dosis', 'cantidad']:            
        """
        Cantidad de dosis aplicadas por vacuna nacionalmente.

        :param nombre: Nombre de la vacuna a obtener.
        :param dosis: Tipo de dosis a obtener, por defecto 'total'.
        :return: Fecha, nombre de la vacuna, tipo de dosis y cantidad aplicada.
        :treturn: ['fecha', 'nombre', 'dosis', 'cantidad']
        """

        if not nombre:
            raise VacunaDesconocida()
        datos = pd.read_csv(URLS['ar']['vacunas'])
        vacuna_filtrada = datos.query(f'vacuna_nombre.str.lower().str.contains("{nombre.lower()}")')
        hoy = self.__fecha_actual()

        if vacuna_filtrada.empty:
            raise VacunaDesconocida()
        
        if dosis == 'total':
            primera, segunda = self.vacuna(nombre=nombre, dosis='primera')[3], self.vacuna(nombre=nombre, dosis='segunda')[3]
            unica, refuerzo = self.vacuna(nombre=nombre, dosis='unica')[3], self.vacuna(nombre=nombre, dosis='refuerzo')[3]
            adicional = self.vacuna(nombre=nombre, dosis='adicional')[3]
            return [hoy, nombre, 'total', primera + segunda + unica + refuerzo + adicional]
        
        if not dosis in FILTROS['dosis']:
            raise DosisDesconocida()
        
        dosis = FILTROS['dosis'][dosis]
        nombre = vacuna_filtrada['vacuna_nombre'].values[0]
        total = vacuna_filtrada[dosis].sum()

        return [hoy, nombre, dosis, total]
             
    def dosis(self, numero: str = 'total', acumulado: bool = True, fecha: str = None) -> ['fecha', 'cantidad']:
        """
        Cantidad de dosis aplicadas nacionalmente.

        :param numero: Tipo de dosis a obtener, por predeterminado 'total'.
        :param acumulado: True para valores acumulados, False para valores diarios.
        :param fecha: Fecha especifica a obtener en formato 'año-mes-día'.
        :return: Fecha y cantidad de dosis aplicadas acumulada/diaria.
        :treturn: ['fecha', 'cantidad']
        """

        url = URLS['ar']['dosis']['acumulado'][numero] if acumulado else URLS['ar']['dosis']['diario'][numero]
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