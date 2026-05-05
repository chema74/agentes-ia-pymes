# Arquitectura del Agente de Onboarding Inteligente para PYMES

## Propósito del documento
Este documento describe la arquitectura conceptual y técnica prevista para el agente, sin declarar como implementado ningún componente o comportamiento que todavía no exista.

## Estado de la arquitectura
- Estado documental: en desarrollo inicial.
- Estado técnico: pendiente de implementación.
- Código funcional: no implementado todavía.
- Automatizaciones reales: no implementadas todavía.
- Integraciones activas: no implementadas todavía.
- Dashboard: no implementado todavía.
- IA funcional: no implementada todavía.

## Visión conceptual
El agente se plantea como una capa de organización entre la entrada inicial de un cliente y el inicio operativo del servicio. En una versión futura, este agente podrá recibir información inicial del cliente, ordenar datos básicos, identificar información pendiente, generar o preparar un checklist y consolidar un expediente inicial para revisión humana antes de avanzar.

Esta visión conceptual define intención de diseño y no equivale a funcionalidad implementada actualmente.

## Flujo general previsto
1. Entrada de información del cliente.
2. Validación inicial de campos mínimos.
3. Organización de datos.
4. Identificación de datos pendientes.
5. Clasificación inicial.
6. Preparación de expediente.
7. Revisión humana.
8. Registro del estado del onboarding.

Este flujo es diseño previsto y no ejecución automática actual.

## Componentes conceptuales

### Entrada de datos
La entrada podría venir de formulario, documento, hoja de cálculo o carga manual, según el nivel de madurez operativa de la empresa.

### Validación inicial
Esta capa serviría para detectar campos vacíos, datos incompletos o ausencia de información mínima necesaria para continuar.

### Checklist de onboarding
El checklist permitiría controlar qué elementos están completos, cuáles permanecen pendientes y cuáles bloquean el inicio operativo.

### Clasificación inicial
La clasificación podría organizar tipo de cliente, prioridad, complejidad o estado inicial mediante reglas simples en V1 (*Version 1 – Versión 1*), con posible asistencia de IA (*Artificial Intelligence – Inteligencia Artificial*) en V2 (*Version 2 – Versión 2*).

### Expediente inicial
Este componente reuniría la información estructurada del cliente antes de iniciar el servicio.

### Registro de trazabilidad
Permitirá conocer qué datos se recibieron, qué falta y qué revisión humana se realizó en cada paso.

### Dashboard futuro
Podría mostrar estados, pendientes y próximos pasos, pero todavía no está implementado.

## Arquitectura V1 implementable
La V1 se define como arquitectura mínima, realista y verificable.

Puede incluir:
- Documentación completa del flujo.
- Modelo conceptual de datos.
- Checklist inicial en formato simple.
- Ejemplo de expediente.
- Validación manual o semiautomática de campos mínimos.
- Clasificación inicial por reglas simples.
- Revisión humana obligatoria.

La V1 no debe depender de automatizaciones complejas ni de IA generativa funcional.

## Arquitectura V2 futura
Posibles ampliaciones futuras:
- Google Forms para entrada de datos.
- Google Sheets para registro operativo.
- Google Docs para generación documental.
- Google Drive para carpetas de cliente.
- Dashboard en HTML, CSS y JavaScript.
- Clasificación asistida mediante IA.
- Resúmenes operativos asistidos.
- Alertas básicas.
- Posible API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) futura si el proyecto crece.

Estas ampliaciones no están implementadas todavía.

## Datos previstos

### Datos de entrada
- Nombre del cliente.
- Datos de contacto.
- Empresa.
- Tipo de servicio solicitado.
- Necesidad principal.
- Documentación recibida.
- Observaciones iniciales.
- Prioridad estimada.
- Estado del checklist.

### Datos intermedios
- Campos completos.
- Campos pendientes.
- Nivel de prioridad.
- Tipo de cliente.
- Estado del expediente.
- Observaciones internas.

### Datos de salida
- Expediente inicial.
- Checklist de onboarding.
- Lista de datos pendientes.
- Clasificación inicial.
- Resumen operativo.
- Próximas acciones para revisión humana.

Todavía no existe tratamiento automatizado real de estos datos.

## Integraciones previstas

### Integraciones no existentes actualmente
- Google Workspace.
- Google Forms.
- Google Sheets.
- Google Docs.
- Google Drive.
- Modelos de lenguaje.
- API.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*) externo.

### Integraciones posibles en V2
- Entrada mediante formulario.
- Registro en hoja de cálculo.
- Generación documental.
- Organización de carpetas.
- Dashboard operativo.
- Resumen asistido con IA.

### Integraciones fuera de alcance inicial
- CRM completo.
- ERP (*Enterprise Resource Planning – Planificación de Recursos Empresariales*).
- Sistemas de pago.
- Firma digital.
- Integraciones críticas con datos reales de clientes.
- Automatizaciones irreversibles.

## Control humano
El agente debe mantener revisión humana en puntos clave:
- Confirmación de datos recibidos.
- Validación de información pendiente.
- Aprobación del expediente inicial.
- Revisión de clasificación.
- Decisión de iniciar el servicio.
- Corrección de errores o ambigüedades.

## Riesgos técnicos
- Automatizar un proceso todavía mal definido.
- Confundir documentación prevista con funcionalidad implementada.
- Prometer IA donde solo existen reglas o diseño.
- Depender demasiado pronto de integraciones externas.
- Crear una V1 demasiado grande.
- Tratar datos sensibles sin controles suficientes.
- Generar expedientes sin revisión humana.

## Fuera de alcance inicial
- Agente autónomo completo.
- Producción real.
- Multiempresa.
- Integraciones activas con clientes reales.
- Seguridad avanzada no implementada.
- Decisiones sensibles sin supervisión.
- Sustitución de criterio profesional.
- Automatizaciones irreversibles.
- CRM completo.
- ERP.
- Gestión legal, fiscal o contractual avanzada.

## Criterios de validación técnica
- ¿La arquitectura se entiende sin necesidad de código?
- ¿La V1 puede implementarse de forma mínima?
- ¿Está claro qué no existe todavía?
- ¿La V2 está planteada como evolución futura?
- ¿Hay revisión humana en puntos relevantes?
- ¿Se evitan promesas no verificables?
- ¿La arquitectura sirve para explicar un caso real de PYME?

## Próximos pasos técnicos
1. Completar el caso de uso funcional.
2. Completar el roadmap de evolución.
3. Definir después el modelo conceptual mínimo de datos para la V1.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
