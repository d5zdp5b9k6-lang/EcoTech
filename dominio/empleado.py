from .persona import Persona

class Empleado(Persona):
    """Clase que representa a un empleado de EcoTech."""

    def __init__(self, rut: str, nombre: str, email: str, telefono: str, cargo: str, sueldo_base: float):
        super().__init__(rut, nombre, email, telefono)
        self.cargo = cargo
        self.set_sueldo_base(sueldo_base)
        self.registros_tiempo = []

    def set_sueldo_base(self, valor: float):
        """Invariante: El sueldo base jamás puede ser negativo."""
        if valor < 0:
            print("⚠️ Advertencia: El sueldo no puede ser negativo. Se asignará 0.0.")
            self._sueldo_base = 0.0
        else:
            self._sueldo_base = float(valor)

    def get_sueldo_base(self) -> float:
        """Devuelve el sueldo base resguardado."""
        return self._sueldo_base

    def agregar_registro_tiempo(self, registro):
        self.registros_tiempo.append(registro)

    def calcular_total_horas(self) -> float:
        return sum(reg.horas_trabajadas for reg in self.registros_tiempo)