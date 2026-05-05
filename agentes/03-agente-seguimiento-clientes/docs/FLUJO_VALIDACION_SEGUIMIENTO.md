# Flujo de Validación de Seguimiento del Agente de Seguimiento de Clientes para PYMES

## Propósito del documento

Este documento define un flujo mínimo para revisar manualmente si una cartera de clientes está suficientemente controlada para avanzar a una V1 (*Version 1 – Versión 1*) implementable del Agente de Seguimiento de Clientes para PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

No describe una automatización implementada, sino un procedimiento operativo para validar datos ficticios de seguimiento. Su objetivo es comprobar si el modelo de datos, la cartera ficticia y las reglas mínimas permiten detectar huecos de seguimiento, bloqueos y riesgos antes de crear código funcional.

## Estado actual

- Estado documental: flujo mínimo de validación para V1.
- Código funcional: no implementado todavía.
- Automatización de seguimiento: no implementada todavía.
- Recordatorios automáticos: no implementados todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- Dashboard: no implementado todavía.
- Integraciones activas: no implementadas todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Criterio general del flujo

El flujo debe ser:

- Simple.
- Repetible.
- Revisable.
- Aplicable a clientes ficticios.
- Útil para detectar clientes sin próxima acción.
- Útil para detectar bloqueos y riesgos.
- Fácil de convertir después en reglas o script mínimo.

El criterio principal es que una persona pueda revisar la cartera sin depender de CRM, dashboard, recordatorios automáticos, Google Workspace, API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) ni IA funcional implementada.

## Entradas necesarias para validar

Entradas mínimas:

- Cartera ficticia de clientes.
- Estado de cada cliente.
- Última interacción.
- Próxima acción.
- Responsable interno.
- Prioridad.
- Riesgo operativo.
- Bloqueo.
- Fecha prevista de seguimiento.
- Acciones de seguimiento.
- Clasificación de riesgo.

Estas entradas pueden proceder del documento `CARTERA_CLIENTES_FICTICIA.md`. La validación debe hacerse con datos ficticios o no sensibles.

## Salida esperada del flujo

Las posibles salidas del flujo son:

- Seguimiento preparado para avanzar: el cliente tiene datos mínimos, próxima acción clara, responsable asignado y no presenta bloqueos activos sin resolver.
- Seguimiento pendiente de información: faltan datos relevantes para decidir la siguiente acción o revisar el estado del cliente.
- Seguimiento bloqueado: existe un impedimento activo que debe resolverse antes de avanzar.
- Seguimiento no aplicable al flujo actual: el cliente está cerrado, descartado o fuera del seguimiento activo previsto para la V1.

Estas salidas deben ser revisadas por una persona. No deben generarse ni ejecutarse decisiones automáticas en esta fase.

## Estados de cliente de referencia

- activo: el cliente está en seguimiento normal y requiere una próxima acción definida.
- pendiente_revision: el cliente necesita revisión humana antes de decidir el siguiente paso.
- esperando_cliente: el avance depende de una respuesta o información pendiente por parte del cliente.
- bloqueado: existe un impedimento que impide avanzar con normalidad.
- en_riesgo: el cliente requiere atención prioritaria por posible deterioro, retraso o pérdida de oportunidad.
- cerrado: el seguimiento operativo ha finalizado y no debe mezclarse con clientes activos.
- descartado: el cliente queda fuera del seguimiento previsto y no requiere acción activa.

## Estados de acción de referencia

- pendiente: la acción está definida, pero todavía no se ha realizado.
- en_revision: la acción necesita validación humana antes de ejecutarse o cerrarse.
- completada: la acción ya se ha realizado.
- bloqueada: la acción no puede avanzar por un impedimento identificado.
- descartada: la acción deja de ser necesaria o queda fuera del flujo actual.

## Paso 1 — Confirmar identificación del cliente

Se revisa:

- Identificador del cliente.
- Nombre del cliente.
- Empresa.
- Estado del cliente.
- Responsable interno.

Criterios de validación:

- Si falta nombre o empresa, el cliente queda pendiente de información.
- Si no hay responsable interno, el cliente no debe avanzar.
- Si el estado del cliente no está definido, requiere revisión.
- Si los datos mínimos están completos, pasa al siguiente paso.

La identificación es el punto de entrada del flujo. Sin datos mínimos de cliente y responsabilidad interna, no debe considerarse que el seguimiento está controlado.

## Paso 2 — Revisar última interacción

Se revisa:

- Fecha o referencia de última interacción.
- Tipo de interacción.
- Resultado de la interacción.
- Observaciones internas.
- Próxima acción derivada.

Criterios de validación:

- Si no hay última interacción y el cliente está activo, requiere revisión.
- Si la última interacción no genera acción y el cliente sigue abierto, debe revisarse.
- Si la interacción está clara, pasa al siguiente paso.

La última interacción permite entender si el seguimiento está actualizado o si existe una posible interrupción operativa.

## Paso 3 — Revisar próxima acción

Se revisa:

- Descripción de la próxima acción.
- Responsable de la acción.
- Estado de la acción.
- Prioridad.
- Fecha prevista ficticia o estimada.

Criterios de validación:

- Un cliente activo sin próxima acción no debe marcarse como controlado.
- Una acción sin responsable queda pendiente.
- Una acción bloqueada debe indicar motivo.
- Si la próxima acción está clara, pasa al siguiente paso.

La próxima acción es el elemento central del seguimiento. Un cliente abierto sin siguiente paso representa un hueco operativo que debe ser revisado.

## Paso 4 — Revisar bloqueos operativos

Se revisa:

- Existencia de bloqueo.
- Motivo del bloqueo.
- Impacto operativo.
- Responsable de revisión.
- Estado del bloqueo.
- Observaciones.

Criterios de validación:

- Un bloqueo activo debe impedir considerar el seguimiento como preparado.
- Un bloqueo sin responsable requiere revisión.
- Un bloqueo resuelto debe quedar reflejado en el estado del cliente.
- No debe ocultarse un bloqueo por tener una acción pendiente.

Los bloqueos deben quedar visibles para evitar que un cliente parezca controlado cuando en realidad no puede avanzar.

## Paso 5 — Revisar riesgo operativo

Se revisa:

- Nivel de riesgo.
- Motivo del riesgo.
- Prioridad de revisión.
- Necesidad de revisión humana.
- Criterio de clasificación.

En V1, la clasificación será manual o por reglas simples, no generada por IA funcional.

Criterios de validación:

- Un cliente en riesgo debe tener próxima acción clara.
- Un cliente en riesgo sin responsable queda pendiente.
- Un riesgo alto requiere revisión humana.
- Si el riesgo está justificado, pasa al siguiente paso.

El riesgo operativo no debe usarse para automatizar decisiones comerciales. Sirve para priorizar revisión humana.

## Paso 6 — Priorizar seguimiento

Se revisa:

- Prioridad del cliente.
- Fecha prevista de seguimiento.
- Riesgo operativo.
- Bloqueo.
- Próxima acción.
- Responsable interno.

Criterios de validación:

- Los clientes sin próxima acción deben priorizarse para revisión.
- Los clientes bloqueados deben aparecer antes que los clientes sin incidencia.
- Los clientes en riesgo deben tener revisión humana.
- Los clientes cerrados o descartados no deben mezclarse con clientes activos.

La priorización debe ayudar a ordenar el trabajo manual. No equivale a una decisión automática ni a una ejecución comercial.

## Paso 7 — Decisión final de revisión humana

Posibles decisiones:

- avanzar: el seguimiento tiene datos mínimos, próxima acción clara y no presenta bloqueos activos sin resolver.
- pedir_informacion: falta información necesaria para decidir o ejecutar la siguiente acción.
- bloquear: existe un impedimento que debe resolverse antes de avanzar.
- descartar: el cliente o la acción queda fuera del seguimiento actual.
- revisar_de_nuevo: el caso necesita una segunda revisión antes de tomar una decisión.

Ninguna decisión debe tomarse de forma automática en esta V1. La salida del flujo debe quedar siempre sujeta a revisión humana.

## Reglas mínimas de validación

- Un cliente activo sin próxima acción no debe avanzar.
- Un cliente sin responsable interno no debe avanzar.
- Un cliente bloqueado debe tener motivo y responsable.
- Un cliente en riesgo debe tener revisión humana.
- Toda acción pendiente debe tener responsable.
- Todo seguimiento abierto debe tener siguiente paso.
- Un cliente cerrado o descartado debe quedar separado del seguimiento activo.
- Toda salida debe incluir una decisión humana.

Estas reglas son deliberadamente simples para que puedan revisarse manualmente y convertirse después, si procede, en una lógica mínima verificable.

## Aplicación a la cartera ficticia

Para aplicar este flujo al documento `CARTERA_CLIENTES_FICTICIA.md`, se debe revisar:

- Clientes inventariados.
- Estados de cliente.
- Interacciones registradas.
- Próximas acciones.
- Bloqueos operativos.
- Clasificación de riesgo.
- Decisión final.

No es necesario reescribir toda la cartera. La validación consiste en recorrer cada cliente ficticio, aplicar los pasos anteriores y asignar una salida final revisada por una persona.

## Datos fuera de alcance en este flujo

Quedan fuera de alcance:

- Datos bancarios.
- Datos fiscales sensibles.
- Datos médicos.
- Credenciales.
- Contratos reales.
- Información confidencial de clientes reales.
- Historial completo de correo real.
- Conversaciones privadas reales.
- Métricas comerciales no verificadas.

La validación debe hacerse con datos ficticios o no sensibles. No deben incorporarse datos reales de clientes ni información privada para probar esta fase documental.

## Evolución posible en V2

En una V2 (*Version 2 – Versión 2*) futura, este flujo podría evolucionar hacia mejoras como:

- Conversión del flujo a reglas automáticas.
- Registro operativo en Google Sheets.
- Captura de interacciones mediante Google Forms.
- Dashboard de seguimiento.
- Alertas por correo.
- Recordatorios básicos.
- Integración futura con calendario.
- Resúmenes asistidos con IA.
- Integración futura con CRM.

Estas opciones no están implementadas todavía. No existe automatización real, conexión con Google Workspace, correo, calendario, CRM, dashboard, API ni IA funcional.

## Criterios de validación del flujo

Preguntas de control:

- ¿El flujo permite revisar una cartera ficticia?
- ¿Los pasos son claros?
- ¿Las decisiones finales están definidas?
- ¿Se detectan clientes sin próxima acción?
- ¿Se detectan bloqueos y riesgos?
- ¿Existe revisión humana?
- ¿Se evita prometer automatización inexistente?
- ¿Se evita prometer CRM, recordatorios o IA no implementada?

Si estas preguntas pueden responderse afirmativamente, el flujo será suficiente para cerrar una validación documental inicial antes de decidir si procede implementar una lógica mínima.

## Próximos pasos

1. Crear una estructura de datos de ejemplo para la cartera de clientes.
2. Revisar si el README del agente 03 debe enlazar los documentos V1.
3. Preparar después una revisión documental del agente 03 antes de decidir si se implementa código mínimo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
