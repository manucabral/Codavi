class ExcepcionCodavi(Exception):
    def __init__(self, mensaje: str = None):
        mensaje = 'Error fatal en los archivos internos.' if not mensaje else mensaje
        super().__init__(mensaje)

class FechaNoEncontrada(ExcepcionCodavi):
    def __init__(self):
        super().__init__('Fecha no encontrada, prueba otra.')

class VacunaDesconocida(ExcepcionCodavi):
    def __init__(self):
        super().__init__('Vacuna desconocida, lo has escrito bien?')