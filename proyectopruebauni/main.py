# ======================================================
# IMPORTACIONES
# ======================================================

from crear_tablas import crear_tablas

from modulos.modulo_libros import menu_libros
from modulos.modulo_usuarios import menu_usuarios
from modulos.modulo_prestamos import menu_prestamos


# ======================================================
# FUNCION: main()
# QUE HACE:
# Controla el funcionamiento general del sistema.
#
# PARA QUE SIRVE:
# Permite acceder a los módulos de libros,
# usuarios y préstamos.
#
# QUE CUMPLE DEL PROYECTO:
# - Uso de funciones.
# - Menú principal.
# - Uso de while.
# - Uso de if, elif y else.
# ======================================================

def main():

    # Crea las tablas si no existen
    crear_tablas()

    while True:

        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Libros")
        print("2. Usuarios")
        print("3. Prestamos")
        print("4. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            menu_libros()

        elif opcion == "2":
            menu_usuarios()

        elif opcion == "3":
            menu_prestamos()

        elif opcion == "4":
            print("Hasta luego")
            break

        else:
            print("Opcion invalida")


# ======================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ======================================================

if __name__ == "__main__":
    main()