# Agente de Pipeline Comercial para PYMES

Agente documental para ordenar oportunidades comerciales, fases de venta, próximas acciones, bloqueos, temperatura comercial, prioridad y estado de avance en una PYME (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

## Estado del agente

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Código funcional: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*) funcional: no implementado todavía.
- Automatización comercial: no implementada todavía.
- Scoring automático: no implementado todavía.
- Dashboard funcional: no implementado todavía.
- Google Workspace: no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.
- Datos ficticios de ejemplo: disponibles.

## Problema que aborda

Muchas PYMES gestionan oportunidades comerciales con correos, llamadas, notas sueltas y hojas dispersas. Eso dificulta ver fases, temperatura, bloqueos, próximas acciones y prioridad real de seguimiento.

## Usuario objetivo

Equipos comerciales, coordinación de ventas y responsables de negocio que necesitan una base documental clara para clasificar oportunidades antes de construir un sistema real.

## Objetivo funcional

Definir una base documental V1 implementable que permita describir cómo se ordenarían oportunidades comerciales, interacciones, bloqueos y acciones siguientes antes de cualquier desarrollo real.

## Alcance V1 implementable

- Documentar el flujo mínimo de entrada y revisión de oportunidades comerciales.
- Definir fases, estados, temperatura y prioridades de forma homogénea.
- Crear un modelo de datos conceptual reutilizable.
- Proporcionar un pipeline comercial ficticio para validación manual.
- Aportar datos de ejemplo en formato JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*).
- Mantener la revisión humana como control principal.

## Evolución V2 (*Version 2 – Versión 2*) futura

- Incorporar captura estructurada de oportunidades desde procesos internos.
- Añadir reglas de priorización más finas.
- Introducir métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*) de seguimiento.
- Preparar un dashboard funcional.
- Explorar integraciones cuando exista una base técnica estable.

## Fuera de alcance inicial

- CRM real.
- Automatización comercial real.
- Scoring automático.
- Dashboard funcional.
- Google Workspace.
- API.
- IA funcional.
- Integración con sistemas externos.
- Asesoramiento comercial garantizado o métricas de conversión no verificadas.

## Entradas previstas

- Oportunidades comerciales registradas manualmente.
- Fases comerciales.
- Interacciones con clientes.
- Bloqueos comerciales.
- Priorización y temperatura.
- Próxima acción.
- Observaciones internas.

## Salidas previstas

- Clasificación de la oportunidad por estado.
- Priorización de seguimiento preliminar.
- Detección de bloqueos y oportunidades sin próxima acción.
- Lista de acciones siguientes.
- Clasificación comercial.
- Resultado de revisión humana.

## Documentación V1 disponible

- [Arquitectura](docs/ARQUITECTURA.md)
- [Caso de uso](docs/CASO_USO.md)
- [Roadmap](docs/ROADMAP.md)
- [Modelo de datos](docs/MODELO_DATOS.md)
- [Pipeline comercial ficticio](docs/PIPELINE_COMERCIAL_FICTICIO.md)
- [Flujo de validación del pipeline](docs/FLUJO_VALIDACION_PIPELINE.md)

## Datos de ejemplo disponibles

- [pipeline_comercial_ficticio.json](datos_ejemplo/pipeline_comercial_ficticio.json)

## Criterios de validación

- La documentación debe describir una V1 implementable, no un CRM ya operativo.
- Todas las entidades principales deben quedar definidas con sus campos mínimos.
- El pipeline ficticio debe mostrar oportunidades, interacciones, bloqueos, acciones y clasificaciones coherentes.
- El flujo de validación debe poder ejecutarse manualmente.
- El JSON debe ser válido y consistente con la documentación.
- Debe quedar explícito que no existe automatización real ni integración viva.

## Próximos pasos

- Revisar la documentación con el resto del catálogo de agentes.
- Decidir más adelante si se construye una implementación mínima V1 o si se continúa con el agente 08.
- Mantener esta base como referencia documental de portfolio.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
