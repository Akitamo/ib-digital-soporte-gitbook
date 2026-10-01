# Guía de estilo – material de referencia

Versión 0.3 (1 de octubre de 2026). Las **reglas SG-1 a SG-25** están en la guía de estilo del sitio en GitBook (Mejorar → Guía de estilo), que es la que aplican el asistente de edición y el agente. Su copia de referencia es `guia-estilo-gitbook.md`: cualquier cambio se hace primero en GitBook y después se copia aquí.

Este archivo recoge lo que la guía del sitio no contiene: el catálogo de bloques y las convenciones. El catálogo resume los criterios aprobados en la ficha «Diseño del contenido» (plantilla de página de tarea, reglas 1 a 16, en `funcionalidades-gitbook`, fuera del repositorio). Si difieren, manda la ficha.

---

## Catálogo de bloques

| Necesidad | Bloque de GitBook | Notas |
|---|---|---|
| Respuesta directa | Descripción de la página + introducción | La descripción se usa en buscadores y en el asistente. La introducción dice dónde está y qué queda fuera, enlazado |
| Requisito o limitación que condiciona toda la página | Aviso `warning` tras la introducción | Antes del procedimiento; enlaza a la respuesta completa (reglas 8 y 13) |
| Requisito, limitación o incidencia de un paso, una zona o una opción | Texto o aviso en ese punto | Desplegable solo si es extensa; si tiene respuesta propia, enlace a la pregunta frecuente |
| Ruta obligatoria hasta la pantalla o secuencia completa | Pasos (stepper) | En orden. Cada paso con contenido propio; la captura dentro del paso si ayuda |
| Web y app | Pestañas «Web» / «App» | Siempre que algo cambie, también la captura. Lo común, fuera de las pestañas |
| Qué muestra una pantalla | Descripción por zonas | Nombre de la zona en negrita, texto breve y su captura en pestañas debajo |
| Acciones independientes desde una pantalla | Opciones A, B, C en negrita | Debajo, su texto o sus pasos numerados y su captura en pestañas |
| Procedimiento corto | Párrafo o lista numerada | La captura, después de la lista, nunca dentro |
| Resultado | Aviso `success` | Solo para un resultado realmente alcanzado |
| Explicación breve que debe ser igual en varias páginas | Contenido reutilizable | En el punto donde se lee: un paso, una opción o un aviso (regla 15) |
| Cierre | `##` «Más sobre…» | Bloque `faq-<tema>` generado y, en «También te puede interesar», hasta 3 referencias a página. No limita los enlaces del texto |
| Contacto | Fuera de las páginas | Está en la navegación del sitio y en «Canales de atención». En una página, solo el canal que la tarea necesita |
| Límites del asistente | Contenido reutilizable `limites-asistente` | Portada y páginas con botón de asistente |
| Datos de salud | Contenido reutilizable `aviso-datos-salud` | Portadas de grupo con datos de salud |
| Ayuda del asistente | Botón de asistente | Solo donde aporte |
| Elegir entre tareas | Tabla en modo tarjetas | Portada y portadas de grupo |
| Plazos por fases | Tabla | Diagrama Mermaid solo si ayuda, siempre con equivalente en texto |

**Combinaciones no permitidas**

* Dentro de un paso: desplegables u otros pasos.
* Dentro de una lista: imágenes o pestañas (la sincronización parte la lista).
* Limitaciones esenciales dentro de desplegables o pestañas de una sola plataforma, si aplican a las dos.
* Texto de instrucción solo en la imagen.
* Pestañas con un único contenido o con el procedimiento repartido entre ellas.

---

## Convenciones

**URL y carpetas.** `/personas/<grupo>/<tarea>`. El nombre del archivo es el slug: verbo en infinitivo y palabras clave, sin artículos innecesarios (`consultar-tus-citas.md`). El menú refleja las carpetas. GitBook forma la dirección con el título del grupo del menú, no con la carpeta: la carpeta se llama igual que el grupo (`## Prestaciones económicas` → `prestaciones-economicas/`). Mientras el sitio no esté publicado, las URL se pueden cambiar sin redirecciones; después de publicarlo, cada cambio exige una redirección.

**Imágenes.** Capturas recortadas a la zona útil, en ficheros nuevos de `.gitbook/assets/` con el origen y la zona (`1a00aeed731a-detalles-recorte.webp`). WebP, 1600 px de ancho como máximo. Si falta la de la app: `app-captura-pendiente.webp` o `app-zona-pendiente.webp`.

**Contenido reutilizable.** `.gitbook/includes/<nombre>.md`, dentro de la sección Personas. Para una explicación breve que la persona necesita leer en ese punto y que debe ser igual en varias páginas. Debe encajar en todas sus páginas: sin indicaciones de una sola plataforma o pantalla si se usa fuera de ellas. Si necesita hacer otra tarea o ampliar una explicación extensa, se enlaza. Un resumen de otra página que deba cambiar con ella también es contenido reutilizable: un enlace no lo actualiza. Se lista con su responsable en `_editorial/inventario-componentes.md`.

**Variables.** `.gitbook/vars.yaml` de la sección, para un mismo dato que se mantiene en frases distintas, también dentro de los bloques: direcciones, teléfonos, plazos. Se comparte un valor porque significa lo mismo, no porque coincida. La condición se escribe completa en la frase y solo el valor sale de la variable (SG-4): «cuando hayan pasado <code class="expression">space.vars.autoliquidacion_espera</code> desde el último pago». No funcionan en títulos.

**Material editorial.** Plantillas, pruebas e inventarios viven en `_editorial/`, fuera de la carpeta de la sección, y no se publican.
