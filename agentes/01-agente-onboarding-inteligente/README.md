# Agente de Onboarding Inteligente para PYMES

## Descripción breve
Este agente está pensado para ordenar el alta inicial de clientes en PYMES mediante recogida estructurada de datos, checklist de onboarding, revisión de documentación y preparación de un expediente inicial. La V1 mínima ya cuenta con una implementación local verificable, limitada a validar un expediente ficticio y generar un informe por consola.

El agente no se presenta como producto terminado. Es una primera base técnica de portfolio para demostrar un flujo pequeño, reproducible y sin dependencias externas.

## Estado actual
- Estado documental: base V1 documentada.
- Estado técnico: V1 mínima local implementada y probada.
- Código funcional disponible: validación local de un expediente ficticio.
- Script local: `src/validar_expediente.py`.
- Datos ficticios: `datos_ejemplo/cliente_onboarding_ficticio.json`.
- Pruebas: `tests/test_validar_expediente.py`.
- Casos de prueba actuales: 4 tests con `unittest`, validados correctamente.
- Dependencias externas: ninguna.
- `requirements.txt`: sin dependencias activas.
- Automatización productiva: no existe todavía.
- IA funcional: no existe todavía.
- Google Workspace: no existe todavía.
- Dashboard: no existe todavía.
- API: no existe todavía.
- Integración real con clientes: no existe todavía.

## Implementación mínima V1 disponible
La implementación mínima V1 se limita a un script local:

- `src/validar_expediente.py`

El script permite:
- Ejecutarse sin argumentos usando el JSON ficticio por defecto.
- Ejecutarse con una ruta explícita a un archivo JSON.
- Cargar datos ficticios de onboarding.
- Validar que existen las secciones principales del expediente.
- Validar campos mínimos del cliente.
- Contar documentos recibidos, pendientes e incompletos.
- Revisar ítems completos, pendientes y bloqueados del checklist.
- Detectar pendientes y bloqueos.
- Recomendar una decisión simple de revisión humana.
- Devolver código de salida distinto de `0` ante archivo inexistente, JSON inválido o estructura incompleta.

Esta implementación usa solo biblioteca estándar de Python. No usa IA, Google Workspace, API externa, dashboard, base de datos ni automatizaciones productivas.

## Ejecución local
Desde la raíz del repositorio, el script puede ejecutarse sin argumentos:

```bash
python agentes/01-agente-onboarding-inteligente/src/validar_expediente.py
```

También puede ejecutarse indicando explícitamente la ruta del JSON ficticio:

```bash
python agentes/01-agente-onboarding-inteligente/src/validar_expediente.py agentes/01-agente-onboarding-inteligente/datos_ejemplo/cliente_onboarding_ficticio.json
```

## Pruebas
Las pruebas se ejecutan desde la raíz del repositorio con:

```bash
python -m unittest discover -s agentes/01-agente-onboarding-inteligente/tests
```

Estado actual de pruebas:
- 4 pruebas con `unittest`.
- Ejecución sin argumentos: OK.
- Ejecución con ruta explícita al JSON ficticio: OK.
- Ruta de JSON inexistente: OK, devuelve error controlado.
- JSON válido con estructura incompleta: OK, devuelve error controlado.

## Resultado de validación actual
Con el expediente ficticio disponible, la validación local produce una decisión recomendada de revisión manual:

- Cliente ficticio: Laura Martín.
- Empresa ficticia: Taller Creativo Bahía, S. L.
- Estado del onboarding: `en_revision`.
- Documentos recibidos: 1.
- Documentos pendientes: 1.
- Documentos incompletos: 1.
- Ítems completos: 7.
- Ítems pendientes: 1.
- Ítems obligatorios pendientes: 2.
- Ítems bloqueados: 2.
- Decisión recomendada de revisión manual: `bloquear`.

Este resultado procede de datos ficticios y de reglas simples. No sustituye revisión humana.

## Problema que aborda
El onboarding en muchas PYMES suele empezar con información dispersa, correos sueltos, documentación incompleta y falta de trazabilidad sobre qué datos faltan para avanzar. Esto provoca retrasos, retrabajo administrativo y dependencia de seguimiento manual.

La V1 mínima demuestra cómo convertir un expediente ficticio en un informe local que ayuda a revisar el estado del onboarding antes de avanzar.

## Alcance actual
Incluye:
- Documentación funcional y técnica.
- Modelo de datos ficticio.
- Checklist de onboarding ficticio.
- Script local de validación.
- Informe por consola.
- Pruebas básicas con `unittest`.
- Control básico de errores.

No incluye:
- IA funcional.
- Google Workspace.
- Dashboard.
- API.
- Base de datos.
- Automatización productiva.
- Integración real con clientes.
- Captura real de datos.
- Generación automática de documentos.

## Evolución futura
Una posible V2 podría explorar integración documental o formularios, pero solo después de preparar documentación específica y mantener una separación clara entre lo implementado y lo previsto.

Cualquier futura integración con Google Workspace, dashboard, API o IA debe tratarse como evolución posterior, no como funcionalidad actual.

## Estructura relevante
- `README.md`
- `docs/ARQUITECTURA.md`
- `docs/CASO_USO.md`
- `docs/ROADMAP.md`
- `datos_ejemplo/cliente_onboarding_ficticio.json`
- `src/validar_expediente.py`
- `tests/test_validar_expediente.py`
- `tests/datos_prueba/expediente_incompleto.json`
- `requirements.txt`

## Próximos pasos
1. Mejorar casos de prueba si aparecen nuevas reglas.
2. Separar reglas de validación si la lógica crece.
3. Preparar una posible V2 documental antes de integrar Google Workspace.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
