# Roadmap del Agente Documental Inteligente para PYMES

## Propósito del documento
Este documento define la evolución prevista del agente documental por fases, diferenciando documentación, diseño mínimo, implementación futura, validación interna y posibles mejoras posteriores. Su función es mantener una planificación técnica clara, revisable y sin declarar como implementado nada que todavía no exista.

## Estado actual
- Estado documental: en desarrollo inicial.
- Estado técnico: pendiente de implementación.
- Código funcional: no implementado todavía.
- Automatizaciones: no implementadas todavía.
- Integraciones activas: no implementadas todavía.
- Buscador documental: no implementado todavía.
- OCR (*Optical Character Recognition – Reconocimiento Óptico de Caracteres*): no implementado todavía.
- RAG (*Retrieval-Augmented Generation – Generación Aumentada por Recuperación*): no implementado todavía.
- Dashboard: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.
- Última fase completada: documentación base en preparación.
- Próxima fase prevista: definición del modelo conceptual mínimo de datos documentales para la V1 (*Version 1 – Versión 1*).

## Fase 0 — Base documental
Esta fase sirve para definir el problema documental, el alcance y la estructura del agente antes de crear código.

Entregables:
- README del agente.
- Arquitectura conceptual.
- Caso de uso funcional.
- Roadmap.
- Límites de alcance.
- Criterios de validación.

Esta fase no implica código funcional.

## Fase 1 — Definición de V1 implementable
Esta fase debe convertir la documentación en un diseño mínimo que pueda implementarse después.

Entregables previstos:
- Modelo conceptual mínimo de datos documentales.
- Criterios de clasificación documental.
- Inventario documental ficticio.
- Estados documentales básicos.
- Reglas simples de validación.
- Reglas simples para detectar documentos pendientes.
- Reglas simples para detectar posibles duplicados o versiones ambiguas.
- Criterios de revisión humana.

Esta fase todavía puede completarse sin automatización real.

## Fase 2 — Implementación mínima V1
Esta fase solo debe abrirse cuando la documentación y el diseño mínimo estén cerrados.

Puede incluir:
- Script o lógica mínima para procesar datos documentales ficticios.
- Validación de campos obligatorios.
- Detección de documentos pendientes.
- Detección básica de documentos incompletos.
- Detección básica de posibles duplicados por nombre, tipo o versión.
- Generación simple de informe por consola.
- Registro básico de estado documental.
- Documentación actualizada al cierre del bloque.

La implementación debe ser pequeña, verificable y sin sobreingeniería.

## Fase 3 — Validación interna
Esta fase sirve para probar el flujo documental con datos ficticios antes de ampliar el agente.

Incluye:
- Prueba con inventario documental ficticio.
- Revisión de documentos completos, pendientes e incompletos.
- Revisión de posibles duplicados o versiones ambiguas.
- Revisión de clasificación documental.
- Ajuste de documentación.
- Confirmación de límites de alcance.

No deben usarse documentos reales sensibles en esta fase.

## Fase 4 — V2 futura
La V2 (*Version 2 – Versión 2*) describe posibles ampliaciones futuras si la V1 queda validada.

Posibles ampliaciones:
- Registro documental en Google Sheets.
- Organización de carpetas en Google Drive.
- Generación de índice documental.
- Dashboard operativo.
- Alertas básicas sobre documentos pendientes u obsoletos.
- Extracción de texto mediante OCR.
- Clasificación asistida con IA.
- Búsqueda documental asistida.
- Integración futura con RAG.
- Posible API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) si el proyecto crece.

Estas funcionalidades no están implementadas todavía.

## Fase 5 — Integraciones avanzadas opcionales
Esta fase solo tendría sentido si la V1 y la V2 quedan validadas.

Puede incluir:
- Conexión con gestores documentales.
- Integración con Google Drive real.
- Control de permisos.
- Historial de versiones.
- Registro de cambios documentales.
- Base vectorial.
- Buscador semántico.
- Conectores externos.
- Analítica documental básica.

Esta fase no pertenece al alcance inicial.

## Fuera de alcance inicial
- Sistema documental completo en producción.
- Buscador semántico funcional.
- RAG implementado.
- OCR implementado.
- Base vectorial.
- Firma digital.
- Gestión legal avanzada.
- Eliminación automática de documentos.
- Automatizaciones irreversibles.
- Integraciones activas con documentos reales de clientes.
- Tratamiento de documentación sensible sin controles específicos.
- Multiempresa real.
- API pública.
- Sustitución de revisión humana.
- Métricas de impacto no verificadas.

## Criterios para cerrar una fase
Preguntas de control:
- ¿La fase tiene entregables claros?
- ¿El resultado puede revisarse?
- ¿La documentación refleja el estado real?
- ¿No se han añadido promesas no implementadas?
- ¿La siguiente fase está justificada?
- ¿El agente sigue resolviendo un problema documental concreto?
- ¿La revisión humana está contemplada?

## Criterios para activar la siguiente fase
Condiciones:
- Documentación base completa.
- Alcance V1 definido.
- Límites claros.
- Flujo documental mínimo comprensible.
- Riesgos principales identificados.
- Revisión humana contemplada.
- Validación interna realizada cuando proceda.

## Evidencias recomendadas para portfolio
Posibles evidencias futuras:
- README claro.
- Arquitectura explicada.
- Caso de uso realista.
- Roadmap transparente.
- Modelo de datos documental.
- Inventario documental ficticio.
- Datos de ejemplo si existen.
- Pruebas si hay implementación mínima.
- Capturas si en el futuro existe interfaz.
- Registro de cambios documentado.

Las evidencias solo deben añadirse cuando existan realmente.

## Próximos pasos inmediatos
1. Definir el modelo conceptual mínimo de datos documentales para la V1.
2. Preparar un inventario documental ficticio.
3. Preparar después un flujo mínimo de validación documental manual.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
