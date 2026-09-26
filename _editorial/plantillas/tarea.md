---
description: >-
  [Una frase: qué puede hacer la persona y dónde. Se muestra bajo el título, en
  buscadores y en el asistente. Máximo 160 caracteres.]
icon: [icono Font Awesome sin «fa-», p. ej. calendar-check]
---

<!--
PLANTILLA DE TAREA – Ayuda de Ibermutua Digital Personas (v0.2)
Página de referencia: citas-y-asistencias/consultar-tus-citas.md
Reglas: guía de estilo del sitio (SG-1 a SG-25). Bloques y convenciones: _editorial/guia-de-estilo.md
Anclas fijas: todo encabezado que pueda enlazarse desde un correo, la app u otra página lleva
  <a href="#tema-accion" id="tema-accion"></a>  con el prefijo del tema (citas-, justificante-, informe-…).
  Un ancla fija no se cambia nunca; se registra en _editorial/enlaces-contextuales.csv si se usa fuera.
Nada que aparezca en dos páginas se copia: bloque reutilizable, variable o enlace.
Antes de subir: python reorg/validar_modulos.py repo-gitbook
Borra estos comentarios y los textos entre corchetes.
-->

# [Verbo en infinitivo + objeto: «Descargar un justificante de asistencia»]

[Respuesta directa en 1 o 2 frases: qué puedes hacer, dónde (web y app) y qué obtienes.]

<!-- Solo si hay un requisito real. -->
{% hint style="info" %}
**Antes de empezar:** [requisito.]
{% endhint %}

<!-- Limitación esencial: si ya existe como bloque reutilizable, insértalo; si no, créalo en .gitbook/includes/ y regístralo en el inventario. -->
{% include "../.gitbook/includes/[aviso-limitacion].md" %}

{% tabs %}
{% tab title="Web" %}
{% stepper %}
{% step %}
### [Título corto del paso] <a href="#[tema-accion]" id="[tema-accion]"></a>

[Una acción, con el verbo al principio. Nombres del portal en negrita, tal cual: **Botón**.]

<figure><img src="../.gitbook/assets/[tema]-web-paso-1.webp" alt="[Qué muestra la pantalla]"><figcaption><p>[Qué hay que mirar]</p></figcaption></figure>
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="App" %}
{% stepper %}
{% step %}
### [Título corto del paso] <a href="#[tema-accion]-app" id="[tema-accion]-app"></a>

[Una acción.]
{% endstep %}
{% endstepper %}
{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Al terminar** [qué tendrás y dónde queda].
{% endhint %}

## Si algo no sale como esperas <a href="#[tema]-incidencias" id="[tema]-incidencias"></a>

<details>

<summary>[Síntoma con las palabras de la persona]</summary>

[Causa y solución. Si persiste, qué canal usar.]

</details>

<!-- Opcional: pregunta preparada que abre el asistente. -->
<button type="button" class="button secondary" data-action="ask" data-icon="gitbook-assistant" data-query="[Pregunta frecuente de esta tarea]">Pregúntale al asistente sobre [tema]</button>

## Siguientes pasos <a href="#[tema]-siguientes-pasos" id="[tema]-siguientes-pasos"></a>

{% content-ref url="[pagina].md" %}
[[pagina].md]([pagina].md)
{% endcontent-ref %}

## ¿Necesitas contactar? <a href="#contacto" id="contacto"></a>

{% include "../.gitbook/includes/contacto.md" %}
