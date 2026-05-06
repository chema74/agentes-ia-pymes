# Arquitectura

## Propósito del documento

Definir la arquitectura conceptual del Agente de Revisión y Cumplimiento para PYMES antes de construir cualquier automatización real.

## Estado de la arquitectura

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Arquitectura funcional: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- Integraciones reales: no implementadas todavía.

## Visión conceptual

La arquitectura se apoya en un flujo simple: entrada manual de controles internos ficticios, registro de evidencias, registro de documentos pendientes, clasificación de hallazgos, identificación de riesgos operativos, priorización de revisión, acciones de seguimiento y revisión humana.

No existe IA (*Artificial Intelligence – Inteligencia Artificial*) funcional ni automatización real; la lógica se describe solo como base documental y como referencia para una V1 implementable futura.

## Flujo general previsto

1. Se recibe un control interno con datos básicos.
2. Se valida que existan identificador, tipo, área y responsable.
3. Se registran evidencias y documentos pendientes asociados.
4. Se clasifican hallazgos y riesgos operativos.
5. Se asigna una prioridad preliminar de revisión.
6. Se registran acciones de seguimiento.
7. Se remite todo a validación humana.
8. Un dashboard futuro, todavía no implementado, podría visualizar el conjunto.

## Componentes conceptuales

- Capa de entrada de controles internos.
- Capa de validación de campos mínimos.
- Capa de registro de evidencias.
- Capa de registro de documentos pendientes.
- Capa de clasificación de hallazgos.
- Capa de identificación de riesgos operativos.
- Capa de priorización de revisión.
- Registro documental de acciones de seguimiento.
- Revisión humana obligatoria.
- Visualización futura no implementada.

## Arquitectura V1 implementable

La V1 debe ser mínima y verificable. Su alcance se limita a:

- Registro manual de controles internos.
- Estructura homogénea de evidencias, hallazgos y documentos pendientes.
- Reglas simples para detectar estados inconsistentes.
- Registro de acciones de seguimiento.
- Revisión manual del resultado antes de aceptar cualquier cambio.

La V1 no debe prometer motor normativo real, revisión automática ni asesoramiento legal o regulatorio.

## Arquitectura V2 futura

La V2 podría ampliar la base documental con:

- Captura semiestructurada desde formularios o correo.
- Reglas más avanzadas de priorización.
- Notificaciones internas.
- Métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).
- Dashboard funcional.
- Integración con API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) cuando exista una base estable.

## Datos previstos

- Controles internos con tipo, estado y prioridad.
- Evidencias de revisión asociadas.
- Hallazgos internos con nivel de riesgo operativo.
- Documentos pendientes con impacto operativo.
- Acciones de seguimiento vinculadas a cada control.

## Integraciones previstas

- Google Workspace, únicamente como posibilidad futura.
- ERP, únicamente como posibilidad futura.
- CRM, únicamente como posibilidad futura.
- API, únicamente como posibilidad futura.

## Control humano

Toda decisión relevante debe pasar por una persona. La arquitectura no contempla validación autónoma, dictámenes automáticos ni cambio de estado sin revisión manual.

## Riesgos técnicos

- Ambigüedad en los datos de entrada.
- Estados incompatibles entre control, evidencia y hallazgo.
- Hallazgos sin responsable de revisión.
- Prioridades incoherentes entre áreas.
- Falsa sensación de automatización si se interpreta el documento como sistema de cumplimiento real.
- Dependencia excesiva de datos incompletos si no se define un criterio mínimo claro.

## Fuera de alcance inicial

- Revisión automática real.
- Motor normativo.
- Dashboard funcional.
- Google Workspace.
- ERP.
- CRM.
- API.
- IA funcional.
- Integración con sistemas productivos.
- Asesoramiento legal, fiscal, laboral, financiero o regulatorio.
- Garantía de cumplimiento normativo.
- Afirmaciones de que evita sanciones, riesgos legales o incumplimientos.

## Criterios de validación técnica

- El control interno debe poder validarse con campos mínimos definidos.
- Cada control debe quedar ligado a evidencias y hallazgos cuando aplique.
- Los documentos pendientes deben ser rastreables por identificador.
- La prioridad debe poder revisarse por una persona.
- El estado debe quedar registrado sin ambigüedad.
- El flujo debe poder explicarse sin recurrir a software ya construido.

## Próximos pasos técnicos

- Convertir este diseño en una V1 mínima si se decide implementar código más adelante.
- Mantener la validación humana como control principal.
- Preparar la siguiente fase solo cuando exista decisión explícita de desarrollo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
