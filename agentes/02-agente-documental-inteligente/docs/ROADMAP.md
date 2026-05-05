# Roadmap del Agente Documental Inteligente para PYMES

## Propósito del documento
Este documento define la evolución prevista del agente documental por fases, diferenciando documentación, diseño mínimo, implementación futura, validación interna y posibles mejoras posteriores. Su función es mantener una planificación técnica clara, revisable y sin declarar como implementado nada que todavía no exista.

## Estado actual
- Estado documental: fase documental V1 preparada.
- Estado técnico: pendiente de implementación.
- Código funcional: no implementado todavía.
- Automatización documental: no implementada todavía.
- Integraciones activas: no implementadas todavía.
- Buscador semántico: no implementado todavía.
- OCR: no implementado todavía.
- RAG: no implementado todavía.
- Dashboard: no implementado todavía.
- Google Workspace: no implementado todavía.
- IA funcional: no implementada todavía.
- Última fase completada: documentación V1 preparada con modelo de datos, inventario ficticio, flujo de validación documental y JSON de ejemplo.
- Próxima decisión real: decidir si se implementa código mínimo más adelante o si se continúa con el agente 03.

## Fase 0 — Base documental
Esta fase sirve para definir el problema documental, el alcance y la estructura del agente antes de crear código.

Entregables preparados:
- README del agente.
- Arquitectura conceptual.
- Caso de uso funcional.
- Roadmap.
- Límites de alcance.
- Criterios de validación.

Esta fase no implica código funcional.

## Fase 1 — Definición de V1 implementable
Esta fase convierte la documentación en un diseño mínimo que pueda implementarse después.

Entregables preparados:
- Modelo conceptual mínimo de datos documentales.
- Criterios de clasificación documental.
- Inventario documental ficticio.
- Estados documentales básicos.
- Reglas simples de validación documental.
- Criterios para detectar documentos pendientes.
- Criterios para detectar posibles duplicados o versiones ambiguas.
- Criterios de revisión humana.
- JSON ficticio para futura validación mínima.

Esta fase queda preparada documentalmente, pero todavía no implica automatización real.

## Fase 2 — Implementación mínima V1 futura
Esta fase sigue pendiente. Solo debería abrirse si se decide implementar código mínimo para procesar datos documentales ficticios.

Podría incluir:
- Script o lógica mínima para procesar el JSON documental ficticio.
- Validación de campos obligatorios.
- Detección de documentos pendientes.
- Detección básica de documentos incompletos.
- Detección básica de posibles duplicados por nombre, tipo o versión.
- Generación simple de informe por consola.
- Registro básico de estado documental.
- Documentación actualizada al cierre del bloque.

La implementación futura debe ser pequeña, verificable y sin sobreingeniería. No debe declarar buscador semántico, OCR, RAG, dashboard, Google Workspace, API, IA funcional ni automatización productiva.

## Fase 3 — Validación interna futura
Esta fase servirá para probar el flujo documental con datos ficticios si se implementa una V1 mínima.

Podría incluir:
- Prueba con inventario documental ficticio.
- Revisión de documentos completos, pendientes e incompletos.
- Revisión de posibles duplicados o versiones ambiguas.
- Revisión de clasificación documental.
- Ajuste de documentación.
- Confirmación de límites de alcance.

No deben usarse documentos reales sensibles en esta fase.

## Fase 4 — V2 futura
La V2 describe posibles ampliaciones futuras si una V1 mínima queda implementada y validada.

Posibles ampliaciones futuras:
- Registro documental en Google Sheets.
- Organización de carpetas en Google Drive.
- Generación de índice documental.
- Dashboard operativo.
- Alertas básicas sobre documentos pendientes u obsoletos.
- Extracción de texto mediante OCR.
- Clasificación asistida con IA.
- Búsqueda documental asistida.
- Integración futura con RAG.
- Posible API si el proyecto crece.

Estas funcionalidades no están implementadas todavía.

## Fase 5 — Integraciones avanzadas opcionales
Esta fase solo tendría sentido si la V1 y la V2 quedan validadas en fases posteriores.

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

Esta fase no pertenece al alcance actual.

## Fuera de alcance actual
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
Evidencias disponibles o posibles:
- README claro.
- Arquitectura explicada.
- Caso de uso realista.
- Roadmap transparente.
- Modelo de datos documental.
- Inventario documental ficticio.
- Flujo de validación documental.
- JSON de ejemplo.
- Pruebas si en el futuro hay implementación mínima.
- Capturas si en el futuro existe interfaz.
- Registro de cambios documentado.

Las evidencias solo deben añadirse cuando existan realmente.

## Próximos pasos inmediatos
1. Validar el JSON de ejemplo.
2. Hacer commit manual de la fase documental V1 del agente 02.
3. Pasar después al agente 03.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
