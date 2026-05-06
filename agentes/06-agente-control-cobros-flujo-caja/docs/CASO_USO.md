# Caso de Uso

## Propósito del documento

Describir un caso ficticio realista para validar la documentación V1 (*Version 1 – Versión 1*) del Agente de Control de Cobros y Flujo de Caja para PYMES.

## Estado del caso de uso

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Automatización real: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial

Una PYME de servicios gestiona cobros pendientes mediante hojas sueltas, correos, notas y revisión manual de vencimientos. No dispone de una visión operativa clara sobre lo pendiente, lo retrasado o lo prioritario.

## Situación inicial sin agente

Antes del agente, los cobros se revisan de forma dispersa, las referencias no siempre están unificadas y los vencimientos se consultan manualmente. Eso dificulta ver el riesgo de retraso y las acciones de seguimiento más urgentes.

## Objetivo del caso de uso

Ordenar la operativa de cobros mediante una base documental que permita clasificar vencimientos, asociar riesgos, registrar acciones de seguimiento y dejar trazabilidad suficiente para revisión humana.

## Actores implicados

- Responsable administrativo.
- Coordinación de operaciones.
- Persona que revisa vencimientos.
- Persona que hace seguimiento de cobros.
- Dirección de la PYME como observadora del estado general.

## Flujo funcional previsto

1. Se registra un cobro pendiente con datos mínimos.
2. Se vincula el cobro a una referencia ficticia.
3. Se asigna un estado y una prioridad de seguimiento.
4. Se revisa el vencimiento y el riesgo de retraso.
5. Se propone una acción de seguimiento.
6. Una persona valida el resultado y decide si avanza, si pide información o si bloquea el cobro.

## Datos mínimos del caso

- Identificador de cobro.
- Nombre del cliente.
- Nombre de la empresa.
- Concepto del cobro.
- Importe previsto.
- Fecha de emisión.
- Fecha de vencimiento.
- Estado del cobro.
- Prioridad de seguimiento.
- Responsable interno.
- Riesgo de retraso.
- Observaciones internas.

## Estados de cobro previstos

- pendiente.
- en_revision.
- vencido.
- cobrado.
- parcialmente_cobrado.
- bloqueado.
- descartado.

## Estados de acción previstos

- pendiente.
- en_revision.
- completada.
- bloqueada.
- descartada.

## Clasificación operativa prevista

- Cobros próximos a vencimiento con seguimiento preventivo.
- Cobros vencidos que requieren revisión prioritaria.
- Cobros parcialmente cobrados con registro de pendiente restante.
- Cobros bloqueados por dependencia interna o externa.
- Cobros ya cobrados para cierre documental.
- Cobros descartados por duplicidad o falta de encaje.

## Resultado esperado en V1

La V1 debe dejar un caso de uso suficientemente claro para demostrar que una PYME puede ordenar cobros y previsión operativa sin software real, pero con una estructura de datos, estados y revisiones manuales coherente.

## Evolución V2 futura

- Entrada estructurada desde formularios.
- Seguimiento más fino por cliente o área.
- Métricas de carga operativa.
- Dashboard funcional.
- Integraciones externas cuando exista una base técnica estable.

## Fuera de alcance inicial

- Automatización real.
- Gestión bancaria conectada.
- Google Workspace.
- ERP.
- CRM.
- API.
- Conexión bancaria.
- Facturación real.
- IA funcional.
- Decisión autónoma.
- Asesoramiento financiero, fiscal, contable o legal.

## Criterios de validación funcional

- El caso de uso debe poder explicarse sin ambigüedad.
- El cobro debe tener estado, prioridad y responsable.
- Los riesgos deben ser visibles y revisables.
- La clasificación debe ser comprensible para un equipo no técnico.
- La cartera ficticia debe reflejar la misma lógica que este caso de uso.

## Próximos pasos

- Verificar que los datos de ejemplo respetan este caso ficticio.
- Mantener la revisión humana como punto de control.
- Decidir más adelante si la V1 pasa a implementación mínima o si se prioriza el siguiente agente del catálogo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
