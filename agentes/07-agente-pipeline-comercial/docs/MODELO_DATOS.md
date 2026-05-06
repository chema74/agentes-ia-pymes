# Modelo de Datos

## Propósito del documento

Definir el modelo conceptual mínimo que sostendría una futura V1 (*Version 1 – Versión 1*) implementable del Agente de Pipeline Comercial para PYMES.

## Estado del modelo

- Modelo conceptual: preparado.
- Persistencia real: no implementada todavía.
- Automatización real: no implementada todavía.

## Entidad principal: Oportunidad comercial

La oportunidad comercial es la unidad central del modelo. Representa un posible negocio que debe ordenarse, revisarse o cerrarse.

### Campos

- `identificador_oportunidad`: código único de la oportunidad.
- `nombre_cliente`: nombre del cliente potencial o actual.
- `nombre_empresa`: nombre de la empresa emisora o responsable interna.
- `servicio_interes`: servicio o solución de interés.
- `fase_comercial`: fase comercial en la que se encuentra.
- `estado_oportunidad`: situación actual de la oportunidad.
- `temperatura_comercial`: valoración operativa de calor comercial.
- `prioridad_seguimiento`: nivel de atención necesario.
- `responsable_interno`: persona encargada del seguimiento.
- `fecha_ultima_interaccion`: último contacto registrado.
- `proxima_accion`: siguiente paso previsto.
- `bloqueo_asociado`: referencia al bloqueo, si existe.
- `observaciones_internas`: notas de contexto para revisión humana.

## Entidad secundaria: Interacción comercial

La interacción comercial recoge el contacto entre la empresa y el cliente para mantener trazabilidad documental.

### Campos

- `identificador_interaccion`: código único de la interacción.
- `identificador_oportunidad`: oportunidad a la que pertenece.
- `tipo_interaccion`: llamada, correo, reunión u otro tipo.
- `fecha_interaccion`: fecha del contacto.
- `resumen_interaccion`: resumen breve de lo tratado.
- `responsable_interaccion`: persona que realizó el contacto.
- `resultado_interaccion`: resultado operativo de la interacción.
- `proxima_accion_derivada`: paso derivado del contacto.
- `observaciones_interaccion`: comentarios adicionales.

## Entidad secundaria: Bloqueo comercial

El bloqueo comercial describe una causa que impide avanzar o cerrar una oportunidad.

### Campos

- `identificador_bloqueo`: código único del bloqueo.
- `identificador_oportunidad`: oportunidad afectada.
- `descripcion_bloqueo`: descripción resumida del problema.
- `motivo_bloqueo`: causa principal del bloqueo.
- `impacto_comercial`: efecto del bloqueo sobre la oportunidad.
- `responsable_revision`: persona que debe revisar el bloqueo.
- `prioridad_bloqueo`: nivel de atención necesario.
- `estado_bloqueo`: situación actual del bloqueo.
- `observaciones_bloqueo`: notas para la revisión manual.

## Entidad secundaria: Acción comercial siguiente

La acción comercial siguiente recoge el próximo paso operativo recomendado para no perder el hilo comercial.

### Campos

- `identificador_accion`: código único de la acción.
- `identificador_oportunidad`: oportunidad a la que se vincula la acción.
- `descripcion_accion`: paso concreto recomendado.
- `responsable_accion`: persona que debe ejecutar la acción.
- `estado_accion`: estado de la acción.
- `prioridad_accion`: prioridad de esa acción.
- `fecha_prevista`: fecha propuesta para ejecutarla.
- `observaciones_accion`: notas adicionales.

## Entidad secundaria: Clasificación comercial

La clasificación comercial permite resumir el estado operativo de una oportunidad de forma legible y revisable.

### Campos

- `identificador_clasificacion`: código único de la clasificación.
- `identificador_oportunidad`: oportunidad clasificada.
- `nivel_prioridad`: prioridad operativa derivada.
- `temperatura_comercial`: temperatura final registrada.
- `motivo_clasificacion`: causa principal de la clasificación.
- `requiere_revision_humana`: indicación de revisión manual.
- `observaciones_clasificacion`: comentarios de contexto.

## Relaciones entre entidades

- Una oportunidad comercial puede tener varias interacciones comerciales.
- Una oportunidad comercial puede tener cero o un bloqueo comercial principal.
- Una oportunidad comercial puede tener una o varias acciones comerciales siguientes.
- Una oportunidad comercial puede tener una clasificación comercial principal.
- Un bloqueo comercial debe apuntar siempre a una oportunidad concreta.

## Datos mínimos para demo V1

- Un identificador único por entidad.
- Estado explícito y legible.
- Responsable interno visible.
- Fase comercial.
- Temperatura comercial.
- Prioridad operativa.
- Relación con la próxima acción.
- Observaciones breves para contexto.

## Datos fuera de alcance

- Historial exhaustivo de pipeline real.
- Logs técnicos.
- Integración con bases de datos reales.
- Scoring automático.
- Sincronización con herramientas externas.
- Métricas de conversión no verificadas.
- Asesoramiento comercial garantizado.

## Evolución V2

- Añadir trazabilidad temporal más completa.
- Incorporar más granularidad en fases y subfases.
- Modelar dependencias entre oportunidades.
- Incluir métricas de carga y tiempos de avance.
- Preparar la base para visualización en dashboard funcional.

## Criterios de validación del modelo

- Cada entidad debe tener un identificador estable.
- La oportunidad comercial debe ser siempre la unidad principal.
- Los bloqueos deben poder asociarse a oportunidades concretas.
- Las clasificaciones deben poder justificar decisiones humanas.
- El modelo debe ser suficiente para explicar un pipeline ficticio sin inventar software ya construido.

## Próximos pasos

- Usar este modelo como guía para el pipeline ficticio y para el JSON de ejemplo.
- Mantener la separación entre documentación y ejecución real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
