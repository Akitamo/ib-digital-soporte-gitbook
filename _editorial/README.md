# Material editorial (no publicado)

Esta carpeta está fuera de `help-center/`, que es la única que GitBook importa. Nada de aquí se publica ni aparece en llms.txt ni en el MCP.

| Archivo | Uso |
|---|---|
| `guia-estilo-gitbook.md` | Copia de la guía de estilo del sitio en GitBook (reglas SG-n) |
| `guia-de-estilo.md` | Catálogo de bloques y convenciones |
| `plantillas/tarea.md` | Plantilla de artículo de tarea. Referencia: «Consultar tus citas» |
| `configuracion-asistente.md` | Instrucciones, saludo y preguntas del asistente |
| `inventario-componentes.md` | Bloques reutilizables, variables y anclas fijas |
| `enlaces-contextuales.csv` | Catálogo de enlaces para correos, pantallas de la app y respuestas de atención |
| `correspondencia.csv` | Página original (Scroll) → página nueva → tipo → responsable → estado |

## Flujo

- Cambios grandes o de estructura: por Git.
- Retoques puntuales: en GitBook, con **Editar** (crea una solicitud de cambio que, al fusionarse, se guarda en GitHub).
- No editar la misma página por las dos vías a la vez.
- Preguntas frecuentes por tema: se etiqueta cada pregunta con sus temas en `indice-contenido.yaml` y se ejecuta `python herramientas/generar_faq.py`, que regenera los bloques `faq-<tema>.md` que muestran las tareas.
- Antes de subir por Git: `python herramientas/validar.py` (menú, enlaces, anclas, imágenes, bloques, variables, índice y catálogo).
