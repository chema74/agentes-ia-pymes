# Agente de Pipeline Comercial para PYMES

## Descripción breve
Agente orientado a validar localmente oportunidades comerciales ficticias, fases, bloqueos y acciones de seguimiento antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_pipeline_comercial.py`
- Prueba `unittest`: `tests/test_validar_pipeline_comercial.py`
- JSON ficticio principal: `datos_ejemplo/pipeline_comercial_ficticio.json`
- Validación local de oportunidades, prioridades, temperatura comercial, bloqueos y decisión humana recomendada.

## V2 futura
- Reglas más detalladas de seguimiento por fase.
- Posible separación entre oportunidades, clasificaciones y acciones.
- Integraciones futuras con CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*), no implementadas.

## Fuera de alcance actual
- predicción comercial,
- garantía de ventas,
- automatización comercial real,
- IA funcional,
- API,
- dashboard.

## Estructura relevante
- `src/validar_pipeline_comercial.py`
- `tests/test_validar_pipeline_comercial.py`
- `tests/datos_prueba/pipeline_incompleto.json`
- `datos_ejemplo/pipeline_comercial_ficticio.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
