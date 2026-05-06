# Agente de Operaciones para PYMES

## Descripción breve
Agente orientado a validar localmente tareas operativas ficticias, bloqueos, prioridades y acciones siguientes antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_operaciones.py`
- Prueba `unittest`: `tests/test_validar_operaciones.py`
- JSON ficticio principal: `datos_ejemplo/operaciones_pymes_ficticias.json`
- Validación local de tareas, bloqueos, dependencias, riesgos y decisión humana recomendada.

## V2 futura
- Reglas más específicas de dependencia y vencimiento.
- Posible desacoplamiento por áreas operativas.
- Integraciones futuras con herramientas reales, no implementadas.

## Fuera de alcance actual
- automatización operativa real,
- IA funcional,
- API,
- dashboard,
- integraciones vivas.

## Estructura relevante
- `src/validar_operaciones.py`
- `tests/test_validar_operaciones.py`
- `tests/datos_prueba/operaciones_incompletas.json`
- `datos_ejemplo/operaciones_pymes_ficticias.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
