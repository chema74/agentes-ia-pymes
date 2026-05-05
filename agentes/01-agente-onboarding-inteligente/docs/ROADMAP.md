# Roadmap del Agente de Onboarding Inteligente para PYMES

## Propósito del documento
Este documento define la evolución del agente por fases, diferenciando lo ya implementado, lo validado y lo que queda como evolución futura. Su función es mantener el alcance técnico claro sin presentar como existente ninguna capacidad no implementada.

## Estado actual
- Estado documental: base V1 documentada.
- Estado técnico: implementación mínima V1 local iniciada y validada en su primera versión.
- Código funcional disponible: `src/validar_expediente.py`.
- Datos ficticios disponibles: `datos_ejemplo/cliente_onboarding_ficticio.json`.
- Pruebas disponibles: `tests/test_validar_expediente.py`.
- Dato de prueba incompleto: `tests/datos_prueba/expediente_incompleto.json`.
- Pruebas actuales: 4 tests con `unittest`, validados correctamente.
- Dependencias externas: ninguna.
- Automatización productiva: no implementada.
- IA funcional: no implementada.
- Google Workspace: no implementado.
- Dashboard: no implementado.
- API: no implementada.
- Base de datos: no implementada.
- Integración real con clientes: no implementada.

## Fase 0 — Base documental
Esta fase definió el problema, el alcance, el caso de uso, la arquitectura conceptual y la evolución prevista.

Estado: completada para la base V1.

Entregables:
- README del agente.
- Arquitectura.
- Caso de uso.
- Roadmap.
- Modelo de datos.
- Checklist.
- Expediente ficticio.
- Flujo de validación manual.

## Fase 1 — Definición de V1 implementable
Esta fase convirtió la documentación en un diseño mínimo implementable con datos ficticios y revisión humana.

Estado: completada para la base V1.

Entregables:
- Expediente ficticio en JSON.
- Secciones principales obligatorias.
- Campos mínimos del cliente.
- Checklist de onboarding.
- Documentación recibida, pendiente e incompleta.
- Reglas simples para decidir si bloquear, pedir información o avanzar.

## Fase 2 — Implementación mínima V1
Esta fase está iniciada y validada en su primera versión.

Ya existe:
- Script local de validación.
- Ejecución sin argumentos usando el JSON ficticio por defecto.
- Ejecución con ruta explícita al JSON.
- Carga de datos desde JSON ficticio.
- Validación de secciones principales.
- Validación de campos mínimos del cliente.
- Revisión de documentación recibida, pendiente e incompleta.
- Revisión del checklist.
- Detección de pendientes y bloqueos.
- Decisión recomendada de revisión humana por consola.
- Códigos de salida para ejecución correcta y errores controlados.

Validación completada:
- Ejecución sin argumento: OK.
- Ejecución con ruta explícita al JSON: OK.
- Ruta inexistente: error controlado.
- JSON válido con estructura incompleta: error controlado.
- Pruebas `unittest`: 4 tests OK.

La Fase 2 no convierte el agente en producto terminado. El alcance sigue limitado a validación local de datos ficticios.

## Fase 3 — Validación interna
Esta fase queda completada para la V1 mínima actual.

Validaciones realizadas:
- El script se ejecuta desde la raíz del repositorio.
- El JSON ficticio se carga correctamente.
- El informe por consola es comprensible.
- Los bloqueos se detectan correctamente.
- La decisión recomendada coincide con los datos ficticios.
- No se usan dependencias externas.
- No se usan datos reales.

## Fase 4 — V2 futura
La V2 sigue siendo futura y debe documentarse antes de cualquier integración.

Podría explorar:
- Formularios de entrada.
- Registro operativo en herramientas externas.
- Generación documental.
- Organización documental.
- Dashboard.
- Integración con Google Workspace.
- API.
- Asistencia con IA.

Nada de lo anterior está implementado actualmente.

## Fuera de alcance actual
- IA funcional.
- Google Workspace.
- Dashboard.
- API.
- Base de datos.
- Automatización productiva.
- Integración real con clientes.
- Decisiones sin revisión humana.
- Datos reales o sensibles.
- Producción real.
- CRM completo.
- ERP.

## Criterios para considerar cerrada la V1 mínima actual
- Existe script local funcional.
- Existen datos ficticios de ejemplo.
- Existen pruebas básicas.
- Las pruebas actuales pasan correctamente.
- Los errores principales están cubiertos.
- La documentación refleja el alcance real.
- No se declaran integraciones inexistentes.

## Próximos pasos inmediatos
1. Mejorar casos de prueba si aparecen nuevas reglas o variantes de expediente.
2. Separar reglas de validación si crece la lógica del script.
3. Preparar una posible V2 documental antes de integrar Google Workspace.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
