# Inventario de componentes reutilizables

Regla: si algo aparece en dos sitios, se convierte en bloque reutilizable, variable o enlace a una página canónica. Nunca se copia.

## Bloques reutilizables (`help-center/.gitbook/includes/`)

| Bloque | Archivo | Dónde se usa | Responsable | Revisión |
|---|---|---|---|---|
| Contacto según el tipo de consulta | `contacto.md` | Portada, «Consultar tus citas» (y todas las tareas) | (por asignar) | Pendiente de validar con Atención |
| Aviso: cambiar una cita | `aviso-cambio-cita.md` | «Consultar tus citas» | (por asignar) | Canal pendiente de validar: la pregunta frecuente dice «teléfono o chat» |
| Qué puede y qué no puede hacer el asistente | `limites-asistente.md` | Portada | (por asignar) | Borrador |
| Aviso sobre datos de salud | `aviso-datos-salud.md` | «Consultar tu historia clínica» | (por asignar) | Borrador |

## Variables de sección (`help-center/.gitbook/vars.yaml`)

| Variable | Valor | Dónde se usa | Revisión |
|---|---|---|---|
| `telefono_atencion` | 900 23 33 33 | Contacto, aviso de cambio de cita | Pendiente de validar |
| `portal_url` | https://personas.ibermutua.es/ | Reservada para enlaces al portal | — |

## Anclas fijas

Todo punto que se enlaza desde correos, desde la app o desde otras páginas lleva un ancla fija con prefijo del tema: `## Título <a href="#tema-accion" id="tema-accion"></a>`. El ancla no se cambia aunque se reescriba el título. El catálogo está en `enlaces-contextuales.csv`, y `reorg/validar_modulos.py` comprueba que todas existen.

| Página | Anclas fijas |
|---|---|
| Portada | `contacto` |
| Consultar tus citas | `citas-abrir`, `citas-detalles`, `citas-como-llegar`, `citas-que-llevar`, `citas-documentacion`, `citas-calendario`, `citas-incidencias`, `citas-siguientes-pasos`, `contacto` |
