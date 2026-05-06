# Flujo de Validación de Formación

## Propósito

Definir un flujo manual para revisar si el plan formativo ficticio está suficientemente ordenado antes de pensar en una implementación mínima V1 (*Version 1 – Versión 1*).

## Estado actual

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Flujo manual: preparado.
- Automatización real: no implementada todavía.

## Criterio general del flujo

La validación debe comprobar que cada ruta tenga información mínima suficiente, que los módulos estén claros y que una persona pueda tomar una decisión sin depender de software real.

## Entradas necesarias

- Identificador de ruta.
- Nombre de la ruta.
- Perfil destinatario.
- Objetivo formativo.
- Estado de la ruta.
- Prioridad.
- Responsable interno.
- Módulos asociados.
- Evidencias.
- Acción siguiente.

## Salida esperada

- Ruta validada.
- Ruta en revisión adicional.
- Ruta bloqueada.
- Ruta descartada.
- Ruta lista para avanzar.

## Estados formativos de referencia

- Ruta: pendiente, en_revision, activa, bloqueada, completada, descartada.
- Módulo: pendiente, en_revision, disponible, bloqueado, completado, descartado.
- Acción: pendiente, en_revision, completada, bloqueada, descartada.

## Paso 1 — Confirmar identificación de ruta

- Verificar que el identificador existe.
- Revisar que el nombre de la ruta sea claro.
- Comprobar que el objetivo formativo explica la necesidad.

## Paso 2 — Revisar perfil destinatario

- Confirmar que exista perfil interno asociado.
- Revisar si el perfil necesita esa ruta.
- Detectar si la ruta requiere revisión humana adicional.

## Paso 3 — Revisar módulos formativos

- Comprobar que existan módulos vinculados.
- Identificar módulos pendientes, bloqueados o disponibles.
- Revisar si el contenido está alineado con la ruta.

## Paso 4 — Revisar evidencias

- Confirmar que existan evidencias cuando aplique.
- Revisar si la evidencia es suficiente.
- Comprobar que el estado de la evidencia sea coherente con la ruta.

## Paso 5 — Revisar acciones siguientes

- Confirmar que exista una acción siguiente concreta.
- Revisar si la acción está alineada con la ruta o con el bloqueo.
- Comprobar que la acción pueda ser ejecutada por una persona.

## Paso 6 — Decisión humana

- Decidir si la ruta puede avanzar.
- Decidir si necesita más información.
- Decidir si debe bloquearse.
- Decidir si debe descartarse.
- Decidir si conviene revisarla de nuevo.

## Reglas mínimas de validación

- No puede faltar identificador de ruta.
- No puede faltar perfil destinatario.
- No puede faltar responsable interno.
- La prioridad debe tener sentido operativo.
- Un módulo bloqueado debe poder explicarse.
- Ninguna ruta debe pasar a estado estable sin revisión humana si hay duda.

## Aplicación al plan ficticio

- RUTA-003 debe quedar en revisión hasta completar la validación.
- RUTA-004 debe seguir bloqueada hasta liberar el módulo asociado.
- RUTA-005 puede considerarse completada si la evidencia está cerrada.
- RUTA-001 requiere revisión de contenido antes de activarse.
- RUTA-002 puede considerarse activa si los módulos disponibles se mantienen coherentes.

## Datos fuera de alcance

- Automatización de validaciones.
- Integración con correo o LMS real.
- Reglas complejas de puntuación.
- Registro técnico persistente.
- Notificaciones automáticas.
- Métricas de aprendizaje no verificadas.

## Evolución posible V2

- Añadir validaciones semiautomáticas.
- Incorporar reglas más finas por tipo de ruta.
- Generar alertas de bloqueo.
- Incorporar métricas de revisión y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).

## Criterios de validación del flujo

- El flujo debe poder ejecutarse paso a paso de forma manual.
- Debe llevar a una decisión humana comprensible.
- Debe distinguir entre bloqueo, revisión y descarte.
- Debe coincidir con el plan ficticio y con el modelo de datos.

## Próximos pasos

- Usar este flujo para revisar los datos de ejemplo.
- Mantenerlo como herramienta documental de V1, no como automatización viva.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
