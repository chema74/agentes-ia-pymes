# Agente de Formación Interna para PYMES

Agente documental para ordenar contenidos internos de capacitación, perfiles de empleado, rutas formativas, módulos pendientes, responsables, evidencias y próximos pasos en una PYME (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

## Estado del agente

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Código funcional: no implementado todavía.
- LMS (*Learning Management System – Sistema de Gestión del Aprendizaje*) funcional: no implementado todavía.
- Automatización formativa: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- Google Workspace: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.
- Datos ficticios de ejemplo: disponibles.

## Problema que aborda

Muchas PYMES gestionan la formación interna con materiales dispersos, niveles distintos por empleado y rutas no estandarizadas. Eso dificulta saber qué está pendiente, qué debe revisarse y qué prioridad tiene cada contenido.

## Usuario objetivo

Responsables de formación interna, coordinación de equipos, operaciones y personas que necesitan una base documental clara para organizar capacitación antes de construir un LMS real.

## Objetivo funcional

Definir una base documental V1 implementable que permita describir cómo se ordenarían rutas formativas, módulos, perfiles, evidencias y acciones siguientes antes de cualquier desarrollo real.

## Alcance V1 implementable

- Documentar el flujo mínimo de entrada y revisión de contenidos formativos.
- Definir estados, perfiles y prioridades de forma homogénea.
- Crear un modelo de datos conceptual reutilizable.
- Proporcionar un plan formativo ficticio para validación manual.
- Aportar datos de ejemplo en formato JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*).
- Mantener la revisión humana como control principal.

## Evolución V2 (*Version 2 – Versión 2*) futura

- Incorporar captura estructurada de contenidos internos.
- Añadir reglas de priorización más finas.
- Introducir métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*) de seguimiento.
- Preparar un dashboard funcional.
- Explorar integraciones cuando exista una base técnica estable.

## Fuera de alcance inicial

- LMS real.
- Automatización formativa real.
- Dashboard funcional.
- Google Workspace.
- CRM.
- API.
- IA funcional.
- Integración con sistemas externos.
- Promesas de mejora garantizada o métricas de aprendizaje no verificadas.

## Entradas previstas

- Rutas formativas registradas manualmente.
- Perfiles internos.
- Módulos formativos.
- Evidencias de revisión o realización.
- Acciones formativas siguientes.
- Observaciones internas.

## Salidas previstas

- Clasificación de la ruta por estado.
- Priorización formativa preliminar.
- Detección de contenidos pendientes.
- Lista de acciones siguientes.
- Resultado de revisión humana.
- Resumen ficticio para tablero documental.

## Documentación V1 disponible

- [Arquitectura](docs/ARQUITECTURA.md)
- [Caso de uso](docs/CASO_USO.md)
- [Roadmap](docs/ROADMAP.md)
- [Modelo de datos](docs/MODELO_DATOS.md)
- [Plan formativo ficticio](docs/PLAN_FORMACION_FICTICIO.md)
- [Flujo de validación de formación](docs/FLUJO_VALIDACION_FORMACION.md)

## Datos de ejemplo disponibles

- [formacion_interna_ficticia.json](datos_ejemplo/formacion_interna_ficticia.json)

## Criterios de validación

- La documentación debe describir una V1 implementable, no una plataforma de formación ya operativa.
- Todas las entidades principales deben quedar definidas con sus campos mínimos.
- El plan ficticio debe mostrar rutas, módulos, perfiles, evidencias y acciones coherentes.
- El flujo de validación debe poder ejecutarse manualmente.
- El JSON debe ser válido y consistente con la documentación.
- Debe quedar explícito que no existe automatización real ni integración viva.

## Próximos pasos

- Revisar la documentación con el resto del catálogo de agentes.
- Decidir más adelante si se construye una implementación mínima V1 o si se continúa con el agente 09.
- Mantener esta base como referencia documental de portfolio.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
