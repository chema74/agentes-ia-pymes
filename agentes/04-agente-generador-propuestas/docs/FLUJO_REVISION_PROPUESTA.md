# Flujo de Revisión Manual de Propuesta del Agente Generador de Propuestas para PYMES

## Propósito del documento

Este documento define un flujo mínimo para revisar manualmente si una propuesta inicial está suficientemente estructurada para avanzar.

No describe una automatización implementada, sino un procedimiento operativo para validar una propuesta ficticia. El objetivo es comprobar si la propuesta, el modelo de datos y las reglas mínimas permiten detectar huecos antes de pensar en una implementación funcional.

## Estado actual

- Estado documental: flujo mínimo de revisión para V1.
- Código funcional: no implementado todavía.
- Generación automática de propuestas: no implementada todavía.
- Plantillas dinámicas: no implementadas todavía.
- Exportación PDF: no implementada todavía.
- Automatizaciones: no implementadas todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
- Dashboard: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Criterio general del flujo

El flujo debe ser:

- Simple.
- Repetible.
- Revisable.
- Aplicable a propuestas ficticias.
- Útil para detectar campos incompletos.
- Útil para detectar condiciones pendientes.
- Útil para separar alcance incluido y fuera de alcance.
- Fácil de convertir después en reglas o script mínimo.

El criterio principal es que una persona pueda revisar la propuesta sin depender de generación automática, PDF, CRM, dashboard, Google Workspace, API ni IA funcional implementada.

## Entradas necesarias para validar

Entradas mínimas:

- Propuesta ficticia.
- Cliente.
- Empresa.
- Servicio propuesto.
- Necesidad principal.
- Alcance preliminar.
- Entregables previstos.
- Condiciones comerciales.
- Acciones comerciales siguientes.
- Revisión humana prevista.

Estas entradas pueden proceder del documento `PROPUESTA_FICTICIA.md`. La validación debe hacerse con datos ficticios o no sensibles.

## Salida esperada del flujo

Las posibles salidas del flujo son:

- Propuesta preparada para avanzar: la propuesta está suficientemente estructurada y solo espera el paso final de revisión humana.
- Propuesta pendiente de información: faltan datos relevantes para decidir o completar la estructura.
- Propuesta bloqueada: existe un impedimento que debe resolverse antes de avanzar.
- Propuesta descartada: la oportunidad o el borrador no continúan en el flujo actual.
- Propuesta no aplicable al flujo actual: la propuesta ya está cerrada o fuera del alcance previsto para la V1.

Estas salidas deben ser revisadas por una persona. No deben generarse ni ejecutarse decisiones automáticas en esta fase.

## Estados de propuesta de referencia

- borrador: existe una versión inicial sin validar.
- pendiente_informacion: faltan datos mínimos para avanzar.
- en_revision: la propuesta está siendo revisada internamente.
- lista_para_revisar: la propuesta puede revisarse por la persona responsable.
- bloqueada: no puede avanzar por falta de información o por un problema operativo.
- descartada: la oportunidad o el borrador no continúan.
- preparada_para_envio: la propuesta ha superado la revisión humana prevista.

## Estados de condición comercial de referencia

- pendiente: la condición todavía no está definida.
- definida: la condición ya está establecida y no bloquea el avance.
- en_revision: la condición necesita revisión antes de considerarse cerrada.
- bloqueada: la condición impide avanzar con seguridad.
- descartada: la condición deja de ser necesaria en el contexto actual.

## Paso 1 — Confirmar datos básicos de la propuesta

Se revisa:

- Identificador de propuesta.
- Nombre del cliente.
- Empresa.
- Tipo de oportunidad.
- Servicio propuesto.
- Responsable interno.

Criterios de validación:

- Si falta cliente o empresa, la propuesta queda pendiente de información.
- Si no hay servicio propuesto, la propuesta no debe avanzar.
- Si no hay responsable interno, debe quedar en revisión.
- Si los datos mínimos están completos, pasa al siguiente paso.

La identificación básica es el punto de entrada del flujo. Sin estos datos no debe considerarse que la propuesta esté suficientemente controlada.

## Paso 2 — Revisar necesidad principal

Se revisa:

- Necesidad declarada.
- Problema que se intenta resolver.
- Contexto del cliente.
- Información incompleta.
- Supuestos pendientes.

Criterios de validación:

- Si la necesidad principal es ambigua, requiere revisión humana.
- Si hay supuestos no confirmados, deben marcarse como pendientes.
- Si la necesidad está clara, pasa al siguiente paso.

La necesidad principal es la base que justifica la propuesta y orienta el resto de la estructura.

## Paso 3 — Revisar alcance incluido y fuera de alcance

Se revisa:

- Alcance incluido.
- Elementos pendientes de definir.
- Elementos fuera de alcance.
- Riesgos de ambigüedad.
- Observaciones internas.

Criterios de validación:

- Una propuesta sin alcance incluido no debe avanzar.
- Una propuesta sin fuera de alcance puede requerir revisión.
- Un alcance pendiente de definir debe marcarse como condición pendiente.
- No debe confundirse borrador conceptual con propuesta final.

Separar el alcance incluido y el fuera de alcance es uno de los puntos más importantes de la revisión manual.

## Paso 4 — Revisar entregables

Se revisa:

- Entregables definidos.
- Entregables pendientes.
- Entregables en revisión.
- Entregables descartados.
- Observaciones de cada entregable.

Criterios de validación:

- Una propuesta sin entregables definidos no debe avanzar.
- Un entregable pendiente debe tener responsable o acción siguiente.
- Un entregable en revisión debe revisarse antes de marcar la propuesta como lista.
- Los entregables descartados no deben aparecer como incluidos.

Los entregables permiten concretar la propuesta y reducen el riesgo de interpretaciones distintas entre equipo y cliente.

## Paso 5 — Revisar condiciones comerciales

Se revisa:

- Condiciones pendientes.
- Condiciones definidas.
- Condiciones en revisión.
- Condiciones bloqueadas.
- Impacto comercial.
- Responsable de revisión.

Criterios de validación:

- Una condición pendiente de alto impacto impide considerar la propuesta lista.
- Una condición bloqueada debe tener motivo y responsable.
- Las condiciones definidas deben estar revisadas antes de avanzar.
- No deben reutilizarse condiciones antiguas sin revisión.

Las condiciones comerciales son parte del control de calidad del borrador. No deben asumirse por inercia ni copiarse sin validación.

## Paso 6 — Revisar acciones comerciales siguientes

Se revisa:

- Acción siguiente.
- Responsable de la acción.
- Estado de la acción.
- Prioridad.
- Fecha prevista ficticia o estimada.
- Observaciones.

Criterios de validación:

- Si no hay próxima acción, la propuesta no está preparada.
- Si no hay responsable de acción, queda pendiente.
- Si la acción está bloqueada, debe indicarse motivo.
- Si hay acción clara y responsable asignado, pasa al cierre.

La acción siguiente ayuda a decidir qué debe ocurrir después de la revisión manual, antes de considerar el documento listo.

## Paso 7 — Decisión final de revisión humana

Posibles decisiones:

- avanzar: la propuesta está suficientemente estructurada y puede seguir el flujo.
- pedir_informacion: falta información necesaria para completar o cerrar la revisión.
- bloquear: existe un impedimento que debe resolverse antes de avanzar.
- descartar: el borrador o la oportunidad no continúan.
- revisar_de_nuevo: el caso necesita una segunda revisión antes de tomar una decisión.

Ninguna decisión debe tomarse de forma automática en esta V1. La decisión final debe quedar siempre sujeta a revisión humana.

## Reglas mínimas de validación

- Una propuesta sin cliente no debe avanzar.
- Una propuesta sin servicio propuesto no debe avanzar.
- Una propuesta sin responsable interno queda en revisión.
- Una propuesta sin alcance incluido no debe avanzar.
- Una propuesta sin entregables definidos no debe avanzar.
- Una condición pendiente de alto impacto bloquea la propuesta.
- Toda propuesta abierta debe tener próxima acción.
- Toda propuesta debe tener revisión humana antes de considerarse lista.
- No debe enviarse ninguna propuesta desde esta V1.

Estas reglas son deliberadamente simples para que puedan revisarse manualmente y convertirse después, si procede, en una lógica mínima verificable.

## Aplicación a la propuesta ficticia

Para aplicar este flujo al documento `PROPUESTA_FICTICIA.md`, se debe revisar:

- Datos básicos.
- Necesidad principal.
- Alcance incluido y fuera de alcance.
- Entregables.
- Condiciones comerciales.
- Acciones siguientes.
- Revisión humana.
- Decisión final.

No es necesario reescribir toda la propuesta. La validación consiste en recorrer cada bloque, aplicar los pasos anteriores y asignar una salida final revisada por una persona.

## Datos fuera de alcance en este flujo

Quedan fuera de alcance:

- Datos bancarios.
- Datos fiscales sensibles.
- Contratos reales.
- Documentación legal compleja.
- Credenciales.
- Firmas digitales.
- Información confidencial de clientes reales.
- Márgenes comerciales reales.
- Condiciones contractuales reales.
- Métricas de conversión no verificadas.

La validación debe hacerse con datos ficticios o no sensibles. No deben incorporarse datos reales de clientes ni información privada para probar esta fase documental.

## Evolución posible en V2

En una V2 (*Version 2 – Versión 2*) futura, este flujo podría evolucionar hacia mejoras como:

- Conversión del flujo a reglas automáticas.
- Entrada mediante formulario.
- Registro en Google Sheets.
- Generación documental en Google Docs.
- Exportación futura a PDF.
- Dashboard de propuestas.
- Plantillas reutilizables.
- Sugerencias asistidas con IA.
- Integración futura con CRM.

Estas opciones no están implementadas todavía. No existe automatización real, conexión con Google Workspace, correo, calendario, CRM, dashboard, API ni IA funcional.

## Criterios de validación del flujo

Preguntas de control:

- ¿El flujo permite revisar una propuesta ficticia?
- ¿Los pasos son claros?
- ¿Las decisiones finales están definidas?
- ¿Se detectan campos incompletos?
- ¿Se detectan condiciones pendientes?
- ¿Se separa alcance incluido y fuera de alcance?
- ¿Existe revisión humana antes de considerar la propuesta lista?
- ¿Se evita prometer generación automática, PDF, CRM o IA no implementados?

## Próximos pasos

1. Crear una estructura de datos de ejemplo para la propuesta.
2. Revisar si el README del agente 04 debe enlazar los documentos V1.
3. Preparar después una revisión documental del agente 04 antes de decidir si se implementa código mínimo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
