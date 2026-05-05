# Arquitectura del Agente Generador de Propuestas para PYMES

## Propósito del documento

Este documento describe la arquitectura conceptual y técnica prevista para el agente generador de propuestas, sin declarar como implementado lo que todavía no existe.

La intención es dejar una base técnica clara para el portfolio, diferenciando diseño, evolución prevista y límites reales. En esta fase no existe una solución productiva cerrada ni una automatización funcional.

## Estado de la arquitectura

- Estado documental: en desarrollo inicial.
- Estado técnico: pendiente de implementación.
- Código funcional: no implementado todavía.
- Generación automática de propuestas: no implementada todavía.
- Plantillas dinámicas: no implementadas todavía.
- Exportación PDF: no implementada todavía.
- Integraciones activas: no implementadas todavía.
- Dashboard: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Visión conceptual

El agente se entiende como una capa de estructuración entre una oportunidad comercial dispersa y una propuesta inicial revisable. Su papel conceptual es ordenar información mínima, señalar huecos y preparar un borrador que una persona responsable pueda validar.

En una futura versión, el agente podrá:

- Recibir información mínima de una oportunidad.
- Ordenar datos del cliente y del servicio.
- Identificar campos incompletos.
- Estructurar alcance preliminar.
- Preparar entregables propuestos.
- Señalar condiciones pendientes.
- Facilitar revisión humana antes de enviar cualquier propuesta.

Esta visión todavía no equivale a funcionalidad implementada. Por ahora solo define el comportamiento deseado de una V1 (*Version 1 – Versión 1*) pequeña y verificable.

## Flujo general previsto

El flujo previsto, sin código, sería el siguiente:

1. Entrada de información de la oportunidad.
2. Validación inicial de campos mínimos.
3. Organización de datos comerciales.
4. Definición preliminar del servicio propuesto.
5. Identificación de alcance y entregables.
6. Detección de condiciones pendientes.
7. Preparación de borrador conceptual.
8. Revisión humana.
9. Decisión de ajustar, completar o preparar propuesta final.

Este flujo es diseño previsto, no ejecución automática actual. Sirve para explicar cómo debería operar el agente si se decide implementar una base mínima más adelante.

## Componentes conceptuales

### Entrada de oportunidad

Podría venir de una carga manual, un formulario, una hoja de cálculo, una nota comercial o una futura integración con CRM.

### Validación inicial

Serviría para detectar cliente sin identificar, servicio no definido, alcance incompleto, entregables ausentes o condiciones pendientes.

### Estructuración de propuesta

Permitiría organizar una propuesta en bloques: contexto, necesidad, solución propuesta, alcance, entregables, plazos, condiciones y próximos pasos.

### Control de campos pendientes

Permitiría detectar información comercial incompleta antes de preparar una propuesta.

### Control de alcance

Permitiría separar lo incluido, lo pendiente de definir y lo fuera de alcance.

### Plantilla conceptual de propuesta

Sería una estructura documental base, no una plantilla dinámica funcional todavía.

### Registro de revisión humana

Permitiría saber qué partes fueron revisadas antes de enviar o convertir la propuesta en documento final.

### Generación documental futura

Podría generar documentos en Google Docs o PDF (*Portable Document Format – Formato de Documento Portátil*) en una V2 (*Version 2 – Versión 2*), pero todavía no está implementada.

### Dashboard futuro

Podría mostrar propuestas en preparación, incompletas, bloqueadas o listas para revisión, pero todavía no está implementado.

## Arquitectura V1 implementable

La V1 implementable debe ser mínima, realista y verificable.

Puede incluir:

- Documentación completa del flujo.
- Modelo conceptual de datos.
- Plantilla conceptual de propuesta.
- Ejemplo ficticio de propuesta.
- Reglas simples para detectar campos incompletos.
- Reglas simples para marcar condiciones pendientes.
- Reglas simples para revisar alcance y entregables.
- Revisión humana obligatoria.

La V1 no debe depender todavía de generación automática real, IA generativa funcional, Google Workspace, exportación PDF, CRM, dashboard ni API. Su objetivo es dejar listo el diseño para una posible implementación posterior sin sobredimensionarlo.

## Arquitectura V2 futura

La V2 futura podría ampliar la arquitectura con una capa más operativa y con mayor automatización documental.

Posibles ampliaciones futuras:

- Formulario de entrada de oportunidad.
- Registro en Google Sheets.
- Generación documental en Google Docs.
- Exportación futura a PDF.
- Plantillas reutilizables.
- Dashboard en HTML, CSS y JavaScript.
- Resumen asistido con IA.
- Sugerencias asistidas de estructura de propuesta.
- Integración futura con CRM.
- Posible API futura si el proyecto crece.

Estas ampliaciones no están implementadas todavía. Forman parte de una evolución posible, no del estado actual del agente.

## Datos previstos

### Datos de entrada

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
- Observaciones internas.

### Datos intermedios

- Campos completos.
- Campos pendientes.
- Alcance incluido.
- Alcance pendiente de definir.
- Elementos fuera de alcance.
- Entregables revisados.
- Condiciones pendientes.
- Estado de revisión.
- Observaciones de control.

### Datos de salida

- Borrador estructurado de propuesta.
- Lista de campos incompletos.
- Alcance preliminar revisable.
- Entregables propuestos.
- Condiciones pendientes.
- Estado de propuesta.
- Próximas acciones para revisión humana.

Todavía no existe tratamiento automatizado real de estos datos. Esta arquitectura solo describe cómo deberían organizarse para una futura implementación mínima o para una evolución posterior.

## Integraciones previstas

### Integraciones no existentes actualmente

- Google Workspace.
- Google Forms.
- Google Sheets.
- Google Docs.
- Google Drive.
- CRM externo.
- Exportación PDF.
- Modelos de lenguaje.
- API.
- Dashboard.

### Integraciones posibles en V2

- Entrada mediante formulario.
- Registro en hoja de cálculo.
- Generación documental.
- Organización de propuestas en carpetas.
- Exportación futura.
- Dashboard operativo.
- Resumen asistido.
- Sugerencias de estructura.
- Conexión futura con CRM.

### Integraciones fuera de alcance inicial

- CRM completo.
- Firma digital.
- Envío automático a clientes.
- Generación contractual avanzada.
- Cálculo financiero avanzado.
- Integraciones críticas con datos reales de clientes.
- API pública.
- Automatizaciones irreversibles.

## Control humano

El agente debe mantener revisión humana en puntos clave:

- Confirmación del cliente y oportunidad.
- Validación del servicio propuesto.
- Revisión del alcance.
- Revisión de entregables.
- Validación de condiciones comerciales.
- Confirmación antes de enviar cualquier propuesta.
- Corrección de errores, ambigüedades o supuestos incompletos.

La arquitectura parte de un principio de control humano explícito. El objetivo es preparar el trabajo, no sustituir el criterio comercial.

## Riesgos técnicos

Los principales riesgos conceptuales son:

- Generar propuestas sobre información incompleta.
- Reutilizar condiciones antiguas sin revisión.
- Confundir borrador conceptual con propuesta final.
- Prometer generación automática no implementada.
- Prometer IA donde solo existe diseño o reglas.
- Depender demasiado pronto de integraciones externas.
- Crear una V1 demasiado grande.
- Enviar documentos sin revisión humana.

Estos riesgos justifican que la arquitectura se mantenga simple en la V1 y que cualquier automatización futura se introduzca de forma progresiva.

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

## Criterios de validación técnica

Preguntas de control:

- ¿La arquitectura se entiende sin necesidad de código?
- ¿La V1 puede implementarse de forma mínima?
- ¿Está claro qué no existe todavía?
- ¿La V2 está planteada como evolución futura?
- ¿Hay revisión humana antes de enviar cualquier propuesta?
- ¿Se evitan promesas no verificables?
- ¿La arquitectura sirve para explicar un problema real de preparación de propuestas en una PYME?

## Próximos pasos técnicos

1. Completar el caso de uso funcional.
2. Completar el roadmap de evolución.
3. Definir después el modelo conceptual mínimo de datos para la V1.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
