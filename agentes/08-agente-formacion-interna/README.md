# Agente de Formación Interna para PYMES

## Descripción breve
Agente orientado a validar localmente rutas, módulos y evidencias formativas ficticias antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_formacion_interna.py`
- Prueba `unittest`: `tests/test_validar_formacion_interna.py`
- JSON ficticio principal: `datos_ejemplo/formacion_interna_ficticia.json`
- Validación local de rutas, módulos, evidencias, riesgos formativos y decisión humana recomendada.

## V2 futura
- Reglas más detalladas de trazabilidad formativa.
- Posible separación entre rutas, perfiles y evidencias.
- Integraciones futuras con LMS (*Learning Management System – Sistema de Gestión del Aprendizaje*), no implementadas.

## Fuera de alcance actual
- certificación de competencias,
- evaluación automática de personas,
- decisiones laborales automáticas,
- LMS real,
- IA funcional,
- API,
- dashboard.

## Estructura relevante
- `src/validar_formacion_interna.py`
- `tests/test_validar_formacion_interna.py`
- `tests/datos_prueba/formacion_incompleta.json`
- `datos_ejemplo/formacion_interna_ficticia.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
