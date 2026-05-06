# Arquitectura

## Propósito del documento

Definir la arquitectura conceptual del Agente de Análisis de Mercado para PYMES antes de construir cualquier automatización real.

## Estado de la arquitectura

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Arquitectura funcional: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- Integraciones reales: no implementadas todavía.

## Visión conceptual

La arquitectura se apoya en un flujo simple: entrada manual de señales de mercado ficticias, registro de competidores, registro de oportunidades, registro de riesgos, clasificación de señales, priorización de observaciones, validación humana y generación de un informe de mercado ficticio.

No existe IA (*Artificial Intelligence – Inteligencia Artificial*) funcional ni automatización real; la lógica se describe solo como base documental y como referencia para una V1 implementable futura.

## Flujo general previsto

1. Se recibe una señal de mercado con datos básicos.
2. Se valida que existan identificador, tipo, fuente y relevancia.
3. Se registra el competidor, oportunidad o riesgo asociado cuando aplique.
4. Se clasifica la señal y se prioriza la observación.
5. Se proponen acciones de exploración.
6. Se remite todo a validación humana.
7. Un dashboard futuro, todavía no implementado, podría visualizar el conjunto.

## Componentes conceptuales

- Capa de entrada de señales de mercado.
- Capa de validación de campos mínimos.
- Capa de registro de competidores.
- Capa de registro de oportunidades.
- Capa de registro de riesgos.
- Capa de clasificación de señales.
- Capa de priorización de observaciones.
- Registro documental de acciones de exploración.
- Validación humana obligatoria.
- Visualización futura no implementada.

## Arquitectura V1 implementable

La V1 debe ser mínima y verificable. Su alcance se limita a:

- Registro manual de señales de mercado.
- Estructura homogénea de competidores, oportunidades y riesgos.
- Reglas simples para detectar estados inconsistentes.
- Registro de acciones de exploración.
- Validación manual del resultado antes de aceptar cualquier cambio.

La V1 no debe prometer scraping real, extracción automática ni inteligencia competitiva completa.

## Arquitectura V2 futura

La V2 podría ampliar la base documental con:

- Captura semiestructurada desde formularios o correo.
- Reglas más avanzadas de priorización.
- Notificaciones internas.
- Métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).
- Dashboard funcional.
- Integración con API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) cuando exista una base estable.

## Datos previstos

- Señales de mercado con tipo, estado y relevancia.
- Competidores observados con fortalezas y debilidades.
- Oportunidades de mercado asociadas a señales.
- Riesgos de mercado con impacto potencial.
- Acciones de exploración vinculadas a señales.

## Integraciones previstas

- Google Workspace, únicamente como posibilidad futura.
- CRM, únicamente como posibilidad futura.
- API, únicamente como posibilidad futura.

## Control humano

Toda decisión relevante debe pasar por una persona. La arquitectura no contempla clasificación autónoma, priorización automática ni toma de decisiones sin validación manual.

## Riesgos técnicos

- Ambigüedad en los datos de entrada.
- Señales con fuente poco clara.
- Clasificaciones incompatibles con el estado real.
- Oportunidades sin revisión humana.
- Falsa sensación de automatización si se interpreta el documento como herramienta real.
- Dependencia excesiva de datos incompletos si no se define un criterio mínimo claro.

## Fuera de alcance inicial

- Extracción automática de fuentes.
- Scraping.
- Dashboard funcional.
- Google Workspace.
- CRM.
- API.
- Conexión a datos reales.
- IA funcional.
- Integración con sistemas productivos.
- Asesoramiento estratégico garantizado o métricas de mercado no verificadas.

## Criterios de validación técnica

- La señal debe poder validarse con campos mínimos definidos.
- Cada señal debe quedar ligada a competidores, riesgos o oportunidades cuando aplique.
- Las acciones de exploración deben ser rastreables por identificador.
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
