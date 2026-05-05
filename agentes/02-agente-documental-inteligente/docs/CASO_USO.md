# Caso de Uso del Agente Documental Inteligente para PYMES

## Propósito del documento
Este documento define el escenario funcional previsto para el agente documental y sirve para entender cómo podría aplicarse a una pequeña o mediana empresa real. El objetivo es describir un caso útil para portfolio técnico, verificable con datos ficticios y limitado a una fase documental inicial.

## Estado del caso de uso
- Estado documental: en desarrollo inicial.
- Código funcional: no implementado todavía.
- Automatizaciones: no implementadas todavía.
- Integraciones activas: no implementadas todavía.
- Buscador documental: no implementado todavía.
- OCR (*Optical Character Recognition – Reconocimiento Óptico de Caracteres*): no implementado todavía.
- RAG (*Retrieval-Augmented Generation – Generación Aumentada por Recuperación*): no implementado todavía.
- Dashboard: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial
El caso de uso parte de una PYME (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*) de servicios que acumula documentación en carpetas compartidas, correos, documentos descargados, propuestas, versiones antiguas y archivos sin criterio uniforme.

El problema no es solo guardar documentos. El problema operativo es saber qué existe, qué falta, qué versión es válida y qué necesita revisión antes de usarse en un expediente, una propuesta o un proceso interno.

## Situación inicial sin agente
- Documentos repartidos entre carpetas, correos y equipos personales.
- Nombres de archivo poco claros.
- Versiones duplicadas o contradictorias.
- Falta de inventario documental.
- Documentos pendientes sin seguimiento.
- Dificultad para encontrar la última versión válida.
- Dependencia de una persona que recuerda dónde está cada archivo.
- Riesgo de usar documentos obsoletos.

## Objetivo del caso de uso
El objetivo es convertir documentación dispersa en un inventario inicial revisable, con clasificación básica, estados documentales y próximos pasos.

Debe incluir:
- Registrar documentos.
- Clasificar documentos por tipo, área o proceso.
- Detectar documentos pendientes.
- Detectar posibles duplicados o versiones ambiguas.
- Preparar inventario documental.
- Generar una vista operativa para revisión humana.

## Actores implicados

### Responsable interno
Revisa documentos, confirma estados, valida versiones y decide qué se mantiene, corrige, solicita o descarta.

### Equipo operativo
Aporta documentos, usa el inventario y consulta qué documentación está disponible o pendiente.

### Agente documental
En la visión prevista, ayuda a estructurar documentos, detectar pendientes, preparar inventario y señalar posibles duplicados. Todavía no hay agente funcional implementado.

## Flujo funcional previsto
1. Recepción o registro de documentos.
2. Registro básico de metadatos documentales.
3. Revisión de campos mínimos.
4. Clasificación documental inicial.
5. Identificación de documentos pendientes.
6. Detección básica de posibles duplicados o versiones.
7. Preparación del inventario documental.
8. Revisión humana.
9. Confirmación de siguiente acción documental.

Este flujo es diseño funcional previsto, no ejecución automática actual.

## Datos mínimos del caso de uso
Posibles datos mínimos:
- Identificador del documento.
- Nombre del documento.
- Tipo documental.
- Área o proceso relacionado.
- Fecha de creación o recepción.
- Estado documental.
- Responsable interno.
- Versión.
- Ubicación prevista.
- Documentos relacionados.
- Observaciones internas.
- Próxima acción documental.

Todavía no existe captura funcional automatizada.

## Inventario documental inicial previsto
Lista de control posible:
- Documento identificado.
- Nombre normalizado.
- Tipo documental asignado.
- Área o proceso relacionado.
- Responsable interno asignado.
- Estado documental definido.
- Versión revisada.
- Ubicación prevista registrada.
- Posibles duplicados anotados.
- Próxima acción definida.

Este inventario es diseño previsto para V1 (*Version 1 – Versión 1*), no automatización implementada.

## Clasificación documental prevista
En V1 la clasificación podría ser manual o basada en reglas simples.

Posibles criterios:
- Tipo documental.
- Área o proceso.
- Estado de revisión.
- Antigüedad.
- Versión.
- Responsable.
- Prioridad de revisión.
- Existencia de duplicados o documentos relacionados.

La clasificación con IA sería una evolución futura, no una funcionalidad actual.

## Estados documentales previstos
- pendiente: el documento se espera, pero todavía no está disponible.
- recibido: el documento ha sido localizado o entregado.
- incompleto: el documento existe, pero le falta información o revisión.
- en_revision: el documento está pendiente de validación humana.
- validado: el documento ha sido revisado y aceptado como versión usable.
- obsoleto: el documento ya no debe usarse como referencia vigente.
- duplicado: el documento parece repetir contenido de otro archivo.
- descartado: el documento no se conserva como parte del inventario útil.

## Resultado esperado en V1
Salida mínima y verificable:
- Inventario documental inicial.
- Lista de documentos pendientes.
- Lista de documentos incompletos.
- Lista de posibles duplicados.
- Clasificación documental básica.
- Estado documental por documento.
- Próximas acciones para revisión humana.

La V1 debe poder demostrarse con datos documentales ficticios, sin depender de integraciones complejas.

## Evolución V2 futura
La V2 (*Version 2 – Versión 2*) podría ampliar el caso de uso si la V1 queda validada.

Posibles mejoras futuras:
- Registro documental en Google Sheets.
- Organización de carpetas en Google Drive.
- Generación de índice documental.
- Dashboard operativo.
- Alertas de documentos pendientes u obsoletos.
- Extracción de texto mediante OCR.
- Clasificación asistida con IA.
- Búsqueda documental asistida.
- Integración futura con RAG.

Estas mejoras no están implementadas todavía.

## Fuera de alcance inicial
- Sistema documental completo en producción.
- Buscador semántico funcional.
- RAG implementado.
- OCR implementado.
- Base vectorial.
- Firma digital.
- Gestión legal avanzada.
- Eliminación automática de documentos.
- Integraciones activas con documentos reales de clientes.
- Tratamiento de documentación sensible sin controles específicos.
- Multiempresa real.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) pública.
- Sustitución de revisión humana.

## Criterios de validación funcional
- ¿El caso de uso representa un problema documental real de PYME?
- ¿La entrada y la salida se entienden?
- ¿La V1 puede demostrarse con datos ficticios?
- ¿Está claro qué parte no está implementada?
- ¿La revisión humana está contemplada?
- ¿La V2 está separada del alcance actual?
- ¿El flujo evita prometer automatización documental inexistente?
- ¿Se evita prometer IA documental, OCR o RAG sin implementación?

## Próximos pasos
1. Completar el roadmap de evolución del agente documental.
2. Definir después el modelo conceptual mínimo de datos documentales para la V1.
3. Preparar después un inventario documental ficticio para validación.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
