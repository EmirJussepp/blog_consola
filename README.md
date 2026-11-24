# Blog por consola

Sistema de blog que funciona en la consola de Python. Guarda los posts en memoria (sin archivos ni base de datos) y permite consultarlos desde un menú.

Es la versión organizada en módulos y paquetes del blog que fui armando en los módulos anteriores.

## Qué hace

Al ejecutarlo aparece este menú:

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Validar posts
5. Salir
```

- **1. Ver todos los posts:** muestra título, autor y estado de cada post.
- **2. Buscar por titulo:** pide una palabra y muestra los posts cuyo título la contiene (no distingue mayúsculas).
- **3. Filtrar por tag:** pide un tag y muestra los posts que lo tienen (no distingue mayúsculas).
- **4. Validar posts:** revisa la estructura de cada post e indica cuáles son válidos y cuáles tienen errores.
- **5. Salir:** muestra un saludo y termina el programa.

Los posts 4 y 5 tienen errores a propósito (le falta el contenido a uno y el otro tiene un estado inválido) para poder probar la validación.

## Cómo ejecutarlo

Hace falta tener Python instalado. Desde la carpeta raíz del proyecto (donde está `main.py`):

```
python main.py
```

El archivo que se ejecuta es `main.py`. Los demás archivos se importan desde ahí.

## Cómo está organizado

```
blog_consola/
├── main.py
├── README.md
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

| Archivo | Para qué sirve |
|---|---|
| `main.py` | Archivo principal. Importa las partes y coordina el menú según la opción elegida. |
| `blog/__init__.py` | Archivo (vacío) que hace que la carpeta `blog` sea un paquete de Python. |
| `blog/datos.py` | Datos base: `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts`. |
| `blog/menu.py` | Muestra el menú y maneja los `input()` del usuario. |
| `blog/operaciones.py` | Funciones para listar, buscar por título, filtrar por tag y mostrar la validación. |
| `blog/validaciones.py` | Reglas para validar un post (`validar_post`). |
