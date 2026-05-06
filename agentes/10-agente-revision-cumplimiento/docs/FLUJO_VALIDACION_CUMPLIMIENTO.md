# Flujo de Validación de Cumplimiento

## Propósito

Definir un flujo manual para revisar si la revisión ficticia está suficientemente ordenada antes de pensar en una implementación mínima V1 (*Version 1 – Versión 1*).

## Estado actual

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Flujo manual: preparado.
- Automatización real: no implementada todavía.

## Aviso de límites profesionales

Este flujo no es asesoría legal, fiscal, laboral, financiera ni regulatoria. Tampoco garantiza cumplimiento normativo ni evita sanciones, riesgos legales o incumplimientos.

## Criterio general del flujo

La validación debe comprobar que cada control tenga información mínima suficiente, que la evidencia esté clara y que una persona pueda tomar una decisión sin depender de software real.

## Entradas necesarias

- Identificador de control.
- Nombre del control.
- Área de control.
- Tipo de control.
- Estado del control.
- Prioridad de revisión.
- Responsable interno.
- Evidencia asociada.
- Hallazgo asociado.
- Documento pendiente.
- Acción de seguimiento.

## Salida esperada

- Control validado.
- Control en revisión adicional.
- Control bloqueado.
- Control descartado.
- Control listo para seguimiento prioritario.

## Tipos de control de referencia

- documental.
- datos_personales.
- proveedores.
- permisos.
- proceso_interno.
- seguridad_basica.
- formacion.

## Estados de control de referencia

- pendiente.
- en_revision.
- revisado.
- bloqueado.
- descartado.

## Paso 1 — Confirmar identificación del control

- Verificar que el identificador existe.
- Revisar que el nombre del control sea claro.
- Comprobar que la descripción explica la revisión.

## Paso 2 — Revisar evidencia disponible

- Confirmar que exista evidencia cuando aplique.
- Revisar si la evidencia es suficiente.
- Detectar si la evidencia necesita validación humana adicional.

## Paso 3 — Revisar hallazgos internos

- Identificar si existe hallazgo asociado.
- Evaluar el nivel de riesgo operativo.
- Verificar si el hallazgo necesita revisión humana.

## Paso 4 — Revisar documentos pendientes

- Comprobar qué documento falta.
- Identificar el motivo del pendiente.
- Evaluar el impacto operativo.

## Paso 5 — Revisar acciones de seguimiento

- Confirmar que exista una acción concreta.
- Revisar si la acción está alineada con el control o con el hallazgo.
- Comprobar que la acción pueda ser ejecutada por una persona.

## Paso 6 — Decisión humana

- Decidir si el control puede avanzar.
- Decidir si necesita más información.
- Decidir si debe bloquearse.
- Decidir si debe descartarse.
- Decidir si conviene revisarlo de nuevo.

## Reglas mínimas de validación

- No puede faltar identificador de control.
- No puede faltar tipo de control.
- No puede faltar responsable interno.
- La prioridad debe tener sentido operativo.
- Un hallazgo debe poder explicarse.
- Ningún control debe pasar a estado estable sin revisión humana si hay duda.

## Aplicación a la revisión ficticia

- CON-002 debe quedar en revisión hasta completar la validación de datos.
- CON-004 debe seguir bloqueado hasta resolver permisos.
- CON-005 puede considerarse revisado si el cierre mensual está documentado.
- CON-003 necesita completar el documento pendiente antes de avanzar.
- CON-007 puede mantenerse descartado si la formación duplicada no aporta valor adicional.

## Datos fuera de alcance

- Revisión automática real.
- Motor normativo.
- Integración con correo o ERP real.
- Registros técnicos persistentes.
- Dashboard funcional.
- Notificaciones automáticas.
- Asesoramiento legal, fiscal, laboral, financiero o regulatorio.

## Evolución posible V2

- Añadir validaciones semiautomáticas.
- Incorporar reglas más finas por tipo de control.
- Generar alertas internas.
- Incorporar métricas de revisión y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).

## Criterios de validación del flujo

- El flujo debe poder ejecutarse paso a paso de forma manual.
- Debe llevar a una decisión humana comprensible.
- Debe distinguir entre bloqueo, revisión y descarte.
- Debe coincidir con la revisión ficticia y con el modelo de datos.

## Próximos pasos

- Usar este flujo para revisar los datos de ejemplo.
- Mantenerlo como herramienta documental de V1, no como automatización viva.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
