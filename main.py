# Archivo principal del blog por consola: coordina las partes del sistema
# Cómo ejecutarlo (desde esta carpeta): python main.py

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_termino, pedir_tag
from blog.operaciones import (
    listar_posts,
    buscar_por_titulo,
    filtrar_por_tag,
    mostrar_resultados,
    mostrar_validacion,
)


def main():
    """Muestra el menú en bucle y llama a la función que corresponde a cada opción."""
    # El bucle while mantiene el programa activo hasta que el usuario elija salir
    while True:
        opcion = mostrar_menu()

        if opcion is None:
            # El usuario escribió texto en lugar de un número: se vuelve a mostrar el menú
            continue

        if opcion == 1:
            print("\nPosts disponibles:")
            listar_posts(posts)

        elif opcion == 2:
            termino = pedir_termino()
            if termino == "":
                print("La búsqueda no puede estar vacía.")
            else:
                encontrados = buscar_por_titulo(posts, termino)
                mostrar_resultados("\nResultados de la búsqueda:", encontrados,
                                   "No se encontraron posts con ese título.")

        elif opcion == 3:
            tag = pedir_tag()
            if tag == "":
                print("El tag no puede estar vacío.")
            else:
                encontrados = filtrar_por_tag(posts, tag)
                mostrar_resultados(f"\nPosts con el tag {tag}:", encontrados,
                                   "No hay posts con ese tag.")

        elif opcion == 4:
            mostrar_validacion(posts)

        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo")


if __name__ == "__main__":
    main()
