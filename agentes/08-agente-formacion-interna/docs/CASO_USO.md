# Caso de Uso

## Propósito del documento

Describir un caso ficticio realista para validar la documentación V1 (*Version 1 – Versión 1*) del Agente de Formación Interna para PYMES.

## Estado del caso de uso

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Automatización real: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial

Una PYME de servicios necesita ordenar formación interna sobre procesos, herramientas, atención al cliente, documentación interna y buenas prácticas. Los materiales están dispersos y los empleados tienen niveles distintos.

## Situación inicial sin agente

Antes del agente, los contenidos se almacenan en carpetas, correos o mensajes dispersos. No existe una visión clara de qué rutas están pendientes, qué módulos faltan o qué perfiles requieren refuerzo.

## Objetivo del caso de uso

Ordenar la operativa formativa mediante una base documental que permita clasificar rutas, asociar módulos, registrar evidencias y dejar trazabilidad suficiente para revisión humana.

## Actores implicados

- Responsable de formación.
- Coordinación interna.
- Persona que crea o revisa contenido.
- Persona que consume la formación.
- Dirección de la PYME como observadora del estado general.

## Flujo funcional previsto

1. Se registra una ruta formativa con datos mínimos.
2. Se vincula la ruta a un perfil interno.
3. Se asignan módulos, evidencias y prioridad.
4. Se revisan contenidos pendientes y bloqueos.
5. Se propone una acción siguiente.
6. Una persona valida el resultado y decide si avanza, si pide información o si bloquea la ruta.

## Datos mínimos del caso

- Identificador de ruta.
- Nombre de la ruta.
- Perfil destinatario.
- Objetivo formativo.
- Estado de la ruta.
- Prioridad.
- Responsable interno.
- Fecha de revisión prevista.
- Observaciones de contexto.

## Estados de módulo formativo

- pendiente.
- en_revision.
- disponible.
- bloqueado.
- completado.
- descartado.

## Estados de ruta formativa

- pendiente.
- en_revision.
- activa.
- bloqueada.
- completada.
- descartada.

## Clasificación formativa prevista

- Rutas iniciales para perfiles nuevos.
- Rutas de refuerzo para perfiles con necesidades detectadas.
- Rutas activas con módulos disponibles.
- Rutas bloqueadas por contenido pendiente.
- Rutas completadas para cierre documental.
- Rutas descartadas por falta de encaje o duplicidad.

## Resultado esperado en V1

La V1 debe dejar un caso de uso suficientemente claro para demostrar que una PYME puede ordenar su formación interna sin plataforma real, pero con una estructura de datos, estados y revisiones manuales coherente.

## Evolución V2 futura

- Entrada estructurada desde formularios.
- Seguimiento más fino por área o perfil.
- Métricas de carga operativa.
- Dashboard funcional.
- Integraciones externas cuando exista una base técnica estable.

## Fuera de alcance inicial

- LMS real.
- Automatización formativa real.
- Google Workspace.
- CRM.
- API.
- IA funcional.
- Decisión autónoma.
- Promesas de mejora garantizada o métricas de aprendizaje no verificadas.

## Criterios de validación funcional

- El caso de uso debe poder explicarse sin ambigüedad.
- La ruta debe tener estado, prioridad y responsable.
- Los módulos deben ser visibles y revisables.
- La clasificación debe ser comprensible para un equipo no técnico.
- El plan ficticio debe reflejar la misma lógica que este caso de uso.

## Próximos pasos

- Verificar que los datos de ejemplo respetan este caso ficticio.
- Mantener la revisión humana como punto de control.
- Decidir más adelante si la V1 pasa a implementación mínima o si se prioriza el siguiente agente del catálogo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
