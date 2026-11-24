# Operaciones del blog: listar, buscar, filtrar y mostrar la validación

from blog.validaciones import validar_post


def obtener_nombre_autor(post):
    """Devuelve el nombre del autor de un post, o un texto de aviso si no se puede leer."""
    autor = post.get("autor")
    if isinstance(autor, dict):
        return autor.get("nombre", "sin nombre")
    return "sin autor"


def listar_posts(lista):
    """Recibe una lista de posts y muestra el título, el autor y el estado de cada uno."""
    if len(lista) == 0:
        print("No hay posts para mostrar.")
        return
    for post in lista:
        if isinstance(post, dict):
            titulo = post.get("titulo", "(sin título)")
            estado = post.get("estado", "sin estado")
            print(f"- {titulo} | Autor: {obtener_nombre_autor(post)} | Estado: {estado}")
        else:
            print("- (elemento inválido, no es un post)")


def buscar_por_titulo(lista, termino):
    """Devuelve los posts cuyo título contiene el término (sin importar mayúsculas)."""
    termino = termino.lower()
    resultados = []
    for post in lista:
        if isinstance(post, dict):
            titulo = post.get("titulo")
            # Solo comparo si el título es un texto
            if isinstance(titulo, str) and termino in titulo.lower():
                resultados.append(post)
    return resultados


def filtrar_por_tag(lista, tag):
    """Devuelve los posts que tienen ese tag (sin importar mayúsculas)."""
    tag = tag.lower()
    resultados = []
    for post in lista:
        if isinstance(post, dict):
            tags_del_post = post.get("tags")
            # Solo recorro los tags si realmente es una lista
            if isinstance(tags_del_post, list):
                for t in tags_del_post:
                    if isinstance(t, str) and t.lower() == tag:
                        resultados.append(post)
                        break
    return resultados


def mostrar_resultados(encabezado, resultados, mensaje_vacio):
    """Muestra un encabezado y los posts encontrados, o un mensaje si no hay ninguno."""
    if len(resultados) == 0:
        print(mensaje_vacio)
    else:
        print(encabezado)
        listar_posts(resultados)


def mostrar_validacion(lista):
    """Valida cada post de la lista y muestra cuáles están bien y cuáles tienen errores."""
    print("\nResultado de la validación:")
    for numero, post in enumerate(lista, start=1):
        es_valido, mensaje = validar_post(post)
        if es_valido:
            print(f"Post {numero}: válido")
        else:
            print(f"Post {numero}: error - {mensaje}")
