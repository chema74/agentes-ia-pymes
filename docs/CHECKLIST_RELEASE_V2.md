# Checklist Release V2

Fecha de referencia: 2026-05-14

## 1. Calidad tecnica

- [ ] `python scripts/verificar_utf8.py` devuelve `Comprobacion UTF-8 correcta.`
- [ ] `python scripts/validar_repositorio.py` finaliza sin errores.
- [ ] `python -m pytest -q` finaliza con todos los tests en verde.
- [ ] No hay artefactos locales en el arbol (`.pytest-tmp/`, `salidas/`, `espacio_trabajo/`).

## 2. Cobertura de agentes

- [ ] `scripts/validar_repositorio.py` detecta todos los directorios bajo `agentes/`.
- [ ] Cada agente con `tests/` ejecuta su suite correctamente.
- [ ] Cada agente con `datos_ejemplo/` tiene JSON valido.
- [ ] Cambios en agentes nuevos (`a11`, `a12`, futuros) no requieren editar una lista hardcodeada.

## 3. CI/CD

- [ ] El workflow `.github/workflows/validacion.yml` ejecuta:
- [ ] `python scripts/validar_repositorio.py`
- [ ] `python scripts/verificar_utf8.py`
- [ ] `python -m pytest -v`
- [ ] El ultimo pipeline en `main` esta en verde.

## 4. Documentacion y trazabilidad

- [ ] `README.md` no contiene bytes no UTF-8.
- [ ] Los documentos V2 obligatorios siguen presentes en `docs/`.
- [ ] `docs/INDICE_DOCUMENTAL.md` incluye esta checklist.
- [ ] `CHANGELOG.md` refleja los cambios de estabilizacion V2.

## 5. Release y control de cambios

- [ ] Cambios agrupados en commits atomicos (infra calidad, docs release).
- [ ] Etiqueta de release creada (por ejemplo `v2.0.0` o equivalente acordado).
- [ ] Evidencias de ejecucion guardadas en `salidas/` cuando aplique demo.
- [ ] Validacion final repetida tras tag para evitar regresiones de ultimo minuto.

## Criterio de salida

La release V2 se considera lista solo si todos los puntos anteriores estan marcados y el estado de CI en `main` permanece en verde.
