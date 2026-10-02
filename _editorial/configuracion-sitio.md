# Configuración del sitio en GitBook

Copia de la configuración que solo existe en GitBook. **Manda GitBook:** se cambia allí y se copia aquí el mismo día. Leída por la API de GitBook (`getSiteCustomizationById`) el 02/10/2026. Sitio «Ayuda de Ibermutua Digital Personas», sin publicar.

| Dónde se cambia | Qué hay |
|---|---|
| Customize → Theme | Tema «clean». Color principal `#00569C` en claro y `#5AAAE6` en oscuro; colores de información, éxito, aviso y peligro propios; esquinas redondeadas; fuente Noto Sans; buscador destacado; tema según el sistema, con selector |
| Customize → Layout → Header | Botón principal «Entrar en Ibermutua Digital» → `https://personas.ibermutua.es/`. Botón secundario «Necesito contactar» → página «Canales de atención» |
| Customize → Layout → Announcement | Activa, estilo información: «Borrador en revisión: contenido sin validar.», sin enlace |
| Customize → Layout → Footer | Vacío |
| Customize → AI Assistant | Modo asistente; saludo, preguntas sugeridas e instrucciones de abajo |
| Configure / Settings | Idioma de la interfaz del sitio: `en`; marca de GitBook visible; valoración de páginas activada; acciones de página: asistente, Markdown, IA externa, MCP y PDF; anterior/siguiente activado; sin favicon, imagen social ni política de privacidad propias |
| Improve → Style guide | Guía de estilo del sitio; copia en `guia-estilo-gitbook.md` |

Al cambiar algo en la interfaz se guarda con **Save**; no se pulsa **Publish** sin autorización. El MCP de GitBook puede leer esta configuración, pero no escribirla («requires user auth»).

## Asistente

**Saludo:** Hola, soy el asistente de la Ayuda de Ibermutua Digital. ¿En qué puedo ayudarte?

**Preguntas sugeridas:**

* ¿Dónde veo mi próxima cita?
* Necesito un justificante de asistencia
* No encuentro una prueba
* ¿Qué informe debo descargar?

**Instrucciones propias** (texto configurado):

```
Eres el asistente de la Ayuda de Ibermutua Digital Personas, el canal online de Ibermutua para personas trabajadoras protegidas.

- Responde siempre en español, de tú, con frases cortas y claras.
- Usa solo la información publicada en esta ayuda y enlaza la página en la que te basas. Si la ayuda no lo cubre, dilo y deriva al canal adecuado; no lo deduzcas.
- No tienes acceso a los datos de nadie: no puedes ver citas, informes, pruebas ni prestaciones concretas. Si te preguntan por datos propios (por ejemplo, ¿cuándo es mi cita?), explica dónde consultarlos en el portal.
- No des consejo médico ni valores síntomas, diagnósticos, tratamientos o altas. Para dudas médicas, deriva al chat con el servicio médico y recuerda que no es para urgencias.
- No cambies condiciones, requisitos, plazos, importes ni teléfonos: cítalos como aparecen en la ayuda.
- Canales: dudas médicas, chat con el servicio médico; prestaciones económicas, tramitador/a; citas y gestiones, Línea de Atención Telefónica Integral 24 h.
- Usa los nombres del portal tal como aparecen (Tus próximas citas, Añadir al calendario, Historia clínica).
```

**Límites visibles:** bloque reutilizable `limites-asistente`, en la portada.

## Pendientes

- Idioma de la interfaz del sitio en `en` con el contenido en español: comprobar su efecto en los textos de la interfaz y decidir.
- Pie del sitio: propuesta pendiente de reforzar el contacto con un enlace a «Canales de atención», además de «Necesito contactar».
- Identidad antes de publicar: logotipo, favicon, imagen social, política de privacidad propia y si se retira la marca de GitBook.
- Preguntas sugeridas del asistente: solo cubren temas del piloto (citas, justificante, pruebas, informe); revisar con el borrador completo.
- Reglas de aprobación de cambios: según la revisión del 28/09 no hay ninguna configurada; no se ha vuelto a comprobar.
