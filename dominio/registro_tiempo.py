class RegistroTiempo:
    """Registra las horas trabajadas por un empleado en una fecha determinada."""

    def __init__(self, fecha: str, horas: float, descripcion: str = ""):
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion

    def __str__(self):
        return f"Registro({self.fecha}: {self.horas} hrs - {self.descripcion})"