# Pipeline Comercial Ficticio

## Propósito

Mostrar un ejemplo ficticio de pipeline comercial para comprobar si la información mínima de una PYME queda suficientemente ordenada.

## Estado actual

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Pipeline funcional real: no implementado todavía.
- Automatización real: no implementada todavía.

## Advertencia sobre datos ficticios

Este pipeline no representa un CRM funcional. Es un caso técnico ficticio, útil solo para documentación, validación manual y portfolio.

## Contexto ficticio de empresa

La empresa ficticia es una PYME de servicios llamada NexoSur Soluciones Comerciales, S.L. Gestiona oportunidades de diagnóstico, propuesta, negociación y cierre con un equipo pequeño y carga variable.

## Criterios de seguimiento comercial

- Cada oportunidad debe tener identificador, fase, estado, temperatura y responsable.
- Cada oportunidad debe registrar interacción o próxima acción.
- Si existe bloqueo, debe ser visible y tener responsable de revisión.
- La prioridad debe reflejar el seguimiento operativo, no una promesa de conversión.
- La clasificación comercial debe ser revisable por una persona.

## Oportunidades ficticias

1. OPO-001, renovación de soporte anual.
- Fase: primer_contacto.
- Estado: abierta.
- Temperatura: templada.
- Prioridad: alta.
- Responsable: Laura.

2. OPO-002, implantación de servicio recurrente.
- Fase: diagnostico.
- Estado: en_revision.
- Temperatura: caliente.
- Prioridad: alta.
- Responsable: Sergio.

3. OPO-003, propuesta para mejora interna.
- Fase: propuesta.
- Estado: abierta.
- Temperatura: templada.
- Prioridad: media.
- Responsable: Marta.

4. OPO-004, negociación de alcance ampliado.
- Fase: negociacion.
- Estado: bloqueada.
- Temperatura: critica.
- Prioridad: alta.
- Responsable: Javier.

5. OPO-005, espera de decisión de dirección.
- Fase: pendiente_decision.
- Estado: abierta.
- Temperatura: caliente.
- Prioridad: alta.
- Responsable: Nerea.

6. OPO-006, cierre de oferta de soporte.
- Fase: ganada.
- Estado: ganada.
- Temperatura: caliente.
- Prioridad: media.
- Responsable: Lucía.

7. OPO-007, oportunidad descartada por falta de encaje.
- Fase: perdida.
- Estado: perdida.
- Temperatura: fria.
- Prioridad: baja.
- Responsable: Sergio.

8. OPO-008, oportunidad pendiente de segunda llamada.
- Fase: diagnostico.
- Estado: abierta.
- Temperatura: templada.
- Prioridad: media.
- Responsable: Laura.

## Interacciones comerciales ficticias

- INT-001: llamada inicial sobre OPO-001.
- INT-002: correo de diagnóstico para OPO-002.
- INT-003: reunión de propuesta para OPO-003.
- INT-004: intercambio de correos de negociación para OPO-004.
- INT-005: llamada de seguimiento para OPO-005.
- INT-006: cierre confirmatorio de OPO-006.
- INT-007: correo de descarte para OPO-007.
- INT-008: llamada de repaso para OPO-008.

## Bloqueos detectados

- BLQ-001: falta confirmación interna para avanzar OPO-004.
- BLQ-002: falta decisión formal de dirección para OPO-005.
- BLQ-003: falta encaje de servicio para OPO-007 ya descartada.

## Acciones siguientes

- AS-001: solicitar confirmación de alcance para OPO-004.
- AS-002: pedir decisión final sobre OPO-005.
- AS-003: registrar cierre documental de OPO-006.
- AS-004: cerrar seguimiento de OPO-007.
- AS-005: realizar segunda llamada de diagnóstico para OPO-008.

## Clasificaciones comerciales

- CLAS-001: OPO-001 como templada y prioritaria.
- CLAS-002: OPO-002 como caliente y en revisión.
- CLAS-003: OPO-004 como crítica y bloqueada.
- CLAS-004: OPO-006 como caliente y ganada.
- CLAS-005: OPO-007 como fría y perdida.

## Resultado esperado

El pipeline debe permitir detectar qué oportunidades avanzan, cuáles están bloqueadas, cuáles no tienen próxima acción y qué revisión humana falta para mantener control comercial sin automatización real.

## Limitaciones

- No existe CRM funcional.
- No existe automatización comercial real.
- No existe scoring automático.
- No existe dashboard funcional.
- No existe Google Workspace.
- No existe API.
- No existe IA funcional.

## Evolución posible V2

- Añadir filtros y vistas por fase.
- Introducir métricas operativas.
- Añadir seguimiento temporal de bloqueos.
- Preparar un dashboard funcional cuando exista una implementación real.

## Criterios de validación

- Deben existir oportunidades en distintas fases.
- Deben existir bloqueos visibles y coherentes.
- Las acciones siguientes deben estar ligadas a oportunidades concretas.
- Las clasificaciones comerciales deben justificar decisiones humanas.
- El pipeline debe coincidir con el modelo de datos y el caso de uso.

## Próximos pasos

- Usar este pipeline como referencia para la validación manual.
- Mantenerlo como ejemplo ficticio, no como herramienta comercial real.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
