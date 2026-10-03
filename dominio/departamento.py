class Departamento:
    """Representa un departamento de la empresa EcoTech."""

    def __init__(self, id_departamento: int, nombre: str):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        """Asigna un empleado a este departamento."""
        self.empleados.append(empleado)

    def listar_empleados(self):
        """Muestra la lista de empleados asociados al departamento."""
        print(f"--- Empleados en {self.nombre} ---")
        for emp in self.empleados:
            print(f"- {emp.nombre} ({emp.cargo})")