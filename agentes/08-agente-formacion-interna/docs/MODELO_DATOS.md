# Modelo de Datos

## Propósito del documento

Definir el modelo conceptual mínimo que sostendría una futura V1 (*Version 1 – Versión 1*) implementable del Agente de Formación Interna para PYMES.

## Estado del modelo

- Modelo conceptual: preparado.
- Persistencia real: no implementada todavía.
- Automatización real: no implementada todavía.

## Entidad principal: Ruta formativa

La ruta formativa es la unidad central del modelo. Representa un recorrido de aprendizaje ordenado para un perfil interno concreto.

### Campos

- `identificador_ruta`: código único de la ruta.
- `nombre_ruta`: nombre breve de la ruta.
- `perfil_destinatario`: perfil o colectivo al que va dirigida.
- `objetivo_formativo`: objetivo de aprendizaje de la ruta.
- `estado_ruta`: situación actual de la ruta.
- `prioridad_ruta`: nivel de atención necesario.
- `responsable_interno`: persona encargada del seguimiento.
- `fecha_revision_prevista`: fecha prevista para revisar la ruta.
- `observaciones_ruta`: notas de contexto para revisión humana.

## Entidad secundaria: Módulo formativo

El módulo formativo agrupa un contenido específico dentro de una ruta.

### Campos

- `identificador_modulo`: código único del módulo.
- `identificador_ruta`: ruta a la que pertenece.
- `nombre_modulo`: nombre breve del módulo.
- `descripcion_modulo`: explicación del contenido.
- `tipo_contenido`: tipo de recurso o formato.
- `estado_modulo`: situación actual del módulo.
- `prioridad_modulo`: nivel de atención necesario.
- `responsable_contenido`: persona responsable del contenido.
- `observaciones_modulo`: notas para revisión manual.

## Entidad secundaria: Perfil interno

El perfil interno describe al empleado o rol que recibe la formación.

### Campos

- `identificador_perfil`: código único del perfil.
- `nombre_perfil`: nombre del perfil o puesto.
- `area`: área interna asociada.
- `necesidades_formativas`: necesidades detectadas.
- `nivel_inicial`: nivel de partida estimado.
- `ruta_asignada`: ruta recomendada o asignada.
- `observaciones_perfil`: notas de contexto.

## Entidad secundaria: Evidencia formativa

La evidencia formativa representa una prueba de revisión o realización vinculada a un módulo.

### Campos

- `identificador_evidencia`: código único de la evidencia.
- `identificador_modulo`: módulo al que se vincula.
- `identificador_perfil`: perfil asociado.
- `tipo_evidencia`: tipo de prueba o registro.
- `estado_evidencia`: situación actual de la evidencia.
- `fecha_evidencia`: fecha del registro.
- `responsable_revision`: persona que revisa la evidencia.
- `observaciones_evidencia`: comentarios adicionales.

## Entidad secundaria: Acción formativa siguiente

La acción formativa siguiente recoge el siguiente paso operativo recomendado para no perder el hilo del trabajo.

### Campos

- `identificador_accion`: código único de la acción.
- `identificador_ruta`: ruta a la que se vincula.
- `descripcion_accion`: paso concreto recomendado.
- `responsable_accion`: persona que debe ejecutar la acción.
- `estado_accion`: estado de la acción.
- `prioridad_accion`: prioridad de esa acción.
- `fecha_prevista`: fecha propuesta para ejecutarla.
- `observaciones_accion`: notas adicionales.

## Relaciones entre entidades

- Una ruta formativa puede tener varios módulos formativos.
- Una ruta formativa puede tener uno o varios perfiles internos asociados.
- Una ruta formativa puede tener una o varias acciones formativas siguientes.
- Un módulo formativo puede tener una o varias evidencias formativas.
- Una evidencia formativa debe apuntar a un módulo y a un perfil concretos.

## Datos mínimos para demo V1

- Un identificador único por entidad.
- Estado explícito y legible.
- Responsable interno visible.
- Prioridad operativa.
- Relación con la ruta o módulo asociado.
- Evidencia o motivo de revisión, si aplica.
- Observaciones breves para contexto.

## Datos fuera de alcance

- Historial exhaustivo de aprendizaje real.
- Logs técnicos.
- Integración con plataformas LMS reales.
- Cálculo automático de progreso complejo.
- Sincronización con herramientas externas.
- Métricas de aprendizaje no verificadas.
- Promesas de mejora garantizada.

## Evolución V2

- Añadir trazabilidad temporal más completa.
- Incorporar más granularidad en estados y subestados.
- Modelar dependencias entre rutas.
- Incluir métricas de carga y tiempos de revisión.
- Preparar la base para visualización en dashboard funcional.

## Criterios de validación del modelo

- Cada entidad debe tener un identificador estable.
- La ruta formativa debe ser siempre la unidad principal.
- Las evidencias deben poder asociarse a módulos concretos.
- Las acciones deben poder justificar decisiones humanas.
- El modelo debe ser suficiente para explicar un plan formativo ficticio sin inventar software ya construido.

## Próximos pasos

- Usar este modelo como guía para el plan ficticio y para el JSON de ejemplo.
- Mantener la separación entre documentación y ejecución real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
