# Material editorial (no publicado)

Esta carpeta está fuera de `help-center/`, que es la única que GitBook importa. Nada de aquí se publica ni aparece en llms.txt ni en el MCP.

| Archivo | Uso |
|---|---|
| `guia-estilo-gitbook.md` | Copia de la guía de estilo del sitio en GitBook (reglas SG-n) |
| `guia-de-estilo.md` | Catálogo de bloques y convenciones |
| `plantillas/tarea.md` | Plantilla de artículo de tarea. Referencia: «Consultar tus citas» (`citas-y-asistencias/consultar-tus-citas.md`, la copia aprobada) |
| `configuracion-asistente.md` | Instrucciones, saludo y preguntas del asistente |
| `inventario-componentes.md` | Bloques reutilizables, variables y anclas fijas |
| `enlaces-contextuales.csv` | Catálogo de enlaces para correos, pantallas de la app y respuestas de atención |
| `correspondencia.csv` | Página original (Scroll) → página nueva → tipo → responsable → estado. Base de las redirecciones |
| `indice-contenido.yaml` | Páginas migradas: tipo, temas, bloque de preguntas (`faq_tema`) e intenciones que resuelven |
| `mapa-contenido.yaml` | Plan de las 82 páginas: destino, relaciones, bloques y variables previstos. Cada entrada pasa al índice al migrar su página |
| `pendientes.yaml` | Fuente de los pendientes del borrador: contradicciones, valores provisionales, app, capturas y decisiones. Fuera de `help-center` para que GitBook no los borre |
| `pendientes.md` | Lista generada con `python herramientas/generar_pendientes.py`; no se edita a mano |

## Flujo

- Cambios grandes o de estructura: por Git.
- Retoques puntuales: en GitBook, con **Editar** (crea una solicitud de cambio que, al fusionarse, se guarda en GitHub).
- No editar la misma página por las dos vías a la vez.
- Preguntas frecuentes por tema: se etiqueta cada pregunta con sus temas en `indice-contenido.yaml` y se ejecuta `python herramientas/generar_faq.py`, que regenera los bloques `faq-<tema>.md` que muestran las tareas.
- Pendientes del borrador: se anotan en `pendientes.yaml` y se ejecuta `python herramientas/generar_pendientes.py`.
- Antes de subir por Git: `python herramientas/validar.py` (menú, enlaces, anclas, imágenes, bloques, variables, índice, catálogo y pendientes).
