import sqlite3
import os
from dotenv import load_dotenv
from infraestructura.conexion import obtener_conexion
from infraestructura.repositorio import (
    insertar_departamento,
    insertar_empleado,
    obtener_empleados_con_departamento
)

load_dotenv()

def inicializar_base_de_datos():
    # Creamos las tablas con execute directo para evitar la falla de executescript
    with obtener_conexion() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                presupuesto REAL DEFAULT 0.0
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rut TEXT NOT NULL UNIQUE,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                sueldo_base REAL NOT NULL,
                departamento_id INTEGER,
                FOREIGN KEY (departamento_id) REFERENCES departamentos(id) ON DELETE SET NULL
            );
        """)
    print("¡Base de datos e infraestructura inicializadas correctamente!")

if __name__ == "__main__":
    # 1. Crear las tablas
    inicializar_base_de_datos()

    # 2. Insertar departamento
    try:
        id_ti = insertar_departamento("Tecnologías de la Información", 5000000.0)
        print(f"¡Departamento TI creado exitosamente con ID: {id_ti}!")
    except Exception as e:
        print(f"Aviso departamento: {e}")
        id_ti = 1

    # 3. Insertar empleado
    try:
        id_emp = insertar_empleado(
            rut="21.456.789-0",
            nombre="Javiera Peña",
            email="javiera.pena@ecotech.cl",
            sueldo_base=950000.0,
            departamento_id=id_ti
        )
        print(f"¡Empleado creado exitosamente con ID: {id_emp}!")
    except Exception as e:
        print(f"Aviso empleado: {e}")

    # 4. Listar
    print("\n--- LISTA DE EMPLEADOS ---")
    empleados = obtener_empleados_con_departamento()
    for emp in empleados:
        print(f"Registro: {emp}")