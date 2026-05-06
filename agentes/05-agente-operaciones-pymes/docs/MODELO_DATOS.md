# Modelo de Datos

## Propósito del documento

Definir el modelo conceptual mínimo que sostendría una futura V1 (*Version 1 – Versión 1*) implementable del Agente de Operaciones para PYMES.

## Estado del modelo

- Modelo conceptual: preparado.
- Persistencia real: no implementada todavía.
- Automatización real: no implementada todavía.

## Entidad principal: Tarea operativa

La tarea operativa es la unidad central del modelo. Representa un trabajo concreto que debe ordenarse, revisarse o cerrarse.

### Campos

- `identificador_tarea`: código único de la tarea.
- `titulo_tarea`: nombre breve y operativo de la tarea.
- `descripcion_tarea`: explicación funcional de la necesidad.
- `area_operativa`: área interna a la que pertenece la tarea.
- `proceso_relacionado`: proceso operativo asociado.
- `estado_tarea`: situación actual de la tarea.
- `prioridad`: nivel de urgencia o impacto.
- `responsable_interno`: persona encargada del seguimiento.
- `fecha_prevista`: fecha de revisión o cierre prevista.
- `bloqueo_asociado`: referencia al bloqueo, si existe.
- `observaciones_internas`: notas de contexto para revisión humana.

## Entidad secundaria: Proceso operativo

El proceso operativo agrupa tareas de la misma naturaleza y ayuda a entender qué flujo de trabajo está afectado.

### Campos

- `identificador_proceso`: código único del proceso.
- `nombre_proceso`: nombre breve del proceso.
- `descripcion_proceso`: explicación del objetivo operativo.
- `area_responsable`: área interna que lidera el proceso.
- `estado_proceso`: situación actual del proceso.
- `responsable_proceso`: persona responsable del proceso.
- `prioridad_proceso`: prioridad del proceso frente a otros.
- `observaciones_proceso`: notas internas de contexto.

## Entidad secundaria: Bloqueo operativo

El bloqueo operativo describe una causa que impide avanzar o cerrar una tarea.

### Campos

- `identificador_bloqueo`: código único del bloqueo.
- `identificador_tarea`: tarea afectada por el bloqueo.
- `descripcion_bloqueo`: descripción resumida del problema.
- `motivo_bloqueo`: causa principal del bloqueo.
- `impacto_operativo`: efecto del bloqueo sobre la operación.
- `responsable_revision`: persona que debe revisar el bloqueo.
- `prioridad_bloqueo`: nivel de atención necesario.
- `estado_bloqueo`: situación actual del bloqueo.
- `observaciones_bloqueo`: notas para la revisión manual.

## Entidad secundaria: Acción siguiente

La acción siguiente recoge el siguiente paso operativo recomendado para no perder el hilo del trabajo.

### Campos

- `identificador_accion`: código único de la acción.
- `identificador_tarea`: tarea a la que se vincula la acción.
- `descripcion_accion`: paso concreto recomendado.
- `responsable_accion`: persona que debe ejecutar la acción.
- `estado_accion`: estado de la acción.
- `prioridad_accion`: prioridad de esa acción.
- `fecha_prevista`: fecha propuesta para ejecutarla.
- `observaciones_accion`: notas adicionales.

## Entidad secundaria: Revisión operativa

La revisión operativa representa la comprobación humana que decide si una tarea puede avanzar, debe bloquearse o necesita más información.

### Campos

- `identificador_revision`: código único de la revisión.
- `identificador_tarea`: tarea revisada.
- `responsable_revision`: persona que realiza la revisión.
- `estado_revision`: estado actual de la revisión.
- `aspectos_revisados`: lista de puntos comprobados.
- `decision_revision`: decisión humana tomada.
- `observaciones_revision`: comentarios finales.

## Relaciones entre entidades

- Una tarea operativa puede pertenecer a un proceso operativo.
- Una tarea operativa puede tener cero o un bloqueo operativo principal.
- Una tarea operativa puede tener una o varias acciones siguientes.
- Una tarea operativa puede tener una o varias revisiones operativas.
- Un proceso operativo puede agrupar varias tareas.
- Un bloqueo operativo debe apuntar siempre a una tarea concreta.

## Datos mínimos para demo V1

- Un identificador único por entidad.
- Estado explícito y legible.
- Responsable interno visible.
- Prioridad operativa.
- Relación con el proceso asociado.
- Bloqueo o motivo de revisión, si aplica.
- Observaciones breves para contexto.

## Datos fuera de alcance

- Historial exhaustivo de eventos.
- Logs técnicos.
- Integración con bases de datos reales.
- Cálculo automático de prioridades complejas.
- Sincronización con herramientas externas.
- Métricas de rendimiento operativas en tiempo real.

## Evolución V2 (*Version 2 – Versión 2*)

- Añadir trazabilidad temporal más completa.
- Incorporar más granularidad en estados y subestados.
- Modelar dependencias entre tareas.
- Incluir métricas de carga y tiempos de resolución.
- Preparar la base para visualización en dashboard funcional.

## Criterios de validación del modelo

- Cada entidad debe tener un identificador estable.
- La tarea operativa debe ser siempre la unidad principal.
- Los bloqueos deben poder asociarse a tareas concretas.
- Las revisiones deben poder justificar decisiones humanas.
- El modelo debe ser suficiente para explicar un tablero operativo ficticio sin inventar software ya construido.

## Próximos pasos

- Usar este modelo como guía para el tablero ficticio y para el JSON de ejemplo.
- Mantener la separación entre documentación y ejecución real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
