# Arquitectura

## Propósito del documento

Definir la arquitectura conceptual del Agente de Pipeline Comercial para PYMES antes de construir cualquier automatización real.

## Estado de la arquitectura

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Arquitectura funcional: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- Integraciones reales: no implementadas todavía.

## Visión conceptual

La arquitectura se apoya en un flujo simple: entrada de oportunidades comerciales ficticias, validación de campos mínimos, control de fases comerciales, control de temperatura comercial, detección de oportunidades sin próxima acción, detección de bloqueos comerciales, priorización operativa, registro de acciones siguientes y revisión humana.

No existe IA (*Artificial Intelligence – Inteligencia Artificial*) funcional ni automatización real; la lógica se describe solo como base documental y como referencia para una V1 implementable futura.

## Flujo general previsto

1. Se recibe una oportunidad comercial con datos básicos.
2. Se valida que existan identificador, cliente, servicio, fase y responsable.
3. Se comprueba el estado de la oportunidad y su temperatura comercial.
4. Se detectan bloqueos o ausencia de próxima acción.
5. Se asigna una prioridad preliminar.
6. Se registran interacciones y acciones siguientes.
7. Se remite a revisión humana.
8. Un dashboard futuro, todavía no implementado, podría visualizar el pipeline.

## Componentes conceptuales

- Capa de entrada de oportunidades comerciales.
- Capa de validación de campos mínimos.
- Capa de control de fases comerciales.
- Capa de control de temperatura comercial.
- Capa de detección de oportunidades sin próxima acción.
- Capa de detección de bloqueos comerciales.
- Capa de priorización operativa.
- Registro documental de acciones siguientes.
- Revisión humana obligatoria.
- Visualización futura no implementada.

## Arquitectura V1 implementable

La V1 debe ser mínima y verificable. Su alcance se limita a:

- Registro manual de oportunidades comerciales.
- Estructura homogénea de interacciones, bloqueos y clasificaciones.
- Reglas simples para detectar estados inconsistentes.
- Registro de acciones siguientes.
- Revisión manual del resultado antes de aceptar cualquier cambio.

La V1 no debe prometer CRM real, scoring automático ni sincronización con herramientas externas.

## Arquitectura V2 futura

La V2 podría ampliar la base documental con:

- Captura semiestructurada desde formularios o correo.
- Reglas más avanzadas de priorización.
- Notificaciones internas.
- Métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).
- Dashboard funcional.
- Integración con API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) cuando exista una base estable.

## Datos previstos

- Oportunidades comerciales con estado, fase, prioridad y temperatura.
- Interacciones comerciales asociadas.
- Bloqueos comerciales con impacto y revisión.
- Acciones comerciales siguientes vinculadas a cada oportunidad.
- Clasificaciones comerciales con prioridad y temperatura.

## Integraciones previstas

- Google Workspace, únicamente como posibilidad futura.
- CRM, únicamente como posibilidad futura.
- API, únicamente como posibilidad futura.

## Control humano

Toda decisión relevante debe pasar por una persona. La arquitectura no contempla ejecución autónoma, cambio de fase automático ni scoring automático sin validación manual.

## Riesgos técnicos

- Ambigüedad en los datos de entrada.
- Fases comerciales incompatibles con el estado real.
- Oportunidades sin próxima acción.
- Bloqueos sin responsable de revisión.
- Falsa sensación de automatización si se interpreta el documento como CRM real.
- Dependencia excesiva de datos incompletos si no se define un criterio mínimo claro.

## Fuera de alcance inicial

- CRM funcional.
- Automatización comercial real.
- Scoring automático.
- Dashboard funcional.
- Google Workspace.
- API.
- IA funcional.
- Integración con sistemas productivos.
- Asesoramiento comercial garantizado o métricas de conversión no verificadas.

## Criterios de validación técnica

- La oportunidad debe poder validarse con campos mínimos definidos.
- Cada oportunidad debe quedar ligada a una fase comercial.
- Los bloqueos deben ser rastreables por identificador.
- La prioridad debe poder revisarse por una persona.
- La temperatura comercial debe quedar registrada sin ambigüedad.
- El flujo debe poder explicarse sin recurrir a software ya construido.

## Próximos pasos técnicos

- Convertir este diseño en una V1 mínima si se decide implementar código más adelante.
- Mantener la revisión humana como control principal.
- Preparar la siguiente fase solo cuando exista decisión explícita de desarrollo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
