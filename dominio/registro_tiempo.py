class RegistroTiempo:
    """Clase que registra la jornada u horas trabajadas de un empleado."""

    def __init__(self, id_registro: int, fecha: str, horas_trabajadas: float, descripcion: str):
        self.id_registro = id_registro
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion

    def obtener_resumen(self) -> str:
        """Retorna un resumen del registro de tiempo."""
        return f"[{self.fecha}] {self.horas_trabajadas} hrs - {self.descripcion}"