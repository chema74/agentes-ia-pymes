# Flujo de Validación Manual del Agente de Onboarding Inteligente para PYMES

## Propósito del documento
Este documento define un flujo mínimo para revisar manualmente si un expediente inicial de cliente está suficientemente preparado para avanzar. No describe una automatización implementada, sino un procedimiento operativo para validar la V1 (*Version 1 – Versión 1*).

## Estado actual
- Estado documental: flujo mínimo de validación para V1.
- Código funcional: no implementado todavía.
- Automatización del flujo: no implementada todavía.
- Integraciones activas: no implementadas todavía.
- Dashboard: no implementado todavía.
- IA funcional: no implementada todavía.

## Criterio general del flujo
El flujo debe ser:
- Simple.
- Repetible.
- Revisable.
- Aplicable a datos ficticios.
- Útil para detectar bloqueos.
- Fácil de convertir después en reglas, formulario o dashboard.

## Entradas necesarias para validar
Las entradas mínimas son:
- Datos básicos del cliente.
- Servicio solicitado.
- Necesidad principal.
- Documentación recibida.
- Documentación pendiente.
- Checklist de onboarding.
- Clasificación inicial.
- Observaciones internas.
- Acciones siguientes.

Estas entradas pueden proceder del expediente ficticio de cliente.

## Salida esperada del flujo
- Onboarding preparado para avanzar: el expediente tiene la información mínima suficiente para seguir.
- Onboarding pendiente de información: faltan datos o documentos que impiden cerrar la revisión.
- Onboarding bloqueado: existe una condición que impide avanzar hasta resolver una incidencia.
- Onboarding no aplicable al flujo actual: el caso no encaja en el proceso previsto y debe revisarse aparte.

## Estados operativos del onboarding
- recibido: el expediente o la información inicial ha llegado al proceso.
- en_revision: el caso está siendo revisado por una persona interna.
- pendiente_informacion: faltan datos o documentos relevantes.
- preparado_para_avanzar: el expediente cumple las condiciones mínimas para seguir.
- bloqueado: existe un impedimento claro que frena el avance.
- descartado: el caso no sigue en este flujo por decisión justificada.

## Paso 1 — Confirmar identificación del cliente
Se revisa:
- Nombre del cliente.
- Empresa.
- Persona de contacto.
- Correo.
- Teléfono.
- Fecha de entrada.
- Responsable interno.

Criterios de validación:
- Si falta información crítica, el estado pasa a pendiente_informacion.
- Si no hay responsable interno, no debe avanzar.
- Si todo está completo, pasa al siguiente paso.

## Paso 2 — Revisar servicio solicitado
Se revisa:
- Tipo de servicio solicitado.
- Necesidad principal.
- Objetivo inicial.
- Urgencia.
- Complejidad.
- Alcance preliminar.

Criterios de validación:
- Si el servicio no se entiende, el onboarding queda pendiente.
- Si la necesidad principal es ambigua, requiere revisión humana.
- Si el servicio está claro, pasa al siguiente paso.

## Paso 3 — Revisar documentación inicial
Se revisa:
- Documentos recibidos.
- Documentos pendientes.
- Documentos incompletos.
- Observaciones documentales.
- Posibles bloqueos.

Criterios de validación:
- Si falta documentación obligatoria, el estado pasa a pendiente_informacion o bloqueado.
- Si la documentación es suficiente para iniciar, pasa al siguiente paso.
- Si hay dudas, debe quedar anotada revisión humana.

## Paso 4 — Aplicar checklist de onboarding
Se revisa el estado de los ítems del checklist:
- pendiente
- completo
- bloqueado
- no_aplica

Criterios de validación:
- Si hay ítems obligatorios pendientes, no debe avanzar.
- Si hay ítems bloqueados, debe indicarse motivo.
- Si los ítems obligatorios están completos o justificados, pasa al siguiente paso.

## Paso 5 — Revisar clasificación inicial
Se revisa:
- Tipo de cliente.
- Complejidad inicial.
- Urgencia.
- Información completa o incompleta.
- Necesidad de revisión previa.
- Criterio de clasificación.

En V1 la clasificación es manual o por reglas simples, no generada por IA (*Artificial Intelligence – Inteligencia Artificial*) funcional.

Criterios de validación:
- Si no existe clasificación, debe completarse antes de avanzar.
- Si la complejidad es alta, requiere revisión humana.
- Si la clasificación es clara, pasa al siguiente paso.

## Paso 6 — Definir acciones siguientes
Se revisa:
- Próxima acción.
- Responsable.
- Prioridad.
- Estado.
- Fecha prevista ficticia o estimada.
- Observaciones.

Criterios de validación:
- Si no hay próxima acción, el expediente no está preparado.
- Si no hay responsable, el expediente no debe avanzar.
- Si hay acción clara y responsable asignado, pasa al cierre.

## Paso 7 — Decisión final de revisión humana
Posibles decisiones:
- avanzar: el expediente puede pasar al siguiente paso.
- pedir_informacion: faltan datos o documentos que deben completarse.
- bloquear: existe un impedimento que frena el avance.
- descartar: el caso no sigue en este flujo.
- revisar_de_nuevo: el expediente requiere una segunda revisión.

Ninguna decisión debe tomarse de forma automática en esta V1.

## Reglas mínimas de validación
- Un cliente sin correo o teléfono no debe avanzar.
- Un cliente sin responsable interno no debe avanzar.
- Un servicio no identificado bloquea el flujo.
- Un checklist con obligatorios pendientes no debe marcarse como preparado.
- Una documentación crítica pendiente debe quedar registrada.
- Toda clasificación inicial debe poder explicarse.
- Toda salida debe incluir una próxima acción.

## Aplicación al expediente ficticio
Este flujo debe aplicarse al documento `EXPEDIENTE_CLIENTE_FICTICIO.md` revisando:
- Datos básicos.
- Documentos recibidos y pendientes.
- Checklist aplicado.
- Clasificación inicial.
- Acciones siguientes.
- Decisión final.

No es necesario reescribir todo el expediente; solo validar que el caso cumple el flujo previsto.

## Datos fuera de alcance en este flujo
- Datos bancarios.
- Credenciales.
- Contratos reales sensibles.
- Información médica.
- Información legal compleja.
- Datos fiscales sensibles.
- Documentación confidencial de clientes reales.
- Firmas digitales.

La validación debe hacerse con datos ficticios o no sensibles.

## Evolución posible en V2
Posibles mejoras futuras:
- Conversión del flujo a reglas automáticas.
- Uso de Google Forms para entrada.
- Uso de Google Sheets para seguimiento.
- Dashboard de estados.
- Alertas de bloqueos.
- Generación documental.
- Clasificación asistida con IA.
- Integración futura con CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*).

Estas opciones no están implementadas todavía.

## Criterios de validación del flujo
- ¿El flujo permite revisar un expediente ficticio?
- ¿Los pasos son claros?
- ¿Las decisiones finales están definidas?
- ¿Se detectan bloqueos?
- ¿Existe revisión humana?
- ¿Se evita automatizar decisiones sensibles?
- ¿No se promete automatización inexistente?

## Próximos pasos
1. Preparar una primera estructura de datos de ejemplo para la V1.
2. Revisar si el README del agente debe enlazar los nuevos documentos V1.
3. Preparar después una revisión documental final del agente 01 antes de abrir código.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
