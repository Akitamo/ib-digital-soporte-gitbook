---
description: >-
  [Una frase: qué puede hacer la persona y dónde. Se muestra bajo el título, en
  buscadores y en el asistente. Máximo 160 caracteres.]
icon: [icono Font Awesome sin «fa-», p. ej. calendar-check]
---

<!--
PLANTILLA DE TAREA – Ayuda de Ibermutua Digital Personas (v0.5, 03/10/2026)
Esqueleto de una página de tarea. Los criterios no se repiten aquí: están en «Plantilla de página de tarea»,
  reglas 1 a 16, de funcionalidades-gitbook/diseno-del-contenido.md (fuera del repositorio). Redacción:
  _editorial/guia-estilo-gitbook.md (SG-n). Convenciones de ficheros y anclas: _editorial/guia-de-estilo.md.
  Sintaxis: funcionalidades-gitbook/flujo-de-edicion-y-sincronizacion.md.
Página de referencia: citas-y-asistencias/consultar-tus-citas.md.
Una tarea que es una secuencia completa (enviar una solicitud) usa el mismo esquema sin descripción de
  pantalla ni opciones: el stepper es el cuerpo de la página.
Página nueva: entrada en help-center/SUMMARY.md, en _editorial/indice-contenido.yaml (tipo, temas, resuelve,
  faq_tema y, si puede quedarse sin cierre, cierre) y en _editorial/mapa-contenido.yaml (origen y relaciones).
Antes de subir: los comandos del README del repositorio, en su orden.
Borra estos comentarios y los textos entre corchetes.
-->

# [Verbo en infinitivo + objeto: «Consultar tus citas»]

[Introducción: dónde está la información o la acción, en la web y en la app, con los nombres de la interfaz en **negrita**, y qué queda fuera de la página, enlazado: «Las citas pasadas quedan en tu historia clínica: consulta [cómo ver tu historia clínica](...)».]

<!-- Aviso de página, solo si una limitación o condición afecta a toda la página. Enlaza a la respuesta completa en lugar de repetirla. Si el aviso se repite en otras páginas, es un bloque: {% include "../.gitbook/includes/[aviso].md" %} -->
{% hint style="warning" %}
**[Limitación en una frase.]** Consulta [la respuesta completa](../preguntas-frecuentes/[pregunta].md).
{% endhint %}

## [Procedimiento: «Abre tu cita»] <a href="#[tema]-abrir" id="[tema]-abrir"></a>

<!-- Stepper solo para la ruta obligatoria, en orden. Web y App siempre en pestañas cuando algo cambia, también la captura. Lo común, fuera de las pestañas. Un requisito o una incidencia de un paso va en ese paso. -->
{% tabs %}
{% tab title="Web" %}
{% stepper %}
{% step %}
### [Título corto del paso]

[Acción, con el verbo al principio y los nombres de la interfaz en **negrita**. Un dato que puede cambiar va como variable: <code class="expression">space.vars.portal_url</code>.]

<figure><img src="../.gitbook/assets/[captura]-recorte.webp" alt="[Qué se ve en la captura]"></figure>
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="App" %}
{% stepper %}
{% step %}
### [Título corto del paso]

[Acción en la app.]

<!-- Si falta la captura de la app: app-captura-pendiente.webp (pantalla completa) o app-zona-pendiente.webp (zona). -->
<figure><img width="300" src="../.gitbook/assets/app-captura-pendiente.webp" alt="Imagen de la app que falta: [qué debería verse]."></figure>
{% endstep %}
{% endstepper %}
{% endtab %}
{% endtabs %}

## [Descripción de pantalla: «Información de la cita»] <a href="#[tema]-detalles" id="[tema]-detalles"></a>

[Frase que presenta los apartados.]

**[Nombre de la zona, tal como aparece en la pantalla]**

[Qué muestra. Lo que pertenece a esta zona se explica aquí.]

{% tabs %}
{% tab title="Web" %}
<figure><img src="../.gitbook/assets/[zona]-recorte.webp" alt="[Qué se ve]"></figure>
{% endtab %}

{% tab title="App" %}
<figure><img width="300" src="../.gitbook/assets/app-zona-pendiente.webp" alt="Imagen de la app que falta: [zona]."></figure>
{% endtab %}
{% endtabs %}

**[Zona sin captura: solo texto, si la imagen no ayuda]**

[Qué muestra.]

## [Opciones: «Qué puedes hacer desde tu cita»] <a href="#[tema]-opciones" id="[tema]-opciones"></a>

[Frase que presenta las opciones.]

**A. [Opción de una sola acción]**

[Una frase con la acción.]

**B. [Opción con varios pasos]**

1. [Paso.]
2. [Paso. Si hay que hacer otra tarea, se enlaza aquí: [sube los documentos](...).]

{% tabs %}
{% tab title="Web" %}
<figure><img src="../.gitbook/assets/[opcion]-recorte.webp" alt="[Qué se ve]"></figure>
{% endtab %}

{% tab title="App" %}
<figure><img width="300" src="../.gitbook/assets/app-zona-pendiente.webp" alt="Imagen de la app que falta: [opción]."></figure>
{% endtab %}
{% endtabs %}

<!-- Cierre opcional (regla 11): solo si aporta preguntas del tema que ayuden, tareas útiles después o ambas.
La parte «Preguntas frecuentes» es generada («Partes generadas» del README del repositorio): no se edita a mano.
«También te puede interesar»: hasta tres tareas o ampliaciones útiles, a mano. Sin bloque de contacto. -->
## Más sobre [tema] <a href="#[tema]-relacionado" id="[tema]-relacionado"></a>

**Preguntas frecuentes**

{% include "../.gitbook/includes/faq-[tema].md" %}

**También te puede interesar**

{% content-ref url="[pagina].md" %}
[[Título de la página]]([pagina].md)
{% endcontent-ref %}
