# Flujo de Validación de Cobros

## Propósito

Definir un flujo manual para revisar si la cartera ficticia de cobros está suficientemente controlada antes de pensar en una implementación mínima V1 (*Version 1 – Versión 1*).

## Estado actual

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Flujo manual: preparado.
- Automatización real: no implementada todavía.

## Criterio general del flujo

La validación debe comprobar que cada cobro tenga información mínima suficiente, que el vencimiento esté claro y que una persona pueda tomar una decisión sin depender de software real.

## Entradas necesarias

- Identificador de cobro.
- Nombre del cliente.
- Importe previsto.
- Fecha de emisión.
- Fecha de vencimiento.
- Estado del cobro.
- Prioridad de seguimiento.
- Responsable interno.
- Riesgo de retraso.
- Acción siguiente.
- Previsión operativa.

## Salida esperada

- Cobro validado.
- Cobro en revisión adicional.
- Cobro bloqueado.
- Cobro descartado.
- Cobro listo para seguimiento prioritario.

## Estados de cobro de referencia

- pendiente.
- en_revision.
- vencido.
- cobrado.
- parcialmente_cobrado.
- bloqueado.
- descartado.

## Paso 1 — Confirmar identificación del cobro

- Verificar que el identificador existe.
- Revisar que el nombre del cliente sea claro.
- Comprobar que el concepto del cobro explica la entrada prevista.

## Paso 2 — Revisar vencimiento

- Confirmar que exista fecha de emisión.
- Revisar que exista fecha de vencimiento.
- Detectar si el vencimiento está próximo, superado o ya cerrado.

## Paso 3 — Revisar estado de cobro

- Comprobar si el cobro está pendiente, vencido, cobrado o bloqueado.
- Detectar si el estado es coherente con la situación descrita.
- Revisar si hay cobro parcial que requiera seguimiento.

## Paso 4 — Revisar riesgo de retraso

- Comprobar si existe riesgo de cobro.
- Identificar el motivo del riesgo.
- Evaluar el impacto operativo.
- Verificar si requiere revisión humana.

## Paso 5 — Revisar acciones de seguimiento

- Confirmar que exista una acción siguiente concreta.
- Revisar si la acción está alineada con el estado del cobro.
- Comprobar que la acción pueda ser ejecutada por una persona.

## Paso 6 — Revisar previsión operativa

- Confirmar que exista previsión documental.
- Revisar si el importe previsto es coherente con el estado.
- Detectar si la previsión es confirmada, incierta o descartada.

## Paso 7 — Decisión humana

- Decidir si el cobro puede avanzar.
- Decidir si necesita más información.
- Decidir si debe bloquearse.
- Decidir si debe descartarse.
- Decidir si conviene revisarlo de nuevo.

## Reglas mínimas de validación

- No puede faltar identificador de cobro.
- No puede faltar vencimiento.
- No puede faltar responsable interno.
- La prioridad debe tener sentido operativo.
- Un riesgo debe poder explicarse.
- Ningún cobro debe pasar a estado estable sin revisión humana si hay duda.

## Aplicación a la cartera ficticia

- COB-002 debe quedar en revisión hasta confirmar documentación.
- COB-003 debe seguir vencido y con seguimiento prioritario.
- COB-005 debe reflejarse como entrada parcial y pendiente de ajuste.
- COB-006 debe seguir bloqueado hasta resolver la dependencia interna.
- COB-004 puede considerarse cerrado si la revisión documental está completa.

## Datos fuera de alcance

- Automatización de cobros.
- Integración con correo o ERP.
- Reglas complejas de scoring financiero.
- Registro técnico persistente.
- Conexión bancaria.
- Notificaciones automáticas.
- Asesoramiento financiero, fiscal, contable o legal.

## Evolución posible V2

- Añadir validaciones semiautomáticas.
- Incorporar reglas más finas por tipo de cobro.
- Generar alertas de retraso.
- Incorporar métricas de seguimiento y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).

## Criterios de validación del flujo

- El flujo debe poder ejecutarse paso a paso de forma manual.
- Debe llevar a una decisión humana comprensible.
- Debe distinguir entre vencido, bloqueado, parcial y cobrado.
- Debe coincidir con la cartera ficticia y con el modelo de datos.

## Próximos pasos

- Usar este flujo para revisar los datos de ejemplo.
- Mantenerlo como herramienta documental de V1, no como automatización viva.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
