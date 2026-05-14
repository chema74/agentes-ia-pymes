# ADR-001: Estandar de calidad y validacion unificada

Fecha: 2026-05-14
Estado: Aprobado

## Contexto

El repositorio crecio con multiples scripts y agentes. Existia riesgo de divergencia entre validaciones locales, CI y pruebas manuales.

## Decision

Se adopta un estandar unificado de calidad:

- validacion global con `scripts/validar_repositorio.py`;
- contrato minimo de agentes con `scripts/validar_contrato_agentes.py`;
- control de codificacion UTF-8 con `scripts/verificar_utf8.py`;
- pipeline CI por fases (`quality`, `tests`, `security`);
- herramientas de calidad (`ruff`, `mypy`, `pytest-cov`, `pip-audit`) declaradas en extras `dev`.

## Consecuencias

Positivas:

- reduce riesgo de regresiones silenciosas;
- estandariza la entrada de nuevos agentes;
- aumenta trazabilidad y auditabilidad tecnica.

Costes:

- mayor tiempo inicial de CI;
- necesidad de mantener reglas de lint/type.

## Alternativas consideradas

- Mantener solo `pytest` y validacion manual: descartado por bajo control de calidad.
- Incluir solo lint sin contrato de agentes: descartado por cobertura incompleta de arquitectura.
