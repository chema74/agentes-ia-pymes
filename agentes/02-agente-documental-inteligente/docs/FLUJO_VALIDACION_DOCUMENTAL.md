# Flujo de Validación Documental del Agente Documental Inteligente para PYMES

## Propósito del documento
Este documento define un flujo mínimo de validación documental para la V1 del Agente Documental Inteligente para PYMES. Su objetivo es explicar cómo revisar un inventario documental ficticio antes de una futura implementación mínima.

No describe una automatización implementada. Es una guía funcional y técnica para validar manualmente documentos ficticios, estados documentales, pendientes, versiones y próximas acciones.

## Estado actual
- Estado documental: flujo de validación en fase de diseño V1.
- Código funcional: no implementado todavía.
- Automatización documental: no implementada todavía.
- Buscador documental: no implementado todavía.
- OCR: no implementado todavía.
- RAG: no implementado todavía.
- Dashboard: no implementado todavía.
- Google Workspace: no implementado todavía.
- IA funcional: no implementada todavía.

## Principios del flujo
El flujo debe ser:
- Simple.
- Manualmente revisable.
- Comprensible sin herramientas externas.
- Verificable con documentos ficticios.
- Orientado a revisión humana.
- Preparado para una futura implementación pequeña.

La prioridad de esta V1 es ordenar el criterio documental, no automatizar decisiones.

## Entrada del flujo
La entrada prevista es un inventario documental ficticio con:
- Documentos identificados.
- Tipo documental.
- Área o proceso relacionado.
- Estado documental.
- Responsable interno.
- Versión.
- Ubicación prevista.
- Posibles duplicados.
- Pendientes.
- Próximas acciones.

No deben usarse documentos reales, datos sensibles, contratos reales, datos fiscales, credenciales ni información confidencial de clientes.

## Paso 1 — Revisar identificación del documento
Se comprueba que cada documento tenga una referencia mínima:
- Identificador documental.
- Nombre del documento.
- Tipo documental.
- Área o proceso relacionado.

Si falta alguno de estos datos, el documento debe marcarse como incompleto o pendiente de revisión.

## Paso 2 — Revisar estado documental
Se valida que cada documento tenga un estado claro.

Estados previstos:
- `pendiente`: el documento se espera, pero aún no está disponible.
- `recibido`: el documento existe, pero todavía no ha sido validado.
- `incompleto`: el documento existe, pero le falta información.
- `en_revision`: el documento está siendo revisado por una persona.
- `validado`: el documento puede usarse como versión aceptada.
- `obsoleto`: el documento no debe usarse como referencia vigente.
- `duplicado`: el documento parece repetir otro documento.
- `descartado`: el documento no se mantiene como parte útil del inventario.

Si el estado no es claro, debe registrarse una acción de revisión humana.

## Paso 3 — Revisar versiones
Se revisa si el documento tiene versiones relacionadas, antiguas o ambiguas.

Criterios de revisión:
- Si hay una versión vigente clara, debe marcarse como referencia principal.
- Si hay versiones antiguas, deben conservarse solo como histórico ficticio.
- Si hay copias con nombres similares, deben marcarse como posibles duplicados.
- Si la versión no puede confirmarse, debe quedar en revisión.

Este paso no sustituye un sistema de control documental completo.

## Paso 4 — Detectar pendientes documentales
Se revisa si existen documentos faltantes, incompletos o bloqueados.

Un pendiente debe incluir:
- Descripción del pendiente.
- Motivo.
- Impacto operativo.
- Responsable de revisión.
- Prioridad.
- Estado.

Si un pendiente impide usar el documento con confianza, debe mantenerse abierto hasta revisión humana.

## Paso 5 — Detectar posibles duplicados
Se revisan documentos con:
- Nombres similares.
- Tipo documental equivalente.
- Versiones próximas.
- Misma área o proceso.
- Observaciones que indiquen copia o sustitución.

La detección de duplicados en esta fase es manual o por reglas simples. No existe buscador semántico, base vectorial ni IA funcional.

## Paso 6 — Revisar clasificación documental
Se comprueba que cada documento tenga una clasificación útil.

Criterios posibles:
- Categoría principal.
- Subcategoría.
- Prioridad de revisión.
- Criterio de clasificación.
- Necesidad de revisión humana.

La clasificación en V1 debe poder explicarse sin IA.

## Paso 7 — Definir próximas acciones
Cada documento con dudas, bloqueos o pendientes debe tener una próxima acción.

Estados posibles de acción:
- `pendiente`
- `en_revision`
- `completada`
- `descartada`

La acción debe indicar responsable, prioridad y observaciones suficientes para continuar la revisión.

## Paso 8 — Decisión de revisión manual
La decisión final debe ser tomada por una persona.

Decisiones posibles:
- `validar`: el documento puede considerarse útil para el inventario.
- `pedir_informacion`: falta información o documentación adicional.
- `revisar_version`: existe duda sobre la versión vigente.
- `marcar_obsoleto`: el documento no debe usarse como referencia actual.
- `marcar_duplicado`: el documento parece repetir otro existente.
- `descartar`: el documento no aporta valor al inventario.

Estas decisiones son criterios de revisión, no automatizaciones productivas.

## Resultado esperado del flujo
Al finalizar la validación manual, debería existir:
- Inventario documental más claro.
- Documentos con estado definido.
- Pendientes documentales identificados.
- Posibles duplicados señalados.
- Versiones ambiguas marcadas para revisión.
- Acciones siguientes asignadas.
- Revisión humana contemplada.

## Limitaciones actuales
- No hay lectura automática de documentos.
- No hay extracción de texto.
- No hay OCR.
- No hay RAG.
- No hay buscador semántico.
- No hay base vectorial.
- No hay dashboard.
- No hay integración con Google Workspace.
- No hay IA funcional.
- No hay tratamiento de documentos reales.

## Criterios de validación del flujo
- ¿El flujo puede aplicarse al inventario ficticio?
- ¿Los estados documentales son comprensibles?
- ¿Los pendientes quedan claramente identificados?
- ¿Los duplicados o versiones ambiguas pueden señalarse sin IA?
- ¿Existe revisión humana antes de cualquier decisión?
- ¿Se evita usar documentación sensible real?
- ¿El flujo puede preparar una futura implementación mínima?

## Próximos pasos
1. Revisar este flujo contra el inventario documental ficticio.
2. Ajustar el modelo de datos si aparecen campos necesarios.
3. Valorar después si el agente 02 está listo para una implementación mínima local.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
