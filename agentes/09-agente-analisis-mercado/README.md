# Agente de Análisis de Mercado para PYMES

## Descripción breve
Agente orientado a validar localmente señales de mercado ficticias, oportunidades, competidores y riesgos antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_analisis_mercado.py`
- Prueba `unittest`: `tests/test_validar_analisis_mercado.py`
- JSON ficticio principal: `datos_ejemplo/analisis_mercado_ficticio.json`
- Validación local de señales, oportunidades, competidores, riesgos y decisión humana recomendada.

## V2 futura
- Reglas más finas de consistencia entre señales y acciones.
- Posible separación entre observación, riesgo y exploración.
- Integraciones futuras con fuentes externas, no implementadas.

## Fuera de alcance actual
- consulta de internet,
- predicción de mercado,
- asesoramiento financiero o de inversión,
- estrategia automática,
- IA funcional,
- API,
- dashboard.

## Estructura relevante
- `src/validar_analisis_mercado.py`
- `tests/test_validar_analisis_mercado.py`
- `tests/datos_prueba/analisis_mercado_incompleto.json`
- `datos_ejemplo/analisis_mercado_ficticio.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
