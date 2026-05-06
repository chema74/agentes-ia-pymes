# Flujo de Validación de Mercado

## Propósito

Definir un flujo manual para revisar si el informe de mercado ficticio está suficientemente ordenado antes de pensar en una implementación mínima V1 (*Version 1 – Versión 1*).

## Estado actual

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Flujo manual: preparado.
- Automatización real: no implementada todavía.

## Criterio general del flujo

La validación debe comprobar que cada señal tenga información mínima suficiente, que la fuente esté clara y que una persona pueda tomar una decisión sin depender de software real.

## Entradas necesarias

- Identificador de señal.
- Título de la señal.
- Descripción.
- Tipo de señal.
- Fuente observada.
- Área de impacto.
- Nivel de relevancia.
- Estado de la señal.
- Oportunidad o riesgo asociado.
- Acción de exploración.

## Salida esperada

- Señal validada.
- Señal en revisión adicional.
- Señal bloqueada.
- Señal descartada.
- Señal lista para seguimiento prioritario.

## Tipos de señal de referencia

- demanda_cliente.
- competidor.
- precio.
- canal.
- tendencia.
- riesgo.
- oportunidad.

## Estados de señal de referencia

- nueva.
- en_revision.
- validada.
- descartada.
- bloqueada.

## Paso 1 — Confirmar identificación de señal

- Verificar que el identificador existe.
- Revisar que el título sea claro.
- Comprobar que la descripción explica la observación.

## Paso 2 — Revisar fuente observada

- Confirmar que exista fuente observada.
- Revisar si la fuente es suficiente para sostener la señal.
- Detectar si la fuente necesita revisión humana adicional.

## Paso 3 — Clasificar tipo de señal

- Confirmar que la señal tenga un tipo concreto.
- Revisar si el tipo encaja con el contenido observado.
- Detectar si la señal pertenece a demanda, competidor, precio, canal, tendencia, riesgo u oportunidad.

## Paso 4 — Revisar oportunidades

- Identificar oportunidades asociadas.
- Revisar si la oportunidad es exploratoria o ya suficientemente validada.
- Comprobar que exista responsable de exploración.

## Paso 5 — Revisar riesgos

- Identificar riesgos asociados.
- Evaluar el impacto potencial.
- Verificar que exista revisión humana cuando el riesgo sea alto o crítico.

## Paso 6 — Definir acciones de exploración

- Confirmar que exista una acción concreta.
- Revisar si la acción está alineada con la señal.
- Comprobar que la acción pueda ser ejecutada por una persona.

## Paso 7 — Decisión humana

- Decidir si la señal puede avanzar.
- Decidir si necesita más información.
- Decidir si debe bloquearse.
- Decidir si debe descartarse.
- Decidir si conviene revisarla de nuevo.

## Reglas mínimas de validación

- No puede faltar identificador de señal.
- No puede faltar fuente observada.
- No puede faltar responsable de revisión.
- La relevancia debe tener sentido operativo.
- Una señal crítica debe poder explicarse.
- Ninguna señal debe pasar a estado estable sin revisión humana si hay duda.

## Aplicación al informe ficticio

- SEN-002 debe quedar en revisión hasta confirmar la amenaza del competidor.
- SEN-006 debe seguir bloqueada hasta revisar la capacidad de atención.
- SEN-005 puede considerarse validada si la tendencia está bien documentada.
- SEN-007 puede pasar a exploración prioritaria si la oportunidad se confirma.
- SEN-008 puede mantenerse descartada si no aporta valor adicional.

## Datos fuera de alcance

- Extracción automática de fuentes.
- Scraping.
- Integración con datos reales.
- Registros técnicos persistentes.
- Dashboard funcional.
- Notificaciones automáticas.
- Asesoramiento estratégico garantizado o métricas de mercado no verificadas.

## Evolución posible V2

- Añadir validaciones semiautomáticas.
- Incorporar reglas más finas por tipo de señal.
- Generar alertas de mercado.
- Incorporar métricas de revisión y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).

## Criterios de validación del flujo

- El flujo debe poder ejecutarse paso a paso de forma manual.
- Debe llevar a una decisión humana comprensible.
- Debe distinguir entre bloqueo, revisión y descarte.
- Debe coincidir con el informe ficticio y con el modelo de datos.

## Próximos pasos

- Usar este flujo para revisar los datos de ejemplo.
- Mantenerlo como herramienta documental de V1, no como automatización viva.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
