# Caso de Uso del Agente Generador de Propuestas para PYMES

## Propósito del documento

Este documento define el escenario funcional previsto para el agente generador de propuestas y sirve para entender cómo podría aplicarse a una pequeña o mediana empresa real.

El contenido se centra en la descripción del caso de uso, los límites del alcance y la relación entre información comercial dispersa y una propuesta inicial revisable. No describe una funcionalidad implementada ni una automatización en producción.

## Estado del caso de uso

- Estado documental: en desarrollo inicial.
- Código funcional: no implementado todavía.
- Generación automática de propuestas: no implementada todavía.
- Plantillas dinámicas: no implementadas todavía.
- Exportación PDF: no implementada todavía.
- Automatizaciones: no implementadas todavía.
- Integraciones activas: no implementadas todavía.
- Dashboard: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial

El escenario de referencia es una PYME de servicios que prepara propuestas comerciales, presupuestos iniciales o documentos base a partir de correos, llamadas, notas internas y documentos antiguos.

El problema no es solo escribir una propuesta. El reto real consiste en estructurar bien el alcance, los entregables, las condiciones pendientes y los límites antes de enviarla. Sin una estructura común, el equipo puede reutilizar material anterior de forma inconsistente y perder claridad sobre lo que realmente se está ofreciendo.

## Situación inicial sin agente

Sin un agente de apoyo, la empresa puede encontrarse con problemas como:

- Propuestas creadas copiando documentos anteriores.
- Condiciones comerciales reutilizadas sin revisión.
- Alcances ambiguos o incompletos.
- Entregables poco definidos.
- Falta de criterios comunes entre propuestas.
- Dependencia de una persona que recuerda cómo preparar cada documento.
- Riesgo de enviar propuestas incompletas.
- Pérdida de tiempo preparando borradores desde cero.

Esta situación produce propuestas heterogéneas y aumenta el riesgo de errores de contenido, de forma y de alcance.

## Objetivo del caso de uso

El objetivo del caso de uso es convertir información comercial dispersa en una propuesta inicial estructurada, revisable y coherente.

El caso de uso debe permitir:

- Registrar datos mínimos de la oportunidad.
- Definir el servicio propuesto.
- Identificar necesidad principal.
- Delimitar alcance preliminar.
- Identificar entregables.
- Marcar condiciones pendientes.
- Preparar un borrador conceptual para revisión humana.

La revisión humana es una condición central del diseño. El agente no debe emitir propuestas finales por sí mismo ni sustituir el criterio comercial.

## Actores implicados

### Responsable comercial o interno

Revisa la oportunidad, valida el alcance, confirma condiciones y decide si la propuesta puede avanzar.

### Equipo técnico u operativo

Aporta información sobre entregables, plazos, límites, condiciones y riesgos de ejecución.

### Agente generador de propuestas

En la visión prevista, ayuda a estructurar información, detectar campos pendientes y preparar un borrador conceptual. Todavía no hay agente funcional implementado, por lo que esta descripción corresponde al diseño funcional esperado y no a una capacidad disponible actualmente.

## Flujo funcional previsto

El flujo funcional previsto, sin código, sería el siguiente:

1. Recepción de información de oportunidad.
2. Registro de datos mínimos.
3. Revisión de necesidad principal.
4. Definición preliminar del servicio.
5. Identificación de alcance y entregables.
6. Detección de condiciones pendientes.
7. Preparación de borrador conceptual.
8. Revisión humana.
9. Decisión de completar, ajustar o preparar propuesta final.

Este flujo es un diseño funcional previsto, no una ejecución automática actual. Su función es orientar una futura implementación mínima y mantener el alcance controlado.

## Datos mínimos del caso de uso

Posibles datos mínimos:

- Identificador de propuesta.
- Nombre del cliente.
- Empresa.
- Tipo de oportunidad.
- Servicio propuesto.
- Necesidad principal.
- Alcance preliminar.
- Entregables previstos.
- Plazo estimado.
- Condiciones comerciales pendientes.
- Responsable interno.
- Estado de propuesta.
- Observaciones internas.
- Próxima acción comercial.

Todavía no existe captura funcional automatizada. Estos datos se presentan como base documental para validar una futura V1 (*Version 1 – Versión 1*).

## Estados de propuesta previstos

- borrador: existe una versión inicial sin validar.
- pendiente_informacion: faltan datos mínimos para avanzar.
- en_revision: la propuesta está siendo revisada internamente.
- lista_para_revisar: la propuesta puede revisarse por la persona responsable.
- bloqueada: no puede avanzar por falta de información o por un problema operativo.
- descartada: la oportunidad o el borrador no continúan.
- preparada_para_envio: la propuesta ha superado la revisión humana prevista.

## Estados de condición comercial previstos

- pendiente: la condición todavía no está definida.
- definida: la condición ya está establecida y no bloquea el avance.
- en_revision: la condición necesita revisión antes de considerarse cerrada.
- bloqueada: la condición impide avanzar con seguridad.
- descartada: la condición deja de ser necesaria en el contexto actual.

## Estructura conceptual de propuesta

La estructura base prevista podría organizarse en los siguientes bloques:

- Contexto del cliente.
- Necesidad detectada.
- Servicio propuesto.
- Alcance incluido.
- Fuera de alcance.
- Entregables.
- Plazo estimado.
- Condiciones pendientes.
- Próximos pasos.
- Revisión interna.

Esta estructura es conceptual y no una plantilla dinámica funcional. Sirve para documentar cómo debería organizarse una propuesta de forma coherente antes de pensar en automatización.

## Clasificación inicial prevista

En la V1, la clasificación podría ser manual o basada en reglas simples.

Posibles criterios:

- Propuesta incompleta.
- Alcance ambiguo.
- Condiciones pendientes.
- Entregables no definidos.
- Propuesta lista para revisión.
- Propuesta bloqueada por falta de datos.

La clasificación con IA sería una evolución futura, no una funcionalidad actual. En esta fase no existe priorización inteligente real ni generación automática de decisiones.

## Resultado esperado en V1

El resultado mínimo esperado en V1 debe ser una salida sencilla, verificable y útil para revisión comercial.

La salida podría incluir:

- Borrador conceptual estructurado.
- Lista de campos incompletos.
- Alcance preliminar revisable.
- Entregables propuestos.
- Condiciones pendientes.
- Estado de propuesta.
- Próximas acciones para revisión humana.

La V1 debe poder demostrarse con datos ficticios de propuesta, sin depender de generación automática real ni integraciones complejas.

## Evolución V2 futura

La V2 (*Version 2 – Versión 2*) futura podría ampliar el caso de uso si se valida la base documental y, más adelante, una implementación mínima.

Posibles mejoras futuras:

- Formulario de entrada de oportunidad.
- Registro en Google Sheets.
- Generación documental en Google Docs.
- Exportación futura a PDF (*Portable Document Format – Formato de Documento Portátil*).
- Plantillas reutilizables.
- Dashboard de propuestas.
- Sugerencias asistidas con IA.
- Resúmenes comerciales asistidos.
- Integración futura con CRM.

Estas mejoras no están implementadas todavía. Describen una evolución posible, no el estado actual del agente.

## Fuera de alcance inicial

Quedan fuera del alcance inicial:

- Generación automática completa de propuestas.
- Envío automático a clientes.
- Firma digital.
- Exportación PDF funcional.
- Gestión contractual avanzada.
- Cálculo financiero avanzado.
- CRM completo en producción.
- Integración real con Google Workspace.
- Dashboard funcional.
- API pública.
- Multiempresa real.
- Sustitución de criterio comercial.
- Métricas de conversión no verificadas.

## Criterios de validación funcional

Preguntas de control:

- ¿El caso de uso representa un problema real de preparación de propuestas en una PYME?
- ¿La entrada y la salida se entienden?
- ¿La V1 puede demostrarse con datos ficticios?
- ¿Está claro qué parte no está implementada?
- ¿La revisión humana está contemplada?
- ¿La V2 está separada del alcance actual?
- ¿El flujo evita prometer generación automática inexistente?
- ¿Se evita prometer IA, PDF, CRM o Google Workspace no implementados?

## Próximos pasos

1. Completar el roadmap de evolución del agente generador de propuestas.
2. Definir después el modelo conceptual mínimo de datos para la V1.
3. Preparar después un ejemplo ficticio de propuesta para validación.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
