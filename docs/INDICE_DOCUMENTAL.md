# Índice Documental del Repositorio

## Propósito del índice

Este documento sirve como guía de lectura y navegación del repositorio. Su objetivo es ayudar a cualquier revisor a localizar rápido la documentación global, la documentación por agente, las evidencias técnicas, la demo local y el cierre técnico V1.

## Lectura recomendada para revisión rápida

1. `README.md`
2. `CATALOGO.md`
3. `docs/EVIDENCIAS_TECNICAS.md`
4. `docs/GUIA_DEMO_LOCAL.md`
5. `docs/CIERRE_TECNICO_V1.md`

## Documentación global

### `README.md`

Es la puerta de entrada del repositorio. Resume el enfoque general, el alcance actual y las referencias principales para entender la estructura del portfolio.

### `CATALOGO.md`

Recoge el catálogo funcional y documental del repositorio. Sirve para ubicar los agentes y entender la organización general antes de entrar en la documentación específica.

### `docs/VISION_GENERAL.md`

Expone la visión general del proyecto y su marco técnico. Aporta contexto de alto nivel para interpretar qué pretende mostrar el repositorio y qué no.

### `docs/CRITERIOS_PORTFOLIO.md`

Define los criterios de presentación del portfolio. Ayuda a mantener coherencia entre evidencia técnica, límites actuales y forma de comunicar el trabajo.

### `docs/EVIDENCIAS_TECNICAS.md`

Resume qué puede demostrarse hoy en el repositorio. Sirve para verificar scripts locales, pruebas `unittest`, JSON de ejemplo, validación global y ausencia de dependencias externas.

### `docs/GUIA_DEMO_LOCAL.md`

Explica cómo ejecutar la demo local paso a paso. Es la guía práctica para un revisor que quiera validar el repositorio desde la terminal.

### `docs/CIERRE_TECNICO_V1.md`

Describe el cierre técnico de la V1 local. Deja constancia de lo que queda implementado, qué límites mantiene el repositorio y cómo se separa la V1 de una futura evolución.

## Documentación por agente

### `agentes/01-agente-onboarding-inteligente/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de expedientes de onboarding ficticios.

### `agentes/02-agente-documental-inteligente/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de inventario documental ficticio.

### `agentes/03-agente-seguimiento-clientes/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de cartera de clientes ficticia.

### `agentes/04-agente-generador-propuestas/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de propuestas ficticias.

### `agentes/05-agente-operaciones-pymes/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de operaciones y bloqueos ficticios.

### `agentes/06-agente-control-cobros-flujo-caja/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de cobros y flujo de caja ficticios.

### `agentes/07-agente-pipeline-comercial/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de pipeline comercial ficticio.

### `agentes/08-agente-formacion-interna/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de formación interna ficticia.

### `agentes/09-agente-analisis-mercado/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de análisis de mercado ficticio.

### `agentes/10-agente-revision-cumplimiento/`

Contiene `README`, documentación V1, JSON ficticio, script local y pruebas `unittest`. Documenta una validación local de revisión de cumplimiento ficticia.

## Documentos de evidencia y validación

`docs/EVIDENCIAS_TECNICAS.md` resume qué puede demostrarse hoy y deja constancia de las evidencias técnicas verificables.

`docs/GUIA_DEMO_LOCAL.md` explica cómo ejecutar la demo local y cómo revisar el comportamiento mínimo del repositorio.

`scripts/validar_repositorio.py` valida los tests y los JSON de ejemplo, además de la coherencia técnica mínima del repositorio.

`.github/workflows/validacion.yml` ejecuta la validación técnica en GitHub Actions para `push` y `pull_request`, como parte de la CI (*Continuous Integration – Integración Continua*).

## Qué leer según el objetivo del revisor

- Para entender el proyecto completo: `README.md` y `CATALOGO.md`.
- Para comprobar evidencias técnicas: `docs/EVIDENCIAS_TECNICAS.md`.
- Para ejecutar la demo local: `docs/GUIA_DEMO_LOCAL.md`.
- Para revisar un agente concreto: la carpeta de ese agente dentro de `agentes/`.
- Para comprobar límites y fuera de alcance: `docs/CIERRE_TECNICO_V1.md`.

## Límites del repositorio actual

- No hay IA (*Artificial Intelligence – Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) real.
- No hay dashboard.
- No hay Google Workspace.
- No hay integraciones reales.
- No se trabaja con datos reales.
- No sustituye revisión humana.

## Cierre

Este índice debe mantenerse actualizado si se añaden nuevas fases, scripts, documentación, API, dashboard o integración real. Su función es ordenar la lectura documental y evitar interpretaciones confusas sobre el alcance actual.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
