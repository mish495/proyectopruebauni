from base_datos.conexion import conectar

# ======================================================
# FUNCION: registrar_prestamo()
# QUE HACE:
# Registra el préstamo de un libro a un usuario.
#
# PARA QUE SIRVE:
# Permite llevar el control de qué usuario tiene
# prestado un libro y reduce la cantidad disponible.
#
# QUE CUMPLE DEL PROYECTO:
# - Registro de préstamos.
# - Uso de SQLite.
# - Relaciones entre tablas.
# - Validaciones.
# ======================================================

def registrar_prestamo():

    usuario = input("ID Usuario: ")
    libro = input("Codigo Libro: ")
    fecha_prestamo = input("Fecha Prestamo: ")
    fecha_devolucion = input("Fecha Devolucion: ")

    conexion = conectar()
    cursor = conexion.cursor()

    # Verifica que el usuario exista
    cursor.execute("""
    SELECT * FROM usuarios
    WHERE identificacion = ?
    """, (usuario,))

    if not cursor.fetchone():
        print("Usuario no encontrado")
        conexion.close()
        return

    # Verifica que el libro exista
    cursor.execute("""
    SELECT * FROM libros
    WHERE codigo = ?
    """, (libro,))

    datos_libro = cursor.fetchone()

    if not datos_libro:
        print("Libro no encontrado")
        conexion.close()
        return

    # Verifica disponibilidad
    if datos_libro[4] <= 0:
        print("No hay existencias disponibles")
        conexion.close()
        return

    # Registra el préstamo
    cursor.execute("""
    INSERT INTO prestamos(
    usuario_id,
    libro_codigo,
    fecha_prestamo,
    fecha_devolucion)
    VALUES(?,?,?,?)
    """, (
        usuario,
        libro,
        fecha_prestamo,
        fecha_devolucion
    ))

    # Reduce la cantidad disponible
    cursor.execute("""
    UPDATE libros
    SET cantidad = cantidad - 1
    WHERE codigo = ?
    """, (libro,))

    conexion.commit()
    conexion.close()

    print("Prestamo registrado correctamente")


# ======================================================
# FUNCION: consultar_prestamos()
# QUE HACE:
# Muestra todos los préstamos registrados.
#
# QUE CUMPLE:
# - Consulta de datos.
# - Uso de for.
# ======================================================

def consultar_prestamos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM prestamos
    """)

    prestamos = cursor.fetchall()

    if not prestamos:
        print("No hay prestamos registrados")

    else:
        for prestamo in prestamos:
            print(prestamo)

    conexion.close()


# ======================================================
# FUNCION: menu_prestamos()
# QUE HACE:
# Muestra el menú del módulo de préstamos.
#
# QUE CUMPLE:
# - while
# - if
# - elif
# - else
# ======================================================

def menu_prestamos():

    while True:

        print("\n--- PRESTAMOS ---")
        print("1. Registrar Prestamo")
        print("2. Consultar Prestamos")
        print("3. Volver")

        opcion = input("Opcion: ")

        if opcion == "1":
            registrar_prestamo()

        elif opcion == "2":
            consultar_prestamos()

        elif opcion == "3":
            break

        else:
            print("Opcion invalida")