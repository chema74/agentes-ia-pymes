# Modelo de Datos

## Propósito del documento

Definir el modelo conceptual mínimo que sostendría una futura V1 (*Version 1 – Versión 1*) implementable del Agente de Análisis de Mercado para PYMES.

## Estado del modelo

- Modelo conceptual: preparado.
- Persistencia real: no implementada todavía.
- Automatización real: no implementada todavía.

## Entidad principal: Señal de mercado

La señal de mercado es la unidad central del modelo. Representa una observación que debe clasificarse, priorizarse o revisarse.

### Campos

- `identificador_senal`: código único de la señal.
- `titulo_senal`: nombre breve de la señal.
- `descripcion_senal`: explicación funcional de la observación.
- `tipo_senal`: tipo de señal observada.
- `fuente_observada`: origen manual o documental.
- `area_impacto`: área interna afectada.
- `nivel_relevancia`: nivel de importancia operativa.
- `estado_senal`: situación actual de la señal.
- `responsable_revision`: persona encargada de revisarla.
- `observaciones_internas`: notas de contexto para revisión humana.

## Entidad secundaria: Competidor observado

El competidor observado recoge información básica de un actor externo para contextualizar la señal.

### Campos

- `identificador_competidor`: código único del competidor.
- `nombre_competidor_ficticio`: nombre simulado del competidor.
- `segmento`: segmento de mercado observado.
- `propuesta_observada`: propuesta o enfoque detectado.
- `fortaleza_detectada`: fortaleza identificada.
- `debilidad_detectada`: debilidad identificada.
- `nivel_amenaza`: nivel de amenaza estimado.
- `observaciones_competidor`: comentarios de contexto.

## Entidad secundaria: Oportunidad de mercado

La oportunidad de mercado representa un posible espacio de exploración o crecimiento derivado de una señal.

### Campos

- `identificador_oportunidad`: código único de la oportunidad.
- `identificador_senal`: señal que la origina.
- `descripcion_oportunidad`: descripción breve de la oportunidad.
- `segmento_objetivo`: segmento o nicho objetivo.
- `prioridad_exploracion`: prioridad de exploración.
- `estado_oportunidad`: estado actual de la oportunidad.
- `responsable_exploracion`: persona encargada de explorarla.
- `observaciones_oportunidad`: notas de contexto.

## Entidad secundaria: Riesgo de mercado

El riesgo de mercado resume una posible amenaza o cambio desfavorable observado en una señal.

### Campos

- `identificador_riesgo`: código único del riesgo.
- `identificador_senal`: señal que origina el riesgo.
- `descripcion_riesgo`: descripción breve del riesgo.
- `impacto_potencial`: impacto esperado.
- `nivel_riesgo`: nivel de riesgo estimado.
- `estado_riesgo`: estado actual del riesgo.
- `requiere_revision_humana`: indicación de revisión manual.
- `observaciones_riesgo`: notas para revisión.

## Entidad secundaria: Acción de exploración

La acción de exploración recoge el siguiente paso operativo recomendado para no perder el hilo del análisis.

### Campos

- `identificador_accion`: código único de la acción.
- `identificador_senal`: señal a la que se vincula.
- `descripcion_accion`: paso concreto recomendado.
- `responsable_accion`: persona que debe ejecutarla.
- `estado_accion`: estado de la acción.
- `prioridad_accion`: prioridad de esa acción.
- `fecha_prevista`: fecha propuesta para ejecutarla.
- `observaciones_accion`: notas adicionales.

## Relaciones entre entidades

- Una señal de mercado puede originar oportunidades, riesgos o ambas cosas.
- Una señal de mercado puede tener varios competidores observados asociados.
- Una oportunidad de mercado debe apuntar a una señal concreta.
- Un riesgo de mercado debe apuntar a una señal concreta.
- Una acción de exploración debe apuntar a una señal concreta.

## Datos mínimos para demo V1

- Un identificador único por entidad.
- Estado explícito y legible.
- Responsable de revisión visible.
- Nivel de relevancia.
- Relación con competidores, oportunidades o riesgos asociados.
- Observaciones breves para contexto.

## Datos fuera de alcance

- Historial exhaustivo de mercado real.
- Logs técnicos.
- Integración con bases de datos reales.
- Predicción automática.
- Scraping automático.
- Métricas de mercado no verificadas.
- Asesoramiento estratégico garantizado.

## Evolución V2

- Añadir trazabilidad temporal más completa.
- Incorporar más granularidad en estados y subestados.
- Modelar dependencias entre señales.
- Incluir métricas de carga y tiempos de revisión.
- Preparar la base para visualización en dashboard funcional.

## Criterios de validación del modelo

- Cada entidad debe tener un identificador estable.
- La señal de mercado debe ser siempre la unidad principal.
- Las oportunidades y riesgos deben poder asociarse a señales concretas.
- Las acciones deben poder justificar decisiones humanas.
- El modelo debe ser suficiente para explicar un informe ficticio sin inventar software ya construido.

## Próximos pasos

- Usar este modelo como guía para el informe ficticio y para el JSON de ejemplo.
- Mantener la separación entre documentación y ejecución real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
