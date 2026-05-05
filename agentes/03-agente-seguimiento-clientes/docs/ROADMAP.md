# Roadmap del Agente de Seguimiento de Clientes para PYMES

## Propósito del documento

Este documento define la evolución prevista del Agente de Seguimiento de Clientes para PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*) por fases. Su objetivo es diferenciar la documentación inicial, el diseño mínimo, la implementación futura, la validación interna y las posibles mejoras posteriores.

El roadmap no presenta el agente como terminado. Sirve como planificación técnica para ordenar el trabajo, mantener límites claros y evitar prometer capacidades que todavía no existen.

## Estado actual

- Estado documental: en desarrollo inicial.
- Estado técnico: pendiente de implementación.
- Código funcional: no implementado todavía.
- Automatizaciones: no implementadas todavía.
- Recordatorios automáticos: no implementados todavía.
- Integraciones activas: no implementadas todavía.
- Dashboard: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.
- Última fase completada: documentación base en preparación.
- Próxima fase prevista: definición del modelo conceptual mínimo de datos para la V1.

## Fase 0 — Base documental

Esta fase sirve para definir el problema de seguimiento, el alcance y la estructura del agente antes de crear código. El objetivo es dejar claro qué problema operativo se quiere resolver, qué límites tiene el agente y qué evidencias documentales sostienen el caso de portfolio.

Entregables:

- README del agente.
- Arquitectura conceptual.
- Caso de uso funcional.
- Roadmap.
- Límites de alcance.
- Criterios de validación.

Esta fase no implica código funcional, automatizaciones reales, dashboard, integración con Google Workspace, CRM ni IA funcional implementada.

## Fase 1 — Definición de V1 implementable

Esta fase debe convertir la documentación en un diseño mínimo que pueda implementarse después. La V1 (*Version 1 – Versión 1*) debe ser pequeña, verificable y centrada en el seguimiento operativo básico de clientes.

Entregables previstos:

- Modelo conceptual mínimo de datos.
- Estados de cliente.
- Estados de acción.
- Cartera ficticia de clientes.
- Flujo de seguimiento manual.
- Reglas simples para detectar clientes sin próxima acción.
- Reglas simples para detectar bloqueos.
- Reglas simples para detectar riesgo operativo.
- Criterios de revisión humana.

Esta fase todavía puede completarse sin automatización real. Su valor está en cerrar el diseño mínimo antes de decidir cualquier implementación.

## Fase 2 — Implementación mínima V1

Esta fase solo debe abrirse cuando la documentación y el diseño mínimo estén cerrados. La implementación debe limitarse a demostrar el flujo básico con datos ficticios, sin introducir complejidad innecesaria ni dependencias externas no justificadas.

Puede incluir:

- Script o lógica mínima para procesar datos ficticios de clientes.
- Validación de campos obligatorios.
- Detección de clientes sin próxima acción.
- Detección de clientes bloqueados.
- Detección de clientes en riesgo.
- Generación simple de informe por consola.
- Registro básico de estado de seguimiento.
- Documentación actualizada al cierre del bloque.

La implementación debe ser pequeña, verificable y sin sobreingeniería. No debe presentarse como un CRM completo, un dashboard funcional, una solución con recordatorios automáticos ni una automatización comercial en producción.

## Fase 3 — Validación interna

Esta fase sirve para probar el flujo de seguimiento con datos ficticios antes de ampliar el agente. El objetivo es comprobar si el diseño ayuda realmente a revisar clientes activos, detectar huecos de seguimiento y priorizar acciones.

Incluye:

- Prueba con cartera ficticia de clientes.
- Revisión de clientes activos.
- Revisión de clientes sin próxima acción.
- Revisión de clientes bloqueados.
- Revisión de clientes en riesgo.
- Revisión de acciones pendientes.
- Ajuste de documentación.
- Confirmación de límites de alcance.

No deben usarse datos reales de clientes en esta fase. La validación debe realizarse con información ficticia y controlada para evitar riesgos de privacidad, confidencialidad o interpretación comercial indebida.

## Fase 4 — V2 futura

La V2 (*Version 2 – Versión 2*) futura describe ampliaciones posibles si la V1 queda validada y existe una necesidad clara de evolucionar el agente. Esta fase no describe funcionalidades implementadas actualmente.

Posibles ampliaciones futuras:

- Registro operativo en Google Sheets.
- Captura de interacciones mediante Google Forms.
- Dashboard operativo.
- Alertas básicas por correo.
- Recordatorios de seguimiento.
- Integración futura con calendario.
- Priorización asistida mediante reglas.
- Resúmenes asistidos con IA.
- Integración futura con CRM.
- KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*) operativos de seguimiento.
- Posible API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) si el proyecto crece.

Estas funcionalidades no están implementadas todavía. Antes de abordarlas debería existir una validación interna suficiente de la V1 y una justificación técnica clara.

## Fase 5 — Integraciones avanzadas opcionales

Esta fase solo tendría sentido si la V1 y la V2 quedan validadas. Su objetivo sería conectar el agente con sistemas externos y mejorar la trazabilidad del seguimiento, siempre manteniendo controles de revisión humana.

Puede incluir:

- Conexión con CRM externo.
- Integración con Google Calendar.
- Integración con correo electrónico.
- Control de permisos.
- Historial de interacciones.
- Analítica básica.
- Automatizaciones controladas.
- Conectores externos.

Esta fase no pertenece al alcance inicial. Tampoco debe asumirse como necesaria hasta que exista una base funcional demostrada y un caso de uso suficientemente validado.

## Fuera de alcance inicial

Quedan fuera del alcance inicial:

- CRM completo en producción.
- Automatización comercial completa.
- Recordatorios automáticos reales.
- Dashboard funcional.
- Integración real con Google Workspace.
- Integración con correo real.
- Integración con calendario real.
- API pública.
- Multiempresa real.
- Decisiones comerciales sin revisión humana.
- Sustitución de gestión comercial o atención humana.
- Métricas de impacto no verificadas.
- Automatizaciones irreversibles.

Estos elementos pueden evaluarse en fases posteriores, pero no forman parte del estado actual ni de la primera definición implementable.

## Criterios para cerrar una fase

Preguntas de control:

- ¿La fase tiene entregables claros?
- ¿El resultado puede revisarse?
- ¿La documentación refleja el estado real?
- ¿No se han añadido promesas no implementadas?
- ¿La siguiente fase está justificada?
- ¿El agente sigue resolviendo un problema concreto de seguimiento?
- ¿La revisión humana está contemplada?

Una fase no debería cerrarse si existen ambigüedades relevantes sobre el alcance, el estado real o las capacidades implementadas.

## Criterios para activar la siguiente fase

Condiciones mínimas:

- Documentación base completa.
- Alcance V1 definido.
- Límites claros.
- Flujo de seguimiento mínimo comprensible.
- Riesgos principales identificados.
- Revisión humana contemplada.
- Validación interna realizada cuando proceda.

Activar una fase posterior sin cumplir estas condiciones aumentaría el riesgo de sobreingeniería o de presentar como implementadas capacidades que todavía son solo previsiones.

## Evidencias recomendadas para portfolio

Posibles evidencias futuras:

- README claro.
- Arquitectura explicada.
- Caso de uso realista.
- Roadmap transparente.
- Modelo de datos.
- Cartera ficticia de clientes.
- Datos de ejemplo si existen.
- Pruebas si hay implementación mínima.
- Capturas si en el futuro existe interfaz.
- Registro de cambios documentado.

Las evidencias solo deben añadirse cuando existan realmente. No deben incorporarse métricas, capturas, integraciones ni resultados que no hayan sido producidos o verificados.

## Próximos pasos inmediatos

1. Definir el modelo conceptual mínimo de datos para la V1.
2. Preparar una cartera ficticia de clientes.
3. Preparar después un flujo mínimo de validación de seguimiento manual.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
