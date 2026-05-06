# Caso de Uso

## Propósito del documento

Describir un caso ficticio realista para validar la documentación V1 (*Version 1 – Versión 1*) del Agente de Revisión y Cumplimiento para PYMES.

## Estado del caso de uso

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Automatización real: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial

Una PYME de servicios quiere ordenar revisiones internas básicas sobre documentación, protección de datos, procesos, proveedores, permisos, evidencias y acciones pendientes. Lo hace sin sustituir asesoría profesional.

## Situación inicial sin agente

Antes del agente, los controles se revisan de forma dispersa, los documentos pendientes no siempre quedan priorizados y los hallazgos se tratan por correo o en notas sueltas.

## Objetivo del caso de uso

Ordenar la revisión interna mediante una base documental que permita clasificar controles, registrar evidencias, identificar hallazgos y dejar trazabilidad suficiente para revisión humana.

## Actores implicados

- Responsable de operaciones.
- Coordinación administrativa.
- Persona que recopila evidencias.
- Persona que revisa hallazgos.
- Dirección de la PYME como observadora del estado general.

## Flujo funcional previsto

1. Se registra un control interno con datos mínimos.
2. Se vinculan evidencias y documentos pendientes.
3. Se clasifican hallazgos y riesgos operativos.
4. Se asigna prioridad de revisión.
5. Se propone una acción de seguimiento.
6. Una persona valida el resultado y decide si avanza, si pide información o si bloquea el control.

## Datos mínimos del caso

- Identificador de control.
- Nombre del control.
- Área de control.
- Descripción del control.
- Tipo de control.
- Estado del control.
- Prioridad de revisión.
- Responsable interno.
- Fecha de revisión prevista.
- Observaciones del control.

## Tipos de control interno

- documental.
- datos_personales.
- proveedores.
- permisos.
- proceso_interno.
- seguridad_basica.
- formacion.

## Estados de revisión

- pendiente.
- en_revision.
- revisado.
- bloqueado.
- descartado.

## Clasificación de hallazgos

- Hallazgos de baja prioridad operativa.
- Hallazgos con necesidad de revisión manual.
- Hallazgos bloqueantes para el control.
- Hallazgos descartados por duplicidad o falta de encaje.
- Hallazgos que requieren seguimiento documental.

## Resultado esperado en V1

La V1 debe dejar un caso de uso suficientemente claro para demostrar que una PYME puede ordenar su revisión interna sin software real, pero con una estructura de datos, estados y revisiones manuales coherente.

## Evolución V2 futura

- Entrada estructurada desde formularios.
- Seguimiento más fino por área.
- Métricas de carga operativa.
- Dashboard funcional.
- Integraciones externas cuando exista una base técnica estable.

## Fuera de alcance inicial

- Revisión automática real.
- Motor normativo.
- Google Workspace.
- ERP.
- CRM.
- API.
- IA funcional.
- Decisión autónoma.
- Asesoramiento legal, fiscal, laboral, financiero o regulatorio.
- Garantía de cumplimiento normativo.
- Afirmaciones de que evita sanciones, riesgos legales o incumplimientos.

## Criterios de validación funcional

- El caso de uso debe poder explicarse sin ambigüedad.
- El control debe tener estado, prioridad y responsable.
- Los hallazgos deben ser visibles y revisables.
- La clasificación debe ser comprensible para un equipo no técnico.
- La revisión ficticia debe reflejar la misma lógica que este caso de uso.

## Próximos pasos

- Verificar que los datos de ejemplo respetan este caso ficticio.
- Mantener la validación humana como punto de control.
- Decidir más adelante si la V1 pasa a implementación mínima o si se prioriza una revisión global del repositorio y la actualización de `README.md` y `CATALOGO.md` raíz cuando corresponda.

## Aviso de límites profesionales

Este agente no es asesoría legal, fiscal, laboral, financiera ni regulatoria. Tampoco garantiza cumplimiento normativo ni evita sanciones, riesgos legales o incumplimientos.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
