# Caso de Uso

## Propósito del documento

Describir un caso ficticio realista para validar la documentación V1 (*Version 1 – Versión 1*) del Agente de Operaciones para PYMES.

## Estado del caso de uso

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Automatización real: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial

Una PYME de servicios técnicos y consultoría interna gestiona tareas de soporte, incidencias, entregas, validaciones y solicitudes internas. El equipo comparte información por correo, notas rápidas y hojas dispersas, sin una base única de control.

## Situación inicial sin agente

Antes del agente, las tareas llegan por canales distintos, se duplican con facilidad y los bloqueos se detectan tarde. La coordinación depende de la memoria del equipo y de revisiones manuales poco consistentes.

## Objetivo del caso de uso

Ordenar la operación diaria mediante una base documental que permita clasificar tareas, asociarlas a procesos, identificar bloqueos y dejar trazabilidad suficiente para revisión humana.

## Actores implicados

- Responsable de operaciones.
- Coordinación interna.
- Personal técnico o administrativo.
- Persona revisora final.
- Dirección de la PYME como observadora del estado general.

## Flujo funcional previsto

1. Se registra una tarea operativa con datos mínimos.
2. Se vincula la tarea a un proceso operativo.
3. Se asigna responsable y prioridad.
4. Se revisan bloqueos y dependencias.
5. Se propone una acción siguiente.
6. Una persona valida el resultado y decide si avanza, si pide información o si bloquea la tarea.

## Datos mínimos del caso

- Identificador de tarea.
- Título de la tarea.
- Descripción breve.
- Área operativa.
- Proceso relacionado.
- Estado de la tarea.
- Prioridad.
- Responsable interno.
- Fecha prevista.
- Bloqueo asociado, si existe.
- Observaciones internas.

## Estados de tarea previstos

- pendiente.
- en_progreso.
- en_revision.
- bloqueada.
- completada.
- descartada.

## Estados de proceso previstos

- activo.
- pendiente_revision.
- bloqueado.
- estable.
- descartado.

## Clasificación operativa prevista

- Tareas urgentes con impacto directo.
- Tareas en revisión que requieren validación humana.
- Tareas bloqueadas por dependencia externa o interna.
- Tareas ya completadas para cierre documental.
- Tareas descartadas por duplicidad o falta de encaje.

## Resultado esperado en V1

La V1 debe dejar un caso de uso suficientemente claro para demostrar que una PYME puede ordenar su operación sin software real, pero con una estructura de datos, estados y revisiones manuales coherente.

## Evolución V2 (*Version 2 – Versión 2*) futura

- Entrada estructurada desde formularios.
- Seguimiento más fino por área.
- Métricas de carga operativa.
- Dashboard funcional.
- Integraciones externas cuando exista una base técnica estable.

## Fuera de alcance inicial

- Automatización real.
- Gestión de correo conectada.
- Google Workspace.
- ERP.
- CRM.
- API.
- IA funcional.
- Decisión autónoma.

## Criterios de validación funcional

- El caso de uso debe poder explicarse sin ambigüedad.
- La tarea debe tener estado, prioridad y responsable.
- Los bloqueos deben ser visibles y revisables.
- La clasificación debe ser comprensible para un equipo no técnico.
- El tablero ficticio debe reflejar la misma lógica que este caso de uso.

## Próximos pasos

- Verificar que los datos de ejemplo respetan este caso ficticio.
- Mantener la revisión humana como punto de control.
- Decidir más adelante si la V1 pasa a implementación mínima o si se prioriza el siguiente agente del catálogo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
