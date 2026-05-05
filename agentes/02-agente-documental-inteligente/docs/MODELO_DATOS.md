# Modelo Conceptual de Datos del Agente Documental Inteligente para PYMES

## Propósito del documento
Este documento define los datos mínimos necesarios para una primera V1 (*Version 1 – Versión 1*) implementable del agente documental. Sirve como base de diseño para preparar una futura implementación mínima orientada a inventariar, clasificar y revisar documentos ficticios.

No describe una base de datos ya creada. Es un modelo conceptual previo para ordenar qué información debería existir antes de escribir código funcional.

## Estado actual
- Estado documental: en diseño inicial de V1.
- Código funcional: no implementado todavía.
- Base de datos: no implementada todavía.
- Automatizaciones: no implementadas todavía.
- Buscador documental: no implementado todavía.
- OCR (*Optical Character Recognition – Reconocimiento Óptico de Caracteres*): no implementado todavía.
- RAG (*Retrieval-Augmented Generation – Generación Aumentada por Recuperación*): no implementado todavía.
- Integraciones activas: no implementadas todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Criterio de diseño del modelo
El modelo debe ser:
- Simple.
- Comprensible.
- Verificable.
- Útil para inventariar documentos.
- Suficiente para demostrar el flujo documental.
- No sobredimensionado.
- Preparado para evolucionar después.

La prioridad de esta fase es que el modelo pueda entenderse, revisarse y probarse con datos ficticios sin introducir complejidad innecesaria.

## Entidad principal: Documento
La entidad principal representa cada documento que forma parte del inventario documental de una PYME (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*). En V1 debe permitir identificar el documento, ubicarlo conceptualmente, conocer su estado y asignar una revisión humana.

Campos mínimos:

- `identificador_documento`: representa una referencia única del documento. Es obligatorio en V1 porque permite relacionar el documento con clasificaciones, versiones, pendientes y acciones.
- `nombre_documento`: representa el nombre legible del documento. Es obligatorio en V1 porque ayuda a identificar rápidamente el contenido.
- `tipo_documental`: representa la naturaleza del documento, por ejemplo contrato, propuesta, manual, factura ficticia o plantilla. Es obligatorio en V1 porque permite clasificar el inventario.
- `area_o_proceso`: representa el área de negocio o proceso al que pertenece el documento. Es recomendable en V1 porque ayuda a ordenar documentos por contexto operativo.
- `fecha_creacion_o_recepcion`: representa cuándo se creó o recibió el documento. Es recomendable en V1 porque permite detectar antigüedad o necesidad de revisión.
- `estado_documental`: representa el estado actual del documento dentro del flujo. Es obligatorio en V1 porque permite distinguir documentos pendientes, incompletos, validados u obsoletos.
- `responsable_interno`: representa la persona o rol encargado de revisar el documento. Es obligatorio en V1 porque mantiene la revisión humana asignada.
- `version_documento`: representa la versión declarada o identificada del documento. Es recomendable en V1 porque ayuda a detectar versiones antiguas o ambiguas.
- `ubicacion_prevista`: representa dónde debería localizarse el documento dentro de una estructura documental. Es recomendable en V1 porque prepara una futura organización de carpetas.
- `observaciones_documento`: representa notas internas sobre el documento. Es recomendable en V1 porque permite registrar dudas, incidencias o aclaraciones.

## Entidad secundaria: Clasificación documental
La clasificación documental sirve para asociar cada documento con una categoría funcional y criterios de revisión. En V1 la clasificación será manual o por reglas simples, no mediante IA funcional.

Campos mínimos:

- `identificador_clasificacion`: representa una referencia única de la clasificación. Es obligatorio en V1 para identificar cada registro de clasificación.
- `identificador_documento`: representa el documento al que pertenece la clasificación. Es obligatorio en V1 porque conecta la clasificación con la entidad Documento.
- `categoria_principal`: representa la categoría general del documento. Es obligatorio en V1 porque permite agrupar documentos de forma comprensible.
- `subcategoria`: representa una clasificación más específica. Es recomendable en V1 porque puede ayudar a distinguir documentos similares.
- `prioridad_revision`: representa la prioridad con la que debe revisarse el documento. Es recomendable en V1 porque ayuda a ordenar el trabajo humano.
- `criterio_clasificacion`: representa la razón por la que se asignó una categoría. Es obligatorio en V1 porque evita clasificaciones opacas.
- `requiere_revision_humana`: indica si una persona debe revisar o confirmar la clasificación. Es obligatorio en V1 porque el modelo no sustituye criterio profesional.
- `observaciones_clasificacion`: representa notas sobre dudas o matices de clasificación. Es recomendable en V1 porque facilita ajustes posteriores.

## Entidad secundaria: Control de versiones
El control de versiones sirve para detectar versiones antiguas, ambiguas o duplicadas. No pretende sustituir un gestor documental completo, solo aportar una primera trazabilidad conceptual.

Campos mínimos:

- `identificador_version`: representa una referencia única de la versión registrada. Es obligatorio en V1 para identificar cada versión.
- `identificador_documento`: representa el documento base al que pertenece la versión. Es obligatorio en V1 porque conecta la versión con el documento principal.
- `nombre_version`: representa el nombre específico de la versión. Es recomendable en V1 porque permite comparar nombres similares.
- `numero_version`: representa el número o etiqueta de versión si existe. Es recomendable en V1 porque facilita detectar cuál podría ser la más reciente.
- `fecha_version`: representa la fecha asociada a esa versión. Es recomendable en V1 porque ayuda a detectar antigüedad.
- `estado_version`: representa el estado de esa versión dentro del flujo documental. Es obligatorio en V1 porque permite marcar versiones vigentes, antiguas o duplicadas.
- `documento_relacionado`: representa otro documento con el que esta versión podría estar vinculada. Es recomendable en V1 porque ayuda a detectar duplicados o versiones ambiguas.
- `observaciones_version`: representa notas sobre diferencias, dudas o incidencias de versión. Es recomendable en V1 porque permite justificar revisiones.

Estados posibles:
- `vigente`: versión que se considera usable actualmente.
- `antigua`: versión superada por otra más reciente.
- `pendiente_revision`: versión que necesita validación humana.
- `duplicada`: versión que parece repetir otra existente.
- `descartada`: versión que no debe usarse en el inventario útil.

Estos estados son una propuesta inicial para V1.

## Entidad secundaria: Pendiente documental
El pendiente documental registra documentos faltantes, incompletos o pendientes de revisión. Su función es hacer visible qué impide cerrar el inventario o usar un documento con confianza.

Campos mínimos:

- `identificador_pendiente`: representa una referencia única del pendiente. Es obligatorio en V1 para controlar cada incidencia documental.
- `identificador_documento`: representa el documento asociado al pendiente. Es obligatorio en V1 porque vincula el problema con un documento concreto.
- `descripcion_pendiente`: representa qué falta o qué debe resolverse. Es obligatorio en V1 porque define la acción necesaria.
- `motivo_pendiente`: representa por qué existe el pendiente. Es recomendable en V1 porque ayuda a priorizar y entender el bloqueo.
- `impacto_operativo`: representa cómo afecta el pendiente al uso del documento. Es recomendable en V1 porque ayuda a decidir urgencia.
- `responsable_revision`: representa quién debe revisar o resolver el pendiente. Es obligatorio en V1 porque mantiene responsabilidad humana.
- `prioridad_pendiente`: representa el nivel de prioridad del pendiente. Es recomendable en V1 porque ayuda a ordenar el trabajo.
- `estado_pendiente`: representa la situación actual del pendiente. Es obligatorio en V1 porque permite saber si sigue abierto.
- `observaciones_pendiente`: representa notas adicionales sobre el pendiente. Es recomendable en V1 porque permite documentar contexto.

Estados posibles:
- `pendiente`
- `en_revision`
- `resuelto`
- `bloqueado`
- `descartado`

## Entidad secundaria: Acción documental siguiente
La acción documental siguiente registra próximos pasos sobre documentos. Sirve para que el inventario no sea solo una lista estática, sino una base operativa revisable.

Campos mínimos:

- `identificador_accion`: representa una referencia única de la acción. Es obligatorio en V1 para identificar cada siguiente paso.
- `identificador_documento`: representa el documento asociado a la acción. Es obligatorio en V1 porque vincula la acción con un documento concreto.
- `descripcion_accion`: representa qué debe hacerse. Es obligatorio en V1 porque define el próximo paso.
- `responsable_accion`: representa quién debe ejecutar o revisar la acción. Es obligatorio en V1 porque mantiene trazabilidad humana.
- `estado_accion`: representa la situación actual de la acción. Es obligatorio en V1 porque permite distinguir acciones abiertas y cerradas.
- `prioridad_accion`: representa la importancia relativa de la acción. Es recomendable en V1 porque ayuda a ordenar el trabajo.
- `fecha_prevista`: representa una fecha orientativa para revisar o completar la acción. Es recomendable en V1 porque aporta planificación básica.
- `observaciones_accion`: representa notas internas sobre la acción. Es recomendable en V1 porque permite añadir contexto.

Estados posibles:
- `pendiente`
- `en_revision`
- `completada`
- `descartada`

## Relaciones entre entidades
Las relaciones conceptuales son simples:

- Un documento puede tener una clasificación documental.
- Un documento puede tener varias versiones relacionadas.
- Un documento puede tener varios pendientes documentales.
- Un documento puede tener varias acciones siguientes.
- Un inventario documental puede agrupar varios documentos.

No se requiere un diagrama complejo para la V1. Basta con mantener identificadores consistentes para relacionar los datos ficticios.

## Datos mínimos para una demo V1
Para demostrar la V1 con documentos ficticios bastaría con:

- Cinco o seis documentos ficticios.
- Tipos documentales variados.
- Estados documentales distintos.
- Algún documento pendiente.
- Algún documento incompleto.
- Alguna posible versión duplicada o ambigua.
- Clasificación documental simple.
- Próximas acciones documentales.
- Revisión humana prevista.

Estos datos deben ser inventados y no deben representar documentos reales.

## Datos fuera de alcance en V1
No deben usarse en esta fase:
- Contratos reales.
- Documentación legal sensible.
- Datos fiscales sensibles.
- Datos médicos.
- Credenciales.
- Firmas digitales.
- Documentos confidenciales de clientes reales.
- Información bancaria.
- Documentos sujetos a control normativo avanzado.

No deben usarse datos reales sensibles en esta fase.

## Evolución posible en V2
La V2 (*Version 2 – Versión 2*) podría ampliar el modelo si la V1 documental queda validada.

Posibles ampliaciones futuras:
- Registro documental en Google Sheets.
- Organización de carpetas en Google Drive.
- Generación de índice documental en Google Docs.
- Dashboard operativo.
- Historial de cambios.
- Extracción futura de texto mediante OCR.
- Clasificación asistida con IA.
- Búsqueda documental asistida.
- Integración futura con RAG.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) futura si el proyecto crece.

Estas opciones no están implementadas todavía.

## Criterios de validación del modelo
Preguntas de control:
- ¿El modelo permite representar un inventario documental básico?
- ¿Los campos mínimos son comprensibles?
- ¿La V1 puede demostrarse con documentos ficticios?
- ¿Se evita tratar documentación sensible real?
- ¿La clasificación puede hacerse sin IA?
- ¿Se pueden detectar pendientes y posibles duplicados?
- ¿El modelo puede evolucionar sin rehacerse desde cero?

## Próximos pasos
1. Preparar un inventario documental ficticio.
2. Preparar un flujo mínimo de validación documental manual.
3. Definir después una primera estructura de datos de ejemplo si procede.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
