# Agente Generador de Propuestas para PYMES

## Descripción breve
Agente orientado a validar localmente una propuesta ficticia, sus entregables, alcance y acciones siguientes antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_propuesta.py`
- Prueba `unittest`: `tests/test_validar_propuesta.py`
- JSON ficticio principal: `datos_ejemplo/propuesta_ficticia.json`
- Validación local de propuesta, entregables, condiciones, acciones y decisión humana recomendada.

## V2 futura
- Reglas más precisas sobre consistencia de alcance y condiciones.
- Posible separación de validadores por bloque temático.
- Integraciones futuras de generación o envío, no implementadas.

## Fuera de alcance actual
- generación automática real de propuestas,
- IA funcional,
- PDF automático,
- API,
- dashboard,
- integraciones reales.

## Estructura relevante
- `src/validar_propuesta.py`
- `tests/test_validar_propuesta.py`
- `tests/datos_prueba/propuesta_incompleta.json`
- `datos_ejemplo/propuesta_ficticia.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
