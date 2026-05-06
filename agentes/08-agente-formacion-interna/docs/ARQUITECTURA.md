# Arquitectura

## Propósito del documento

Definir la arquitectura conceptual del Agente de Formación Interna para PYMES antes de construir cualquier automatización real.

## Estado de la arquitectura

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Arquitectura funcional: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- Integraciones reales: no implementadas todavía.

## Visión conceptual

La arquitectura se apoya en un flujo simple: entrada de contenidos formativos ficticios, perfiles o roles internos, rutas formativas, módulos de formación, evidencias de revisión o realización, detección de contenidos pendientes, priorización formativa y revisión humana.

No existe IA (*Artificial Intelligence – Inteligencia Artificial*) funcional ni automatización real; la lógica se describe solo como base documental y como referencia para una V1 implementable futura.

## Flujo general previsto

1. Se recibe una ruta formativa con datos básicos.
2. Se valida que existan identificador, perfil destinatario, objetivo y responsable.
3. Se comprueba el estado de la ruta y de sus módulos asociados.
4. Se revisan evidencias y contenidos pendientes.
5. Se asigna una prioridad formativa preliminar.
6. Se registra el resultado y se remite a revisión humana.
7. Un dashboard futuro, todavía no implementado, podría visualizar el conjunto.

## Componentes conceptuales

- Capa de entrada de contenidos formativos.
- Capa de validación de campos mínimos.
- Capa de gestión de perfiles internos.
- Capa de control de rutas formativas.
- Capa de control de módulos de formación.
- Capa de detección de contenidos pendientes.
- Capa de priorización formativa.
- Registro documental de evidencias.
- Revisión humana obligatoria.
- Visualización futura no implementada.

## Arquitectura V1 implementable

La V1 debe ser mínima y verificable. Su alcance se limita a:

- Registro manual de rutas y módulos formativos.
- Estructura homogénea de perfiles, evidencias y acciones.
- Reglas simples para detectar estados inconsistentes.
- Registro de acciones siguientes.
- Revisión manual del resultado antes de aceptar cualquier cambio.

La V1 no debe prometer LMS real ni sincronización con herramientas externas.

## Arquitectura V2 futura

La V2 podría ampliar la base documental con:

- Captura semiestructurada desde formularios.
- Reglas más avanzadas de priorización.
- Notificaciones internas.
- Métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*).
- Dashboard funcional.
- Integración con API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) cuando exista una base estable.

## Datos previstos

- Rutas formativas con estado, prioridad y responsable.
- Módulos formativos asociados.
- Perfiles internos con necesidades formativas.
- Evidencias formativas de revisión o realización.
- Acciones formativas siguientes.

## Integraciones previstas

- Google Workspace, únicamente como posibilidad futura.
- CRM, únicamente como posibilidad futura.
- API, únicamente como posibilidad futura.
- LMS, únicamente como posibilidad futura.

## Control humano

Toda decisión relevante debe pasar por una persona. La arquitectura no contempla ejecución autónoma, cierre automático de rutas ni cambio de estado sin validación manual.

## Riesgos técnicos

- Ambigüedad en los datos de entrada.
- Estados de ruta o módulo incompatibles.
- Contenidos pendientes sin responsable de revisión.
- Prioridades formativas incoherentes entre áreas.
- Falsa sensación de automatización si se interpreta el documento como plataforma real.
- Dependencia excesiva de datos incompletos si no se define un criterio mínimo claro.

## Fuera de alcance inicial

- LMS funcional.
- Automatización formativa real.
- Dashboard funcional.
- Google Workspace.
- CRM.
- API.
- IA funcional.
- Integración con sistemas productivos.
- Promesas de mejora garantizada o métricas de aprendizaje no verificadas.

## Criterios de validación técnica

- La ruta debe poder validarse con campos mínimos definidos.
- Cada ruta debe quedar ligada a perfiles y módulos concretos.
- Las evidencias deben ser rastreables por identificador.
- La prioridad debe poder revisarse por una persona.
- El estado debe quedar registrado sin ambigüedad.
- El flujo debe poder explicarse sin recurrir a software ya construido.

## Próximos pasos técnicos

- Convertir este diseño en una V1 mínima si se decide implementar código más adelante.
- Mantener la revisión humana como control principal.
- Preparar la siguiente fase solo cuando exista decisión explícita de desarrollo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
