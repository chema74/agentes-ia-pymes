# Roadmap V2.1 (calidad y fiabilidad)

Fecha base: 2026-05-14

## Objetivos

1. Cobertura y pruebas
- KPI: cobertura de `scripts/` >= 70% en CI.
- KPI: 0 tests flaky en 20 ejecuciones consecutivas locales.

2. Integracion de agentes a11/a12
- KPI: `a11` y `a12` con `tests/` y `datos_ejemplo/` en el mismo contrato operativo que el resto.

3. Gobernanza tecnica
- KPI: 100% PRs usando plantilla y checklist tecnica completada.
- KPI: `pip-audit` sin vulnerabilidades criticas abiertas en `main`.

4. DX de mantenimiento
- KPI: script unico `python scripts/ci_local.py` como referencia de validacion completa.

## Entregables

- Q2 2026, Semana 1: cobertura + estabilizacion tests servidor.
- Q2 2026, Semana 2: alta calidad para `a11/a12` (tests + datos + docs).
- Q2 2026, Semana 3: hardening seguridad y reglas de merge.
- Q2 2026, Semana 4: cierre V2.1 y release tag.
