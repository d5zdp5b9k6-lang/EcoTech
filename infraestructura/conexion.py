import os
import sqlite3
from contextlib import contextmanager
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

class ErrorDeConexion(Exception):
    """Excepción para errores de base de datos."""
    pass

@contextmanager
def obtener_conexion():
    ruta_db = os.environ.get("DB_NOMBRE")
    if not ruta_db:
        raise ErrorDeConexion("Falta la variable DB_NOMBRE en el archivo .env")
    
    conn = None
    try:
        conn = sqlite3.connect(ruta_db)
        conn.execute("PRAGMA foreign_keys = ON;")  # Activa llaves foráneas
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        raise ErrorDeConexion(f"Error en la base de datos: {e}") from e
    finally:
        if conn:
            conn.close()