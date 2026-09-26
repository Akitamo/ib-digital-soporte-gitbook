# Guía de estilo – material de referencia

Versión 0.2. Las **reglas SG-1 a SG-25** están en la guía de estilo del sitio en GitBook (Mejorar → Guía de estilo), que es la que aplican el asistente de edición y el agente. Su copia de referencia es `guia-estilo-gitbook.md`: cualquier cambio se hace primero en GitBook y después se copia aquí.

Este archivo recoge lo que la guía del sitio no contiene: el catálogo de bloques y las convenciones.

---

## Catálogo de bloques

| Necesidad | Bloque de GitBook | Notas |
|---|---|---|
| Respuesta directa | Descripción de la página + primer párrafo | La descripción se usa en buscadores y en el asistente |
| Requisito previo | Aviso `info` | Solo si existe |
| Limitación esencial | Aviso `warning` | Siempre visible, antes del procedimiento |
| Resultado | Aviso `success` | Qué tendrás o dónde queda el documento |
| Web y app | Pestañas «Web» / «App» | Procedimiento completo en cada una |
| Procedimiento de 3 o más pasos | Pasos (stepper) | Cada paso: título corto, instrucción y captura |
| Procedimiento corto | Párrafo o lista numerada | |
| Incidencia de la tarea | Desplegable | Título = síntoma, con palabras de la persona |
| Siguientes pasos | Referencias a página (content-ref) | 2 o 3, por lo que se necesita después |
| Contacto | Contenido reutilizable `contacto` | Siempre al final |
| Límites del asistente | Contenido reutilizable `limites-asistente` | Portada y páginas con botón de asistente |
| Datos de salud | Contenido reutilizable `aviso-datos-salud` | Portadas de grupo con datos de salud |
| Ayuda del asistente | Botón de asistente | Solo donde aporte |
| Elegir entre tareas | Tabla en modo tarjetas | Portada y portadas de grupo |
| Plazos por fases | Tabla | Diagrama Mermaid solo si ayuda, siempre con equivalente en texto |

**Combinaciones no permitidas**

* Dentro de un paso: desplegables u otros pasos.
* Limitaciones esenciales dentro de desplegables o pestañas de una sola plataforma, si aplican a las dos.
* Texto de instrucción solo en la imagen.
* Pestañas con un único contenido o con el procedimiento repartido entre ellas.

---

## Convenciones

**URL y carpetas.** `/personas/<grupo>/<tarea>`. El nombre del archivo es el slug: verbo en infinitivo y palabras clave, sin artículos innecesarios (`consultar-tus-citas.md`). El menú refleja las carpetas. Mientras el sitio no esté publicado, las URL se pueden cambiar sin redirecciones; después de publicarlo, cada cambio exige una redirección.

**Imágenes.** `<tarea>-<plataforma>-paso-<n>.webp` (por ejemplo, `citas-web-paso-2.webp`), en `.gitbook/assets/`. WebP, 1600 px de ancho como máximo.

**Contenido reutilizable.** `.gitbook/includes/<nombre>.md`, dentro de la sección Personas. Se lista con su responsable en `_editorial/inventario-componentes.md`.

**Variables.** `.gitbook/vars.yaml` de la sección, solo para datos estables (dirección del portal, teléfonos verificados). Las condiciones y los plazos se escriben completos en el texto.

**Material editorial.** Plantillas, pruebas e inventarios viven en `_editorial/`, fuera de la carpeta de la sección, y no se publican.
