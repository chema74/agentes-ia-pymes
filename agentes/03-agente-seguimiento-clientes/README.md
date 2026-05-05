# Agente de Seguimiento de Clientes para PYMES

## Descripción breve

Este agente está pensado para ayudar a una pequeña o mediana empresa a controlar el estado de sus clientes, próximas acciones, tareas pendientes, bloqueos y seguimiento operativo.  
Su propósito es ordenar información dispersa y convertirla en una base revisable para la gestión diaria de clientes.  
El enfoque está orientado a PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*) que necesitan claridad operativa sin implantar una infraestructura compleja.  
En su estado actual, el agente cuenta con la fase documental V1 preparada, pero no es un producto terminado ni una automatización funcional.

## Estado del agente

- Estado actual: fase documental V1 preparada.
- Código funcional: no implementado todavía.
- Automatización de seguimiento: no implementada todavía.
- Recordatorios automáticos: no implementados todavía.
- Integraciones activas: no implementadas todavía.
- Google Workspace: no implementado todavía.
- Dashboard: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
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

El diseño conceptual está orientado a empresas sin infraestructura técnica compleja, sin necesidad inicial de CRM completo, integraciones avanzadas o automatizaciones productivas.

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

## Documentación V1 disponible

La fase documental V1 (*Version 1 – Versión 1*) está preparada como base de portfolio técnico. Estos documentos describen el alcance, el caso de uso, el modelo de datos, la cartera ficticia y el flujo de validación manual, sin afirmar que exista implementación funcional.

Documentos disponibles:

- [Arquitectura conceptual](docs/ARQUITECTURA.md)
- [Caso de uso funcional](docs/CASO_USO.md)
- [Roadmap de evolución](docs/ROADMAP.md)
- [Modelo conceptual de datos](docs/MODELO_DATOS.md)
- [Cartera ficticia de clientes](docs/CARTERA_CLIENTES_FICTICIA.md)
- [Flujo de validación de seguimiento](docs/FLUJO_VALIDACION_SEGUIMIENTO.md)

Esta documentación permite revisar el diseño de la V1 antes de decidir si se implementa una lógica mínima más adelante.

## Datos de ejemplo disponibles

Existe un dato de ejemplo ficticio para apoyar una futura validación mínima:

- [Cartera ficticia de clientes en JSON](datos_ejemplo/cartera_clientes_ficticia.json)

Este JSON contiene una cartera inventada coherente con la documentación del agente. Sirve como dato de ejemplo para una posible implementación mínima futura, pero no es código funcional, no automatiza el seguimiento, no ejecuta recordatorios y no implica integración con sistemas externos.

## Alcance V1 documental

La V1 documental preparada incluye:

- Documentación funcional y técnica.
- Definición del flujo de seguimiento.
- Modelo conceptual de datos.
- Estados de cliente.
- Estados de acción.
- Ejemplo ficticio de cartera de clientes.
- Flujo manual de validación.
- JSON ficticio de ejemplo.
- Reglas simples para detectar clientes sin próxima acción, bloqueos y riesgos.

Esta V1 documental no implica recordatorios automáticos, integración con CRM, dashboard, Google Workspace, API ni IA generativa funcional. Tampoco implica captura automática de correos, conexión con calendarios, envío de alertas ni automatización productiva.

## Evolución V2 futura

La V2 (*Version 2 – Versión 2*) futura describe una posible evolución del agente si se decide avanzar después de validar la documentación y, en su caso, una implementación mínima.

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

Esta sección describe posibilidades futuras, no funcionalidades implementadas.

## Fuera de alcance actual

Quedan fuera del alcance actual:

- CRM completo en producción.
- Automatización comercial completa.
- Recordatorios automáticos reales.
- Dashboard funcional.
- Integración real con Google Workspace.
- Integración con correo real.
- Integración con calendario real.
- API pública.
- Toma de decisiones sin revisión humana.
- Multiempresa real.
- Sustitución de gestión comercial o atención humana.
- Métricas de impacto no verificadas.

El agente no debe presentarse como una solución cerrada de ventas, atención al cliente o productividad. En esta fase es un caso técnico documental preparado para revisión y posible evolución posterior.

## Criterios de validación

Para validar la calidad documental y técnica del agente, pueden utilizarse las siguientes preguntas:

- ¿Se entiende qué problema de seguimiento resuelve?
- ¿La V1 documental puede revisarse sin sobreingeniería?
- ¿Está claro qué no está implementado?
- ¿La evolución futura está separada del alcance actual?
- ¿El agente puede demostrarse con datos ficticios de clientes?
- ¿Existe revisión humana en puntos relevantes?
- ¿No se promete automatización comercial inexistente?

## Próximos pasos

1. Validar el JSON de ejemplo.
2. Hacer commit manual de la fase documental V1 del agente 03.
3. Pasar después al agente 04.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
