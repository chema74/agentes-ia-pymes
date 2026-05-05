# Roadmap del Agente de Onboarding Inteligente para PYMES

## Propósito del documento
Este documento define la evolución prevista del agente por fases, diferenciando documentación, implementación mínima, validación interna y posibles mejoras futuras. Su función es servir como guía técnica progresiva sin presentar como implementado ningún elemento que todavía no exista.

El agente está orientado a PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*) que necesitan ordenar el alta inicial de clientes con datos ficticios, reglas simples y revisión humana.

## Estado actual
- Estado documental: base V1 (*Version 1 – Versión 1*) documentada.
- Estado técnico: implementación mínima V1 parcial iniciada.
- Código funcional: script local básico disponible.
- Script disponible: `src/validar_expediente.py`.
- Datos ficticios de ejemplo: disponibles.
- Automatizaciones: no implementadas todavía.
- Integraciones activas: no implementadas todavía.
- Dashboard: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.
- Base de datos: no implementada todavía.
- Última fase completada: documentación V1 y primera validación local con datos ficticios.
- Próxima fase prevista: crear prueba básica del script con datos ficticios.

## Fase 0 — Base documental
Esta fase sirve para definir el problema, el alcance y la estructura del agente antes de crear código.

Entregables:
- README del agente.
- Arquitectura conceptual.
- Caso de uso funcional.
- Roadmap.
- Límites de alcance.
- Criterios de validación.

Estado: completada para la base V1.

## Fase 1 — Definición de V1 implementable
Esta fase convierte la documentación en un diseño mínimo que puede implementarse de forma pequeña, local y verificable.

Entregables disponibles:
- Modelo conceptual mínimo de datos.
- Checklist inicial de onboarding.
- Ejemplo de expediente de cliente.
- Flujo básico de entrada y salida.
- Reglas simples de validación.
- Criterios de revisión humana.
- Datos de ejemplo en JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*).

Estado: preparada para la base V1.

## Fase 2 — Implementación mínima V1
Esta fase está iniciada parcialmente mediante un script local de validación.

Ya existe:
- Script local de validación.
- Carga de datos desde JSON ficticio.
- Validación de secciones principales.
- Validación de campos mínimos del cliente.
- Revisión de documentación recibida, pendiente e incompleta.
- Revisión de checklist.
- Detección de pendientes y bloqueos.
- Decisión recomendada de revisión humana por consola.

Todavía falta:
- Prueba básica automatizada.
- Mejorar separación de reglas si procede.
- Documentar criterios de ejecución.
- Mantener el alcance pequeño.

La implementación actual es parcial. No implica IA funcional, Google Workspace, dashboard, API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*), automatización productiva, integración real con clientes ni base de datos.

## Estado de la primera ejecución local
Con los datos ficticios disponibles, el resultado actual esperado es:

- Cliente ficticio: Laura Martín.
- Empresa ficticia: Taller Creativo Bahía, S. L.
- Estado del onboarding: en_revision.
- Documentos recibidos: 1.
- Documentos pendientes: 1.
- Documentos incompletos: 1.
- Ítems completos: 7.
- Ítems pendientes: 1.
- Ítems obligatorios pendientes: 2.
- Ítems bloqueados: 2.
- Decisión recomendada de revisión manual: bloquear.

Este resultado procede de datos ficticios. No implica automatización productiva, no sustituye revisión humana y solo valida la lógica mínima inicial.

## Fase 3 — Validación interna
Esta fase sirve para probar el flujo con datos de ejemplo antes de ampliar el agente.

Incluye:
- Prueba básica del script con un cliente ficticio.
- Revisión de campos completos y pendientes.
- Revisión del checklist.
- Confirmación de bloqueos detectados.
- Comparación de la decisión recomendada con los datos ficticios.
- Ajuste de documentación si la prueba detecta diferencias.
- Confirmación de límites de alcance.

No deben usarse datos reales sensibles en esta fase.

## Fase 4 — V2 futura
La V2 (*Version 2 – Versión 2*) representa una posible evolución posterior, no una funcionalidad implementada.

Posibles ampliaciones futuras:
- Entrada mediante Google Forms.
- Registro en Google Sheets.
- Generación documental con Google Docs.
- Organización de carpetas en Google Drive.
- Dashboard operativo.
- Alertas básicas por correo.
- Clasificación asistida con IA.
- Resumen operativo asistido.
- Integración futura con CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*).
- Posible API si el proyecto crece.

Estas funcionalidades no están implementadas todavía.

## Fase 5 — Integraciones avanzadas opcionales
Esta fase solo tendría sentido si la V1 y la V2 quedan validadas.

Puede incluir:
- Conexión con herramientas internas.
- Integración con CRM externo.
- Gestión documental avanzada.
- Control de permisos.
- Registro histórico.
- Analítica básica.
- Mejoras de experiencia de usuario.
- Conectores externos.

Esta fase no pertenece al alcance inicial.

## Fuera de alcance inicial
- Agente autónomo completo.
- Producción real.
- Multiempresa real.
- Integraciones activas con clientes reales.
- Firma digital.
- CRM completo.
- ERP (*Enterprise Resource Planning – Planificación de Recursos Empresariales*).
- Gestión legal, fiscal o contractual avanzada.
- Automatizaciones irreversibles.
- Decisiones sin revisión humana.
- Tratamiento de datos sensibles sin controles específicos.
- Métricas de impacto no verificadas.
- Base de datos.
- Dashboard.
- Google Workspace operativo.
- API externa.
- IA funcional.

## Criterios para cerrar una fase
Preguntas de control:
- ¿La fase tiene entregables claros?
- ¿El resultado puede revisarse?
- ¿La documentación refleja el estado real?
- ¿No se han añadido promesas no implementadas?
- ¿La siguiente fase está justificada?
- ¿El agente sigue resolviendo un problema concreto?
- ¿La revisión humana está contemplada?

Criterios específicos para cerrar la implementación mínima V1:
- El script se ejecuta desde la raíz del repositorio.
- El JSON de ejemplo se carga correctamente.
- El informe por consola es comprensible.
- Los bloqueos se detectan correctamente.
- La decisión recomendada coincide con los datos ficticios.
- No se usan dependencias externas.
- No se usan datos reales.

## Criterios para activar la siguiente fase
Condiciones:
- Documentación base completa.
- Alcance V1 definido.
- Límites claros.
- Flujo mínimo comprensible.
- Riesgos principales identificados.
- Revisión humana contemplada.
- Validación interna realizada cuando proceda.
- Prueba básica del script creada antes de ampliar el alcance técnico.

## Evidencias recomendadas para portfolio
Evidencias disponibles o recomendadas:
- README claro.
- Arquitectura explicada.
- Caso de uso realista.
- Roadmap transparente.
- Datos de ejemplo ficticios.
- Checklist demostrable.
- Expediente de cliente ficticio.
- Script local de validación.
- Informe por consola reproducible.
- Registro de cambios documentado.

Las evidencias solo deben añadirse cuando existan realmente.

## Próximos pasos inmediatos
1. Crear una prueba básica del script con datos ficticios.
2. Actualizar después la documentación técnica si la prueba confirma el comportamiento esperado.
3. Hacer commit manual de la primera implementación mínima cuando el estado quede limpio.

## Ã°Å¸ÂªÂª Licencia y AutorÃƒÂ­a

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
Ã‚Â© 2025 Ã¢â‚¬â€œ Txema RÃƒÂ­os. Todos los derechos compartidos.
