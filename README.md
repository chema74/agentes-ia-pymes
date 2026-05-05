# Repositorio Técnico agentes-ia-pymes

## Descripción breve del objetivo
Este repositorio organiza un portfolio técnico en castellano para diseñar, documentar y validar agentes orientados a pequeñas y medianas empresas. El foco es avanzar por iteraciones pequeñas, trazables y verificables, separando claramente lo implementado de lo previsto para fases futuras.

El repositorio sigue en evolución. No se presenta como producto terminado ni como una suite comercial de agentes.

## Estado actual del repositorio
El agente 01 ya tiene una V1 mínima local cerrada, implementada y probada.

Estado actual:
- `01-agente-onboarding-inteligente`: V1 mínima local cerrada.
- Agentes `02` a `10`: estructura reservada y desarrollo pendiente.
- Dependencias externas: ninguna para la V1 mínima del agente 01.
- IA funcional: no existe.
- Google Workspace: no existe.
- Dashboard: no existe.
- API: no existe.
- Automatización productiva: no existe.
- Integración real con clientes: no existe.

## Agente 01: V1 mínima local cerrada
El Agente de Onboarding Inteligente para PYMES ya dispone de una primera implementación mínima local.

Incluye:
- Script local de validación: `agentes/01-agente-onboarding-inteligente/src/validar_expediente.py`.
- Datos ficticios: `agentes/01-agente-onboarding-inteligente/datos_ejemplo/cliente_onboarding_ficticio.json`.
- Pruebas: `agentes/01-agente-onboarding-inteligente/tests/test_validar_expediente.py`.
- Dato de prueba incompleto: `agentes/01-agente-onboarding-inteligente/tests/datos_prueba/expediente_incompleto.json`.

Validación real:
- Ejecución sin argumento: OK.
- Ejecución con ruta explícita al JSON: OK.
- Pruebas `unittest`: 4 tests OK.
- Biblioteca estándar de Python: sí.
- Dependencias externas: ninguna.

La V1 mínima valida un expediente ficticio mediante Python estándar y pruebas `unittest`. Su alcance se limita a validación local, informe por consola y control básico de errores.

## Problema general que aborda
Muchas PYMES tienen procesos críticos dispersos, con baja estandarización y alta dependencia manual. Este portfolio aborda ese problema mediante diseños de agentes que ayudan a estructurar información, mejorar trazabilidad y preparar automatizaciones progresivas con enfoque implementable.

## Agentes previstos del portfolio
- `01-agente-onboarding-inteligente`: V1 mínima local cerrada.
- `02-agente-documental-inteligente`: estructura reservada, desarrollo pendiente.
- `03-agente-seguimiento-clientes`: estructura reservada, desarrollo pendiente.
- `04-agente-generador-propuestas`: estructura reservada, desarrollo pendiente.
- `05-agente-operaciones-pymes`: estructura reservada, desarrollo pendiente.
- `06-agente-control-cobros-flujo-caja`: estructura reservada, desarrollo pendiente.
- `07-agente-pipeline-comercial`: estructura reservada, desarrollo pendiente.
- `08-agente-formacion-interna`: estructura reservada, desarrollo pendiente.
- `09-agente-analisis-mercado`: estructura reservada, desarrollo pendiente.
- `10-agente-revision-cumplimiento`: estructura reservada, desarrollo pendiente.

## Alcance actual
Incluye:
- Documentación global del portfolio.
- Catálogo de agentes y estados.
- Desarrollo completo de la V1 mínima local del agente 01.
- Estructura reservada para agentes 02 a 10.

No incluye:
- IA funcional.
- Google Workspace.
- Dashboard.
- API.
- Automatización productiva.
- Integración real con clientes.
- Despliegue productivo.

## Estructura del repositorio
- `README.md`: presentación técnica general del portfolio.
- `CATALOGO.md`: inventario de agentes y estado general.
- `docs/`: visión global y criterios técnicos transversales.
- `plantillas/`: plantillas base para documentación de agentes.
- `agentes/`: carpetas individuales de cada agente.

Dentro del agente 01 existe además una V1 mínima local con `src/`, `tests/` y datos ficticios.

## Próximos pasos
1. Mantener estable la V1 mínima del agente 01.
2. Mejorar casos de prueba si aparecen nuevas reglas.
3. Preparar una posible V2 documental antes de integrar herramientas externas.
4. Mantener agentes 02 a 10 como reservados hasta activar su documentación base.

## Nota de evolución del portfolio
El repositorio se encuentra en evolución controlada. La prioridad actual es mantener trazabilidad de alcance, evitar promesas no implementadas y avanzar agente por agente con validaciones pequeñas y reproducibles.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
