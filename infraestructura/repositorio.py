from infraestructura.conexion import obtener_conexion

def insertar_departamento(nombre: str, presupuesto: float):
    sql = "INSERT INTO departamentos (nombre, presupuesto) VALUES (?, ?)"
    with obtener_conexion() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (nombre, presupuesto))
        return cursor.lastrowid

def obtener_departamentos():
    sql = "SELECT id, nombre, presupuesto FROM departamentos"
    with obtener_conexion() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

def insertar_empleado(rut: str, nombre: str, email: str, sueldo_base: float, departamento_id: int):
    sql = """
        INSERT INTO empleados (rut, nombre, email, sueldo_base, departamento_id)
        VALUES (?, ?, ?, ?, ?)
    """
    with obtener_conexion() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (rut, nombre, email, sueldo_base, departamento_id))
        return cursor.lastrowid

def obtener_empleados_con_departamento():
    sql = """
        SELECT e.id, e.rut, e.nombre, e.email, e.sueldo_base, d.nombre AS departamento
        FROM empleados e
        LEFT JOIN departamentos d ON e.departamento_id = d.id
    """
    with obtener_conexion() as conn:
        conn.row_factory = sqlite3.Row if 'sqlite3' in globals() else None
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()