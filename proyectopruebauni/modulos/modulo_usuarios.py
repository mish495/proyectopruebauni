from base_datos.conexion import conectar

# ======================================================
# FUNCION: registrar_usuario()
# QUE HACE:
# Registra un nuevo usuario en la biblioteca.
#
# PARA QUE SIRVE:
# Permite almacenar los datos de las personas que
# podrán solicitar préstamos de libros.
#
# QUE CUMPLE DEL PROYECTO:
# - Registrar usuarios.
# - Inserción en SQLite.
# - Validaciones.
# ======================================================

def registrar_usuario():

    identificacion = input("Identificacion: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    telefono = input("Telefono: ")

    conexion = conectar()
    cursor = conexion.cursor()

    # Verifica si ya existe
    cursor.execute("""
    SELECT * FROM usuarios
    WHERE identificacion = ?
    """, (identificacion,))

    if cursor.fetchone():
        print("La identificacion ya existe")
        conexion.close()
        return

    cursor.execute("""
    INSERT INTO usuarios
    VALUES(?,?,?,?)
    """, (
        identificacion,
        nombre,
        correo,
        telefono
    ))

    conexion.commit()
    conexion.close()

    print("Usuario registrado correctamente")


# ======================================================
# FUNCION: consultar_usuarios()
# QUE HACE:
# Muestra todos los usuarios registrados.
#
# QUE CUMPLE:
# - Consulta de datos.
# - Uso de for.
# ======================================================

def consultar_usuarios():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM usuarios")

    usuarios = cursor.fetchall()

    if not usuarios:
        print("No hay usuarios registrados")

    else:

        for usuario in usuarios:

            print(f"""
Identificacion: {usuario[0]}
Nombre: {usuario[1]}
Correo: {usuario[2]}
Telefono: {usuario[3]}
-----------------------------------
""")

    conexion.close()


# ======================================================
# FUNCION: buscar_usuario()
# QUE HACE:
# Busca un usuario por identificación.
#
# QUE CUMPLE:
# - Búsqueda.
# - Uso de if y else.
# ======================================================

def buscar_usuario():

    identificacion = input("Identificacion: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE identificacion = ?
    """, (identificacion,))

    usuario = cursor.fetchone()

    if usuario:

        print(f"""
Identificacion: {usuario[0]}
Nombre: {usuario[1]}
Correo: {usuario[2]}
Telefono: {usuario[3]}
""")

    else:
        print("Usuario no encontrado")

    conexion.close()


# ======================================================
# FUNCION: modificar_usuario()
# QUE HACE:
# Actualiza la información de un usuario.
#
# QUE CUMPLE:
# - UPDATE.
# - Modificación de registros.
# ======================================================

def modificar_usuario():

    identificacion = input(
        "Identificacion del usuario: "
    )

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE identificacion = ?
    """, (identificacion,))

    if not cursor.fetchone():

        print("Usuario no encontrado")
        conexion.close()
        return

    nombre = input("Nuevo nombre: ")
    correo = input("Nuevo correo: ")
    telefono = input("Nuevo telefono: ")

    cursor.execute("""
    UPDATE usuarios
    SET nombre = ?,
        correo = ?,
        telefono = ?
    WHERE identificacion = ?
    """, (
        nombre,
        correo,
        telefono,
        identificacion
    ))

    conexion.commit()
    conexion.close()

    print("Usuario actualizado correctamente")


# ======================================================
# FUNCION: eliminar_usuario()
# QUE HACE:
# Elimina un usuario.
#
# QUE CUMPLE:
# - DELETE.
# - CRUD completo.
# ======================================================

def eliminar_usuario():

    identificacion = input("Identificacion: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE identificacion = ?
    """, (identificacion,))

    if not cursor.fetchone():

        print("Usuario no encontrado")
        conexion.close()
        return

    cursor.execute("""
    DELETE FROM usuarios
    WHERE identificacion = ?
    """, (identificacion,))

    conexion.commit()
    conexion.close()

    print("Usuario eliminado correctamente")


# ======================================================
# FUNCION: menu_usuarios()
# QUE HACE:
# Muestra el menú del módulo de usuarios.
#
# QUE CUMPLE:
# - while
# - if
# - elif
# - else
# ======================================================

def menu_usuarios():

    while True:

        print("\n--- USUARIOS ---")
        print("1. Registrar")
        print("2. Consultar")
        print("3. Buscar")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Volver")

        opcion = input("Opcion: ")

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            consultar_usuarios()

        elif opcion == "3":
            buscar_usuario()

        elif opcion == "4":
            modificar_usuario()

        elif opcion == "5":
            eliminar_usuario()

        elif opcion == "6":
            break

        else:
            print("Opcion invalida")