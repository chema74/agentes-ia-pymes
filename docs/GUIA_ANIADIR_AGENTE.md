# Guia: aniadir un agente nuevo

Esta guia define el contrato minimo para incorporar un agente al repositorio sin romper CI ni trazabilidad.

## 1. Estructura obligatoria

Crear carpeta `agentes/<id>-<nombre>/` con:

- `README.md`
- `requirements.txt`
- `src/`

Ejemplo:

```text
agentes/11-agente-ejemplo/
  README.md
  requirements.txt
  src/
```

## 2. Estructura recomendada

- `tests/`
- `datos_ejemplo/`
- `docs/`

Estas rutas no son criticas para pasar contrato, pero si para calidad y mantenibilidad.

## 3. Reglas de datos

- Solo datos ficticios.
- JSON en UTF-8.
- No incluir PII real ni credenciales.

## 4. Validaciones obligatorias antes de PR

```bash
python scripts/verificar_utf8.py
python scripts/validar_contrato_agentes.py
python scripts/validar_repositorio.py
python -m pytest -q
```

## 5. Criterios de aceptacion

- CI en verde.
- Contrato de agente valido.
- Tests del agente (si existen) pasando.
- Documentacion minima actualizada (`README` del agente y catalogo global si aplica).
