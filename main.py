from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.registro_tiempo import RegistroTiempo

def main():
    print("=== SISTEMA ECOTECH ===")

    # 1. Crear un departamento
    depto_ti = Departamento(1, "Tecnologías de la Información")

    # 2. Crear un empleado
    emp1 = Empleado(
        rut="21.456.789-0",
        nombre="Javiera Peña",
        email="javiera.pena@ecotech.cl",
        telefono="+56912345678",
        cargo="Desarrolladora Python",
        sueldo_base=850000.0
    )

    # 3. Prueba de encapsulamiento con sueldo negativo
    print("\n--- Prueba de Validación / Encapsulamiento ---")
    emp2 = Empleado(
        rut="11.111.111-1",
        nombre="Carlos Pérez",
        email="carlos@ecotech.cl",
        telefono="+56987654321",
        cargo="Tester QA",
        sueldo_base=-500000.0
    )
    print(f"Sueldo asignado a Carlos: ${emp2.get_sueldo_base()}")
    print("----------------------------------------------\n")

    # 4. Asignar empleado y registros de tiempo
    depto_ti.agregar_empleado(emp1)

    reg1 = RegistroTiempo(101, "2026-09-24", 8.0, "Desarrollo de módulos")
    reg2 = RegistroTiempo(102, "2026-09-25", 7.5, "Pruebas unitarias")

    emp1.agregar_registro_tiempo(reg1)
    emp1.agregar_registro_tiempo(reg2)

    # 5. Imprimir resultados
    print(emp1.mostrar_informacion())
    depto_ti.listar_empleados()
    print(f"Total de horas registradas por {emp1.nombre}: {emp1.calcular_total_horas()} hrs")

if __name__ == "__main__":
    main()