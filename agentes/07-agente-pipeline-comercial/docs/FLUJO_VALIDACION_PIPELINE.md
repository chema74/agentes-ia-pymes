# Flujo de Validación del Pipeline

## Propósito

Definir un flujo manual para revisar si el pipeline comercial ficticio está suficientemente controlado antes de pensar en una implementación mínima V1 (*Version 1 – Versión 1*).

## Estado actual

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Flujo manual: preparado.
- Automatización real: no implementada todavía.

## Criterio general del flujo

La validación debe comprobar que cada oportunidad tenga información mínima suficiente, que la fase esté clara y que una persona pueda tomar una decisión sin depender de software real.

## Entradas necesarias

- Identificador de oportunidad.
- Nombre del cliente.
- Servicio de interés.
- Fase comercial.
- Estado de la oportunidad.
- Temperatura comercial.
- Prioridad.
- Responsable interno.
- Próxima acción.
- Bloqueo comercial.
- Clasificación comercial.

## Salida esperada

- Oportunidad validada.
- Oportunidad en revisión adicional.
- Oportunidad bloqueada.
- Oportunidad descartada.
- Oportunidad lista para seguimiento prioritario.

## Fases comerciales de referencia

- primer_contacto.
- diagnostico.
- propuesta.
- negociacion.
- pendiente_decision.
- ganada.
- perdida.

## Estados de oportunidad de referencia

- abierta.
- en_revision.
- bloqueada.
- ganada.
- perdida.
- descartada.

## Paso 1 — Confirmar identificación de oportunidad

- Verificar que el identificador existe.
- Revisar que el nombre del cliente sea claro.
- Comprobar que el servicio de interés explica la necesidad comercial.

## Paso 2 — Revisar fase comercial

- Confirmar que exista una fase comercial concreta.
- Revisar si la fase es coherente con el estado actual.
- Detectar si la oportunidad necesita avance o revisión humana.

## Paso 3 — Revisar temperatura y prioridad

- Comprobar que exista temperatura comercial.
- Revisar si la prioridad es coherente con el impacto operativo.
- Detectar si la temperatura está inflada o infravalorada.

## Paso 4 — Revisar próxima acción

- Confirmar que exista una acción siguiente concreta.
- Revisar si la acción está alineada con la fase comercial.
- Comprobar que la acción pueda ser ejecutada por una persona.

## Paso 5 — Revisar bloqueos comerciales

- Comprobar si existe bloqueo asociado.
- Identificar la causa del bloqueo.
- Evaluar el impacto comercial.
- Verificar que exista responsable de revisión.

## Paso 6 — Revisar decisión humana

- Decidir si la oportunidad puede avanzar.
- Decidir si necesita más información.
- Decidir si debe bloquearse.
- Decidir si debe descartarse.
- Decidir si conviene revisarla de nuevo.

## Reglas mínimas de validación

- No puede faltar identificador de oportunidad.
- No puede faltar fase comercial.
- No puede faltar responsable interno.
- La prioridad debe tener sentido operativo.
- Un bloqueo debe poder explicarse.
- Ninguna oportunidad debe pasar a estado estable sin revisión humana si hay duda.

## Aplicación al pipeline ficticio

- OPO-002 debe quedar en revisión hasta confirmar el diagnóstico.
- OPO-004 debe seguir bloqueada hasta resolver el alcance.
- OPO-005 necesita una decisión humana antes de avanzar.
- OPO-006 puede considerarse ganada si el cierre documental está completo.
- OPO-007 puede tratarse como perdida si la falta de encaje está documentada.

## Datos fuera de alcance

- Automatización comercial.
- Integración con correo o CRM real.
- Scoring automático.
- Registro técnico persistente.
- Dashboard funcional.
- Notificaciones automáticas.
- Asesoramiento comercial garantizado o métricas de conversión no verificadas.

## Evolución posible V2

- Añadir validaciones semiautomáticas.
- Incorporar reglas más finas por tipo de oportunidad.
- Generar alertas de bloqueo.
- Incorporar métricas de revisión y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).

## Criterios de validación del flujo

- El flujo debe poder ejecutarse paso a paso de forma manual.
- Debe llevar a una decisión humana comprensible.
- Debe distinguir entre bloqueo, revisión y descarte.
- Debe coincidir con el pipeline ficticio y con el modelo de datos.

## Próximos pasos

- Usar este flujo para revisar los datos de ejemplo.
- Mantenerlo como herramienta documental de V1, no como automatización viva.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
