import salas
import estadisticas

def menu_principal():
    """
    Muestra el menú principal y devuelve la opción seleccionada.
    """
    print("""
    Bienvenido al sistema de gestión de cine.
    Seleccione una opción:
    1 - Crear usuario
    2 - Salir
    """)
    opcion = int(input("Ingrese su opción: "))
    return opcion

def imprimir_funciones_admin():
    """
    Imprime las funciones disponibles para el administrador.

    Se accede escribiendo "admin" como nombre de usuario.
    """
    print("""
    Funciones disponibles:
    1 - Gestionar cartelera
    2 - Cambiar precio de entradas
    3 - Crear sala de cine
    4 - Mostrar estadisticas
    5 - salir
    """)
    eleccion = input("Ingrese su opción: ")
    return eleccion

def imprimir_funciones_usuario():
    """
    Imprime las funciones disponibles para el usuario. Permitiendo al usuario ver la cartelera y comprar entradas.
    
    Al escribir "admin" abre el menu para administradores.
    """
    print("""
    Funciones disponibles:
    1 - Mostar cartelera
    2 - Comprar entradas
    3 - Salir
    """)
    eleccion = input("Ingrese su opción: ")
    return eleccion


"""
------------------------------------------------------------------------------------------------------------
"""


def main():
    opcion = menu_principal()
    while opcion != 2:
        if opcion == 1:
            usuario = input("Ingrese su nombre de usuario: ")
            if usuario == "admin":
                imprimir_funciones_admin()
            else:
                print("\nBienvenido!", usuario)
                funciones_usuario = imprimir_funciones_usuario()
        else:
            print("Opción inválida. Intente nuevamente.")
        opcion = menu_principal()

    print("Saliendo del sistema...")

main()