# Repositorio Técnico agentes-ia-pymes

## Descripción breve
`agentes-ia-pymes` es un portfolio técnico con 10 agentes demostrables orientados a problemas habituales de pequeñas y medianas empresas. El repositorio prioriza trazabilidad, alcance real y revisión humana frente a promesas de automatización no implementada.

## Estado actual del repositorio
- Los 10 agentes tienen V1 técnica local mínima disponible.
- Cada agente incluye documentación base, un archivo JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) ficticio, un script Python de consola y pruebas `unittest`.
- Toda la ejecución actual funciona con biblioteca estándar de Python.
- La V1 actual valida estructura, estados e incidencias locales con datos ficticios y salida por consola.
- No hay IA (*Artificial Intelligence – Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*).
- No hay dashboard.
- No hay Google Workspace.
- No hay integraciones reales.
- No hay RAG (*Retrieval-Augmented Generation – Generación Aumentada por Recuperación*) real.
- No hay OCR (*Optical Character Recognition – Reconocimiento Óptico de Caracteres*) real.

## V1 implementada
La V1 implementada del repositorio consiste en una base técnica local verificable:
- Scripts de consola pequeños y didácticos.
- Validación de JSON ficticios por agente.
- Reglas mínimas de análisis operativo.
- Informes en castellano con decisión humana recomendada.
- Pruebas `unittest` ejecutables por agente.
- Validación técnica global del repositorio mediante `python scripts/validar_repositorio.py`.
- Workflow de GitHub Actions para ejecutar esa validación técnica global en `push` y `pull_request`.

Esta V1 no representa una suite productiva ni un sistema automatizado de agentes en producción. Representa una primera base reproducible de portfolio técnico.

## Validacion tecnica global
El repositorio incluye una capa transversal mínima de validación técnica:
- `python scripts/validar_repositorio.py`
- comprobación de los tests `unittest` de los 10 agentes
- validación de los 10 archivos JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) de ejemplo
- ejecución automatizable mediante GitHub Actions

Esta validación global mejora la trazabilidad técnica del portfolio, pero no convierte la V1 en producto terminado ni en automatización real de negocio.

## Agentes incluidos
- `01-agente-onboarding-inteligente`: validación local de expedientes ficticios de onboarding.
- `02-agente-documental-inteligente`: validación local de inventario documental ficticio.
- `03-agente-seguimiento-clientes`: validación local de cartera ficticia de seguimiento de clientes.
- `04-agente-generador-propuestas`: validación local de propuesta ficticia.
- `05-agente-operaciones-pymes`: validación local de tareas y bloqueos operativos ficticios.
- `06-agente-control-cobros-flujo-caja`: validación local de cobros y previsión operativa ficticia.
- `07-agente-pipeline-comercial`: validación local de oportunidades comerciales ficticias.
- `08-agente-formacion-interna`: validación local de rutas y módulos formativos ficticios.
- `09-agente-analisis-mercado`: validación local de señales de mercado ficticias.
- `10-agente-revision-cumplimiento`: validación local de revisión interna ficticia y seguimiento de evidencias.

## Alcance actual
El repositorio sirve como evidencia técnica de:
- capacidad de estructurar casos de uso por agente,
- capacidad de traducir documentación V1 a validadores locales mínimos,
- capacidad de mantener coherencia entre datos ficticios, scripts y pruebas,
- capacidad de delimitar con claridad lo implementado y lo no implementado.

Las evidencias técnicas verificables del repositorio se resumen en `docs/EVIDENCIAS_TECNICAS.md`.

La guía para ejecutar la demo local está en `docs/GUIA_DEMO_LOCAL.md`.
El documento de cierre técnico V1 está en `docs/CIERRE_TECNICO_V1.md` y recoge el estado de cierre de la V1 técnica local.

## V2 futura
La ficha de portfolio reutilizable estÃ¡ en `docs/FICHA_PORTFOLIO.md` y resume el proyecto para una futura web de portfolio.
El índice documental del repositorio está en `docs/INDICE_DOCUMENTAL.md` y sirve como guía de navegación documental.
La V2 futura puede explorar, si se prioriza más adelante:
- automatizaciones internas adicionales,
- mayor separación de reglas y lógica,
- interfaces de uso más cómodas,
- conectores o integraciones externas,
- IA funcional,
- API,
- dashboard,
- flujos con Google Workspace,
- capas posteriores de RAG u OCR cuando el alcance lo justifique.

Nada de lo anterior está implementado en esta V1.

## Fuera de alcance actual
- Producto SaaS.
- Automatización real de procesos de negocio.
- Decisiones automáticas sobre clientes, personas, documentos, cobros o cumplimiento.
- Integración con sistemas vivos.
- Servicios en red, paneles o despliegues.
- Uso de dependencias externas.

## Estructura del repositorio
- `README.md`
- `CATALOGO.md`
- `docs/`
- `agentes/01-agente-onboarding-inteligente/`
- `agentes/02-agente-documental-inteligente/`
- `agentes/03-agente-seguimiento-clientes/`
- `agentes/04-agente-generador-propuestas/`
- `agentes/05-agente-operaciones-pymes/`
- `agentes/06-agente-control-cobros-flujo-caja/`
- `agentes/07-agente-pipeline-comercial/`
- `agentes/08-agente-formacion-interna/`
- `agentes/09-agente-analisis-mercado/`
- `agentes/10-agente-revision-cumplimiento/`

## Nota de portfolio
El valor actual del repositorio está en la veracidad del alcance: cada agente muestra documentación, datos ficticios, validación local y pruebas pequeñas, sin presentarse como producto terminado ni como automatización real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
