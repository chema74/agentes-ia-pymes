# Modelo de Datos

## Propósito del documento

Definir el modelo conceptual mínimo que sostendría una futura V1 (*Version 1 – Versión 1*) implementable del Agente de Control de Cobros y Flujo de Caja para PYMES.

## Estado del modelo

- Modelo conceptual: preparado.
- Persistencia real: no implementada todavía.
- Automatización real: no implementada todavía.

## Entidad principal: Cobro pendiente

El cobro pendiente es la unidad central del modelo. Representa una entrada de dinero esperada que debe seguirse de forma ordenada.

### Campos

- `identificador_cobro`: código único del cobro.
- `nombre_cliente`: nombre del cliente asociado.
- `nombre_empresa`: nombre de la empresa emisora o responsable interna.
- `concepto_cobro`: descripción breve del cobro.
- `importe_previsto`: cantidad estimada de entrada.
- `fecha_emision`: fecha en la que se generó la referencia.
- `fecha_vencimiento`: fecha límite prevista.
- `estado_cobro`: situación actual del cobro.
- `prioridad_seguimiento`: nivel de atención necesario.
- `responsable_interno`: persona encargada del seguimiento.
- `riesgo_retraso`: valoración operativa del riesgo.
- `observaciones_internas`: notas de contexto para revisión humana.

## Entidad secundaria: Factura o referencia de cobro

La referencia de cobro conecta el cobro pendiente con una identificación ficticia o interna para mantener trazabilidad documental.

### Campos

- `identificador_referencia`: código único de la referencia.
- `identificador_cobro`: cobro al que pertenece.
- `numero_referencia_ficticia`: número o código simulado.
- `tipo_referencia`: tipo documental o interno.
- `estado_referencia`: situación de la referencia.
- `fecha_referencia`: fecha asociada a la referencia.
- `observaciones_referencia`: comentarios de contexto.

## Entidad secundaria: Acción de seguimiento de cobro

La acción de seguimiento define el próximo paso operativo que debe ejecutarse para no perder el control del cobro.

### Campos

- `identificador_accion`: código único de la acción.
- `identificador_cobro`: cobro al que se vincula.
- `descripcion_accion`: paso concreto recomendado.
- `responsable_accion`: persona que debe ejecutar la acción.
- `estado_accion`: estado de la acción.
- `prioridad_accion`: prioridad de esa acción.
- `fecha_prevista`: fecha propuesta para ejecutarla.
- `observaciones_accion`: notas adicionales.

## Entidad secundaria: Riesgo de cobro

El riesgo de cobro recoge la valoración operativa de posible retraso, bloqueo o necesidad de seguimiento adicional.

### Campos

- `identificador_riesgo`: código único del riesgo.
- `identificador_cobro`: cobro afectado.
- `nivel_riesgo`: nivel de riesgo operativo.
- `motivo_riesgo`: causa principal del riesgo.
- `impacto_operativo`: efecto esperado sobre la operación.
- `requiere_revision_humana`: indicación de revisión manual.
- `observaciones_riesgo`: notas para la revisión.

## Entidad secundaria: Previsión operativa de entrada

La previsión operativa de entrada es una estimación documental de cuánto podría entrar y en qué periodo, sin plantear automatización financiera real.

### Campos

- `identificador_prevision`: código único de la previsión.
- `identificador_cobro`: cobro al que se asocia.
- `periodo_previsto`: periodo estimado de entrada.
- `importe_previsto`: importe estimado.
- `probabilidad_operativa`: probabilidad documental o de seguimiento.
- `estado_prevision`: estado de la previsión.
- `observaciones_prevision`: notas adicionales.

## Relaciones entre entidades

- Un cobro pendiente puede tener una o varias referencias de cobro.
- Un cobro pendiente puede tener una o varias acciones de seguimiento.
- Un cobro pendiente puede tener uno o varios riesgos asociados.
- Un cobro pendiente puede tener una previsión operativa principal.
- Cada riesgo debe apuntar a un cobro concreto.

## Datos mínimos para demo V1

- Un identificador único por entidad.
- Estado explícito y legible.
- Responsable interno visible.
- Prioridad operativa.
- Relación con la referencia asociada.
- Riesgo o motivo de seguimiento, si aplica.
- Observaciones breves para contexto.

## Datos fuera de alcance

- Historial exhaustivo de movimientos bancarios.
- Reconciliación contable real.
- Integración con bancos.
- Cálculo automático de saldos.
- Sincronización con herramientas externas.
- Información fiscal o legal.
- Asesoramiento financiero, fiscal, contable o legal.

## Evolución V2

- Añadir trazabilidad temporal más completa.
- Incorporar más granularidad en estados y subestados.
- Modelar dependencias entre cobros.
- Incluir métricas de seguimiento y tiempos de resolución.
- Preparar la base para visualización en dashboard funcional.

## Criterios de validación del modelo

- Cada entidad debe tener un identificador estable.
- El cobro pendiente debe ser siempre la unidad principal.
- Los riesgos deben poder asociarse a cobros concretos.
- Las previsiones deben poder justificarse como operativas, no financieras reales.
- El modelo debe ser suficiente para explicar una cartera ficticia sin inventar software ya construido.

## Próximos pasos

- Usar este modelo como guía para la cartera ficticia y para el JSON de ejemplo.
- Mantener la separación entre documentación y ejecución real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
