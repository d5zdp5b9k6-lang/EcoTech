class Persona:
    """Clase base que representa a una persona en el sistema EcoTech."""

    def __init__(self, rut: str, nombre: str, email: str, telefono: str):
        self.rut = rut
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def mostrar_informacion(self) -> str:
        """Devuelve una cadena con los datos básicos de la persona."""
        return f"RUT: {self.rut} | Nombre: {self.nombre} | Email: {self.email} | Teléfono: {self.telefono}"