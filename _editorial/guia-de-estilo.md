# Guía de estilo – convenciones de ficheros

Versión 0.4 (2 de octubre de 2026). Recoge las convenciones de ficheros, nombres, imágenes, bloques, variables y anclas. No repite reglas que tienen otra fuente:

- **Redacción (reglas SG-1 a SG-25):** la guía de estilo del sitio en GitBook (Improve → Style guide), que aplican el asistente de edición y el agente. Su copia es `guia-estilo-gitbook.md`: cualquier cambio se hace primero en GitBook.
- **Cuándo usar cada componente y plantillas de página:** el documento maestro «Diseño del contenido» (`funcionalidades-gitbook/diseno-del-contenido.md`, fuera del repositorio). La versión 0.3 de esta guía tenía un catálogo de bloques que repetía esos criterios; se retiró el 02/10.
- **Sintaxis de GitBook y combinaciones que no funcionan:** la guía de edición (`funcionalidades-gitbook/flujo-de-edicion-y-sincronizacion.md`).

## Convenciones

**Direcciones y carpetas.** El nombre del archivo es el slug: verbo en infinitivo y palabras clave, sin artículos innecesarios (`consultar-tus-citas.md`). GitBook forma la dirección con el menú, no con la carpeta: grupo, páginas padre y nombre del archivo (`prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud`). La carpeta se llama igual que su grupo del menú (`## Prestaciones económicas` → `prestaciones-economicas/`). Mientras el sitio no esté publicado, las URL se pueden cambiar sin redirecciones; después de publicarlo, cada cambio exige una redirección.

**Imágenes.** Capturas recortadas a la zona útil, en ficheros nuevos de `.gitbook/assets/` con el origen y la zona (`1a00aeed731a-detalles-recorte.webp`). WebP, 1600 px de ancho como máximo. Si falta la de la app: `app-captura-pendiente.webp` o `app-zona-pendiente.webp`.

**Contenido reutilizable.** `.gitbook/includes/<nombre>.md`, dentro de la sección Personas. Para una explicación breve que la persona necesita leer en ese punto y que debe ser igual en varias páginas. Debe encajar en todas sus páginas: sin indicaciones de una sola plataforma o pantalla si se usa fuera de ellas. Si necesita hacer otra tarea o ampliar una explicación extensa, se enlaza. Un resumen de otra página que deba cambiar con ella también es contenido reutilizable: un enlace no lo actualiza. Se registra en el catálogo de `_editorial/mapa-contenido.yaml` (contenido, origen, dónde se usa y estado).

**Variables.** `.gitbook/vars.yaml` de la sección, para un mismo dato que se mantiene en frases distintas, también dentro de los bloques: direcciones, teléfonos, plazos. Se comparte un valor porque significa lo mismo, no porque coincida. La condición se escribe completa en la frase y solo el valor sale de la variable (SG-4): «cuando hayan pasado <code class="expression">space.vars.autoliquidacion_espera</code> desde el último pago». No funcionan en títulos.

**Anclas.** Todo punto que se enlaza desde correos, desde la app o desde otras páginas lleva un ancla fija en su encabezado `##`, con el prefijo del tema de la página: `## Título <a href="#tema-accion" id="tema-accion"></a>`. El ancla no se cambia aunque se reescriba el título. Si se usa desde fuera de la ayuda, se registra en `_editorial/enlaces-contextuales.csv`; `herramientas/validar.py` comprueba que todas existen.

**Material editorial.** Las fuentes de trabajo y las plantillas viven en `_editorial/`, fuera de la carpeta de la sección, y no se publican.
