# Tablero Operativo Ficticio

## Propósito

Mostrar un ejemplo ficticio de tablero operativo para comprobar si la información mínima de una PYME queda suficientemente ordenada.

## Estado actual

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Tablero funcional real: no implementado todavía.
- Automatización real: no implementada todavía.

## Advertencia sobre datos ficticios

Este tablero no representa un dashboard funcional. Es un caso técnico ficticio, útil solo para documentación, validación manual y portfolio.

## Contexto ficticio de empresa

La empresa ficticia es una PYME de servicios técnicos internos llamada NexoSur Servicios Técnicos, S.L. Gestiona incidencias, entregas, validaciones, solicitudes internas y cierres semanales con un equipo pequeño y carga variable.

## Criterios operativos

- Cada tarea debe tener identificador, estado, prioridad y responsable.
- Cada tarea debe asociarse a un proceso operativo.
- Si existe bloqueo, debe ser visible y tener responsable de revisión.
- Las acciones siguientes deben indicar el próximo paso.
- Las revisiones operativas deben cerrar o reorientar la tarea.

## Procesos operativos

- PO-001 Gestión de incidencias internas.
- PO-002 Validación y cierre documental.
- PO-003 Seguimiento de proveedores.
- PO-004 Coordinación de tareas recurrentes.

## Tareas ficticias

1. TO-001, revisar retraso en la entrega del informe semanal.
- Estado: pendiente.
- Prioridad: alta.
- Proceso: PO-002.
- Responsable: Laura.
- Bloqueo: ninguno registrado.
- Observación: falta confirmar la fecha de recepción de datos.

2. TO-002, actualizar el procedimiento de alta de incidencias.
- Estado: en_progreso.
- Prioridad: media.
- Proceso: PO-001.
- Responsable: Sergio.
- Bloqueo: ninguno registrado.
- Observación: se está revisando la versión base con el equipo técnico.

3. TO-003, validar la devolución pendiente de un proveedor.
- Estado: en_revision.
- Prioridad: alta.
- Proceso: PO-003.
- Responsable: Marta.
- Bloqueo: BLQ-001.
- Observación: falta confirmación formal del proveedor.

4. TO-004, resolver el acceso bloqueado al gestor de tickets.
- Estado: bloqueada.
- Prioridad: alta.
- Proceso: PO-001.
- Responsable: Javier.
- Bloqueo: BLQ-002.
- Observación: el acceso depende de una validación externa.

5. TO-005, cerrar la consolidación del informe mensual operativo.
- Estado: completada.
- Prioridad: media.
- Proceso: PO-002.
- Responsable: Nerea.
- Bloqueo: ninguno registrado.
- Observación: la revisión final quedó documentada.

6. TO-006, descartar un duplicado de solicitud de compra menor.
- Estado: descartada.
- Prioridad: baja.
- Proceso: PO-004.
- Responsable: Lucía.
- Bloqueo: ninguno registrado.
- Observación: era una repetición de una solicitud ya aprobada.

7. TO-007, preparar el plan de guardias del mes siguiente.
- Estado: pendiente.
- Prioridad: media.
- Proceso: PO-004.
- Responsable: Andrés.
- Bloqueo: BLQ-003.
- Observación: falta acuerdo sobre disponibilidad.

## Bloqueos detectados

- BLQ-001: falta confirmación formal del proveedor para cerrar TO-003.
- BLQ-002: acceso no habilitado al gestor de tickets para continuar TO-004.
- BLQ-003: ausencia de fecha aprobada para el plan de guardias de TO-007.

## Acciones siguientes

- AS-001: solicitar confirmación al proveedor para liberar TO-003.
- AS-002: revisar permisos de acceso del gestor de tickets para liberar TO-004.
- AS-003: coordinar fecha de guardias con el equipo responsable de TO-007.
- AS-004: cerrar la validación documental del informe mensual de TO-005.
- AS-005: registrar la versión final del procedimiento de incidencias de TO-002.

## Revisiones operativas

- RV-001: revisar si TO-003 puede avanzar o necesita información adicional.
- RV-002: revisar si TO-004 debe mantenerse bloqueada o escalarse.
- RV-003: confirmar que TO-005 puede darse por estable y cerrada.

## Resultado esperado

El tablero debe permitir detectar qué tareas avanzan, cuáles están bloqueadas y qué revisión humana falta para mantener control operativo sin automatización real.

## Limitaciones

- No existe dashboard funcional.
- No existe automatización real.
- No existe integración con Google Workspace.
- No existe ERP.
- No existe CRM.
- No existe API.
- No existe IA funcional.

## Evolución posible V2 (*Version 2 – Versión 2*)

- Añadir filtros y vistas por área.
- Introducir métricas operativas.
- Añadir seguimiento temporal de bloqueos.
- Preparar un dashboard funcional cuando exista una implementación real.

## Criterios de validación

- Deben existir tareas en distintos estados.
- Debe haber bloqueos visibles y coherentes.
- Las acciones siguientes deben estar ligadas a tareas concretas.
- Las revisiones operativas deben justificar decisiones humanas.
- El tablero debe coincidir con el modelo de datos y el caso de uso.

## Próximos pasos

- Usar este tablero como referencia para la validación manual.
- Mantenerlo como ejemplo ficticio, no como herramienta operativa real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
