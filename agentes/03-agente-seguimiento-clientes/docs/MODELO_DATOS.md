# Modelo Conceptual de Datos del Agente de Seguimiento de Clientes para PYMES

## Propósito del documento

Este documento define los datos mínimos necesarios para una primera V1 (*Version 1 – Versión 1*) implementable del Agente de Seguimiento de Clientes para PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

No describe una base de datos ya creada ni una estructura técnica en producción. Es un modelo conceptual previo, pensado para preparar una futura implementación mínima, facilitar la revisión funcional y evitar que el agente se sobredimensione antes de validar el caso de uso.

## Estado actual

- Estado documental: en diseño inicial de V1.
- Código funcional: no implementado todavía.
- Base de datos: no implementada todavía.
- Automatizaciones: no implementadas todavía.
- Recordatorios automáticos: no implementados todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- Dashboard: no implementado todavía.
- Integraciones activas: no implementadas todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Criterio de diseño del modelo

El modelo debe ser:

- Simple.
- Comprensible.
- Verificable.
- Útil para revisar clientes activos.
- Suficiente para detectar próximas acciones y bloqueos.
- No sobredimensionado.
- Preparado para evolucionar después.

La prioridad de diseño es representar la información mínima necesaria para revisar una cartera de clientes, identificar huecos de seguimiento y preparar decisiones humanas. No se busca crear un CRM completo, un dashboard ni una integración avanzada.

## Entidad principal: Cliente en seguimiento

La entidad principal representa a un cliente que forma parte de una cartera activa o revisable. Su función es concentrar el estado operativo básico del seguimiento.

Campos mínimos:

- identificador_cliente: representa un identificador único del cliente; es útil para relacionar el cliente con interacciones, acciones y bloqueos; sería obligatorio en V1.
- nombre_cliente: representa el nombre de la persona de contacto o cliente principal; es útil para identificar rápidamente a quién se está siguiendo; sería obligatorio en V1.
- nombre_empresa: representa la empresa asociada al cliente; es útil cuando una misma organización tiene varias personas o contactos; sería recomendable en V1.
- estado_cliente: representa la situación operativa general del cliente; es útil para filtrar clientes activos, bloqueados, en riesgo o cerrados; sería obligatorio en V1.
- ultima_interaccion: representa la fecha o referencia de la última interacción registrada; es útil para detectar seguimientos antiguos o posibles olvidos; sería recomendable en V1.
- proxima_accion: representa la siguiente acción prevista con el cliente; es útil para detectar clientes sin seguimiento definido; sería obligatorio en V1 cuando el cliente esté activo.
- responsable_interno: representa la persona del equipo que debe revisar o ejecutar el seguimiento; es útil para evitar ambigüedad operativa; sería obligatorio en V1.
- prioridad: representa el nivel de atención necesario; es útil para ordenar revisiones y decidir qué clientes revisar primero; sería recomendable en V1.
- riesgo_operativo: representa una señal de posible problema, retraso o deterioro de la relación; es útil para priorizar revisión humana; sería recomendable en V1.
- bloqueo: representa si existe un impedimento que dificulta avanzar; es útil para diferenciar clientes pendientes de clientes realmente bloqueados; sería recomendable en V1.
- fecha_prevista_seguimiento: representa cuándo debería revisarse de nuevo el cliente; es útil para detectar seguimientos vencidos; sería recomendable en V1.
- observaciones_internas: representa notas de contexto no estructuradas; es útil para añadir información cualitativa revisable por una persona; sería recomendable en V1.

## Entidad secundaria: Interacción con cliente

Esta entidad conceptual permite registrar contactos, llamadas, correos, reuniones o cualquier comunicación relevante con el cliente. Su objetivo es aportar trazabilidad básica sin depender de integraciones reales con correo o calendario.

Campos mínimos:

- identificador_interaccion: representa un identificador único de la interacción; es útil para diferenciar registros de contacto; sería obligatorio en V1 si se registran interacciones.
- identificador_cliente: representa el cliente al que pertenece la interacción; es útil para vincular cada contacto con su cliente correspondiente; sería obligatorio en V1.
- tipo_interaccion: representa si la interacción fue una llamada, correo, reunión, mensaje u otro contacto; es útil para entender el canal utilizado; sería recomendable en V1.
- fecha_interaccion: representa cuándo ocurrió la interacción; es útil para revisar antigüedad y secuencia de seguimiento; sería obligatorio en V1.
- resumen_interaccion: representa una descripción breve de lo tratado; es útil para conservar contexto operativo; sería recomendable en V1.
- responsable_interaccion: representa quién registró o realizó la interacción; es útil para trazabilidad interna; sería recomendable en V1.
- resultado_interaccion: representa el resultado principal del contacto; es útil para saber si hubo avance, bloqueo o nueva tarea; sería recomendable en V1.
- proxima_accion_derivada: representa una acción que surge de la interacción; es útil para conectar conversaciones con seguimiento operativo; sería recomendable en V1.
- observaciones_interaccion: representa notas adicionales de contexto; es útil para información que no encaja en campos cerrados; sería opcional en V1.

En V1, esta entidad puede gestionarse como una lista simple o una estructura básica. No implica integración real con correo, calendario, Google Workspace ni sistemas externos.

## Entidad secundaria: Acción de seguimiento

Esta entidad conceptual permite controlar próximas acciones asociadas a un cliente. Su función es separar el estado general del cliente de las tareas concretas necesarias para avanzar.

Campos mínimos:

- identificador_accion: representa un identificador único de la acción; es útil para distinguir acciones dentro de un mismo cliente; sería obligatorio en V1 si se registran acciones separadas.
- identificador_cliente: representa el cliente asociado a la acción; es útil para relacionar cada tarea con su contexto; sería obligatorio en V1.
- descripcion_accion: representa qué debe hacerse; es útil para que la acción sea comprensible y ejecutable; sería obligatorio en V1.
- responsable_accion: representa quién debe revisar o ejecutar la acción; es útil para asignar responsabilidad interna; sería obligatorio en V1.
- estado_accion: representa la situación actual de la acción; es útil para diferenciar acciones pendientes, bloqueadas, completadas o descartadas; sería obligatorio en V1.
- prioridad_accion: representa la importancia relativa de la acción; es útil para ordenar el trabajo; sería recomendable en V1.
- fecha_prevista: representa cuándo debería revisarse o completarse la acción; es útil para detectar retrasos; sería recomendable en V1.
- bloqueo_asociado: representa si la acción depende de un impedimento; es útil para explicar por qué una acción no avanza; sería recomendable en V1.
- observaciones_accion: representa notas internas sobre la acción; es útil para conservar contexto adicional; sería opcional en V1.

Estados posibles:

- pendiente
- en_revision
- completada
- bloqueada
- descartada

Estos estados son una propuesta inicial para V1. Deben validarse con datos ficticios antes de considerarse definitivos.

## Entidad secundaria: Bloqueo operativo

Esta entidad conceptual permite registrar impedimentos que afectan al seguimiento de un cliente. Su objetivo es hacer visibles situaciones que impiden avanzar, en lugar de mezclarlas con notas informales.

Campos mínimos:

- identificador_bloqueo: representa un identificador único del bloqueo; es útil para registrar varios bloqueos si existen; sería obligatorio en V1 si se registran bloqueos separados.
- identificador_cliente: representa el cliente afectado por el bloqueo; es útil para vincular el impedimento con el seguimiento correspondiente; sería obligatorio en V1.
- descripcion_bloqueo: representa qué impide avanzar; es útil para entender el problema operativo; sería obligatorio en V1.
- motivo_bloqueo: representa la causa principal del bloqueo; es útil para clasificar si depende del cliente, del equipo interno o de un tercero; sería recomendable en V1.
- impacto_operativo: representa cómo afecta el bloqueo al seguimiento; es útil para priorizar la revisión; sería recomendable en V1.
- responsable_revision: representa quién debe revisar el bloqueo; es útil para asignar responsabilidad; sería obligatorio en V1.
- prioridad_bloqueo: representa la urgencia o importancia del bloqueo; es útil para ordenar la resolución; sería recomendable en V1.
- estado_bloqueo: representa la situación actual del bloqueo; es útil para distinguir bloqueos activos, en revisión o resueltos; sería obligatorio en V1.
- observaciones_bloqueo: representa notas adicionales sobre el impedimento; es útil para conservar contexto; sería opcional en V1.

Estados posibles:

- activo
- en_revision
- resuelto
- descartado

## Entidad secundaria: Clasificación de riesgo

Esta entidad conceptual permite clasificar clientes según riesgo operativo o necesidad de atención. Su función es ayudar a priorizar revisiones, no automatizar decisiones comerciales.

Campos mínimos:

- identificador_clasificacion: representa un identificador único de la clasificación; es útil para separar la evaluación de riesgo del registro principal del cliente; sería recomendable en V1.
- identificador_cliente: representa el cliente clasificado; es útil para vincular la clasificación con su contexto operativo; sería obligatorio en V1 si se registra clasificación.
- nivel_riesgo: representa el nivel de riesgo asignado; es útil para priorizar revisiones; sería recomendable en V1.
- motivo_riesgo: representa por qué se considera que el cliente tiene riesgo; es útil para justificar la clasificación; sería obligatorio en V1 cuando haya riesgo marcado.
- prioridad_revision: representa la prioridad de revisión humana; es útil para ordenar clientes que requieren atención; sería recomendable en V1.
- requiere_revision_humana: representa si una persona debe validar el caso; es útil para mantener control humano sobre decisiones relevantes; sería obligatorio en V1.
- criterio_clasificacion: representa si la clasificación se hizo manualmente o mediante una regla simple; es útil para trazabilidad; sería recomendable en V1.
- observaciones_clasificacion: representa notas adicionales sobre la clasificación; es útil para aclarar dudas o matices; sería opcional en V1.

En V1, la clasificación será manual o por reglas simples, no mediante IA funcional. No existe análisis inteligente implementado ni priorización autónoma.

## Relaciones entre entidades

Las relaciones previstas son simples:

- Un cliente puede tener varias interacciones.
- Un cliente puede tener varias acciones de seguimiento.
- Un cliente puede tener varios bloqueos operativos.
- Un cliente puede tener una clasificación de riesgo.
- Una cartera de seguimiento puede agrupar varios clientes.

Estas relaciones son conceptuales y no implican todavía una base de datos real, una API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) ni integración con herramientas externas.

## Datos mínimos para una demo V1

Para demostrar la V1 con clientes ficticios bastaría con preparar un conjunto pequeño y controlado de datos.

Datos mínimos recomendados:

- Cinco o seis clientes ficticios.
- Estados de cliente variados.
- Clientes con próxima acción.
- Clientes sin próxima acción.
- Clientes bloqueados.
- Clientes en riesgo.
- Interacciones recientes o antiguas.
- Acciones pendientes.
- Revisión humana prevista.

La demo debería permitir comprobar que el modelo ayuda a revisar una cartera básica, detectar huecos de seguimiento y diferenciar casos normales, bloqueados y en riesgo.

## Datos fuera de alcance en V1

Quedan fuera de alcance en V1:

- Datos bancarios.
- Datos fiscales sensibles.
- Datos médicos.
- Credenciales.
- Contratos reales.
- Información confidencial de clientes reales.
- Historial completo de correo real.
- Conversaciones privadas reales.
- Métricas comerciales no verificadas.

No deben usarse datos reales sensibles en esta fase. Cualquier demostración debe realizarse con clientes ficticios o datos expresamente preparados para validación interna.

## Evolución posible en V2

La V2 (*Version 2 – Versión 2*) podría ampliar el modelo si la V1 queda validada y existe una necesidad real de evolucionar el agente.

Posibles ampliaciones futuras:

- Registro operativo en Google Sheets.
- Captura de interacciones mediante Google Forms.
- Recordatorios básicos.
- Dashboard operativo.
- Alertas por correo.
- Integración futura con calendario.
- Priorización asistida mediante reglas.
- Resúmenes asistidos con IA.
- Integración futura con CRM.
- API futura si el proyecto crece.

Estas opciones no están implementadas todavía. Tampoco existe Google Workspace conectado, dashboard operativo, recordatorios automáticos, CRM ni IA funcional.

## Criterios de validación del modelo

Preguntas de control:

- ¿El modelo permite representar una cartera básica de clientes?
- ¿Los campos mínimos son comprensibles?
- ¿La V1 puede demostrarse con clientes ficticios?
- ¿Se evita tratar información sensible real?
- ¿La clasificación puede hacerse sin IA?
- ¿Se pueden detectar clientes sin próxima acción?
- ¿Se pueden detectar bloqueos y riesgos?
- ¿El modelo puede evolucionar sin rehacerse desde cero?

Estas preguntas ayudan a comprobar si el modelo es suficiente para una primera implementación mínima sin introducir complejidad prematura.

## Próximos pasos

1. Preparar una cartera ficticia de clientes.
2. Preparar un flujo mínimo de validación de seguimiento manual.
3. Definir después una primera estructura de datos de ejemplo si procede.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
