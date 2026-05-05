# Agente de Onboarding Inteligente para PYMES

## Descripción breve
Este agente está pensado para ordenar el alta inicial de clientes en pequeñas y medianas empresas mediante recogida estructurada de datos, checklist de onboarding, clasificación inicial y preparación de expediente. El enfoque actual es construir una base técnica demostrable y documentada que permita estandarizar el proceso de entrada de clientes. Su propósito es reducir ambigüedad operativa y mejorar trazabilidad desde el primer contacto. En esta etapa no se presenta como producto terminado, sino como marco inicial de trabajo para evolución progresiva.

## Estado del agente
- Fase documental inicial: activa.
- Diseño V1: en preparación avanzada.
- Código funcional: no implementado todavía.
- Automatizaciones: no implementadas todavía.
- Integraciones: no implementadas todavía.
- Dashboard: no implementado todavía.
- IA funcional: no implementada todavía.
- Datos ficticios de ejemplo: disponibles.

## Documentación V1 disponible
- [Modelo conceptual de datos](docs/MODELO_DATOS.md): define los datos mínimos necesarios para la V1 y sirve como base conceptual previa a cualquier implementación.
- [Checklist inicial de onboarding](docs/CHECKLIST_ONBOARDING.md): establece la lista operativa de verificación para ordenar el alta inicial de clientes.
- [Expediente ficticio de cliente](docs/EXPEDIENTE_CLIENTE_FICTICIO.md): muestra un ejemplo completo y ficticio para validar el modelo, el checklist y la revisión manual.
- [Flujo de validación manual](docs/FLUJO_VALIDACION_MANUAL.md): describe el procedimiento mínimo para revisar si un expediente puede avanzar.

## Datos de ejemplo disponibles
- [cliente_onboarding_ficticio.json](datos_ejemplo/cliente_onboarding_ficticio.json): archivo JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) con datos ficticios para validar documentalmente el modelo, el checklist y el flujo manual de la V1.

Este archivo no contiene datos reales, no es código funcional, no implica automatización implementada y sirve como base para una futura implementación mínima.

## Problema que aborda
El onboarding en muchas PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*) suele comenzar con información inicial dispersa y sin estructura operativa uniforme. Es habitual trabajar con correos y documentos sueltos, sin checklist claro ni trazabilidad mínima de qué datos faltan para avanzar. Esto provoca inicios de proyecto sin expediente completo, retrabajo administrativo y dependencia de memoria, llamadas o seguimiento manual para cerrar pendientes críticos.

## Usuario objetivo
Este agente está orientado a entornos como:
- Consultorías pequeñas.
- Agencias de servicios.
- Despachos profesionales.
- Formadores.
- Empresas de servicios recurrentes.
- Equipos internos de operaciones o administración.

Está pensado para organizaciones sin infraestructura técnica compleja y con necesidad de ordenar su proceso de alta de clientes antes de escalar automatizaciones.

## Objetivo funcional
El objetivo funcional es ayudar a convertir una entrada de cliente desordenada en un expediente inicial más claro, estructurado y revisable.

Este objetivo incluye:
- Recogida inicial de datos.
- Organización de información.
- Identificación de datos pendientes.
- Checklist de onboarding.
- Preparación de expediente.
- Revisión humana antes de avanzar.

## Alcance V1 implementable
La V1 (*Version 1 – Versión 1*) se plantea como una primera versión pequeña, realista y verificable.

Puede incluir:
- Documentación funcional y técnica.
- Definición del flujo básico.
- Checklist inicial de onboarding.
- Modelo conceptual de datos.
- Ejemplo de expediente de cliente.
- Validación manual de campos mínimos.
- Preparación para automatización futura.

Esta V1 no implica todavía automatización completa ni IA (*Artificial Intelligence – Inteligencia Artificial*) generativa funcional.

## Evolución V2 futura
La V2 (*Version 2 – Versión 2*) define una posible evolución técnica posterior.

Puede incluir:
- Formulario de entrada con Google Forms.
- Registro operativo en Google Sheets.
- Generación documental con Google Docs.
- Carpetas de cliente en Google Drive.
- Dashboard operativo.
- Clasificación inicial mediante reglas.
- Resumen asistido con IA.
- Alertas o avisos básicos.
- Evolución hacia integración con CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*) y conexión por API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*), cuando proceda.

Esta sección describe posibilidades futuras y no funcionalidades implementadas.

## Fuera de alcance inicial
- Agente autónomo completo.
- Toma de decisiones sin revisión humana.
- Despliegue productivo.
- Multiempresa real.
- Integraciones activas con clientes reales.
- Sustitución de criterio profesional.
- Gestión legal, fiscal o contractual avanzada.
- Automatizaciones irreversibles.
- CRM completo.

## Entradas previstas
Posibles entradas futuras:
- Nombre del cliente.
- Datos de contacto.
- Tipo de servicio solicitado.
- Necesidad principal.
- Documentación recibida.
- Prioridad inicial.
- Observaciones internas.
- Estado del checklist.

Todavía no existe sistema funcional de captura implementado.

## Salidas previstas
Posibles salidas futuras:
- Expediente inicial del cliente.
- Checklist de onboarding.
- Lista de datos pendientes.
- Clasificación inicial.
- Resumen operativo.
- Próximas acciones recomendadas para revisión humana.

Todavía no existe generación automática implementada.

## Estructura documental del agente
- README.md
- docs/ARQUITECTURA.md
- docs/CASO_USO.md
- docs/ROADMAP.md
- requirements.txt
- .gitignore

## Criterios de validación
- ¿Se entiende qué problema resuelve?
- ¿La V1 puede implementarse sin sobreingeniería?
- ¿Está claro qué no está implementado?
- ¿La evolución futura está separada del alcance actual?
- ¿El agente puede demostrarse con datos de ejemplo?
- ¿Existe revisión humana en puntos relevantes?

## Próximos pasos
1. Revisar la coherencia documental completa del agente 01.
2. Preparar después una primera implementación mínima si la documentación queda validada.
3. Hacer commit manual de la fase documental V1 cuando se revise el estado del repositorio.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
