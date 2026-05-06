# Agente de Control de Cobros y Flujo de Caja para PYMES

## Descripción breve
Agente orientado a validar localmente cobros ficticios, estados, riesgos y señales operativas de seguimiento antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_cobros_flujo_caja.py`
- Prueba `unittest`: `tests/test_validar_cobros_flujo_caja.py`
- JSON ficticio principal: `datos_ejemplo/cobros_flujo_caja_ficticios.json`
- Validación local de cobros, vencimientos, riesgos, previsiones operativas y decisión humana recomendada.

## V2 futura
- Reglas más finas de coherencia operativa.
- Mejor separación entre cobros, riesgos y previsiones.
- Integraciones futuras con sistemas internos, no implementadas.

## Fuera de alcance actual
- asesoría financiera, fiscal, contable o legal,
- predicciones financieras,
- automatización real de cobros,
- IA funcional,
- API,
- dashboard.

## Estructura relevante
- `src/validar_cobros_flujo_caja.py`
- `tests/test_validar_cobros_flujo_caja.py`
- `tests/datos_prueba/cobros_incompletos.json`
- `datos_ejemplo/cobros_flujo_caja_ficticios.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
