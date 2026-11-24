# Menú y manejo de input() con el usuario


def mostrar_menu():
    """Muestra el menú y devuelve la opción elegida como número.
    Si el usuario escribe algo que no es un número, avisa y devuelve None."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    try:
        opcion = int(input("Elegí una opción: "))
        return opcion
    except ValueError:
        # int() falla si el texto no es un número, así el programa no se cierra
        print("Opción inválida: tenés que escribir un número.")
        return None


def pedir_termino():
    """Pide el texto a buscar en los títulos y lo devuelve sin espacios sobrantes."""
    return input("Buscar por titulo: ").strip()


def pedir_tag():
    """Pide el tag a filtrar y lo devuelve sin espacios sobrantes."""
    return input("Filtrar por tag: ").strip()
