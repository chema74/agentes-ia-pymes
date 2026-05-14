# Registro de cambios

## [2.1.0-dev] - 2026-05-14

### Added
- Pipeline local de calidad: `scripts/ci_local.py`.
- Validacion de contrato tecnico de agentes: `scripts/validar_contrato_agentes.py`.
- Configuracion `pre-commit` y extras de desarrollo en `pyproject.toml`.
- Politica de seguridad: `SECURITY.md`.
- Plantilla de PR con checklist tecnico.
- ADR inicial de calidad: `docs/adr/ADR-001-calidad-validacion-unificada.md`.
- Guia para incorporar agentes: `docs/GUIA_ANIADIR_AGENTE.md`.
- Roadmap V2.1 de calidad: `docs/ROADMAP_V2_1_CALIDAD.md`.

### Changed
- Integracion de `a11` y `a12` con `tests/`, `datos_ejemplo/` y `docs/`.
- Secret scanning en CI via `gitleaks`.
- `Makefile` para flujos DX de calidad y release.
- Migracion de tests de servidor a puertos dinamicos en toda la suite del editor local.
- CI dividida en fases: `quality`, `tests`, `security`.
- `validar_repositorio.py` ahora incluye control UTF-8 y contrato de agentes.
- `pytest.ini` incluye marcadores de tipologia de pruebas.

### Fixed
- Robustez de test de historico en editor local con puerto dinamico.

## v1-local-completa - Demo local completa

Esta versión deja cerrada la V1 local completa como demo técnica reproducible, explicable, validada y documentada en entorno local temporal.

## Añadido

- consola local temporal,
- edición guiada local,
- histórico local,
- comparador local,
- informe consolidado local,
- paquete local de evidencias,
- demo local reproducible,
- guion local de demo.

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.

## v1.7.0 - Demo local reproducible

Esta versión cerró la fase V1.7 con un orquestador local para ejecutar la cadena completa de demo con un solo flujo reproducible.

## Añadido

- orquestador local de demo reproducible,
- cadena local completa sobre espacio de trabajo, agentes, panel, consolidado y evidencias,
- generación de panel local,
- generación de informe consolidado,
- exportación de evidencias,
- ZIP local opcional,
- integración con editor y consola local,
- pruebas transversales de la demo local.

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.

## v1.6.0 - Paquete local de evidencias de demo

Esta versión incorporó un paquete local de evidencias de demo para revisión humana en entorno local temporal.

## Añadido

- exportador local de evidencias,
- índice Markdown de evidencias,
- índice HTML local de evidencias,
- copia de panel local e informe consolidado,
- copia de informes disponibles,
- ZIP local opcional,
- integración con editor y consola local,
- pruebas transversales del paquete de evidencias.

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.

## v1.5.0 - Informe consolidado local

Esta versión incorporó consolidación local de los últimos informes de los 10 agentes dentro de la consola local temporal.

## Añadido

- generador de informe consolidado,
- salida Markdown local,
- salida HTML local,
- integración con editor y consola local,
- pruebas transversales del informe consolidado.

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.

## v1.4.0 - Comparador local de ejecuciones

Esta versión incorporó comparación local entre el último informe y los informes históricos por agente, dentro de la consola local temporal.

## Añadido

- comparador local de informes,
- comparación del último informe con históricos,
- detección de cambio de decisión recomendada,
- integración con editor y consola local,
- pruebas transversales del comparador.

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.

## v1.3.0 - Histórico local de ejecuciones

Esta versión incorporó conservación y consulta de informes históricos locales por agente, manteniendo la consola local como herramienta temporal de trabajo con datos ficticios.

## Añadido

- histórico local de informes por agente,
- conservación del último informe en `salidas/agente-XX/informe.txt`,
- consulta de histórico desde consola local,
- ejecución con `--guardar-historico` en el lanzador común,
- integración del histórico en el editor y la consola local.

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.

## v1.2.0 - Edición guiada local completa

Esta versión completó la fase V1.2 como capa de edición guiada local para los 10 agentes del repositorio, manteniendo la consola local como herramienta temporal de trabajo con datos ficticios.

## Añadido

- edición guiada para los 10 agentes,
- formularios locales por agente,
- ejecución con datos editados en el espacio de trabajo,
- conservación de JSON originales en `agentes/*/datos_ejemplo/`,
- integración con consola local, informes y panel HTML local.

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.

## v1.1.0 - Capa local interactiva

Esta versión amplió la V1 técnica local con una capa local interactiva orientada a revisión humana, manipulación controlada de datos ficticios y visualización local reproducible.

## Añadido

- lanzador común,
- salidas locales,
- panel HTML local,
- espacio de trabajo editable,
- editor y consola local,
- resumen local de agentes.

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.

## v1.0.0 - V1 técnica local

Esta versión representa el cierre de la primera versión técnica local del repositorio `agentes-ia-pymes`.

## Añadido

- estructura modular de 10 agentes para PYMES,
- documentación V1 por agente,
- datos ficticios en JSON (*JavaScript Object Notation - Notación de Objetos de JavaScript*),
- scripts locales de consola,
- pruebas `unittest` por agente,
- validación técnica global,
- workflow de GitHub Actions,
- documentos de evidencias técnicas,
- guía de demo local,
- cierre técnico V1,
- índice documental,
- ficha de portfolio.

## Validación

La versión se valida con:

```powershell
python scripts/validar_repositorio.py
```

## Límites de la versión

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay Google Workspace.
- No hay integraciones reales.
- No se trabaja con datos reales.
- No sustituye revisión humana.

## Criterio de cierre

La versión puede considerarse cerrada cuando la validación global devuelve:

`Resultado final: validacion global correcta.`

## Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
