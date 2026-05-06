# Flujo de Validación Operativa

## Propósito

Definir un flujo manual para revisar si el tablero operativo ficticio está suficientemente controlado antes de pensar en una implementación mínima V1 (*Version 1 – Versión 1*).

## Estado actual

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Flujo manual: preparado.
- Automatización real: no implementada todavía.

## Criterio general del flujo

La validación debe comprobar que cada tarea tenga información mínima suficiente, que los bloqueos estén identificados y que una persona pueda tomar una decisión clara sin depender de software real.

## Entradas necesarias

- Identificador de tarea.
- Título y descripción.
- Área operativa.
- Proceso relacionado.
- Estado de la tarea.
- Prioridad.
- Responsable interno.
- Bloqueo, si existe.
- Acción siguiente.
- Revisión humana.

## Salida esperada

- Tarea validada.
- Tarea en revisión adicional.
- Tarea bloqueada.
- Tarea descartada.
- Tarea lista para avanzar.

## Estados operativos de referencia

- Tarea: pendiente, en_progreso, en_revision, bloqueada, completada, descartada.
- Proceso: activo, pendiente_revision, bloqueado, estable, descartado.
- Acción: pendiente, en_revision, completada, bloqueada, descartada.

## Paso 1 — Confirmar identificación de tarea

- Verificar que el identificador existe.
- Revisar que el título sea breve y operativo.
- Comprobar que la descripción explica la necesidad sin ambigüedad.

## Paso 2 — Revisar proceso relacionado

- Confirmar que la tarea apunta a un proceso operativo concreto.
- Revisar si el proceso está activo, estable o bloqueado.
- Detectar si el proceso necesita revisión humana adicional.

## Paso 3 — Revisar responsable y prioridad

- Comprobar que exista responsable interno.
- Revisar si la prioridad es coherente con el impacto operativo.
- Detectar si la prioridad está inflada o infravalorada.

## Paso 4 — Revisar bloqueos

- Comprobar si existe bloqueo asociado.
- Identificar la causa del bloqueo.
- Evaluar el impacto operativo.
- Verificar que exista responsable de revisión.

## Paso 5 — Revisar acciones siguientes

- Confirmar que exista una acción siguiente concreta.
- Revisar si la acción está alineada con el bloqueo o con el avance de la tarea.
- Comprobar que la acción pueda ser ejecutada por una persona.

## Paso 6 — Revisar decisión humana

- Decidir si la tarea puede avanzar.
- Decidir si necesita más información.
- Decidir si debe bloquearse.
- Decidir si debe descartarse.
- Decidir si conviene revisarla de nuevo.

## Reglas mínimas de validación

- No puede faltar identificador de tarea.
- No puede faltar proceso relacionado.
- No puede faltar responsable interno.
- La prioridad debe tener sentido operativo.
- Un bloqueo debe poder explicarse.
- Ninguna tarea debe pasar a estado estable sin revisión humana si hay duda.

## Aplicación al tablero ficticio

- TO-003 debe quedar en revisión hasta recibir confirmación del proveedor.
- TO-004 debe seguir bloqueada hasta resolver el acceso.
- TO-005 puede considerarse completada si la revisión final está cerrada.
- TO-007 necesita información adicional antes de avanzar.

## Datos fuera de alcance

- Automatización de validaciones.
- Integración con correo o ERP.
- Reglas complejas de puntuación.
- Registro técnico persistente.
- Notificaciones automáticas.

## Evolución posible V2 (*Version 2 – Versión 2*)

- Añadir validaciones semiautomáticas.
- Incorporar reglas más finas por tipo de tarea.
- Generar alertas de bloqueo.
- Incorporar métricas de revisión y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).

## Criterios de validación del flujo

- El flujo debe poder ejecutarse paso a paso de forma manual.
- Debe llevar a una decisión humana comprensible.
- Debe distinguir entre bloqueo, revisión y descarte.
- Debe coincidir con el tablero ficticio y con el modelo de datos.

## Próximos pasos

- Usar este flujo para revisar los datos de ejemplo.
- Mantenerlo como herramienta documental de V1, no como automatización viva.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
