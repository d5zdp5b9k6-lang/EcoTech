import os
import sqlite3
from datetime import date
from dominio.empleado import Empleado
from infraestructura.empleado_repositorio import EmpleadoRepositorio

def inicializar_base_de_datos():
    ruta_db = os.environ.get("DB_NOMBRE", "ecotech.db")
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))
    ruta_absoluta = os.path.join(directorio_raiz, ruta_db)
    
    conn = sqlite3.connect(ruta_absoluta)
    try:
        with open(os.path.join(directorio_raiz, "db", "01_esquema.sql"), encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
    finally:
        conn.close()

if __name__ == "__main__":
    inicializar_base_de_datos()
    repo = EmpleadoRepositorio()

    print("--- 1. CREAR (INSERT) ---")
    ana = Empleado("12345678-9", "Ana Rojas", date(2024, 3, 1), 950000)
    repo.guardar(ana)
    print("Empleado guardado con éxito.")

    print("\n--- 2. LEER (SELECT) ---")
    emp = repo.obtener("12345678-9")
    print(f"Obtenido: {emp}")
    print(f"Total registrados: {len(repo.listar())}")

    print("\n--- 3. ACTUALIZAR (UPDATE) ---")
    ana.sueldo_base = 1050000
    repo.actualizar(ana)
    print(f"Actualizado: {repo.obtener('12345678-9')}")

    print("\n--- 4. PRUEBA DE INYECCIÓN SQL ---")
    resultado = repo.listar(nombre_contiene="' OR '1'='1")
    print(f"Resultado test inyección: {resultado}")
    if len(resultado) == 0:
        print("✔ PRUEBA SUPERADA: La consulta está correctamente parametrizada.")

    print("\n--- 5. ELIMINAR (DELETE) ---")
    borrado = repo.eliminar("12345678-9")
    print(f"¿Empleado eliminado?: {borrado}")