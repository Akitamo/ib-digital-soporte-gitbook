---
description: >-
  [Una frase: qué puede hacer la persona y dónde. Se muestra bajo el título, en
  buscadores y en el asistente. Máximo 160 caracteres.]
icon: [icono Font Awesome sin «fa-», p. ej. calendar-check]
---

<!--
PLANTILLA DE TAREA – Ayuda de Ibermutua Digital Personas (v0.3, 01/10/2026)
Página de referencia: citas-y-asistencias/consultar-tus-citas.md (copia aprobada, que sustituyó a la página original el 01/10/2026).
Criterios: «Plantilla de página de tarea», reglas 1 a 16, en funcionalidades-gitbook/diseno-del-contenido.md
  (fuera del repositorio). Redacción: _editorial/guia-estilo-gitbook.md (SG-n). Sintaxis: guía de edición.
Una tarea que es una secuencia completa (enviar una solicitud) usa el mismo esquema sin descripción de
  pantalla ni opciones: el stepper es el cuerpo de la página.
Cada cosa donde se necesita (regla 13): lo que condiciona toda la página, arriba; lo que afecta a un paso,
  una zona o una opción, en ese punto; lo que sirve después de terminar, en el cierre.
Mostrar o enlazar (regla 14): se muestra en ese punto lo mínimo necesario para continuar, no un bloque
  completo porque contenga parte de la respuesta; otra tarea o una explicación extensa se enlaza. Una pregunta frecuente se enlaza donde surge la duda y además sale en el cierre.
Texto compartido (regla 15): explicación breve que debe ser igual en varias páginas → bloque reutilizable
  de .gitbook/includes/, en el punto donde se lee. Debe encajar en todas sus páginas: sin indicaciones de
  una sola plataforma o pantalla si se usa fuera de ellas. Variables (regla 16): solo el valor sale de la variable;
  la condición se escribe completa. No van en títulos.
Relaciones, bloques y variables previstos para cada página: _editorial/mapa-contenido.yaml. Al migrar la
  página, su entrada pasa a _editorial/indice-contenido.yaml (con faq_tema).
Anclas fijas en los encabezados ##: <a href="#tema-parte" id="tema-parte"></a>, con el prefijo del tema.
  Un ancla fija no se cambia; se registra en _editorial/enlaces-contextuales.csv si se usa fuera.
Antes de subir: python herramientas/generar_faq.py y python herramientas/validar.py
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

## Más sobre [tema] <a href="#[tema]-relacionado" id="[tema]-relacionado"></a>

**Preguntas frecuentes**

<!-- Bloque generado por herramientas/generar_faq.py desde el índice editorial (faq_tema de la página). No se edita a mano. -->
{% include "../.gitbook/includes/faq-[tema].md" %}

**También te puede interesar**

<!-- Hasta tres tareas o ampliaciones útiles después de terminar. No sustituyen a los enlaces del texto. Sin bloque de contacto: el contacto está en la navegación del sitio. -->
{% content-ref url="[pagina].md" %}
[[Título de la página]]([pagina].md)
{% endcontent-ref %}
