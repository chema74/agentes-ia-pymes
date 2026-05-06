# Catálogo de Agentes IA para PYMES

## Objetivo del catálogo
Este archivo resume los agentes incluidos dentro del repositorio y su estado real de avance. Su función es ofrecer una vista técnica rápida para entender qué está cerrado en V1 mínima, qué tiene documentación V1 preparada y qué permanece como evolución futura.

## Estado general
- El repositorio sigue en evolución.
- La infraestructura documental común está creada.
- El agente 01 tiene una V1 mínima local funcional.
- Los agentes 02 al 10 tienen fase documental V1 preparada.
- No existe IA funcional, Google Workspace, dashboard, API, automatización productiva ni integración real con clientes.

## Agente 01 — V1 mínima local funcional
- Carpeta: `agentes/01-agente-onboarding-inteligente/`
- Estado: V1 mínima local funcional.
- Objetivo: ordenar el alta inicial de clientes en PYMES mediante validación local de un expediente ficticio, checklist, documentación recibida y revisión manual prevista.

Incluye:
- Documentación funcional y técnica.
- Modelo de datos.
- Checklist.
- Expediente ficticio.
- Flujo de validación manual.
- Script local de validación.
- Datos ficticios.
- 4 pruebas `unittest` OK.

Alcance real de la V1 mínima:
- Validación local con Python estándar.
- Informe por consola.
- Ejecución sin argumento.
- Ejecución con ruta explícita al JSON ficticio.
- Control de ruta inexistente.
- Control de JSON válido con estructura incompleta.

Fuera de alcance actual:
- Producto comercial terminado.
- IA funcional.
- Google Workspace.
- Dashboard.
- API.
- Automatización productiva.
- Integración real con clientes.
- Decisiones sin revisión humana.

Evolución V2:
- Se mantiene como evolución futura.
- Debe documentarse antes de integrar Google Workspace, dashboard, API o IA.

## Agentes 02 al 10 — Fase documental V1 preparada

### 02 — Agente Documental Inteligente
- Carpeta: `agentes/02-agente-documental-inteligente/`
- Estado: fase documental V1 preparada.
- Propósito: organizar, versionar y priorizar documentación operativa y comercial con criterios homogéneos.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

### 03 — Agente de Seguimiento de Clientes
- Carpeta: `agentes/03-agente-seguimiento-clientes/`
- Estado: fase documental V1 preparada.
- Propósito: centralizar hitos de seguimiento y próximos pasos de clientes para reducir olvidos operativos.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

### 04 — Agente Generador de Propuestas
- Carpeta: `agentes/04-agente-generador-propuestas/`
- Estado: fase documental V1 preparada.
- Propósito: estandarizar la preparación de propuestas comerciales a partir de insumos estructurados.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

### 05 — Agente de Operaciones para PYMES
- Carpeta: `agentes/05-agente-operaciones-pymes/`
- Estado: fase documental V1 preparada.
- Propósito: mapear tareas recurrentes de operaciones y establecer trazabilidad mínima de ejecución.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

### 06 — Agente de Control de Cobros y Flujo de Caja
- Carpeta: `agentes/06-agente-control-cobros-flujo-caja/`
- Estado: fase documental V1 preparada.
- Propósito: ordenar eventos de cobro, alertas básicas y seguimiento de vencimientos para mejorar visibilidad operativa.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

### 07 — Agente de Pipeline Comercial
- Carpeta: `agentes/07-agente-pipeline-comercial/`
- Estado: fase documental V1 preparada.
- Propósito: definir etapas comerciales, criterios de avance y señales de bloqueo para oportunidades en curso.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

### 08 — Agente de Formación Interna
- Carpeta: `agentes/08-agente-formacion-interna/`
- Estado: fase documental V1 preparada.
- Propósito: estructurar contenidos internos de capacitación y rutas de aprendizaje por rol.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

### 09 — Agente de Análisis de Mercado
- Carpeta: `agentes/09-agente-analisis-mercado/`
- Estado: fase documental V1 preparada.
- Propósito: definir un marco para recopilar y organizar señales de mercado relevantes para decisiones comerciales.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

### 10 — Agente de Revisión y Cumplimiento
- Carpeta: `agentes/10-agente-revision-cumplimiento/`
- Estado: fase documental V1 preparada.
- Propósito: establecer controles de revisión documental y verificación de cumplimiento operativo básico.
- Evidencia disponible: documentación V1 + JSON ficticio.
- Fuera de alcance actual: código funcional, IA funcional, dashboard, API e integraciones reales.

## Criterios de activación de un agente
- Un agente solo pasará de documental a activo cuando tenga documentación base mínima.
- Debe existir una V1 implementable con alcance verificable.
- Deben quedar claros los límites de lo que no está implementado.
- No se debe avanzar a integración externa sin pruebas y documentación previa.

## Orden de trabajo
- Mantener la V1 mínima del agente 01 como referencia inicial.
- Mejorar pruebas del agente 01 solo si aparecen nuevas reglas.
- Preparar V2 documental antes de integrar herramientas externas.
- Mantener los agentes 02 a 10 como documentación V1 preparada.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
