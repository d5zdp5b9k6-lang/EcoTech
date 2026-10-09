CREATE TABLE IF NOT EXISTS persona (
    rut TEXT PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS empleado (
    rut TEXT PRIMARY KEY,
    fecha_ingreso TEXT NOT NULL,
    sueldo_base REAL NOT NULL,
    FOREIGN KEY (rut) REFERENCES persona(rut) ON DELETE CASCADE
);