# Inventario de componentes reutilizables

Regla: lo que aparece en dos sitios no se copia. Una explicación breve que hay que leer en ese punto y debe ser igual en varias páginas es un bloque reutilizable; un mismo dato en frases distintas, una variable; otra tarea o una explicación extensa, un enlace a su página (reglas 14 a 16 de la plantilla de tarea).

Los bloques y las variables previstos para el resto de páginas están en `mapa-contenido.yaml` (propuesta pendiente de validar); se pasan a este inventario al crearlos.

## Bloques reutilizables (`help-center/.gitbook/includes/`)

| Bloque | Archivo | Dónde se usa | Responsable | Revisión |
|---|---|---|---|---|
| Contacto según el tipo de consulta | `contacto.md` | Hoy: portada y las 8 tareas del piloto. Sale de las páginas de tarea al rehacerlas con la plantilla: el contacto va en la navegación y en «Canales de atención» | (por asignar) | Pendiente de validar con Atención |
| Aviso: cambiar una cita | `aviso-cambio-cita.md` | «Consultar tus citas» | (por asignar) | Canal pendiente de validar: la pregunta frecuente dice «teléfono o chat» |
| Qué puede y qué no puede hacer el asistente | `limites-asistente.md` | Portada | (por asignar) | Borrador |
| Aviso sobre datos de salud | `aviso-datos-salud.md` | «Consultar tu historia clínica» | (por asignar) | Borrador |

## Variables de sección (`help-center/.gitbook/vars.yaml`)

| Variable | Valor | Dónde se usa | Revisión |
|---|---|---|---|
| `telefono_atencion` | 900 23 33 33 | Contacto, aviso de cambio de cita | Pendiente de validar |
| `portal_url` | https://personas.ibermutua.es/ | Reservada para enlaces al portal | — |

Una variable se usa para el mismo dato en frases distintas, también dentro de los bloques (`aviso-cambio-cita` usa `telefono_atencion`). La condición se escribe completa; solo el valor sale de la variable.

## Anclas fijas

Todo punto que se enlaza desde correos, desde la app o desde otras páginas lleva un ancla fija con prefijo del tema: `## Título <a href="#tema-accion" id="tema-accion"></a>`. El ancla no se cambia aunque se reescriba el título. El catálogo está en `enlaces-contextuales.csv`, y `herramientas/validar.py` comprueba que todas existen.

| Página | Anclas fijas |
|---|---|
| Portada | `contacto` |
| Consultar tus citas | `citas-abrir`, `citas-detalles`, `citas-como-llegar`, `citas-que-llevar`, `citas-documentacion`, `citas-calendario`, `citas-incidencias`, `citas-siguientes-pasos`, `contacto` |
