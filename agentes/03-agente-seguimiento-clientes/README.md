# Agente de Seguimiento de Clientes para PYMES

## Descripción breve

Este agente está pensado para ayudar a una pequeña o mediana empresa a controlar el estado de sus clientes, las próximas acciones, las tareas pendientes, los bloqueos y el seguimiento operativo.  
Su propósito es ordenar información dispersa y convertirla en una base revisable para la gestión diaria de clientes.  
El enfoque está orientado a PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*) que necesitan claridad operativa sin implantar una infraestructura compleja.  
En su estado actual, el agente es una base técnica demostrable en fase documental inicial, no un producto terminado ni una automatización funcional.

## Estado del agente

- Estado actual: fase documental inicial.
- Código funcional: no implementado todavía.
- Automatizaciones: no implementadas todavía.
- Recordatorios automáticos: no implementados todavía.
- Integraciones: no implementadas todavía.
- Dashboard: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Problema que aborda

En muchas PYMES, el seguimiento de clientes activos depende de notas personales, correos, llamadas, hojas sueltas o memoria individual. Esta forma de trabajo puede funcionar durante un tiempo, pero se vuelve frágil cuando aumenta el número de clientes, responsables o tareas abiertas.

Los problemas habituales que aborda este agente son:

- Clientes activos sin estado claro.
- Tareas pendientes dispersas en distintos canales.
- Próximas acciones no registradas de forma consistente.
- Seguimientos que dependen de la memoria personal.
- Correos o llamadas sin trazabilidad operativa.
- Falta de prioridad para decidir qué revisar primero.
- Dificultad para saber qué clientes requieren atención.
- Riesgo de perder oportunidades o deteriorar la relación con el cliente.

El objetivo no es sustituir la gestión humana, sino hacer visible el estado operativo de cada cliente y reducir la dependencia de información informal.

## Usuario objetivo

Este agente está pensado para organizaciones pequeñas o equipos que gestionan varios clientes activos a la vez y necesitan una forma sencilla de ordenar el seguimiento.

Perfiles posibles:

- Consultorías pequeñas.
- Agencias de servicios.
- Despachos profesionales.
- Empresas de formación.
- Empresas de mantenimiento.
- Equipos comerciales pequeños.
- Equipos de atención o soporte.
- Profesionales que gestionan varios clientes activos a la vez.

El diseño conceptual está orientado a empresas sin infraestructura técnica compleja, sin necesidad inicial de un CRM completo, integraciones avanzadas o automatizaciones en producción.

## Objetivo funcional

El objetivo funcional es ayudar a convertir un seguimiento disperso de clientes en una vista operativa clara, revisable y priorizable. La propuesta se centra en documentar qué información mínima debe existir para que una persona pueda revisar la cartera de clientes y decidir los siguientes pasos con criterio.

La base funcional prevista incluye:

- Registro básico de clientes activos.
- Estado de seguimiento.
- Próxima acción.
- Responsable interno.
- Prioridad.
- Bloqueos.
- Riesgo operativo.
- Revisión humana antes de decisiones relevantes.

La revisión humana es un principio central del diseño: cualquier recomendación, priorización o siguiente paso debe poder ser revisado por una persona antes de ejecutarse o comunicarse al cliente.

## Alcance V1 implementable

La V1 (*Version 1 – Versión 1*) implementable debe ser pequeña, realista y verificable. Su objetivo es crear una base documental y técnica que permita demostrar el caso de uso sin presentar capacidades que todavía no existen.

El alcance previsto para esta V1 puede incluir:

- Documentación funcional y técnica.
- Definición del flujo de seguimiento.
- Modelo conceptual de datos.
- Estados de cliente.
- Estados de tarea.
- Ejemplo ficticio de cartera de clientes.
- Validación manual de próximos pasos.
- Reglas simples para detectar clientes sin próxima acción.
- Preparación para automatización futura.

Esta V1 no implica todavía recordatorios automáticos, integración con CRM, dashboard ni IA generativa funcional. Tampoco implica captura automática de correos, conexión con calendarios, envío de alertas ni análisis inteligente real. La prioridad de esta fase es definir bien el problema, el flujo operativo y las reglas mínimas que podrían implementarse posteriormente.

## Evolución V2 futura

La V2 (*Version 2 – Versión 2*) futura describe una posible evolución del agente cuando la base documental esté validada y exista una primera implementación verificable. Esta sección no describe funcionalidades implementadas, sino opciones razonables para una fase posterior.

Una evolución futura podría incluir:

- Registro operativo en Google Sheets.
- Captura de interacciones mediante formulario.
- Alertas por correo.
- Recordatorios básicos.
- Dashboard de seguimiento.
- Priorización asistida mediante reglas.
- Resúmenes asistidos con IA.
- Integración futura con CRM.
- Integración futura con calendario.

También podría contemplarse el uso de una API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) si en el futuro existiera una necesidad real de conectar el agente con otros sistemas. En ese caso, cualquier integración debería diseñarse con controles de permisos, trazabilidad y revisión humana.

La evolución V2 no debe confundirse con el estado actual del agente. Actualmente no existe automatización real, dashboard funcional, integración con Google Workspace, CRM ni IA funcional implementada.

## Fuera de alcance inicial

Quedan fuera del alcance inicial:

- CRM completo en producción.
- Automatización comercial completa.
- Recordatorios automáticos reales.
- Dashboard funcional.
- Integración real con Google Workspace.
- Integración con correo real.
- Integración con calendario real.
- Toma de decisiones sin revisión humana.
- Multiempresa real.
- API pública.
- Sustitución de gestión comercial o atención humana.
- Métricas de impacto no verificadas.

El agente tampoco debe presentarse como una solución cerrada de ventas, atención al cliente o productividad. En esta fase es un caso técnico documental para preparar una implementación controlada y demostrable.

## Entradas previstas

En una fase futura, el agente podría trabajar con entradas operativas básicas asociadas al seguimiento de clientes.

Entradas posibles:

- Nombre del cliente.
- Empresa.
- Estado del cliente.
- Última interacción.
- Próxima acción.
- Responsable interno.
- Prioridad.
- Riesgo.
- Bloqueo.
- Fecha prevista de seguimiento.
- Observaciones internas.

Todavía no existe un sistema funcional de captura de estas entradas. No hay formularios implementados, integración con hojas de cálculo, conexión con correo ni sincronización automática con herramientas externas.

## Salidas previstas

En una fase futura, el agente podría generar salidas orientadas a la revisión operativa y la priorización manual.

Salidas posibles:

- Lista de clientes activos.
- Clientes sin próxima acción.
- Clientes bloqueados.
- Clientes en riesgo.
- Seguimientos pendientes.
- Priorización operativa.
- Próximas acciones recomendadas para revisión humana.

Todavía no existe generación automática implementada. Cualquier salida descrita en esta sección corresponde a una capacidad prevista o diseñable, no a una funcionalidad actualmente disponible.

## Estructura documental del agente

- README.md
- docs/ARQUITECTURA.md
- docs/CASO_USO.md
- docs/ROADMAP.md
- requirements.txt
- .gitignore

## Criterios de validación

Para validar la calidad documental y técnica del agente, pueden utilizarse las siguientes preguntas:

- ¿Se entiende qué problema de seguimiento resuelve?
- ¿La V1 puede implementarse sin sobreingeniería?
- ¿Está claro qué no está implementado?
- ¿La evolución futura está separada del alcance actual?
- ¿El agente puede demostrarse con datos ficticios de clientes?
- ¿Existe revisión humana en puntos relevantes?
- ¿No se promete automatización comercial inexistente?

Si el documento permite responder afirmativamente a estas preguntas, la base del agente será suficientemente clara para avanzar hacia arquitectura, caso de uso y roadmap sin confundir alcance actual con evolución futura.

## Próximos pasos

1. Completar la arquitectura del agente de seguimiento.
2. Completar el caso de uso funcional.
3. Completar el roadmap de evolución.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
