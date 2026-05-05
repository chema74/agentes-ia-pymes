# Caso de Uso del Agente de Seguimiento de Clientes para PYMES

## Propósito del documento

Este documento define el escenario funcional previsto para el Agente de Seguimiento de Clientes para PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*). Su finalidad es explicar cómo podría aplicarse el agente a una pequeña o mediana empresa real que necesita ordenar el seguimiento de clientes activos.

El documento sirve como base de análisis funcional para el portfolio técnico. No describe un producto terminado ni una automatización actualmente operativa, sino un caso de uso realista, verificable y preparatorio para una implementación posterior.

## Estado del caso de uso

- Estado documental: en desarrollo inicial.
- Código funcional: no implementado todavía.
- Automatizaciones: no implementadas todavía.
- Recordatorios automáticos: no implementados todavía.
- Integraciones activas: no implementadas todavía.
- Dashboard: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial

El escenario de referencia es una PYME de servicios que gestiona varios clientes activos a la vez. La información sobre cada cliente suele estar repartida entre correos, llamadas, notas internas, conversaciones informales y hojas sueltas.

El problema no consiste únicamente en tener muchos clientes registrados. La dificultad real aparece cuando el equipo necesita saber qué necesita cada cliente, cuál fue la última interacción, qué próxima acción está pendiente, quién debe ejecutarla y qué seguimiento se encuentra bloqueado.

En este contexto, el agente se plantea como una base funcional para ordenar el seguimiento operativo, facilitar la revisión humana y reducir el riesgo de perder compromisos relevantes.

## Situación inicial sin agente

Sin un sistema común de seguimiento, la empresa puede encontrarse con problemas como:

- Clientes sin estado operativo claro.
- Próximas acciones no registradas.
- Seguimientos que dependen de memoria personal.
- Llamadas y correos sin trazabilidad.
- Tareas dispersas entre varias personas.
- Clientes bloqueados sin visibilidad.
- Dificultad para priorizar.
- Riesgo de olvidar compromisos o perder oportunidades.

Esta situación genera una gestión reactiva. El equipo actúa cuando recuerda una tarea, recibe una reclamación o detecta tarde que un cliente llevaba tiempo sin seguimiento.

## Objetivo del caso de uso

El objetivo del caso de uso es convertir una cartera de clientes dispersa en una vista inicial revisable, con estados, próximas acciones, bloqueos y prioridades.

El caso de uso debe permitir:

- Registrar clientes activos.
- Definir estado de seguimiento.
- Detectar clientes sin próxima acción.
- Identificar bloqueos.
- Priorizar seguimiento.
- Generar una vista operativa para revisión humana.

La revisión humana es una condición funcional clave. El agente no debe decidir por la empresa ni ejecutar acciones comerciales sin validación de una persona responsable.

## Actores implicados

### Responsable interno

Revisa el estado del cliente, valida próximas acciones y decide prioridades. También confirma si una recomendación operativa tiene sentido antes de aplicarla.

### Equipo operativo o comercial

Aporta información sobre interacciones, tareas pendientes y compromisos con clientes. Puede informar de bloqueos, cambios de prioridad o acciones ya realizadas.

### Agente de seguimiento

En la visión prevista, ayuda a estructurar estados, detectar huecos de seguimiento, señalar bloqueos y preparar próximas acciones. Todavía no hay agente funcional implementado, por lo que esta descripción corresponde al diseño funcional esperado y no a una capacidad actualmente disponible.

## Flujo funcional previsto

El flujo funcional previsto, sin código ni automatización actual, sería el siguiente:

1. Registro o revisión del cliente.
2. Registro de última interacción.
3. Revisión del estado actual.
4. Identificación de próxima acción.
5. Detección de clientes sin seguimiento.
6. Identificación de bloqueos o riesgos.
7. Priorización operativa.
8. Revisión humana.
9. Confirmación de siguiente acción.

Este flujo es un diseño funcional previsto, no una ejecución automática actual. En la fase documental inicial no existe procesamiento automático, integración con herramientas externas ni generación autónoma de recomendaciones.

## Datos mínimos del caso de uso

Para que el caso de uso pueda validarse en una V1 (*Version 1 – Versión 1*) implementable, se prevén datos mínimos como:

- Identificador del cliente.
- Nombre del cliente.
- Empresa.
- Estado del cliente.
- Última interacción.
- Próxima acción.
- Responsable interno.
- Prioridad.
- Riesgo operativo.
- Bloqueo.
- Fecha prevista de seguimiento.
- Observaciones internas.
- Estado de la acción siguiente.

Todavía no existe captura funcional automatizada. Estos datos son una propuesta de estructura mínima para una implementación futura o para una demostración con datos ficticios.

## Estados de cliente previstos

Los estados de cliente previstos son:

- activo: el cliente está en seguimiento normal y tiene actividad vigente.
- pendiente_revision: el cliente necesita una revisión interna antes de confirmar la siguiente acción.
- esperando_cliente: el seguimiento depende de una respuesta, documentación o decisión del cliente.
- bloqueado: existe un impedimento que detiene el avance operativo.
- en_riesgo: hay señales de posible deterioro de la relación, retraso relevante o pérdida de oportunidad.
- cerrado: el seguimiento se ha completado o la relación operativa ha finalizado.
- descartado: el cliente o caso queda fuera del seguimiento previsto.

Estos estados son conceptuales y deben validarse antes de convertirse en reglas operativas.

## Estados de acción previstos

Los estados de acción previstos son:

- pendiente: la acción está definida, pero todavía no se ha ejecutado.
- en_revision: la acción necesita validación interna antes de completarse.
- completada: la acción ya se ha realizado y puede registrarse como cerrada.
- bloqueada: la acción no puede avanzar por una dependencia o impedimento.
- descartada: la acción deja de ser necesaria o queda fuera del seguimiento.

Estos estados ayudan a separar el estado general del cliente del estado concreto de la siguiente acción.

## Clasificación inicial prevista

En la V1, la clasificación podría ser manual o basada en reglas simples. El objetivo sería detectar situaciones operativas evidentes sin depender de modelos avanzados ni de automatización compleja.

Criterios posibles:

- Cliente sin próxima acción.
- Cliente con bloqueo.
- Cliente con seguimiento vencido.
- Cliente con riesgo operativo.
- Cliente prioritario.
- Cliente en espera de respuesta.

La clasificación con IA sería una evolución futura, no una funcionalidad actual. En esta fase no hay análisis inteligente implementado, generación automática de resúmenes ni priorización autónoma.

## Resultado esperado en V1

El resultado mínimo esperado en V1 debe ser una salida sencilla, verificable y útil para revisión operativa.

La salida podría incluir:

- Lista de clientes activos.
- Lista de clientes sin próxima acción.
- Lista de clientes bloqueados.
- Lista de clientes en riesgo.
- Seguimientos pendientes.
- Priorización operativa simple.
- Próximas acciones para revisión humana.

La V1 debe poder demostrarse con datos ficticios de clientes, sin depender de integraciones complejas, CRM, dashboard, recordatorios automáticos ni IA generativa funcional.

## Evolución V2 futura

La V2 (*Version 2 – Versión 2*) futura podría ampliar el caso de uso una vez validada la base documental y una primera implementación mínima.

Mejoras posibles:

- Registro operativo en Google Sheets.
- Captura de interacciones mediante Google Forms.
- Dashboard operativo.
- Alertas por correo.
- Recordatorios básicos.
- Integración futura con calendario.
- Resúmenes asistidos con IA.
- Integración futura con CRM.
- KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*) operativos de seguimiento.

Estas mejoras no están implementadas todavía. También podría evaluarse una API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) en una fase posterior si existiera una necesidad real de integración, pero no forma parte del alcance inicial.

## Fuera de alcance inicial

Quedan fuera del alcance inicial:

- CRM completo en producción.
- Automatización comercial completa.
- Recordatorios automáticos reales.
- Dashboard funcional.
- Integración real con Google Workspace.
- Integración con correo real.
- Integración con calendario real.
- Decisiones comerciales sin revisión humana.
- Multiempresa real.
- API pública.
- Sustitución de gestión comercial o atención humana.
- Métricas de impacto no verificadas.

Estos elementos pueden ser relevantes en una solución avanzada, pero no deben presentarse como capacidades actuales del agente.

## Criterios de validación funcional

Preguntas de control para validar el caso de uso:

- ¿El caso de uso representa un problema real de seguimiento de clientes en una PYME?
- ¿La entrada y la salida se entienden?
- ¿La V1 puede demostrarse con datos ficticios?
- ¿Está claro qué parte no está implementada?
- ¿La revisión humana está contemplada?
- ¿La V2 está separada del alcance actual?
- ¿El flujo evita prometer automatización comercial inexistente?
- ¿Se evita prometer CRM, recordatorios o IA no implementada?

Si estas preguntas pueden responderse afirmativamente, el caso de uso estará suficientemente delimitado para avanzar hacia el roadmap y el modelo conceptual mínimo de datos.

## Próximos pasos

1. Completar el roadmap de evolución del agente de seguimiento.
2. Definir después el modelo conceptual mínimo de datos para la V1.
3. Preparar después una cartera ficticia de clientes para validación.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
