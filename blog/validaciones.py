# Reglas de validación de los posts

from blog.datos import estados_post


def validar_post(post):
    """Revisa que un post tenga la estructura esperada.
    Devuelve una tupla: (True, "") si está bien, o (False, "mensaje del error") si no."""
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    # Que existan todas las claves obligatorias
    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    # Que título y contenido sean texto y no estén vacíos
    for clave in ["titulo", "contenido"]:
        valor = post.get(clave)
        if not isinstance(valor, str) or valor.strip() == "":
            return False, f'"{clave}" está vacío o no es texto'

    # Que el autor sea un diccionario y tenga el nombre
    autor = post.get("autor")
    if not isinstance(autor, dict):
        return False, '"autor" no es un diccionario'
    if "nombre" not in autor:
        return False, 'al autor le falta la clave "nombre"'

    # Que tags sea una lista
    if not isinstance(post.get("tags"), list):
        return False, '"tags" no es una lista'

    # Que el estado sea uno de los permitidos
    if post.get("estado") not in estados_post:
        return False, f'el estado "{post.get("estado")}" no está en estados_post'

    return True, ""
