# Pendientes del borrador

Lista generada por `herramientas/generar_pendientes.py` a partir de `_editorial/pendientes.yaml` y de los marcadores de captura de la app. No se edita a mano: se corrige la fuente y se vuelve a generar. GitBook no importa esta carpeta.

**104 pendientes**: 98 en páginas y 6 en bloques o variables compartidos, que se repiten en cada página donde se usan. 44 páginas afectadas.

| Tipo | Qué significa | Número |
|---|---|---|
| contradicción | incoherencia de negocio del análisis de contenido, apartado 4 (con su número) | 18 |
| valor provisional | dato que figura en la ayuda pero falta confirmar | 2 |
| app | funcionamiento o texto de la app sin confirmar | 22 |
| captura de la app | falta la captura de la app (marcador de imagen) | 9 |
| captura dudosa | captura usada que conviene revisar | 8 |
| captura descartada | captura original no usada, con el motivo | 17 |
| sin verificar | contenido funcional sin fuente o genérico | 25 |
| decisión | decisión editorial o de estructura pendiente de Sergio | 3 |

## Bloques y variables compartidos

### Bloque `abrir-solicitud-prestacion`

| Tipo | Pendiente | Línea |
|---|---|---|
| contradicción 9 | Etiquetas del botón y del menú, tomadas de las capturas («Solicitar nueva prestación económica»; «Prestaciones económicas» > «Solicitudes»). P27 dice «Solicitar nueva prestación» y «Solicitar una nueva prestación»; P57, «Prestaciones» > «Solicitar nueva prestación». En P32 y su captura, «Solicitudes» lleva directamente a las tarjetas de las prestaciones. | [L11](../help-center/.gitbook/includes/abrir-solicitud-prestacion.md#L11) |
| app | P19 y P27 dicen que «en este momento» la solicitud no está disponible en la app. Confirmar si sigue igual. | [L6](../help-center/.gitbook/includes/abrir-solicitud-prestacion.md#L6) |

Páginas afectadas: [¿Qué prestaciones puedo pedir desde Ibermutua Digital Personas?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-prestaciones-puedo-pedir) › [Cómo empezar](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-prestaciones-puedo-pedir#prestaciones-empezar); [Solicitar el pago directo por incapacidad temporal](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-el-pago-directo) › [Empieza la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-el-pago-directo#pago-directo-empezar); [Iniciar la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud) › [Abre el trámite](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud#rel-iniciar-abrir).

### Bloque `aviso-cambio-cita`

| Tipo | Pendiente | Línea |
|---|---|---|
| contradicción 1 | Canal para cambiar una cita. El bloque remite al teléfono; P52 dice teléfono o chat y P80, que el chat es solo para temas médicos. | [L5](../help-center/.gitbook/includes/aviso-cambio-cita.md#L5) |

Páginas afectadas: [¿Puedo cambiar las citas desde Ibermutua Digital?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cambiar-una-cita) › [Cómo pedir el cambio](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cambiar-una-cita#cita-cambio).

### Bloque `canal-chat`

| Tipo | Pendiente | Línea |
|---|---|---|
| contradicción 1 | P38 incluye las citas entre las dudas que se pueden plantear por chat; P80 y el aviso de citas las remiten al teléfono. El bloque no menciona las citas. | [L6](../help-center/.gitbook/includes/canal-chat.md#L6) |

Páginas afectadas: [Canales de atención](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/canales-de-atencion) › [Chat con el servicio médico](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/canales-de-atencion#canales-chat); [¿El chat se responde al momento?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-responden-el-chat) › [Para qué es el chat](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-responden-el-chat#chat-uso); [Hablar con el servicio médico por chat](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/chat-con-el-servicio-medico).

### Variable `autoliquidacion_espera`

| Tipo | Pendiente | Línea |
|---|---|---|
| valor provisional | Días que tienen que pasar desde tu último pago o tu última autoliquidación para poder pedirla (P34, P67, P70-P72); confirmar con negocio. | [L3](../help-center/.gitbook/vars.yaml#L3) |

Páginas afectadas: [¿La autoliquidación necesita aprobación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/aprobacion-de-la-autoliquidacion) › [Qué se comprueba antes](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/aprobacion-de-la-autoliquidacion#autoliquidacion-comprobacion-previa); [¿Cuándo recibo la autoliquidación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-recibo-la-autoliquidacion) › [Cada cuánto puedes pedirla](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-recibo-la-autoliquidacion#autoliquidacion-frecuencia); [¿Por qué no puedo solicitar la autoliquidación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/no-puedo-solicitar-la-autoliquidacion) › [Qué se comprueba](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/no-puedo-solicitar-la-autoliquidacion#autoliquidacion-que-se-comprueba); [¿Por qué no puedo solicitar la autoliquidación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/no-puedo-solicitar-la-autoliquidacion); [¿Qué es la autoliquidación y qué condiciones tiene?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-es-la-autoliquidacion) › [Condiciones](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-es-la-autoliquidacion#autoliquidacion-condiciones); [Solicitar la autoliquidación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-autoliquidacion).

### Variable `autoliquidacion_plazo_abono`

| Tipo | Pendiente | Línea |
|---|---|---|
| contradicción 4 | Plazo de abono. P34 dice «en un máximo de 2 días laborables» y también «en 1-2 días». | [L4](../help-center/.gitbook/vars.yaml#L4) |

Páginas afectadas: [¿La autoliquidación necesita aprobación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/aprobacion-de-la-autoliquidacion); [¿Cuándo recibo la autoliquidación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-recibo-la-autoliquidacion); [¿Qué es la autoliquidación y qué condiciones tiene?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-es-la-autoliquidacion) › [Cómo se comprueban](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-es-la-autoliquidacion#autoliquidacion-comprobacion); [Solicitar la autoliquidación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-autoliquidacion) › [Cuándo cobras y cómo sigues la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-autoliquidacion#autoliquidacion-seguimiento).

## Por página

### [¿En qué podemos ayudarte?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/)

`README.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | decisión | Portada sin muestra aprobada, para revisar aparte. Nueve tarjetas con las gestiones de P02 (citas, historia clínica, informe, documentación, chat, rehabilitación, prestaciones, pagos y certificado). Se quita la sección de contacto (va en la navegación) y el botón «Necesito contactar» lleva a Canales de atención. | [L24](../help-center/README.md#L24) |

### [Darte de alta en Ibermutua Digital Personas](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/darte-de-alta)

`alta-y-acceso/darte-de-alta.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | captura descartada | Originales no usados de P04 y P05. 74df252ef3e4 (inicio tras entrar) muestra un diagnóstico y una cita; ffb6c450c6d2 y b4ae3218e619 repiten la pantalla de inicio de sesión; 770dd5c08837 y c8d6fce2a2d9 repiten la portada de la app; 5d8eeaae6b5e es una maqueta promocional con textos deformados y nombres, parece retocada. | [L14](../help-center/alta-y-acceso/darte-de-alta.md#L14) |
| [Regístrate](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/darte-de-alta#alta-registro) | sin verificar | El formulario y las capturas son del registro con DNI. Falta cómo sigue el registro con certificado digital. | [L38](../help-center/alta-y-acceso/darte-de-alta.md#L38) |
| [Regístrate](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/darte-de-alta#alta-registro) | sin verificar | Lo dice P44 («el proceso es el mismo que para el alta»); P04 no describe el final del alta ni cómo llega la contraseña temporal. | [L46](../help-center/alta-y-acceso/darte-de-alta.md#L46) |
| [Regístrate](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/darte-de-alta#alta-registro) | app | Faltan los pasos y las capturas del alta en la app; P05 solo muestra la portada y los enlaces de descarga. | [L64](../help-center/alta-y-acceso/darte-de-alta.md#L64) |
| [Entra en Ibermutua Digital Personas](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/darte-de-alta#alta-acceso) | app | Confirmar el inicio de sesión en la app y sus pantallas. | [L82](../help-center/alta-y-acceso/darte-de-alta.md#L82) |

### [Acceder con biometría](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/acceder-con-biometria)

`alta-y-acceso/acceder-con-biometria.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Activa el acceso biométrico](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/acceder-con-biometria#biometria-activar) | captura descartada | Originales 4fcf87346f29 y c985cf1f12ee. Son composiciones con textos deformados («digitol», «biométrice», «He obrdado mi contraseña») y nombres; parecen retocadas. Hacen falta capturas reales de activar la biometría y del aviso de dispositivo sin biometría. | [L19](../help-center/alta-y-acceso/acceder-con-biometria.md#L19) |
| [Activa el acceso biométrico](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/acceder-con-biometria#biometria-activar) | captura de la app | pantalla para activar el acceso biométrico. | [L23](../help-center/alta-y-acceso/acceder-con-biometria.md#L23) |

### [Verificar tu identidad con el doble factor](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/doble-factor-de-seguridad)

`alta-y-acceso/doble-factor-de-seguridad.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Introduce el código](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/doble-factor-de-seguridad#doble-factor-codigo) | app | P07 solo muestra la web. Confirmar el doble factor en la app. | [L22](../help-center/alta-y-acceso/doble-factor-de-seguridad.md#L22) |
| [Introduce el código](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/doble-factor-de-seguridad#doble-factor-codigo) | sin verificar | P07 no indica cómo se pide un código nuevo; la captura no muestra esa opción. | [L26](../help-center/alta-y-acceso/doble-factor-de-seguridad.md#L26) |

### [Cambiar tu contraseña](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/cambiar-tu-contrasena)

`alta-y-acceso/cambiar-tu-contrasena.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | app | P43 solo describe la web. Confirmar si se puede cambiar la contraseña desde la app y cómo. | [L10](../help-center/alta-y-acceso/cambiar-tu-contrasena.md#L10) |
| [Cambia la contraseña](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/cambiar-tu-contrasena#contrasena-cambiar) | captura dudosa | El nombre de la cuenta está difuminado en el recorte. P43 llama «Datos Personales» a lo que la pantalla titula «Mi cuenta». | [L20](../help-center/alta-y-acceso/cambiar-tu-contrasena.md#L20) |

### [Recuperar tu contraseña](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/recuperar-tu-contrasena)

`alta-y-acceso/recuperar-tu-contrasena.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Genera una contraseña nueva](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/recuperar-tu-contrasena#contrasena-recuperar) | app | P44 solo describe la web. Confirmar la recuperación en la app. | [L18](../help-center/alta-y-acceso/recuperar-tu-contrasena.md#L18) |

### [Cambiar tus datos de contacto](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/cambiar-tus-datos-de-contacto)

`alta-y-acceso/cambiar-tus-datos-de-contacto.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | app | P46 solo describe la web. Confirmar si se pueden cambiar desde la app y cómo. | [L10](../help-center/alta-y-acceso/cambiar-tus-datos-de-contacto.md#L10) |
| [Cambia el teléfono o el correo](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/alta-y-acceso/cambiar-tus-datos-de-contacto#datos-cambiar) | captura dudosa | Recorte con el nombre difuminado; el resto de datos ya venía difuminado. No se usa e41588a63945 (composición borrosa con nombre) y la ventana del correo (9662f39002a6) es igual que la del móvil. | [L28](../help-center/alta-y-acceso/cambiar-tus-datos-de-contacto.md#L28) |

### [Consultar tus citas](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/citas-y-asistencias/consultar-tus-citas)

`citas-y-asistencias/consultar-tus-citas.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | sin verificar | Confirmar que las citas pasadas se ven dentro de cada episodio de la historia clínica (ficha de diseño, pendiente 2). | [L8](../help-center/citas-y-asistencias/consultar-tus-citas.md#L8) |
| [Abre tu cita](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/citas-y-asistencias/consultar-tus-citas#citas-abrir) | app | Confirmar «Pulsa la cita» en la app y cómo es su detalle; no hay capturas del detalle de la cita en la app. | [L48](../help-center/citas-y-asistencias/consultar-tus-citas.md#L48) |
| [Información de la cita](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/citas-y-asistencias/consultar-tus-citas#citas-detalles) | captura de la app | apartado Detalles de la cita. | [L68](../help-center/citas-y-asistencias/consultar-tus-citas.md#L68) |
| [Información de la cita](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/citas-y-asistencias/consultar-tus-citas#citas-detalles) | captura de la app | apartado Lo que vas a necesitar. | [L86](../help-center/citas-y-asistencias/consultar-tus-citas.md#L86) |
| [Qué puedes hacer desde tu cita](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/citas-y-asistencias/consultar-tus-citas#citas-opciones) | captura de la app | apartado para aportar documentación. | [L111](../help-center/citas-y-asistencias/consultar-tus-citas.md#L111) |
| [Qué puedes hacer desde tu cita](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/citas-y-asistencias/consultar-tus-citas#citas-opciones) | captura de la app | añadir la cita al calendario. | [L126](../help-center/citas-y-asistencias/consultar-tus-citas.md#L126) |

### [Descargar un justificante de asistencia](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/citas-y-asistencias/descargar-un-justificante)

`citas-y-asistencias/descargar-un-justificante.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | app | P16 y P55 solo describen la web. Falta cómo se descarga un justificante en la app. | [L10](../help-center/citas-y-asistencias/descargar-un-justificante.md#L10) |
| [Otras formas de descargarlo](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/citas-y-asistencias/descargar-un-justificante#justificante-episodio) | contradicción 10 | Incidencias, dudas y consejos de P16, genéricos y sin verificar (PDF firmado, validez ante la empresa, filtros, nombre del archivo). | [L50](../help-center/citas-y-asistencias/descargar-un-justificante.md#L50) |

### [Consultar tu historia clínica](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/consultar-tu-historia-clinica)

`tu-historia-clinica/consultar-tu-historia-clinica.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Qué puedes hacer desde aquí](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/consultar-tu-historia-clinica#historia-gestiones) | app | Las opciones se describen solo para la web. En la app, H. Clínica muestra Descargar informe y Subir documentos (captura de P09); confirmar qué opciones tiene. | [L67](../help-center/tu-historia-clinica/consultar-tu-historia-clinica.md#L67) |

### [Ver tus pruebas diagnósticas](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/ver-tus-pruebas-diagnosticas)

`tu-historia-clinica/ver-tus-pruebas-diagnosticas.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Ver las pruebas de un episodio](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/ver-tus-pruebas-diagnosticas#pruebas-episodio) | app | En la app, la ficha del episodio muestra las pestañas Información e Histórico (captura de P15). Confirmar dónde se ven las pruebas de un episodio. | [L38](../help-center/tu-historia-clinica/ver-tus-pruebas-diagnosticas.md#L38) |

### [Descargar un informe](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/descargar-un-informe)

`tu-historia-clinica/descargar-un-informe.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | app | P12 solo describe la web. La app muestra el botón Descargar informe en H. Clínica; confirmar el recorrido. | [L10](../help-center/tu-historia-clinica/descargar-un-informe.md#L10) |
| [Descarga el informe](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/descargar-un-informe#informe-descargar) | sin verificar | P12 indica abrir el episodio y pulsar Descargar informe de historia. En las capturas, ese botón está en Historia clínica > General; en la ficha del episodio el botón es Descargar informe de episodio médico (ver P50). | [L26](../help-center/tu-historia-clinica/descargar-un-informe.md#L26) |
| [Descarga el informe](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/descargar-un-informe#informe-descargar) | captura descartada | Original 84d336033c70 (ejemplo de informe en PDF). Muestra diagnósticos, medicación y antecedentes; hace falta un informe de demostración. | [L34](../help-center/tu-historia-clinica/descargar-un-informe.md#L34) |

### [Solicitar una segunda opinión médica](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/solicitar-una-segunda-opinion)

`tu-historia-clinica/solicitar-una-segunda-opinion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 6 | Red de centros. P14 enlaza a /red-de-centros/ y otras páginas a /redcentros/. | [L10](../help-center/tu-historia-clinica/solicitar-una-segunda-opinion.md#L10) |
| Inicio de la página | contradicción 3 | P14 y la confirmación dicen «3 a 10 días»; el formulario, «3 a 10 días hábiles»; P49 da los plazos de la norma. | [L10](../help-center/tu-historia-clinica/solicitar-una-segunda-opinion.md#L10) |
| Inicio de la página | captura descartada | Original c73acdb96fb9 (composición web y móvil). Muestra un diagnóstico y un texto con datos de salud; el formulario ya aparece en cada paso. | [L12](../help-center/tu-historia-clinica/solicitar-una-segunda-opinion.md#L12) |
| [Solicita la segunda opinión](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/solicitar-una-segunda-opinion#segunda-opinion-solicitar) | app | P14 dice que se selecciona el episodio, pero la captura de la app lo muestra ya seleccionado. Falta el control intermedio. | [L52](../help-center/tu-historia-clinica/solicitar-una-segunda-opinion.md#L52) |
| [Solicita la segunda opinión](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/solicitar-una-segunda-opinion#segunda-opinion-solicitar) | captura de la app | confirmación de la solicitud de segunda opinión. | [L58](../help-center/tu-historia-clinica/solicitar-una-segunda-opinion.md#L58) |

### [Enviar documentación a la mutua](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/enviar-documentacion)

`tu-historia-clinica/enviar-documentacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Envía la documentación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/enviar-documentacion#documentacion-enviar) | sin verificar | P37 indica este acceso, pero su captura (860e61dd68c1, no usada) solo muestra el filtro Documentos del histórico, sin el control para enviar. | [L20](../help-center/tu-historia-clinica/enviar-documentacion.md#L20) |
| [Envía la documentación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/enviar-documentacion#documentacion-enviar) | sin verificar | Peso máximo del archivo. La captura web indica 0,5 MB y la de la app, 5 MB; no se menciona en el texto. | [L28](../help-center/tu-historia-clinica/enviar-documentacion.md#L28) |
| [Envía la documentación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/tu-historia-clinica/enviar-documentacion#documentacion-enviar) | app | Tomado de las capturas de la ficha del episodio en la app (P14 y P15); P37 no lo describe. | [L46](../help-center/tu-historia-clinica/enviar-documentacion.md#L46) |

### [Solicitar el pago directo por incapacidad temporal](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-el-pago-directo)

`prestaciones-economicas/pago-directo/solicitar-el-pago-directo.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Empieza la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-el-pago-directo#pago-directo-empezar) | contradicción 9 | Bloque `abrir-solicitud-prestacion`: Etiquetas del botón y del menú, tomadas de las capturas («Solicitar nueva prestación económica»; «Prestaciones económicas» > «Solicitudes»). P27 dice «Solicitar nueva prestación» y «Solicitar una nueva prestación»; P57, «Prestaciones» > «Solicitar nueva prestación». En P32 y su captura, «Solicitudes» lleva directamente a las tarjetas de las prestaciones. | [L11](../help-center/.gitbook/includes/abrir-solicitud-prestacion.md#L11) |
| [Empieza la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-el-pago-directo#pago-directo-empezar) | app | Bloque `abrir-solicitud-prestacion`: P19 y P27 dicen que «en este momento» la solicitud no está disponible en la app. Confirmar si sigue igual. | [L6](../help-center/.gitbook/includes/abrir-solicitud-prestacion.md#L6) |

### [Rellenar la solicitud de pago directo](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/rellenar-la-solicitud)

`prestaciones-economicas/pago-directo/rellenar-la-solicitud.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | captura descartada | No se usan los GIF de P20 (verificación previa, modelo 145, declaración de actividad, documentación adicional y firma OTP) ni la etiqueta 6e773b71d630, de 2021, con la interfaz anterior; tampoco 18d6a0b8de0a (datos de contacto), con la marca ✦ de imagen generada o retocada con IA. | [L12](../help-center/prestaciones-economicas/pago-directo/rellenar-la-solicitud.md#L12) |
| [Completa el formulario](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/rellenar-la-solicitud#formulario-pasos) | sin verificar | P20 identifica los documentos obligatorios con una etiqueta (imagen de 2021) cuyo texto no consta. Confirmar cómo se marcan en la pantalla actual. | [L48](../help-center/prestaciones-economicas/pago-directo/rellenar-la-solicitud.md#L48) |

### [Solicitar el pago directo como representante](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-como-representante)

`prestaciones-economicas/pago-directo/solicitar-como-representante.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | sin verificar | P22 no explica dónde se revoca el código (solo «desde la propia prestación»). | [L13](../help-center/prestaciones-economicas/pago-directo/solicitar-como-representante.md#L13) |
| [Accede como representante](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-como-representante#representante-acceder) | captura dudosa | Capturas de 2021 (acceso como representante y avisos de SMS, 4aa56c3fecb9). Confirmar que las pantallas siguen igual. No se usa ef56624f71d9 (inicio de sesión del portal de representantes, de 2021). | [L30](../help-center/prestaciones-economicas/pago-directo/solicitar-como-representante.md#L30) |
| [Consigue el código de autorización](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-como-representante#representante-codigo) | sin verificar | Las capturas de P19 (marzo de 2026) muestran la tarjeta del pago directo solo con «Comenzar trámite» y, en «Tu solicitud», la opción «Un representante»; las de P22 (abril) añaden el botón «Gestión por representante». Confirmar la pantalla actual y el camino para generar el código. | [L46](../help-center/prestaciones-economicas/pago-directo/solicitar-como-representante.md#L46) |
| [Consigue el código de autorización](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-como-representante#representante-codigo) | contradicción 9 | P22 dice «Gestión por representación» y «Obtener código para representante»; las capturas, «Gestión por representante» y «Generar código». Se usan las de las capturas. | [L46](../help-center/prestaciones-economicas/pago-directo/solicitar-como-representante.md#L46) |

### [Consultar el estado de tu solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/consultar-el-estado)

`prestaciones-economicas/pago-directo/consultar-el-estado.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | app | P21 solo describe la web. Confirmar si el estado de la solicitud se consulta en la app. | [L8](../help-center/prestaciones-economicas/pago-directo/consultar-el-estado.md#L8) |
| Inicio de la página | sin verificar | P21 no dice cómo se abre la solicitud. Se toma de la pantalla de Solicitudes (26ecaafc47b6, con «Abrir ficha de la prestación económica»), que no se usa como captura porque muestra importes y fechas de una prestación. | [L10](../help-center/prestaciones-economicas/pago-directo/consultar-el-estado.md#L10) |
| Inicio de la página | captura descartada | 9420b05b11fd (página de la solicitud con nombres sin difuminar). 9b5014ad1939 y e3cc05cd6b8c son correos (justificante y resolución), no pantallas del portal. | [L12](../help-center/prestaciones-economicas/pago-directo/consultar-el-estado.md#L12) |
| [Consulta la resolución](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/consultar-el-estado#estado-resolucion) | captura dudosa | El histórico muestra una fecha de 2020 y el título «Historico» sin tilde. Confirmar que es la pantalla actual. | [L28](../help-center/prestaciones-economicas/pago-directo/consultar-el-estado.md#L28) |

### [Subsanar la documentación de tu solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/subsanar-documentacion)

`prestaciones-economicas/pago-directo/subsanar-documentacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | app | P24 solo describe la web. Confirmar si la subsanación se puede hacer desde la app. | [L8](../help-center/prestaciones-economicas/pago-directo/subsanar-documentacion.md#L8) |
| Inicio de la página | captura descartada | 7e8da3b19d42 (correo), e8352f18fdf2 (correo de justificante) y 84d3b37e0321 (histórico), con la marca ✦ de imagen generada o retocada con IA. 61357bf7da7e muestra un aviso temporal de mantenimiento de la firma y es de una solicitud de lactancia. | [L14](../help-center/prestaciones-economicas/pago-directo/subsanar-documentacion.md#L14) |
| [Envía la documentación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/subsanar-documentacion#subsanar-enviar) | sin verificar | La tarea de la captura (ee0d8f03b328) da 10 días desde la carta de subsanación y avisa de que, si no, se da por desistida la petición; P24 no lo menciona. No se ha escrito el plazo. | [L28](../help-center/prestaciones-economicas/pago-directo/subsanar-documentacion.md#L28) |

### [Solicitar la prestación por riesgo durante el embarazo o la lactancia](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion)

`prestaciones-economicas/riesgo-embarazo-lactancia/solicitar-la-prestacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | app | P27 dice que la solicitud no está disponible en la app. Confirmar si tampoco se pueden seguir las fases (certificación, finalizar y resolución). | [L8](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/solicitar-la-prestacion.md#L8) |
| [Fases del trámite](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion#rel-fases) | captura descartada | d4850c6c5b44, 3fab6bb323fc y 1c12de808964 (requisitos e informe médico de la lactancia), con la marca ✦. cc7af9527203 es la misma captura que d5fda311735e. | [L42](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/solicitar-la-prestacion.md#L42) |
| [Si la pides por lactancia](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion#rel-lactancia) | sin verificar | Redacción de P32 («a partir de la semana 16 del parto o de la 18 si es embarazo múltiple»). Confirmar el plazo. | [L46](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/solicitar-la-prestacion.md#L46) |

### [Iniciar la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud)

`prestaciones-economicas/riesgo-embarazo-lactancia/iniciar-la-solicitud.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Abre el trámite](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud#rel-iniciar-abrir) | contradicción 9 | Bloque `abrir-solicitud-prestacion`: Etiquetas del botón y del menú, tomadas de las capturas («Solicitar nueva prestación económica»; «Prestaciones económicas» > «Solicitudes»). P27 dice «Solicitar nueva prestación» y «Solicitar una nueva prestación»; P57, «Prestaciones» > «Solicitar nueva prestación». En P32 y su captura, «Solicitudes» lleva directamente a las tarjetas de las prestaciones. | [L11](../help-center/.gitbook/includes/abrir-solicitud-prestacion.md#L11) |
| [Abre el trámite](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud#rel-iniciar-abrir) | app | Bloque `abrir-solicitud-prestacion`: P19 y P27 dicen que «en este momento» la solicitud no está disponible en la app. Confirmar si sigue igual. | [L6](../help-center/.gitbook/includes/abrir-solicitud-prestacion.md#L6) |
| [Abre el trámite](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud#rel-iniciar-abrir) | sin verificar | La pantalla ofrece también «Un representante»; las fuentes solo explican la representación en el pago directo (P22). | [L32](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/iniciar-la-solicitud.md#L32) |
| [Completa la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud#rel-iniciar-completar) | captura descartada | a259b3793bc9 (informe médico), 0be5668e99d7 (calculadora de fechas) y 5892e10da72b (datos bancarios), con la marca ✦. be00dbf0f033 muestra el explorador de archivos del equipo con un nombre de fichero que incluye un identificador; cba303738d8a y 0d0256e61fa8 tienen la marca ✦ y el mismo nombre de fichero. | [L54](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/iniciar-la-solicitud.md#L54) |
| [Completa la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/iniciar-la-solicitud#rel-iniciar-completar) | captura descartada | 1a4721f5d29f y 7241fb467526 (solicitud enviada e histórico), con la marca ✦. 7629f958b5de es el correo del justificante, no una pantalla del portal. | [L106](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/iniciar-la-solicitud.md#L106) |

### [Certificación de riesgo](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/certificacion-de-riesgo)

`prestaciones-economicas/riesgo-embarazo-lactancia/certificacion-de-riesgo.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Mientras se evalúa](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/certificacion-de-riesgo#certificacion-evaluacion) | sin verificar | El desplegable «Más información sobre Otras acciones disponibles» de P29 está vacío en la extracción. La lista sale de la captura 4a26a572bfb1. | [L12](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/certificacion-de-riesgo.md#L12) |
| [Tipos de certificación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/certificacion-de-riesgo#certificacion-tipos) | captura dudosa | Captura de baja resolución (587 px de ancho); el texto se lee con dificultad. | [L36](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/certificacion-de-riesgo.md#L36) |

### [Finalizar la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/finalizar-la-solicitud)

`prestaciones-economicas/riesgo-embarazo-lactancia/finalizar-la-solicitud.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Completa y envía la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/finalizar-la-solicitud#finalizar-enviar) | sin verificar | El desplegable «Descubre aquí los pasos para realizar la solicitud online de esta documentación» de P30 está vacío en la extracción. | [L30](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/finalizar-la-solicitud.md#L30) |
| [Completa y envía la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/finalizar-la-solicitud#finalizar-enviar) | captura descartada | cbca6915818c (modificar la declaración, con la marca ✦ y un nombre de fichero con identificador); 27ec26005514, 108c93f10e1d y aa924d334fd2, con la marca ✦; 4ab81515e4c7, con texto deformado («Contacta con nuestro de taler/Cese»). 1943708883f9 repite la certificación positiva y a6f50f561506 es el correo del justificante. | [L36](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/finalizar-la-solicitud.md#L36) |

### [Resolución de la prestación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/resolucion)

`prestaciones-economicas/riesgo-embarazo-lactancia/resolucion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | captura descartada | c15afa7b0dab (marca ✦ y texto «(nombre personale)») y fd8fc3b023ba (histórico con la carta de reconocimiento, marca ✦). | [L10](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/resolucion.md#L10) |
| [Consulta la resolución](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-prestacion/resolucion#resolucion-consultar) | captura dudosa | Captura de baja resolución (660 px de ancho). | [L14](../help-center/prestaciones-economicas/riesgo-embarazo-lactancia/resolucion.md#L14) |

### [Consultar tus pagos](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/consultar-tus-pagos)

`prestaciones-economicas/consultar-tus-pagos.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | app | P33 y P23 solo describen la web. Confirmar si los pagos se consultan en la app. | [L8](../help-center/prestaciones-economicas/consultar-tus-pagos.md#L8) |
| Inicio de la página | captura descartada | 76b94cf13394 (menú y pagos), con la marca ✦; 43d8a294bc90 (correo real de un gestor); 2f47f1b3ebd8 y 0ec96a7c12a0 (pantalla anterior «Datos Económicos», en el menú Gestiones); 26ecaafc47b6 (importes y fechas de una prestación). | [L10](../help-center/prestaciones-economicas/consultar-tus-pagos.md#L10) |

### [Solicitar la autoliquidación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-autoliquidacion)

`prestaciones-economicas/solicitar-la-autoliquidacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 5 | Nombre de la opción. El menú de las capturas de marzo de 2026 (9e5f5f992ca2, d5fda311735e), usado en pagos y retenciones, dice «Autopagos»; esta página y la captura descartada 76b94cf13394, «Autoliquidación». | [L10](../help-center/prestaciones-economicas/solicitar-la-autoliquidacion.md#L10) |
| Inicio de la página | valor provisional | Variable `autoliquidacion_espera`: Días que tienen que pasar desde tu último pago o tu última autoliquidación para poder pedirla (P34, P67, P70-P72); confirmar con negocio. | [L3](../help-center/.gitbook/vars.yaml#L3) |
| [Pide la autoliquidación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-autoliquidacion#autoliquidacion-pedir) | app | Texto visible de la pestaña App en la página de prueba (P34 solo describe la web). | [L52](../help-center/prestaciones-economicas/solicitar-la-autoliquidacion.md#L52) |
| [Pide la autoliquidación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-autoliquidacion#autoliquidacion-pedir) | captura de la app | acceso a Autoliquidación. | [L54](../help-center/prestaciones-economicas/solicitar-la-autoliquidacion.md#L54) |
| [Cuándo cobras y cómo sigues la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-autoliquidacion#autoliquidacion-seguimiento) | contradicción 4 | Variable `autoliquidacion_plazo_abono`: Plazo de abono. P34 dice «en un máximo de 2 días laborables» y también «en 1-2 días». | [L4](../help-center/.gitbook/vars.yaml#L4) |
| [Cuándo cobras y cómo sigues la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/solicitar-la-autoliquidacion#autoliquidacion-seguimiento) | captura de la app | estado de la autoliquidación. | [L70](../help-center/prestaciones-economicas/solicitar-la-autoliquidacion.md#L70) |

### [Descargar el certificado de retenciones (IRPF)](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/descargar-el-certificado-de-retenciones)

`prestaciones-economicas/descargar-el-certificado-de-retenciones.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 10 | No se incluyen los requisitos, las incidencias, el contacto por ticket con el NIF ni el enlace de P35 a sí misma, contenido genérico sin verificar. | [L8](../help-center/prestaciones-economicas/descargar-el-certificado-de-retenciones.md#L8) |
| [Descarga el certificado](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/descargar-el-certificado-de-retenciones#retenciones-descargar) | contradicción 9 | Menú «Certificados de retenciones» y pestaña «Retenciones». | [L16](../help-center/prestaciones-economicas/descargar-el-certificado-de-retenciones.md#L16) |
| [Descarga el certificado](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/descargar-el-certificado-de-retenciones#retenciones-descargar) | sin verificar | P35 habla de elegir el ejercicio y de los botones «Ver» y «Descargar»; la pantalla muestra el último ejercicio y un histórico, cada uno con un icono de descarga. | [L24](../help-center/prestaciones-economicas/descargar-el-certificado-de-retenciones.md#L24) |
| [Descarga el certificado](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/descargar-el-certificado-de-retenciones#retenciones-descargar) | app | P35 dice que el portal se usa desde el navegador del móvil; no menciona la app. | [L30](../help-center/prestaciones-economicas/descargar-el-certificado-de-retenciones.md#L30) |

### [Reclamar una resolución de la mutua](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/reclamar-una-resolucion)

`prestaciones-economicas/reclamar-una-resolucion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Qué puedes reclamar](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/reclamar-una-resolucion#reclamar-que) | sin verificar | P63 describe la reclamación de la certificación sin capturas de sus pantallas. | [L21](../help-center/prestaciones-economicas/reclamar-una-resolucion.md#L21) |
| [Qué puedes reclamar](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/reclamar-una-resolucion#reclamar-que) | sin verificar | No hay captura de la opción para reclamar la resolución final; P63 dice que está «en la propia página de la resolución». | [L29](../help-center/prestaciones-economicas/reclamar-una-resolucion.md#L29) |
| [Sigue tu reclamación](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/prestaciones-economicas/reclamar-una-resolucion#reclamar-seguimiento) | contradicción 2 | Texto de P63 (chat con el servicio médico o vías de contacto de la notificación); P80 dice que el chat no es para prestaciones. El bloque del tramitador/a va porque el mapa lo asigna a esta página, no como sustituto del chat. Lo resuelve negocio. | [L42](../help-center/prestaciones-economicas/reclamar-una-resolucion.md#L42) |

### [Hablar con el servicio médico por chat](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/chat-con-el-servicio-medico)

`servicios-medicos-digitales/chat-con-el-servicio-medico.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 1 | Bloque `canal-chat`: P38 incluye las citas entre las dudas que se pueden plantear por chat; P80 y el aviso de citas las remiten al teléfono. El bloque no menciona las citas. | [L6](../help-center/.gitbook/includes/canal-chat.md#L6) |
| Inicio de la página | captura descartada | 32f7d6046783 (marca ✦ y nombres de chats con diagnósticos); 344e9b3ad1e6 (móvil, con diagnósticos y de baja resolución); 584541297a10 (marca ✦, nombre de una profesional y contenido de salud en la conversación); 117a11ec61f6 (app con diagnósticos y un nombre); 79896a7c87b4 repite la página de inicio. | [L12](../help-center/servicios-medicos-digitales/chat-con-el-servicio-medico.md#L12) |
| [Abre el chat](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/chat-con-el-servicio-medico#chat-abrir) | sin verificar | P38 no da el nombre de la opción. En las capturas se llama «Habla con el servicio médico» (32478f0944c3, descartada) y, con mensajes sin leer, «Tienes mensajes nuevos» (e4a40a28b488). | [L16](../help-center/servicios-medicos-digitales/chat-con-el-servicio-medico.md#L16) |
| [Abre el chat](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/chat-con-el-servicio-medico#chat-abrir) | sin verificar | P38 lo dice, pero no hay captura del acceso al chat desde el episodio. | [L16](../help-center/servicios-medicos-digitales/chat-con-el-servicio-medico.md#L16) |
| [Abre el chat](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/chat-con-el-servicio-medico#chat-abrir) | captura dudosa | En este recorte y en el de la app (25de37a4cc4e) se han difuminado los nombres de los chats, que son diagnósticos, y los textos de los mensajes. | [L22](../help-center/servicios-medicos-digitales/chat-con-el-servicio-medico.md#L22) |

### [Hacer una videoconsulta](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/videoconsulta)

`servicios-medicos-digitales/videoconsulta.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | captura descartada | 32478f0944c3 (página de inicio de la web con la marca ✦, el nombre de la persona y el diagnóstico del episodio), por eso la pestaña Web no lleva captura del detalle; a591a6ff977f (marca ✦ e imagen de la videollamada con personas). | [L12](../help-center/servicios-medicos-digitales/videoconsulta.md#L12) |
| [Entra en la videoconsulta](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/videoconsulta#videoconsulta-entrar) | sin verificar | P39 no da el nombre del botón para entrar en la sala y no hay captura. | [L38](../help-center/servicios-medicos-digitales/videoconsulta.md#L38) |
| [Entra en la videoconsulta](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/videoconsulta#videoconsulta-entrar) | captura dudosa | Recortes de la sala de espera; se ha difuminado el nombre de la doctora. El resto de la captura muestra a una persona y el chat de la videoconsulta. | [L54](../help-center/servicios-medicos-digitales/videoconsulta.md#L54) |
| [Entra en la videoconsulta](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/videoconsulta#videoconsulta-entrar) | app | P39 muestra la app solo en el detalle de la cita; las capturas de la sala son del navegador (ordenador y móvil). Confirmar los pasos en la app. | [L60](../help-center/servicios-medicos-digitales/videoconsulta.md#L60) |
| [Entra en la videoconsulta](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/videoconsulta#videoconsulta-entrar) | captura de la app | sala de espera y videollamada entrante. | [L62](../help-center/servicios-medicos-digitales/videoconsulta.md#L62) |

### [Hacer tu rehabilitación online](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/rehabilitacion-online)

`servicios-medicos-digitales/rehabilitacion-online.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | captura descartada | 3dc810a9efd1 (fotografía de una persona); 5162f9cf0155, ef14e18c1470, aea9e4c68c66 y 4ee4367b2fba (pantallas de ejercicio con personas); 7780dd43fc83 (nombre de la persona); f32be98e234e (lista de ejercicios con un comentario del personal médico); 91e19c2706d0, 960187fc9b84 y 5a82ab52b836 son versiones de mayo de 2025 de pantallas con captura más reciente. | [L14](../help-center/servicios-medicos-digitales/rehabilitacion-online.md#L14) |
| [Haz los ejercicios de hoy](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/servicios-medicos-digitales/rehabilitacion-online#rehabilitacion-ejercicios) | app | P40 y P75 describen la web. Confirmar si los ejercicios se pueden hacer desde la app. | [L20](../help-center/servicios-medicos-digitales/rehabilitacion-online.md#L20) |

### [¿Qué hago si no puedo darme de alta con el DNI o no tengo certificado digital?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/no-puedo-darme-de-alta)

`preguntas-frecuentes/no-puedo-darme-de-alta.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 6 | Red de centros. P45 enlaza a /redcentros/ y P14 a /red-de-centros/. | [L10](../help-center/preguntas-frecuentes/no-puedo-darme-de-alta.md#L10) |

### [¿Puedo cambiar las citas desde Ibermutua Digital?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cambiar-una-cita)

`preguntas-frecuentes/cambiar-una-cita.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Cómo pedir el cambio](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cambiar-una-cita#cita-cambio) | contradicción 1 | Bloque `aviso-cambio-cita`: Canal para cambiar una cita. El bloque remite al teléfono; P52 dice teléfono o chat y P80, que el chat es solo para temas médicos. | [L5](../help-center/.gitbook/includes/aviso-cambio-cita.md#L5) |
| [Cómo pedir el cambio](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cambiar-una-cita#cita-cambio) | contradicción 1 | La respuesta usa el aviso compartido (teléfono, como P80) y mantiene la opción del chat de P52. Se resuelve junto con el canal del aviso. | [L16](../help-center/preguntas-frecuentes/cambiar-una-cita.md#L16) |

### [¿Qué prestaciones puedo pedir desde Ibermutua Digital Personas?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-prestaciones-puedo-pedir)

`preguntas-frecuentes/que-prestaciones-puedo-pedir.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Cómo empezar](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-prestaciones-puedo-pedir#prestaciones-empezar) | contradicción 9 | Bloque `abrir-solicitud-prestacion`: Etiquetas del botón y del menú, tomadas de las capturas («Solicitar nueva prestación económica»; «Prestaciones económicas» > «Solicitudes»). P27 dice «Solicitar nueva prestación» y «Solicitar una nueva prestación»; P57, «Prestaciones» > «Solicitar nueva prestación». En P32 y su captura, «Solicitudes» lleva directamente a las tarjetas de las prestaciones. | [L11](../help-center/.gitbook/includes/abrir-solicitud-prestacion.md#L11) |
| [Cómo empezar](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-prestaciones-puedo-pedir#prestaciones-empezar) | app | Bloque `abrir-solicitud-prestacion`: P19 y P27 dicen que «en este momento» la solicitud no está disponible en la app. Confirmar si sigue igual. | [L6](../help-center/.gitbook/includes/abrir-solicitud-prestacion.md#L6) |
| [Quién puede hacer la solicitud](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-prestaciones-puedo-pedir#prestaciones-quien) | sin verificar | P57 dice que el representante se habilita «desde tu perfil» y que también puede tramitarla la empresa; P22 explica un código que se genera en la solicitud. Se sigue P22. | [L19](../help-center/preguntas-frecuentes/que-prestaciones-puedo-pedir.md#L19) |

### [¿Qué es la autoliquidación y qué condiciones tiene?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-es-la-autoliquidacion)

`preguntas-frecuentes/que-es-la-autoliquidacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Condiciones](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-es-la-autoliquidacion#autoliquidacion-condiciones) | valor provisional | Variable `autoliquidacion_espera`: Días que tienen que pasar desde tu último pago o tu última autoliquidación para poder pedirla (P34, P67, P70-P72); confirmar con negocio. | [L3](../help-center/.gitbook/vars.yaml#L3) |
| [Cómo se comprueban](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/que-es-la-autoliquidacion#autoliquidacion-comprobacion) | contradicción 4 | Variable `autoliquidacion_plazo_abono`: Plazo de abono. P34 dice «en un máximo de 2 días laborables» y también «en 1-2 días». | [L4](../help-center/.gitbook/vars.yaml#L4) |

### [¿Qué importe recibiré con la autoliquidación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/importe-de-la-autoliquidacion)

`preguntas-frecuentes/importe-de-la-autoliquidacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Dónde ves tu importe](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/importe-de-la-autoliquidacion#autoliquidacion-ver-importe) | sin verificar | P68 dice que indicas la fecha de solicitud y el sistema calcula el importe; la pantalla de la página de autoliquidación muestra el periodo y el importe sin pedir fecha. Se sigue la pantalla. | [L29](../help-center/preguntas-frecuentes/importe-de-la-autoliquidacion.md#L29) |

### [¿La autoliquidación necesita aprobación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/aprobacion-de-la-autoliquidacion)

`preguntas-frecuentes/aprobacion-de-la-autoliquidacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 4 | Variable `autoliquidacion_plazo_abono`: Plazo de abono. P34 dice «en un máximo de 2 días laborables» y también «en 1-2 días». | [L4](../help-center/.gitbook/vars.yaml#L4) |
| [Qué se comprueba antes](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/aprobacion-de-la-autoliquidacion#autoliquidacion-comprobacion-previa) | valor provisional | Variable `autoliquidacion_espera`: Días que tienen que pasar desde tu último pago o tu última autoliquidación para poder pedirla (P34, P67, P70-P72); confirmar con negocio. | [L3](../help-center/.gitbook/vars.yaml#L3) |

### [¿Cuándo recibo la autoliquidación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-recibo-la-autoliquidacion)

`preguntas-frecuentes/cuando-recibo-la-autoliquidacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 4 | Variable `autoliquidacion_plazo_abono`: Plazo de abono. P34 dice «en un máximo de 2 días laborables» y también «en 1-2 días». | [L4](../help-center/.gitbook/vars.yaml#L4) |
| [Plazo del ingreso](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-recibo-la-autoliquidacion#autoliquidacion-plazo) | contradicción 4 | Se omite el ejemplo del viernes de P71, mal redactado, hasta confirmar cómo se cuentan los días. | [L14](../help-center/preguntas-frecuentes/cuando-recibo-la-autoliquidacion.md#L14) |
| [Cada cuánto puedes pedirla](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-recibo-la-autoliquidacion#autoliquidacion-frecuencia) | valor provisional | Variable `autoliquidacion_espera`: Días que tienen que pasar desde tu último pago o tu última autoliquidación para poder pedirla (P34, P67, P70-P72); confirmar con negocio. | [L3](../help-center/.gitbook/vars.yaml#L3) |

### [¿Por qué no puedo solicitar la autoliquidación?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/no-puedo-solicitar-la-autoliquidacion)

`preguntas-frecuentes/no-puedo-solicitar-la-autoliquidacion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | valor provisional | Variable `autoliquidacion_espera`: Días que tienen que pasar desde tu último pago o tu última autoliquidación para poder pedirla (P34, P67, P70-P72); confirmar con negocio. | [L3](../help-center/.gitbook/vars.yaml#L3) |
| [Qué se comprueba](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/no-puedo-solicitar-la-autoliquidacion#autoliquidacion-que-se-comprueba) | valor provisional | Variable `autoliquidacion_espera`: Días que tienen que pasar desde tu último pago o tu última autoliquidación para poder pedirla (P34, P67, P70-P72); confirmar con negocio. | [L3](../help-center/.gitbook/vars.yaml#L3) |

### [¿El chat se responde al momento?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-responden-el-chat)

`preguntas-frecuentes/cuando-responden-el-chat.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| [Para qué es el chat](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/cuando-responden-el-chat#chat-uso) | contradicción 1 | Bloque `canal-chat`: P38 incluye las citas entre las dudas que se pueden plantear por chat; P80 y el aviso de citas las remiten al teléfono. El bloque no menciona las citas. | [L6](../help-center/.gitbook/includes/canal-chat.md#L6) |

### [¿Qué ventajas tiene la rehabilitación online?](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/preguntas-frecuentes/ventajas-de-la-rehabilitacion-online)

`preguntas-frecuentes/ventajas-de-la-rehabilitacion-online.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 10 | P76 son unas 640 palabras genéricas; se ha reducido a lo esencial. Confirmar que no falta nada que negocio quiera mantener. | [L10](../help-center/preguntas-frecuentes/ventajas-de-la-rehabilitacion-online.md#L10) |

### [Canales de atención](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/canales-de-atencion)

`canales-de-atencion.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | decisión | Página de referencia sin muestra aprobada, para revisar aparte. Tabla de canales (P80) y una sección por canal con los bloques canal-chat y contacto-tramitador; recoge el contenido del bloque contacto de la portada. | [L10](../help-center/canales-de-atencion.md#L10) |
| [Chat con el servicio médico](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/canales-de-atencion#canales-chat) | contradicción 1 | Bloque `canal-chat`: P38 incluye las citas entre las dudas que se pueden plantear por chat; P80 y el aviso de citas las remiten al teléfono. El bloque no menciona las citas. | [L6](../help-center/.gitbook/includes/canal-chat.md#L6) |
| [Tu tramitador/a](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/canales-de-atencion#canales-tramitador) | captura descartada | No se usa 8795ab9cd23b, con datos del tramitador/a y de la persona solo en parte difuminados; se reutiliza el recorte de la página de estado de la solicitud. 74b500660222 repite la página de inicio con el chat. | [L30](../help-center/canales-de-atencion.md#L30) |
| [Línea de Atención Telefónica Integral 24 h](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/canales-de-atencion#canales-telefono) | sin verificar | P80 remite los cambios de datos al teléfono, pero el móvil y el correo se cambian en Mi cuenta (P46). Confirmar qué datos se cambian por teléfono. | [L34](../help-center/canales-de-atencion.md#L34) |

### [Glosario](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/glosario)

`glosario.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | decisión | Presentación. Secciones por letras con cada término en negrita y su definición, en lugar de la tabla de P81, porque un bloque no cabe en una celda. Autoliquidación, certificación de riesgo, pago directo y segunda opinión usan las definiciones compartidas, que sustituyen las de P81 (la de pago directo añadía ejemplos de cuándo se aplica). «Gran invalidez» pasa de A-D a E-K. | [L10](../help-center/glosario.md#L10) |
| [E-K](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/glosario#glosario-e-k) | valor provisional | Cifras de Ibermutua de P81 (más de 1,8 millones de trabajadores y cerca de 170.500 empresas asociadas). Confirmar o quitar. | [L76](../help-center/glosario.md#L76) |
| [P-R](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/glosario#glosario-p-r) | contradicción 6 | P81 enlaza a /redcentros, sin barra final; se usa la misma dirección que en el resto de páginas. | [L146](../help-center/glosario.md#L146) |

### [Política de cookies](https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/otros-temas/politica-de-cookies)

`politica-de-cookies.md`

| Sección | Tipo | Pendiente | Línea |
|---|---|---|---|
| Inicio de la página | contradicción 11 | P82 describe Confluence. Falta el apartado de qué cookies usa el sitio en GitBook, para redactar con Legal. Solo se conservan las partes genéricas (qué son y cómo desactivarlas). | [L10](../help-center/politica-de-cookies.md#L10) |
