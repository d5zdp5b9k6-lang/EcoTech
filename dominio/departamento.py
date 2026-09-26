class Departamento:
    """Representa un departamento de la empresa EcoTech."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.empleados = []  # Cardinalidad 0..* (lista de empleados)

    def agregar_empleado(self, empleado):
        """Asigna un empleado a este departamento."""
        self.empleados.append(empleado)
        empleado.departamento = self  # Relación bidireccional

    def __str__(self):
        return f"Departamento: {self.nombre} (Total empleados: {len(self.empleados)})"