# Modelo Conceptual de Datos del Agente Generador de Propuestas para PYMES

## Propósito del documento

Este documento define los datos mínimos necesarios para una primera V1 (*Version 1 – Versión 1*) implementable del agente generador de propuestas.

No describe una base de datos ya creada, sino un modelo conceptual previo. Su función es servir de base para una futura implementación mínima y para revisar si la estructura propuesta es suficiente antes de pensar en automatización.

## Estado actual

- Estado documental: en diseño inicial de V1.
- Código funcional: no implementado todavía.
- Base de datos: no implementada todavía.
- Generación automática de propuestas: no implementada todavía.
- Plantillas dinámicas: no implementadas todavía.
- Exportación PDF: no implementada todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- Dashboard: no implementado todavía.
- Integraciones activas: no implementadas todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Criterio de diseño del modelo

El modelo debe ser:

- Simple.
- Comprensible.
- Verificable.
- Útil para estructurar propuestas.
- Suficiente para detectar campos incompletos y condiciones pendientes.
- No sobredimensionado.
- Preparado para evolucionar después.

La prioridad de diseño es representar la información mínima necesaria para preparar una propuesta revisable por una persona responsable. No se busca construir un CRM, un dashboard ni un sistema de automatización en esta fase.

## Entidad principal: Propuesta

La entidad principal representa una propuesta comercial en preparación o revisión.

Campos mínimos:

- identificador_propuesta: representa un identificador único de la propuesta; es útil para relacionar datos, entregables y revisiones; sería obligatorio en V1.
- nombre_cliente: representa el nombre del cliente o contacto principal; es útil para identificar rápidamente a quién va dirigida la propuesta; sería obligatorio en V1.
- nombre_empresa: representa la empresa asociada a la oportunidad; es útil para contextualizar la propuesta dentro de la organización; sería recomendable en V1.
- tipo_oportunidad: representa la naturaleza comercial de la propuesta; es útil para clasificar el caso y adaptar la estructura; sería recomendable en V1.
- servicio_propuesto: representa el servicio que se ofrece; es útil para centrar la solución y evitar ambigüedades; sería obligatorio en V1.
- necesidad_principal: representa el problema o necesidad detectada; es útil para justificar la propuesta y su enfoque; sería obligatorio en V1.
- alcance_preliminar: representa el primer límite funcional de lo que se incluye; es útil para separar lo que se propone de lo que queda fuera; sería recomendable en V1.
- plazo_estimado: representa el tiempo previsto para la entrega o arranque; es útil para revisar viabilidad y expectativas; sería recomendable en V1.
- estado_propuesta: representa la situación general de la propuesta dentro del flujo; es útil para saber si está en borrador, revisión o lista para enviar; sería obligatorio en V1.
- responsable_interno: representa la persona del equipo que revisa o impulsa la propuesta; es útil para asignar responsabilidad; sería obligatorio en V1.
- observaciones_internas: representa notas internas de contexto; es útil para añadir información que no encaja en campos cerrados; sería opcional en V1.

## Entidad secundaria: Entregable propuesto

Esta entidad conceptual sirve para definir los entregables incluidos en la propuesta.

Campos mínimos:

- identificador_entregable: representa un identificador único del entregable; es útil para diferenciar elementos dentro de una misma propuesta; sería obligatorio en V1 si se registran entregables separados.
- identificador_propuesta: representa la propuesta a la que pertenece el entregable; es útil para mantener la relación con la entidad principal; sería obligatorio en V1.
- nombre_entregable: representa el nombre corto del entregable; es útil para identificarlo rápidamente; sería obligatorio en V1.
- descripcion_entregable: representa la explicación del entregable; es útil para delimitar qué se espera exactamente; sería recomendable en V1.
- estado_entregable: representa la situación del entregable; es útil para saber si está definido, pendiente, en revisión o descartado; sería obligatorio en V1.
- incluido_en_alcance: representa si el entregable forma parte del alcance de la propuesta; es útil para evitar confusiones sobre lo que se ofrece; sería recomendable en V1.
- requiere_revision: representa si el entregable necesita validación humana; es útil para controlar la calidad de la propuesta; sería recomendable en V1.
- observaciones_entregable: representa notas adicionales de contexto; es útil para aclaraciones internas; sería opcional en V1.

Estados posibles:

- definido
- pendiente
- en_revision
- descartado

Estos estados son una propuesta inicial para V1 y deben validarse con datos ficticios antes de considerarse definitivos.

## Entidad secundaria: Condición comercial

Esta entidad conceptual sirve para registrar condiciones pendientes o definidas.

Campos mínimos:

- identificador_condicion: representa un identificador único de la condición; es útil para distinguir varias condiciones dentro de la misma propuesta; sería recomendable en V1.
- identificador_propuesta: representa la propuesta a la que pertenece la condición; es útil para mantener trazabilidad; sería obligatorio en V1.
- descripcion_condicion: representa el contenido de la condición; es útil para saber qué debe revisarse o cerrarse; sería obligatorio en V1.
- estado_condicion: representa el estado de la condición; es útil para saber si está pendiente, definida, en revisión, bloqueada o descartada; sería obligatorio en V1.
- impacto_comercial: representa cómo afecta la condición a la propuesta; es útil para priorizar su revisión; sería recomendable en V1.
- responsable_revision: representa quién debe revisar la condición; es útil para asignar responsabilidad interna; sería recomendable en V1.
- prioridad_condicion: representa la urgencia relativa de la condición; es útil para ordenar la revisión; sería recomendable en V1.
- observaciones_condicion: representa notas internas sobre la condición; es útil para añadir contexto; sería opcional en V1.

Estados posibles:

- pendiente
- definida
- en_revision
- bloqueada
- descartada

## Entidad secundaria: Alcance de propuesta

Esta entidad conceptual sirve para separar alcance incluido, pendiente y fuera de alcance.

Campos mínimos:

- identificador_alcance: representa un identificador único del elemento de alcance; es útil para distinguir varias piezas de la propuesta; sería recomendable en V1.
- identificador_propuesta: representa la propuesta a la que pertenece el alcance; es útil para mantener la relación con la entidad principal; sería obligatorio en V1.
- elemento_alcance: representa el elemento concreto del alcance; es útil para describir qué se incluye o se excluye; sería obligatorio en V1.
- tipo_alcance: representa si el elemento está incluido, pendiente de definir o fuera de alcance; es útil para separar el contenido propuesto de sus límites; sería obligatorio en V1.
- descripcion_alcance: representa la explicación del elemento; es útil para documentar con claridad lo que se quiere ofrecer; sería recomendable en V1.
- estado_alcance: representa la situación del elemento dentro del flujo; es útil para saber si está revisado, pendiente o bloqueado; sería recomendable en V1.
- requiere_revision: representa si el elemento necesita validación humana; es útil para controlar el cierre del alcance; sería recomendable en V1.
- observaciones_alcance: representa notas de contexto sobre el alcance; es útil para aclarar límites o excepciones; sería opcional en V1.

Tipos posibles:

- incluido
- pendiente_definir
- fuera_de_alcance

## Entidad secundaria: Acción comercial siguiente

Esta entidad conceptual sirve para registrar próximos pasos antes de cerrar o enviar una propuesta.

Campos mínimos:

- identificador_accion: representa un identificador único de la acción; es útil para diferenciar varias acciones dentro de una misma propuesta; sería obligatorio en V1 si se registran acciones separadas.
- identificador_propuesta: representa la propuesta asociada a la acción; es útil para mantener trazabilidad; sería obligatorio en V1.
- descripcion_accion: representa la tarea a realizar; es útil para saber qué queda por hacer; sería obligatorio en V1.
- responsable_accion: representa quién debe ejecutar o revisar la acción; es útil para asignar responsabilidad interna; sería obligatorio en V1.
- estado_accion: representa la situación de la acción; es útil para diferenciar acciones pendientes, bloqueadas, completadas o descartadas; sería obligatorio en V1.
- prioridad_accion: representa la urgencia relativa de la acción; es útil para ordenar el trabajo; sería recomendable en V1.
- fecha_prevista: representa la fecha estimada para ejecutar la acción; es útil para revisar tiempos y secuencia; sería recomendable en V1.
- observaciones_accion: representa notas internas sobre la acción; es útil para añadir contexto; sería opcional en V1.

Estados posibles:

- pendiente
- en_revision
- completada
- bloqueada
- descartada

## Entidad secundaria: Revisión humana

Esta entidad conceptual sirve para registrar revisión interna antes de considerar una propuesta lista.

Campos mínimos:

- identificador_revision: representa un identificador único de la revisión; es útil para rastrear varias revisiones sobre la misma propuesta; sería recomendable en V1.
- identificador_propuesta: representa la propuesta revisada; es útil para mantener la relación con la entidad principal; sería obligatorio en V1.
- responsable_revision: representa quién realiza la revisión; es útil para dejar trazabilidad interna; sería obligatorio en V1.
- estado_revision: representa la situación de la revisión; es útil para distinguir una revisión pendiente, en curso o cerrada; sería obligatorio en V1.
- aspectos_revisados: representa qué se ha revisado; es útil para entender el alcance de la validación interna; sería recomendable en V1.
- observaciones_revision: representa notas sobre la revisión; es útil para registrar dudas, correcciones o matices; sería opcional en V1.
- decision_revision: representa la decisión final de la revisión; es útil para saber si la propuesta puede avanzar, pedir información o bloquearse; sería obligatorio en V1.

Decisiones posibles:

- avanzar
- pedir_informacion
- bloquear
- descartar
- revisar_de_nuevo

Ninguna decisión debe tomarse automáticamente en V1. La revisión humana es una condición de diseño, no una opción secundaria.

## Relaciones entre entidades

Las relaciones previstas son simples:

- Una propuesta puede tener varios entregables.
- Una propuesta puede tener varias condiciones comerciales.
- Una propuesta puede tener varios elementos de alcance.
- Una propuesta puede tener varias acciones comerciales siguientes.
- Una propuesta debe tener al menos una revisión humana antes de considerarse lista.
- Un conjunto de propuestas puede agruparse como cartera comercial futura.

Estas relaciones son conceptuales y no implican todavía una base de datos real, una API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) ni integraciones externas.

## Datos mínimos para una demo V1

Para demostrar la V1 con propuestas ficticias bastaría con preparar datos básicos y controlados.

Datos mínimos recomendados:

- Una o varias propuestas ficticias.
- Cliente y empresa ficticios.
- Servicio propuesto.
- Necesidad principal.
- Alcance preliminar.
- Entregables.
- Condiciones pendientes.
- Acciones siguientes.
- Revisión humana prevista.

La demo debería permitir comprobar que el modelo ayuda a estructurar una propuesta básica y a detectar huecos antes de enviar cualquier documento.

## Datos fuera de alcance en V1

Quedan fuera de alcance en V1:

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

No deben usarse datos reales sensibles en esta fase. Cualquier demostración debe realizarse con propuestas ficticias o datos expresamente preparados para validación interna.

## Evolución posible en V2

La V2 (*Version 2 – Versión 2*) podría ampliar el modelo si la V1 queda validada y existe una necesidad real de evolucionar el agente.

Posibles ampliaciones futuras:

- Registro en Google Sheets.
- Generación documental en Google Docs.
- Organización de propuestas en Google Drive.
- Exportación futura a PDF (*Portable Document Format – Formato de Documento Portátil*).
- Dashboard operativo.
- Plantillas reutilizables.
- Sugerencias asistidas con IA.
- Resúmenes comerciales asistidos.
- Integración futura con CRM.
- API futura si el proyecto crece.

Estas opciones no están implementadas todavía. Describen una posible evolución, no el estado actual del agente.

## Criterios de validación del modelo

Preguntas de control:

- ¿El modelo permite representar una propuesta básica?
- ¿Los campos mínimos son comprensibles?
- ¿La V1 puede demostrarse con propuestas ficticias?
- ¿Se evita tratar información sensible real?
- ¿La propuesta puede revisarse sin IA?
- ¿Se detectan campos incompletos y condiciones pendientes?
- ¿Hay revisión humana antes de considerar una propuesta lista?
- ¿El modelo puede evolucionar sin rehacerse desde cero?

## Próximos pasos

1. Preparar un ejemplo ficticio de propuesta.
2. Preparar un flujo mínimo de revisión manual de propuesta.
3. Definir después una primera estructura de datos de ejemplo si procede.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
