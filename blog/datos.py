# Datos base del blog (los mismos de los módulos anteriores)
# Este módulo no importa nada de los otros, así se evitan los imports circulares.

# Diccionario con los datos del autor, incluye una lista de redes sociales
perfil_autor = {
    "nombre": "Emir Jussepp",
    "bio": "Estudiante de programación que aprende Python y desarrollo web.",
    "especialidad": "Python y desarrollo web",
    "redes_sociales": ["@emir_dev", "@emir_python"]
}

# Tupla con los estados posibles de un post (valores fijos)
estados_post = ("borrador", "publicado", "archivado")

# Set de etiquetas: "Python" está repetida a propósito, el set la guarda una sola vez
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

# Lista de posts. Los posts 4 y 5 tienen errores a propósito para probar la validación
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "Django es un framework web creado con Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con listas",
        "contenido": "Las listas permiten guardar varios elementos en una sola variable.",
        "autor": perfil_autor,
        "tags": ["Python", "Listas"],
        "estado": "archivado"
    },
    {
        # Error a propósito: le falta la clave "contenido"
        "id": 4,
        "titulo": "Funciones en Python",
        "autor": perfil_autor,
        "tags": ["Python", "Funciones"],
        "estado": "borrador"
    },
    {
        # Error a propósito: el estado "pendiente" no está en estados_post
        "id": 5,
        "titulo": "Errores comunes al programar",
        "contenido": "Leer bien el mensaje de error ayuda a encontrar el problema.",
        "autor": perfil_autor,
        "tags": ["Python", "Errores"],
        "estado": "pendiente"
    }
]
