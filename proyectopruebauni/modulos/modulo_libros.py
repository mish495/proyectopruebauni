from proyectopruebauni.base_datos.conexion import conectar


# ======================================================
# FUNCION: registrar_libro()
# QUE HACE:
# Registra un nuevo libro en la base de datos.
#
# QUE CUMPLE:
# - CRUD (Create)
# - Validaciones
# - try-except
# - SQLite
# ======================================================


def registrar_libro():

    try:

        codigo = input("Codigo: ")
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")
        cantidad = int(input("Cantidad: "))

        if cantidad < 0:
            print("La cantidad no puede ser negativa")
            return

        conexion = conectar()
        cursor = conexion.cursor()

        # Verifica si el código ya existe
        cursor.execute(
            """
        SELECT * FROM libros
        WHERE codigo = ?
        """,
            (codigo,),
        )

        if cursor.fetchone():
            print("Ese codigo ya existe")
            conexion.close()
            return

        cursor.execute(
            """
        INSERT INTO libros
        VALUES (?, ?, ?, ?, ?)
        """,
            (codigo, titulo, autor, categoria, cantidad),
        )

        conexion.commit()

        print("Libro registrado correctamente")

    except ValueError:
        print("La cantidad debe ser numerica")

    except Exception as e:
        print("Error:", e)

    finally:
        try:
            conexion.close()
        except Exception:
            pass


# ======================================================
# FUNCION: consultar_libros()
# QUE HACE:
# Muestra todos los libros registrados.
#
# QUE CUMPLE:
# - CRUD (Read)
# - SELECT
# - ciclo for
# ======================================================


def consultar_libros():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM libros
    """)

    libros = cursor.fetchall()

    if not libros:
        print("No hay libros registrados")

    else:

        print("\n========== LIBROS ==========")

        for libro in libros:

            print(f"""
Codigo: {libro[0]}
Titulo: {libro[1]}
Autor: {libro[2]}
Categoria: {libro[3]}
Cantidad: {libro[4]}
-----------------------------------
""")

    conexion.close()


# ======================================================
# FUNCION: buscar_libro()
# QUE HACE:
# Busca un libro por código.
#
# QUE CUMPLE:
# - Consultas específicas
# - if y else
# ======================================================


def buscar_libro():

    codigo = input("Codigo del libro: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
    SELECT * FROM libros
    WHERE codigo = ?
    """,
        (codigo,),
    )

    libro = cursor.fetchone()

    if libro:

        print(f"""
Codigo: {libro[0]}
Titulo: {libro[1]}
Autor: {libro[2]}
Categoria: {libro[3]}
Cantidad: {libro[4]}
""")

    else:
        print("Libro no encontrado")

    conexion.close()


# ======================================================
# FUNCION: modificar_libro()
# QUE HACE:
# Actualiza la información de un libro.
#
# QUE CUMPLE:
# - CRUD (Update)
# - UPDATE
# ======================================================


def modificar_libro():

    codigo = input("Codigo del libro a modificar: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
    SELECT * FROM libros
    WHERE codigo = ?
    """,
        (codigo,),
    )

    libro = cursor.fetchone()

    if not libro:

        print("Libro no encontrado")
        conexion.close()
        return

    try:

        titulo = input("Nuevo titulo: ")
        autor = input("Nuevo autor: ")
        categoria = input("Nueva categoria: ")
        cantidad = int(input("Nueva cantidad: "))

        if cantidad < 0:
            print("Cantidad invalida")
            conexion.close()
            return

        cursor.execute(
            """
        UPDATE libros
        SET titulo = ?,
            autor = ?,
            categoria = ?,
            cantidad = ?
        WHERE codigo = ?
        """,
            (titulo, autor, categoria, cantidad, codigo),
        )

        conexion.commit()

        print("Libro actualizado correctamente")

    except ValueError:
        print("La cantidad debe ser numerica")

    finally:
        conexion.close()


# ======================================================
# FUNCION: eliminar_libro()
# QUE HACE:
# Elimina un libro.
#
# QUE CUMPLE:
# - CRUD (Delete)
# - DELETE
# ======================================================


def eliminar_libro():

    codigo = input("Codigo del libro: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
    SELECT * FROM libros
    WHERE codigo = ?
    """,
        (codigo,),
    )

    libro = cursor.fetchone()

    if not libro:

        print("Libro no encontrado")
        conexion.close()
        return

    confirmar = input("Desea eliminar este libro? (S/N): ")

    if confirmar.upper() != "S":

        print("Operacion cancelada")
        conexion.close()
        return

    cursor.execute(
        """
    DELETE FROM libros
    WHERE codigo = ?
    """,
        (codigo,),
    )

    conexion.commit()
    conexion.close()

    print("Libro eliminado correctamente")


# ======================================================
# FUNCION: menu_libros()
# QUE HACE:
# Muestra el menú del módulo de libros.
#
# QUE CUMPLE:
# - while
# - if
# - elif
# - else
# ======================================================


def menu_libros():

    while True:

        print("\n===== MODULO LIBROS =====")
        print("1. Registrar libro")
        print("2. Consultar libros")
        print("3. Buscar libro")
        print("4. Modificar libro")
        print("5. Eliminar libro")
        print("6. Volver")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_libro()

        elif opcion == "2":
            consultar_libros()

        elif opcion == "3":
            buscar_libro()

        elif opcion == "4":
            modificar_libro()

        elif opcion == "5":
            eliminar_libro()

        elif opcion == "6":
            break

        else:
            print("Opcion invalida")
