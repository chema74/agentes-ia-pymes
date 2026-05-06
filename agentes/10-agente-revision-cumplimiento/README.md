# Agente de Revisión y Cumplimiento para PYMES

## Descripción breve
Agente orientado a validar localmente controles internos ficticios, evidencias, hallazgos y acciones de seguimiento antes de revisión humana.

## Estado técnico
El agente dispone de V1 técnica local mínima.

## V1 implementada
- Script local: `src/validar_revision_cumplimiento.py`
- Prueba `unittest`: `tests/test_validar_revision_cumplimiento.py`
- JSON ficticio principal: `datos_ejemplo/revision_cumplimiento_ficticia.json`
- Validación local de controles, evidencias, hallazgos, documentos pendientes y decisión humana recomendada.

## V2 futura
- Reglas más finas de consistencia de hallazgos y acciones correctivas.
- Posible separación entre controles, evidencias y documentos.
- Integraciones futuras de soporte documental, no implementadas.

## Fuera de alcance actual
- asesoría legal, fiscal, laboral, financiera o regulatoria,
- acreditación de cumplimiento normativo,
- interpretación de legislación real,
- automatización de decisiones de cumplimiento,
- IA funcional,
- API,
- dashboard.

## Estructura relevante
- `src/validar_revision_cumplimiento.py`
- `tests/test_validar_revision_cumplimiento.py`
- `tests/datos_prueba/revision_cumplimiento_incompleta.json`
- `datos_ejemplo/revision_cumplimiento_ficticia.json`

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
