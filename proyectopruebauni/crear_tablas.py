from base_datos.conexion import conectar

def crear_tablas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros(
        codigo TEXT PRIMARY KEY,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        categoria TEXT NOT NULL,
        cantidad INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        identificacion TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL,
        telefono TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prestamos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id TEXT NOT NULL,
        libro_codigo TEXT NOT NULL,
        fecha_prestamo TEXT NOT NULL,
        fecha_devolucion TEXT NOT NULL,
        devuelto INTEGER DEFAULT 0,

        FOREIGN KEY(usuario_id)
        REFERENCES usuarios(identificacion),

        FOREIGN KEY(libro_codigo)
        REFERENCES libros(codigo)
    )
    """)

    cursor.executemany("""
    INSERT OR IGNORE INTO libros
    (codigo, titulo, autor, categoria, cantidad)
    VALUES (?, ?, ?, ?, ?)
    """, [

        ("libro11", "Libro1", "Ana", "Fantasia", 40),
        ("libro22", "Libro2", "Sofia", "Terror", 1),
        ("libro33", "Libro3", "Marco", "Psicologia", 50),
        ("libro44", "Libro4", "Luis", "Miedo", 3),
        ("libro55", "Libro5", "Valeria", "Aventura", 60),
        ("libro66", "Libro6", "Carlos", "Fantasia", 25),
        ("libro77", "Libro7", "Elena", "Romance", 10),
        ("libro88", "Libro8", "Diego", "Ciencia Ficcion", 45),
        ("libro99", "Libro9", "Daniela", "Historia", 5),
        ("libro1010", "Libro10", "Javier", "Misterio", 30),

        ("libro1111", "Libro11", "Andrea", "Fantasia", 8),
        ("libro1212", "Libro12", "Miguel", "Psicologia", 55),
        ("libro1313", "Libro13", "Fernanda", "Miedo", 2),
        ("libro1414", "Libro14", "Jose", "Terror", 18),
        ("libro1515", "Libro15", "Gabriela", "Aventura", 65),
        ("libro1616", "Libro16", "Ricardo", "Historia", 12),
        ("libro1717", "Libro17", "Paula", "Romance", 4),
        ("libro1818", "Libro18", "Kevin", "Ciencia Ficcion", 35),
        ("libro1919", "Libro19", "Natalia", "Fantasia", 70),
        ("libro2020", "Libro20", "Mario", "Misterio", 15),

        ("libro2121", "Libro21", "Camila", "Psicologia", 6),
        ("libro2222", "Libro22", "Esteban", "Terror", 1),
        ("libro2323", "Libro23", "Laura", "Fantasia", 90),
        ("libro2424", "Libro24", "Roberto", "Historia", 20),
        ("libro2525", "Libro25", "Isabel", "Romance", 7),
        ("libro2626", "Libro26", "Fernando", "Aventura", 80),
        ("libro2727", "Libro27", "Melissa", "Miedo", 14),
        ("libro2828", "Libro28", "Oscar", "Psicologia", 22),
        ("libro2929", "Libro29", "Carmen", "Ciencia Ficcion", 95),
        ("libro3030", "Libro30", "Alejandro", "Misterio", 11)

    ])

    conexion.commit()
    conexion.close()