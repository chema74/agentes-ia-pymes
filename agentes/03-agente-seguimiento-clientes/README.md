# Agente de Seguimiento de Clientes para PYMES

## Descripción breve
Agente orientado a validar localmente una cartera ficticia de clientes y sus acciones de seguimiento antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_cartera_clientes.py`
- Prueba `unittest`: `tests/test_validar_cartera_clientes.py`
- JSON ficticio principal: `datos_ejemplo/cartera_clientes_ficticia.json`
- Validación local de estados, riesgos, bloqueos, próximas acciones y decisión humana recomendada.

## V2 futura
- Reglas más detalladas de seguimiento.
- Posible modularización adicional.
- Integraciones futuras con CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*), no implementadas.

## Fuera de alcance actual
- CRM real.
- IA funcional.
- API.
- dashboard.
- automatización comercial real.

## Estructura relevante
- `src/validar_cartera_clientes.py`
- `tests/test_validar_cartera_clientes.py`
- `tests/datos_prueba/cartera_incompleta.json`
- `datos_ejemplo/cartera_clientes_ficticia.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
