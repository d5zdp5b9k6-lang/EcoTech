class Persona:
    """Representa a una persona en el sistema de EcoTech."""

    def __init__(self, rut: str, nombre: str):
        self.rut = rut  # RUT como string para no perder digito verificador ni ceros a la izquierda
        self.nombre = nombre

    def __str__(self):
        return f"Persona(RUT: {self.rut}, Nombre: {self.nombre})"