# Agente Documental Inteligente para PYMES

## Descripción breve
Agente orientado a validar localmente un inventario documental ficticio, sus estados, pendientes y acciones siguientes antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_inventario_documental.py`
- Prueba `unittest`: `tests/test_validar_inventario_documental.py`
- JSON ficticio principal: `datos_ejemplo/inventario_documental_ficticio.json`
- Validación local de secciones principales, estados documentales, pendientes y decisión humana recomendada.

## V2 futura
- Reglas más finas de inventario y priorización.
- Separación adicional de reglas y presentación.
- Posibles integraciones documentales futuras, no implementadas.

## Fuera de alcance actual
- IA funcional.
- RAG real.
- OCR real.
- Google Workspace.
- API.
- dashboard.
- integraciones reales.

## Estructura relevante
- `src/validar_inventario_documental.py`
- `tests/test_validar_inventario_documental.py`
- `tests/datos_prueba/inventario_incompleto.json`
- `datos_ejemplo/inventario_documental_ficticio.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
