# Modelo de Datos

## Propósito del documento

Definir el modelo conceptual mínimo que sostendría una futura V1 (*Version 1 – Versión 1*) implementable del Agente de Revisión y Cumplimiento para PYMES.

## Estado del modelo

- Modelo conceptual: preparado.
- Persistencia real: no implementada todavía.
- Automatización real: no implementada todavía.

## Entidad principal: Control interno

El control interno es la unidad central del modelo. Representa un control o revisión básica que debe ordenarse, revisarse o cerrarse.

### Campos

- `identificador_control`: código único del control.
- `nombre_control`: nombre breve del control.
- `area_control`: área interna a la que pertenece.
- `descripcion_control`: explicación funcional del control.
- `tipo_control`: tipología del control interno.
- `estado_control`: situación actual del control.
- `prioridad_revision`: nivel de atención necesario.
- `responsable_interno`: persona encargada del seguimiento.
- `fecha_revision_prevista`: fecha prevista para revisar el control.
- `observaciones_control`: notas de contexto para revisión humana.

## Entidad secundaria: Evidencia de revisión

La evidencia de revisión recoge una prueba o referencia que ayuda a sustentar una revisión interna.

### Campos

- `identificador_evidencia`: código único de la evidencia.
- `identificador_control`: control al que pertenece.
- `nombre_evidencia`: nombre breve de la evidencia.
- `tipo_evidencia`: tipo de prueba o registro.
- `estado_evidencia`: situación actual de la evidencia.
- `fecha_evidencia`: fecha de registro.
- `responsable_revision`: persona que revisa la evidencia.
- `observaciones_evidencia`: comentarios adicionales.

## Entidad secundaria: Hallazgo interno

El hallazgo interno representa una observación derivada de un control que requiere tratamiento documental.

### Campos

- `identificador_hallazgo`: código único del hallazgo.
- `identificador_control`: control al que se vincula.
- `descripcion_hallazgo`: descripción breve del hallazgo.
- `tipo_hallazgo`: tipo de incidencia detectada.
- `nivel_riesgo_operativo`: nivel de riesgo operativo estimado.
- `requiere_revision_humana`: indicación de revisión manual.
- `estado_hallazgo`: situación actual del hallazgo.
- `observaciones_hallazgo`: notas para revisión.

## Entidad secundaria: Acción de seguimiento

La acción de seguimiento recoge el siguiente paso operativo recomendado para no perder el hilo del control.

### Campos

- `identificador_accion`: código único de la acción.
- `identificador_control`: control al que se vincula.
- `descripcion_accion`: paso concreto recomendado.
- `responsable_accion`: persona que debe ejecutarla.
- `estado_accion`: estado de la acción.
- `prioridad_accion`: prioridad de esa acción.
- `fecha_prevista`: fecha propuesta para ejecutarla.
- `observaciones_accion`: notas adicionales.

## Entidad secundaria: Documento pendiente

El documento pendiente describe un elemento documental que falta para completar o sostener una revisión interna.

### Campos

- `identificador_documento`: código único del documento.
- `identificador_control`: control al que se vincula.
- `nombre_documento`: nombre breve del documento.
- `motivo_pendiente`: causa del pendiente.
- `impacto_operativo`: efecto del pendiente sobre la operación.
- `responsable_revision`: persona que debe revisarlo.
- `estado_documento`: situación actual del documento.
- `observaciones_documento`: notas adicionales.

## Relaciones entre entidades

- Un control interno puede tener varias evidencias de revisión.
- Un control interno puede tener uno o varios hallazgos internos.
- Un control interno puede tener una o varias acciones de seguimiento.
- Un control interno puede tener uno o varios documentos pendientes.
- Un hallazgo interno debe apuntar siempre a un control concreto.

## Datos mínimos para demo V1

- Un identificador único por entidad.
- Estado explícito y legible.
- Responsable interno visible.
- Prioridad de revisión.
- Relación con evidencias, hallazgos y documentos asociados.
- Observaciones breves para contexto.

## Datos fuera de alcance

- Historial exhaustivo de auditoría real.
- Logs técnicos.
- Integración con bases de datos reales.
- Cálculo automático de cumplimiento.
- Diagnóstico normativo.
- Sincronización con herramientas externas.
- Asesoramiento legal, fiscal, laboral, financiero o regulatorio.

## Evolución V2

- Añadir trazabilidad temporal más completa.
- Incorporar más granularidad en estados y subestados.
- Modelar dependencias entre controles.
- Incluir métricas de carga y tiempos de revisión.
- Preparar la base para visualización en dashboard funcional.

## Criterios de validación del modelo

- Cada entidad debe tener un identificador estable.
- El control interno debe ser siempre la unidad principal.
- Los hallazgos deben poder asociarse a controles concretos.
- Los documentos pendientes deben poder justificarse documentalmente.
- El modelo debe ser suficiente para explicar una revisión ficticia sin inventar software ya construido.

## Próximos pasos

- Usar este modelo como guía para la revisión ficticia y para el JSON de ejemplo.
- Mantener la separación entre documentación y ejecución real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
