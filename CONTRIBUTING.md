# Contribuir a agentes-ia-pymes

Este es un portfolio técnico personal. Las contribuciones externas no están abiertas, pero se aceptan correcciones de errores y mejoras de documentación mediante pull request.

## Requisitos

- Python 3.11 o superior
- Sin dependencias externas (solo biblioteca estándar)

## Ejecutar los tests

```bash
# Tests globales (todos los agentes + transversales)
python scripts/validar_repositorio.py

# Solo tests transversales
python -m pytest tests/ -v

# Tests de un agente concreto
python -m unittest discover -s agentes/01-agente-onboarding-inteligente/tests
```

## Estructura del repositorio

```
agentes/          # 10 agentes, cada uno con src/, tests/ y datos_ejemplo/
scripts/          # Orquestación: ejecutar, validar, panel, demo, evidencias
tests/            # Tests transversales (todos los agentes juntos)
docs/             # Documentación técnica de cierre y portfolio
plantillas/       # Plantillas reutilizables
```

## Convenciones

- Código en español (nombres de variables, funciones, mensajes)
- Sin dependencias externas — solo `stdlib`
- Cada agente es independiente y ejecutable por separado
- Los datos de ejemplo son ficticios y no contienen información real

## Reportar un problema

Abre un [issue](https://github.com/chema74/agentes-ia-pymes/issues) describiendo el problema y los pasos para reproducirlo.
