## Puntos que necesitan tu validación

Son dudas de contenido o de funcionamiento que no se pueden resolver desde el texto. Mientras no se decidan, las páginas dicen lo que ya decía el Centro de Ayuda actual.

| # | Tema | Situación | Qué hace falta |
|---|------|-----------|----------------|
| V1 | Cambiar una cita | La pregunta frecuente dice «por teléfono o, si tienes el alta como paciente digital, por chat». El aviso de la página de citas y la página de canales dicen solo teléfono. | Confirmar si el chat sirve para cambiar citas. Se corrige en un solo sitio (el aviso reutilizable y la pregunta). |
| V2 | Descargar un informe en la app | La página solo explica la web, pero la captura de la app en «Consultar tu historia clínica» muestra un botón **Descargar informe**. | Confirmar si se puede en la app. Si se puede, añado la pestaña App con capturas. |
| V3 | Plazo de la segunda opinión | «Te contactarán en un plazo de 3 a 10 días» (tomado de la página actual). | Confirmar el plazo vigente. Está en la página de concepto y en la tarea. |
| V4 | Incidencias del justificante | La sección «Si algo no sale como esperas» recoge casos genéricos. | Validar con Atención cuáles son las incidencias reales más frecuentes. |
| V5 | Capturas con datos de ejemplo | Algunas capturas muestran nombres o datos de ejemplo (por ejemplo, en «Descargar un informe»). | Confirmar que son ficticios o sustituirlas por capturas difuminadas. |
| V6 | Capturas que no son de la aplicación | En «Solicitar una segunda opinión» hay dos imágenes que parecen maquetas. | Sustituir por capturas reales. |
| V7 | Capturas de la app en citas | El detalle de una cita solo tiene capturas de la web. | Aportar capturas de la app si el flujo es distinto. |
| V8 | Capturas con texto antiguo incrustado | La captura del paso «Entra en Historia clínica» incluye el texto de la página de Confluence dentro de la imagen. | Recortarla (lo puedo hacer yo) y revisar si hay más casos en la vista previa. |
| V9 | Logotipo | La cabecera usa el nombre del sitio sin logotipo. | Facilitar el logotipo en SVG o PNG (claro y oscuro). |

## Qué se comprueba después de subir a GitBook

Estas cosas solo se pueden verificar en GitBook, no en la vista previa local:

* **Enlaces a un paso dentro de la pestaña App** (por ejemplo, `#historia-episodio-app`): en la vista previa se abre la pestaña correcta; hay que ver si GitBook hace lo mismo.
* **Enlaces dentro de los bloques de preguntas frecuentes**: se escriben relativos al bloque (`../../preguntas-frecuentes/…`); hay que ver que GitBook los resuelve en cada página que incluye el bloque.
* **Importación sin cambios**: que GitBook no reescriba los bloques reutilizables ni las anclas al sincronizar.

## Cómo se mantiene a partir de ahora

* **Preguntas frecuentes por tema:** para que una pregunta aparezca en las tareas de un tema, se añade el tema a su entrada en `_editorial/indice-contenido.yaml` y se ejecuta `herramientas/generar_faq.py`. No se tocan las tareas.
* **Enlaces por intención:** las propuestas viven en `_editorial/enlaces-propuestos.json` con su motivo. Solo se aplican las aceptadas (`herramientas/aplicar_enlaces.py`); las rechazadas se guardan para no volver a proponerlas.
* **Antes de subir:** `herramientas/validar.py` sin errores y revisión en esta vista previa.
