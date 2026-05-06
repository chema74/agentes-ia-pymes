# Agente de Onboarding Inteligente para PYMES

## Descripción breve
Agente orientado a validar de forma local un expediente ficticio de onboarding y detectar ausencias documentales básicas antes de revisión humana.

## Estado técnico
El agente dispone de V1 mínima local funcional.

## V1 implementada
- Script local: `src/validar_expediente.py`
- Prueba `unittest`: `tests/test_validar_expediente.py`
- JSON ficticio principal: `datos_ejemplo/expediente_onboarding_ficticio.json`
- Validación de estructura, campos mínimos y salida por consola en castellano.

## V2 futura
- Reglas adicionales de validación.
- Separación de lógica si el caso crece.
- Posibles integraciones futuras, no implementadas.

## Fuera de alcance actual
- IA funcional.
- Google Workspace.
- API.
- dashboard.
- integraciones reales.
- decisiones automáticas sobre personas.

## Estructura relevante
- `src/validar_expediente.py`
- `tests/test_validar_expediente.py`
- `tests/datos_prueba/expediente_incompleto.json`
- `datos_ejemplo/expediente_onboarding_ficticio.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
