# Arquitectura del Agente de Onboarding Inteligente para PYMES

## Propósito del documento
Este documento describe la arquitectura conceptual y técnica del agente 01, diferenciando la implementación mínima V1 ya disponible de las posibles ampliaciones futuras.

## Estado técnico actual
- Arquitectura actual: mínima, local y verificable.
- Implementación disponible: script local de validación.
- Script: `src/validar_expediente.py`.
- Entrada principal: archivo JSON ficticio.
- Salida principal: informe por consola.
- Pruebas: `unittest` mediante subprocess.
- Dependencias externas: ninguna.
- Automatización productiva: no existe.
- IA funcional: no existe.
- Google Workspace: no existe.
- Dashboard: no existe.
- API: no existe.
- Base de datos: no existe.
- Integraciones reales: no existen.

## Arquitectura actual V1 mínima
La arquitectura implementada se compone de cuatro piezas:

- JSON ficticio de entrada: `datos_ejemplo/cliente_onboarding_ficticio.json`.
- Script Python local: `src/validar_expediente.py`.
- Salida por consola: informe de validación y decisión recomendada.
- Pruebas con biblioteca estándar: `tests/test_validar_expediente.py`.

El flujo técnico actual es:

1. El script recibe una ruta opcional de JSON o usa la ruta ficticia por defecto.
2. Carga el JSON con biblioteca estándar.
3. Valida secciones principales.
4. Valida campos mínimos del cliente.
5. Revisa documentación y checklist.
6. Detecta pendientes y bloqueos.
7. Imprime un informe por consola.
8. Devuelve código `0` si la validación se ejecuta correctamente.
9. Devuelve código distinto de `0` ante archivo inexistente, JSON inválido o estructura incompleta.

## Componentes funcionales actuales
### Entrada
La entrada actual es un JSON ficticio. No existe captura real de datos, formulario, conexión externa ni integración con clientes.

### Validación
La validación actual se basa en reglas simples:
- Presencia de secciones principales.
- Presencia de campos mínimos del cliente.
- Conteo de documentos por estado.
- Conteo y revisión de ítems del checklist.
- Detección de ítems obligatorios pendientes.
- Detección de bloqueos.

### Decisión recomendada
La decisión recomendada procede de reglas simples del script. No procede de IA ni sustituye revisión humana.

### Salida
La salida actual es texto por consola. No se generan archivos, dashboards, documentos ni registros en base de datos.

### Pruebas
La arquitectura incluye pruebas con `unittest` que ejecutan el script mediante `subprocess`, simulando el uso desde consola.

Casos cubiertos:
- Ejecución sin argumentos.
- Ejecución con ruta explícita al JSON ficticio.
- Ruta inexistente.
- JSON válido con estructura incompleta.

## Arquitectura futura posible
Una futura V2 podría estudiar integraciones, pero no forman parte de la V1 mínima.

Posibles líneas futuras:
- Entrada con formularios.
- Registro operativo externo.
- Organización documental.
- Dashboard.
- Integración con Google Workspace.
- API.
- Asistencia con IA.

Estas líneas requieren documentación previa, revisión del alcance y nuevas pruebas antes de implementarse.

## Riesgos controlados en V1
- No se usan datos reales.
- No se instalan dependencias.
- No se conectan servicios externos.
- No se automatizan acciones productivas.
- No se toman decisiones sin revisión humana.
- No se presenta el agente como sistema terminado.

## Fuera de alcance actual
- IA funcional.
- Google Workspace.
- Dashboard.
- API.
- Base de datos.
- Automatización productiva.
- Integración real con clientes.
- Producción real.
- Seguridad avanzada.
- Gestión legal, fiscal o contractual.
- CRM completo.
- ERP.

## Próximos pasos técnicos
1. Mejorar casos de prueba si aparecen nuevos escenarios.
2. Separar reglas de validación si la lógica crece.
3. Diseñar una V2 documental antes de integrar herramientas externas.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
