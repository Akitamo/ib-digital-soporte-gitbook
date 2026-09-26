---
description: Página temporal de prueba técnica. Se eliminará tras la prueba.
icon: flask
vars:
  plazo_prueba: 3 días hábiles
---

# Prueba de módulos

**T3 – Variable de sección:** teléfono = <code class="expression">space.vars.telefono_atencion</code>.

**T5 – Variable de página:** plazo = <code class="expression">page.vars.plazo_prueba</code>.

## T1a – Bloque reutilizable suelto

{% include "../.gitbook/includes/prueba-bloque.md" %}

## T1b – Bloque dentro de pestañas y pasos

{% tabs %}
{% tab title="Web" %}
{% include "../.gitbook/includes/prueba-bloque.md" %}

{% stepper %}
{% step %}
### Abre la cita

Paso de prueba 1.
{% endstep %}

{% step %}
### Añade la cita a tu calendario

Paso de prueba 2 con bloque reutilizable dentro del paso:

{% include "../.gitbook/includes/prueba-bloque.md" %}
{% endstep %}
{% endstepper %}
{% endtab %}

{% tab title="App" %}
Contenido de la pestaña App.
{% endtab %}
{% endtabs %}

## T4 – Botones

<button type="button" class="button primary" data-action="ask" data-icon="gitbook-assistant" data-query="¿Cómo añado una cita a mi calendario?">Preguntar con pregunta preparada</button>

<button type="button" class="button secondary" data-action="search" data-icon="magnifying-glass" data-query="justificante">Buscar «justificante»</button>

## Apartado con ancla estable

Texto de destino para enlaces directos.
