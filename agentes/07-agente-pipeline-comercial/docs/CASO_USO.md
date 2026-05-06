# Caso de Uso

## Propósito del documento

Describir un caso ficticio realista para validar la documentación V1 (*Version 1 – Versión 1*) del Agente de Pipeline Comercial para PYMES.

## Estado del caso de uso

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Automatización real: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial

Una PYME de servicios gestiona oportunidades comerciales mediante correos, llamadas, notas y hojas sueltas. No dispone de una visión clara de fases, temperatura, bloqueos o próximas acciones.

## Situación inicial sin agente

Antes del agente, las oportunidades se registran de forma dispersa, las fases no siempre coinciden entre personas y la priorización depende de memoria o seguimiento manual poco consistente.

## Objetivo del caso de uso

Ordenar la operativa comercial mediante una base documental que permita clasificar oportunidades, registrar interacciones, identificar bloqueos y dejar trazabilidad suficiente para revisión humana.

## Actores implicados

- Responsable comercial.
- Coordinación de ventas.
- Persona que registra interacciones.
- Persona que revisa el avance.
- Dirección de la PYME como observadora del estado general.

## Flujo funcional previsto

1. Se registra una oportunidad comercial con datos mínimos.
2. Se vincula la oportunidad a una fase comercial.
3. Se asigna temperatura y prioridad.
4. Se revisan interacciones, bloqueos y próxima acción.
5. Se propone una clasificación comercial.
6. Una persona valida el resultado y decide si avanza, si pide información o si bloquea la oportunidad.

## Datos mínimos del caso

- Identificador de oportunidad.
- Nombre del cliente.
- Nombre de la empresa.
- Servicio de interés.
- Fase comercial.
- Estado de la oportunidad.
- Temperatura comercial.
- Prioridad de seguimiento.
- Responsable interno.
- Fecha de última interacción.
- Próxima acción.
- Bloqueo asociado.
- Observaciones internas.

## Estados de oportunidad previstos

- abierta.
- en_revision.
- bloqueada.
- ganada.
- perdida.
- descartada.

## Fases comerciales previstas

- primer_contacto.
- diagnostico.
- propuesta.
- negociacion.
- pendiente_decision.
- ganada.
- perdida.

## Clasificación comercial prevista

- Oportunidades frías con poco avance.
- Oportunidades templadas con revisión activa.
- Oportunidades calientes con seguimiento prioritario.
- Oportunidades críticas con bloqueo o decisión pendiente.
- Oportunidades ganadas para cierre documental.
- Oportunidades perdidas o descartadas por falta de encaje.

## Resultado esperado en V1

La V1 debe dejar un caso de uso suficientemente claro para demostrar que una PYME puede ordenar su pipeline comercial sin software real, pero con una estructura de datos, estados y revisiones manuales coherente.

## Evolución V2 futura

- Entrada estructurada desde formularios.
- Seguimiento más fino por fase o segmento.
- Métricas de carga operativa.
- Dashboard funcional.
- Integraciones externas cuando exista una base técnica estable.

## Fuera de alcance inicial

- CRM real.
- Automatización comercial real.
- Scoring automático.
- Google Workspace.
- API.
- IA funcional.
- Decisión autónoma.
- Asesoramiento comercial garantizado o métricas de conversión no verificadas.

## Criterios de validación funcional

- El caso de uso debe poder explicarse sin ambigüedad.
- La oportunidad debe tener fase, temperatura y responsable.
- Los bloqueos deben ser visibles y revisables.
- La clasificación debe ser comprensible para un equipo no técnico.
- El pipeline ficticio debe reflejar la misma lógica que este caso de uso.

## Próximos pasos

- Verificar que los datos de ejemplo respetan este caso ficticio.
- Mantener la revisión humana como punto de control.
- Decidir más adelante si la V1 pasa a implementación mínima o si se prioriza el siguiente agente del catálogo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
