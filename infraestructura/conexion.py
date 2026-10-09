import os
import sqlite3
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()

class ErrorDeConexion(Exception):
    """Excepción para errores de base de datos."""
    pass

@contextmanager
def obtener_conexion():
    nombre_db = os.environ.get("DB_NOMBRE", "ecotech.db")
    directorio_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_absoluta = os.path.join(directorio_raiz, nombre_db)

    conn = None
    try:
        conn = sqlite3.connect(ruta_absoluta)
        conn.execute("PRAGMA foreign_keys = ON;")
        yield conn
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        raise ErrorDeConexion(f"Error en la base de datos: {e}") from e
    finally:
        if conn:
            conn.close()