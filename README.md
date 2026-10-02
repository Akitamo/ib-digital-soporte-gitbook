# Ayuda de Ibermutua Digital Personas

Contenido de la ayuda de Ibermutua Digital Personas en Markdown, sincronizado con GitBook mediante Git Sync: rama `main`, carpeta `help-center`, sitio «Ayuda de Ibermutua Digital Personas», sección Personas. El sitio no está publicado.

Este README describe los ficheros del repositorio, el entorno y los comandos. Las decisiones, el método y el estado del proyecto están fuera del repositorio, en la carpeta del proyecto: `funcionalidades-gitbook/README.md` dice qué documento manda en cada asunto y dónde se retoma el trabajo, y `funcionalidades-gitbook/flujo-de-edicion-y-sincronizacion.md` detalla el procedimiento y el comportamiento comprobado de GitBook.

## Qué hay y cómo se edita

| Ruta | Qué es | Cómo se edita |
|---|---|---|
| `gitbook-docs.yaml` | Estructura del sitio para Git Sync (sección Personas → `help-center`) | A mano; conservar las claves de sección y espacio |
| `help-center/` | Lo único que importa GitBook | — |
| `help-center/.gitbook.yaml` | Configuración del espacio para Git Sync: raíz, portada (`README.md`) y menú (`SUMMARY.md`) | No se toca |
| `help-center/SUMMARY.md` | Menú. La dirección de cada página sigue el menú: grupo, páginas padre y nombre del fichero | A mano |
| `help-center/README.md` | Portada | A mano |
| `help-center/<grupo>/<página>.md` | Páginas de tarea, preguntas frecuentes y referencia | A mano, salvo la parte «Preguntas frecuentes» del cierre de las tareas, que es generada |
| `help-center/preguntas-frecuentes/README.md` | Portada de preguntas frecuentes | **Generada** |
| `help-center/.gitbook/includes/faq-*.md` | Bloques de preguntas por tema | **Generados** |
| `help-center/.gitbook/includes/*.md` (resto) | Bloques reutilizables: un texto compartido por varias páginas | A mano; su catálogo está en `_editorial/mapa-contenido.yaml` |
| `help-center/.gitbook/vars.yaml` | Variables: un mismo dato usado en frases distintas | A mano. Al fusionar una solicitud de cambio en GitBook vuelve sin comentarios. Dónde sale un valor: `grep -rn "vars.<nombre>" help-center` y, si sale en un bloque, las páginas que lo incluyen |
| `help-center/.gitbook/assets/` | Imágenes | Recortes nuevos con nombre propio; no sobrescribir originales |
| `_editorial/` | Material de trabajo; GitBook no lo importa | — |
| `_editorial/indice-contenido.yaml` | Fuente: tipo, temas y preguntas que muestra cada página (`faq_tema`, `cierre`); secciones de la portada de preguntas (`portada_faq`) | A mano; después, `generar_faq.py` |
| `_editorial/mapa-contenido.yaml` | Fuente: origen de cada página en Confluence, relaciones entre páginas y catálogo de bloques y variables | A mano |
| `_editorial/pendientes.yaml` | Fuente de los pendientes de contenido | A mano; después, `generar_pendientes.py` |
| `_editorial/pendientes.md` | Lista de pendientes con enlaces a GitBook | **Generada** |
| `_editorial/enlaces-contextuales.csv` | Catálogo de enlaces a anclas desde correos, app y atención | A mano; el validador comprueba sus anclas |
| `_editorial/correspondencia.csv` | Página de Confluence → página nueva; base de las redirecciones | Se revisa al preparar la publicación |
| `_editorial/guia-estilo-gitbook.md` | Copia de la guía de estilo del sitio (reglas SG) | Manda la guía en GitBook: se cambia allí y se copia aquí el mismo día |
| `_editorial/guia-de-estilo.md` | Convenciones de ficheros, nombres, imágenes y anclas | A mano |
| `_editorial/plantillas/tarea.md` | Esqueleto de una página de tarea | A mano; sus criterios están en el documento maestro |
| `_editorial/configuracion-sitio.md` | Copia de la configuración que solo existe en GitBook | Manda GitBook: se cambia allí y se copia aquí el mismo día |
| `herramientas/` | Generadores y validador | — |

## Partes generadas: no se editan a mano

| Parte | Fuente | Comando |
|---|---|---|
| Bloques `help-center/.gitbook/includes/faq-<tema>.md` | Temas de las preguntas en `indice-contenido.yaml` | `generar_faq.py` |
| Parte «Preguntas frecuentes» del cierre «Más sobre…» de cada tarea (y el encabezado, si el cierre se queda vacío o hay que crearlo) | `faq_tema` y `cierre` de la tarea en `indice-contenido.yaml` | `generar_faq.py` |
| Portada de preguntas frecuentes | `portada_faq` en `indice-contenido.yaml` | `generar_faq.py` |
| `_editorial/pendientes.md` | `_editorial/pendientes.yaml` y los marcadores «Imagen de la app que falta» | `generar_pendientes.py` |

El resto del cierre («También te puede interesar») se edita a mano. Cuando un tema recibe su primera pregunta, `generar_faq.py` crea su bloque y añade la parte de preguntas al cierre de todas las tareas con ese `faq_tema` (con el encabezado de `cierre` si la tarea no lo tiene): revisar ese diff. Si un tema se queda sin preguntas, `generar_faq.py` avisa de que su bloque sobra: se borra con `git rm`.

## Entorno

- Python 3.10 o superior con PyYAML (`herramientas/requirements.txt`).
- **Intérprete comprobado el 02/10/2026** en el equipo de Sergio: Python 3.12.8 con PyYAML 6.0.2, en `%LOCALAPPDATA%\Programs\Python\Python312\python.exe`. Funciona desde PowerShell 5.1 y desde CMD en la sesión de Sergio, también a través de Desktop Commander; ahí `python` y `py -3.12` llegan a ese intérprete. En el entorno Linux de Claude se usa `python3` (3.10.12 con PyYAML).
- Si `python` no se encuentra (otro usuario o un entorno aislado sin ese PATH), usar la ruta completa. Si tampoco existe, ese entorno no tiene el intérprete: instalar Python 3.10 o superior y las dependencias, o ejecutar las comprobaciones en la sesión de Sergio.
- **Git solo desde Windows,** en esta carpeta y con las credenciales de Sergio. Ejecutar git desde un entorno Linux que monta la carpeta deja `.git/index.lock` y bloquea el repositorio.

Preparar la consola, desde la raíz del repositorio:

| Consola | Tildes en la salida | Intérprete | Dependencias |
|---|---|---|---|
| PowerShell | `$env:PYTHONIOENCODING = "utf-8"` | `$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"`; se ejecuta con `& $py` | `& $py -m pip install -r herramientas\requirements.txt` |
| CMD | `set PYTHONIOENCODING=utf-8` | `set PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe`; se ejecuta con `"%PY%"` | `"%PY%" -m pip install -r herramientas\requirements.txt` |
| Linux (entorno de Claude) | No hace falta | `python3` | Instaladas |

## Comandos

Desde la raíz del repositorio, en este orden. En la tabla, `python` es el intérprete de la consola: `& $py` en PowerShell, `"%PY%"` en CMD y `python3` en Linux.

| Comando | Qué hace | ¿Modifica ficheros? |
|---|---|---|
| `python herramientas/generar_faq.py` | Bloques de preguntas por tema, parte de preguntas del cierre de las tareas y portada de preguntas | Sí. Con `--comprobar`, solo comprueba |
| `python herramientas/generar_pendientes.py` | `_editorial/pendientes.md` | Sí. Con `--comprobar`, solo comprueba |
| `python herramientas/validar.py` | Menú, enlaces, imágenes, anclas, bloques y su estructura, variables, índice, preguntas al día, catálogo de enlaces y coherencia de pendientes | No. Sale con 1 si hay errores |

Python crea `herramientas/__pycache__/`, que Git ignora; con `-B` no se escribe nada. Comprobación completa sin escribir ficheros (probada el 02/10 en las dos consolas):

```powershell
# PowerShell
$env:PYTHONIOENCODING = "utf-8"
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
& $py -B herramientas\generar_faq.py --comprobar
& $py -B herramientas\generar_pendientes.py --comprobar
& $py -B herramientas\validar.py
```

```bat
:: CMD
set PYTHONIOENCODING=utf-8
set PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe
"%PY%" -B herramientas\generar_faq.py --comprobar
"%PY%" -B herramientas\generar_pendientes.py --comprobar
"%PY%" -B herramientas\validar.py
```

Antes de cada subida, `validar.py` debe terminar en «Resultado: correcto» y `git diff --stat` solo debe mostrar los ficheros previstos.

`validar.py` no comprueba que las relaciones del mapa estén enlazadas, la pertinencia de un enlace o de un cierre, los destinos de `correspondencia.csv`, las imágenes sin uso ni el catálogo de `mapa-contenido.yaml` (dónde se usan bloques y variables).

## Subir y comprobar

1. Commit con un mensaje que explique qué cambia y por qué; `git push` a `main` desde Windows.
2. GitBook importa en alrededor de un minuto. Comprobar con el MCP de GitBook: `getSpaceById` (estado de `gitSync.operation`) y `get_page` de las páginas afectadas.
3. Revisar en app.gitbook.com: el enlace de vista previa caduca.

## Cambios desde GitBook

El contenido se edita en este repositorio. Si se cambia algo en GitBook, solo en partes no generadas y con una solicitud de cambio. Al fusionarla, GitBook la devuelve a `main` normalizada y sin comentarios HTML. Después hay que actualizar la copia local y ejecutar los generadores y el validador.

No se usan comentarios HTML en `help-center`: GitBook los elimina. Los pendientes van en `_editorial/pendientes.yaml`.

## Lo que no se hace sin autorización de Sergio

Publicar el sitio, fusionar borradores de GitBook (el #1 y el #2 están desactualizados) o cambiar la configuración del sitio. Ninguna captura ni texto puede mostrar nombres, diagnósticos, números de historia ni documentos reales (regla SG-24).
