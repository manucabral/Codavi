class ExcepcionCodavi(Exception):
    def __init__(self, mensaje: str = None):
        mensaje = 'Error fatal en los archivos internos.' if not mensaje else mensaje
        super().__init__(mensaje)
class DatosNoActualizados(ExcepcionCodavi):
    def __init__(self):
        super().__init__('No hay datos actualizados para hoy.')
class FechaNoEncontrada(ExcepcionCodavi):
    def __init__(self):
        super().__init__('Fecha no encontrada, prueba otra.')
class VacunaDesconocida(ExcepcionCodavi):
    def __init__(self):
        super().__init__('Vacuna desconocida, lo has escrito bien?')
class DosisDesconocida(ExcepcionCodavi):
    def __init__(self):
        super().__init__('Dosis desconocida, intenta poner otra dosis.')     
class SexoDesconocido(ExcepcionCodavi):
    def __init__(self):
        super().__init__('Sexo desconocido')