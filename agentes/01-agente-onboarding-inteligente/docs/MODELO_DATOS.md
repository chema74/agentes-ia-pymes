# Modelo Conceptual de Datos del Agente de Onboarding Inteligente para PYMES

## Propósito del documento
Este documento define los datos mínimos necesarios para una primera V1 (*Version 1 – Versión 1*) implementable del agente. No describe una base de datos ya creada, sino un modelo conceptual previo para preparar una futura implementación mínima.

## Estado actual
- Estado documental: en diseño inicial de V1.
- Código funcional: no implementado todavía.
- Base de datos: no implementada todavía.
- Automatizaciones: no implementadas todavía.
- Integraciones activas: no implementadas todavía.
- IA funcional: no implementada todavía.

## Criterio de diseño del modelo
El modelo debe ser:
- Simple.
- Comprensible.
- Verificable.
- Suficiente para demostrar el flujo.
- No sobredimensionado.
- Preparado para evolucionar después.

## Entidad principal: Cliente en onboarding
La entidad principal representa el expediente básico del cliente durante el proceso de alta inicial.

- `identificador_cliente`: identificador interno único del cliente; sirve para relacionar datos entre entidades; en V1 es recomendable.
- `nombre_cliente`: nombre de la persona de contacto o del cliente; sirve para identificar el caso; en V1 es obligatorio.
- `nombre_empresa`: nombre de la empresa asociada al onboarding; sirve para contextualizar el expediente; en V1 es obligatorio.
- `correo_contacto`: correo principal de contacto; sirve para comunicación y seguimiento; en V1 es obligatorio.
- `telefono_contacto`: teléfono principal de contacto; sirve para contacto rápido si hace falta; en V1 es recomendable.
- `tipo_servicio_solicitado`: tipo de servicio que el cliente solicita; sirve para orientar el flujo; en V1 es obligatorio.
- `necesidad_principal`: motivo principal del onboarding; sirve para entender el problema a resolver; en V1 es obligatorio.
- `fecha_entrada`: fecha en la que entra el cliente al proceso; sirve para trazabilidad temporal; en V1 es obligatorio.
- `prioridad_inicial`: nivel inicial de prioridad del caso; sirve para ordenar el trabajo; en V1 es recomendable.
- `estado_onboarding`: estado general del proceso de alta; sirve para saber en qué punto está el caso; en V1 es obligatorio.
- `responsable_interno`: persona interna que revisa o gestiona el caso; sirve para asignación operativa; en V1 es recomendable.
- `observaciones_internas`: notas internas del equipo; sirven para registrar contexto adicional; en V1 es recomendable.

## Entidad secundaria: Documentación recibida
Esta entidad conceptual permite controlar los documentos aportados por el cliente. En V1 puede gestionarse como lista simple o estructura básica, sin repositorio documental avanzado.

- `identificador_documento`: identificador interno del documento; sirve para trazabilidad; en V1 es recomendable.
- `identificador_cliente`: referencia al cliente asociado; sirve para vincular el documento con el expediente; en V1 es obligatorio.
- `nombre_documento`: nombre descriptivo del archivo o documento; sirve para identificarlo con claridad; en V1 es obligatorio.
- `tipo_documento`: categoría del documento; sirve para clasificar lo recibido; en V1 es recomendable.
- `estado_documento`: estado del documento dentro del onboarding; sirve para saber si está recibido, pendiente o revisado; en V1 es obligatorio.
- `fecha_recepcion`: fecha en la que se recibe el documento; sirve para trazabilidad; en V1 es recomendable.
- `observaciones_documento`: notas sobre calidad, faltas o incidencias; sirven para seguimiento; en V1 es recomendable.

## Entidad secundaria: Checklist de onboarding
Esta entidad conceptual controla el avance del alta inicial.

- `identificador_item`: identificador interno del elemento de checklist; sirve para trazabilidad; en V1 es recomendable.
- `identificador_cliente`: referencia al cliente asociado; sirve para vincular el checklist con el expediente; en V1 es obligatorio.
- `nombre_item`: nombre breve del elemento a revisar; sirve para identificar la tarea; en V1 es obligatorio.
- `descripcion_item`: explicación del elemento o validación; sirve para aclarar el criterio; en V1 es recomendable.
- `estado_item`: estado actual del ítem; sirve para medir avance; en V1 es obligatorio.
- `obligatorio`: indica si el ítem es imprescindible; sirve para distinguir bloqueos de simples recomendaciones; en V1 es recomendable.
- `responsable_revision`: persona que revisa el ítem; sirve para control humano; en V1 es recomendable.
- `observaciones_item`: notas sobre el estado del ítem; sirven para seguimiento; en V1 es recomendable.

Estados posibles:
- pendiente
- completo
- bloqueado
- no_aplica

Estos estados son una propuesta inicial para V1.

## Entidad secundaria: Clasificación inicial
Esta entidad conceptual permite clasificar el onboarding.

- `identificador_clasificacion`: identificador interno de la clasificación; sirve para trazabilidad; en V1 es recomendable.
- `identificador_cliente`: referencia al cliente asociado; sirve para vincular la clasificación al expediente; en V1 es obligatorio.
- `tipo_cliente`: tipo de cliente o perfil de relación; sirve para orientar el tratamiento del caso; en V1 es recomendable.
- `complejidad_inicial`: nivel de complejidad estimado; sirve para priorizar la gestión; en V1 es recomendable.
- `urgencia`: grado de urgencia del onboarding; sirve para ordenar el trabajo; en V1 es recomendable.
- `informacion_completa`: indica si la información recibida está completa; sirve para decidir si se puede avanzar; en V1 es recomendable.
- `requiere_revision_previa`: indica si necesita revisión antes de avanzar; sirve para reforzar el control humano; en V1 es recomendable.
- `criterio_clasificacion`: motivo de la clasificación aplicada; sirve para explicar la decisión; en V1 es obligatorio.

En V1 la clasificación será manual o por reglas simples, no mediante IA funcional.

## Entidad secundaria: Acciones siguientes
Esta entidad conceptual registra los próximos pasos del onboarding.

- `identificador_accion`: identificador interno de la acción; sirve para trazabilidad; en V1 es recomendable.
- `identificador_cliente`: referencia al cliente asociado; sirve para vincular la acción al expediente; en V1 es obligatorio.
- `descripcion_accion`: explicación de la acción a realizar; sirve para saber qué sigue; en V1 es obligatorio.
- `responsable_accion`: persona encargada de la acción; sirve para asignar trabajo; en V1 es recomendable.
- `estado_accion`: estado actual de la acción; sirve para seguimiento; en V1 es obligatorio.
- `prioridad_accion`: prioridad operativa de la acción; sirve para ordenar el trabajo; en V1 es recomendable.
- `fecha_prevista`: fecha estimada para completar la acción; sirve para planificación; en V1 es recomendable.
- `observaciones_accion`: notas sobre la acción; sirven para seguimiento y contexto; en V1 es recomendable.

Estados posibles:
- pendiente
- en_revision
- completada
- descartada

## Relaciones entre entidades
- Un cliente puede tener varios documentos.
- Un cliente puede tener varios elementos de checklist.
- Un cliente puede tener una clasificación inicial.
- Un cliente puede tener varias acciones siguientes.

## Datos mínimos para una demo V1
Para demostrar la V1 con un cliente ficticio bastan:
- Datos básicos del cliente.
- Servicio solicitado.
- Necesidad principal.
- Dos o tres documentos recibidos.
- Dos o tres documentos pendientes.
- Checklist con estados.
- Clasificación inicial simple.
- Próximas acciones.

## Datos fuera de alcance en V1
- Datos bancarios.
- Datos fiscales sensibles.
- Datos médicos.
- Datos legales complejos.
- Contratos reales.
- Documentación confidencial de clientes reales.
- Credenciales.
- Firmas digitales.
- Datos de pago.

No deben usarse datos reales sensibles en esta fase.

## Evolución posible en V2
Posibles ampliaciones futuras:
- Registro en Google Sheets.
- Generación documental en Google Docs.
- Carpetas en Google Drive.
- Dashboard operativo.
- Historial de cambios.
- Clasificación asistida con IA (*Artificial Intelligence – Inteligencia Artificial*).
- Integración futura con CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*).
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) futura si el proyecto crece.

Estas opciones no están implementadas todavía.

## Criterios de validación del modelo
- ¿El modelo permite representar un cliente en onboarding?
- ¿Los campos mínimos son comprensibles?
- ¿La V1 puede demostrarse con datos ficticios?
- ¿Se evita tratar datos sensibles?
- ¿La clasificación puede hacerse sin IA?
- ¿El modelo puede evolucionar sin rehacerse desde cero?

## Próximos pasos
1. Preparar un checklist inicial de onboarding.
2. Preparar un expediente ficticio de cliente.
3. Definir después el primer flujo mínimo de validación manual.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
