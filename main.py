from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.registro_tiempo import RegistroTiempo

def main():
    # 1. Crear Departamento
    dep = Departamento("Operaciones")

    # 2. Crear Empleado
    javiera = Empleado("12345678-9", "javiera peña", "2024-03-01", 950_000)

    # 3. Asignar empleado al departamento
    dep.agregar_empleado(javiera)

    # 4. Registrar horas de trabajo
    reg1 = RegistroTiempo("2026-03-20", 4.5, "Desarrollo de prototipo EcoTech")
    reg2 = RegistroTiempo("2026-03-21", 3.0, "Pruebas de software")
    javiera.registrar_hora(reg1)
    javiera.registrar_hora(reg2)

    # 5. Imprimir información de prueba
    print(dep)
    print(javiera)
    print(f"Horas registradas por {javiera.nombre}: {javiera.total_horas()} hrs")

if __name__ == "__main__":
    main()