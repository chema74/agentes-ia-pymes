# Agente de Control de Cobros y Flujo de Caja para PYMES

Agente documental para ordenar cobros pendientes, vencimientos, previsión operativa de entradas de dinero, riesgos de retraso y próximas acciones de seguimiento en una PYME (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

## Estado del agente

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Código funcional: no implementado todavía.
- Automatización de cobros: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- Google Workspace: no implementado todavía.
- ERP (*Enterprise Resource Planning – Planificación de Recursos Empresariales*): no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
- Conexión bancaria: no implementada todavía.
- Facturación real: no implementada todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.
- Datos ficticios de ejemplo: disponibles.

## Problema que aborda

Muchas PYMES controlan cobros y previsión de caja con hojas dispersas, correos y seguimiento manual. Eso dificulta ver qué está pendiente, qué está vencido, qué presenta riesgo y qué requiere seguimiento prioritario.

## Usuario objetivo

Responsables administrativos, equipos de operaciones y personas que coordinan la previsión básica de entradas de dinero sin convertir este trabajo en una herramienta financiera real.

## Objetivo funcional

Definir una base documental V1 implementable que permita describir cómo se ordenarían cobros, vencimientos, riesgos y acciones de seguimiento antes de cualquier desarrollo real.

## Alcance V1 implementable

- Documentar el flujo mínimo de entrada y revisión de cobros pendientes.
- Definir estados, riesgos y prioridades de seguimiento.
- Crear un modelo de datos conceptual reutilizable.
- Proporcionar una cartera ficticia para validación manual.
- Aportar datos de ejemplo en formato JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*).
- Mantener la revisión humana como control principal.

## Evolución V2 (*Version 2 – Versión 2*) futura

- Incorporar captura estructurada de cobros desde procesos internos.
- Añadir criterios de priorización más finos.
- Introducir métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*) de seguimiento.
- Preparar un dashboard funcional.
- Explorar integraciones cuando exista una base técnica estable.

## Fuera de alcance inicial

- Automatización real de cobros.
- Dashboard funcional.
- Google Workspace.
- ERP.
- CRM.
- API.
- Conexión bancaria.
- Facturación real.
- IA funcional.
- Integración con sistemas externos.
- Asesoramiento financiero, fiscal, contable o legal.

## Entradas previstas

- Cobros pendientes registrados manualmente.
- Referencias de cobro ficticias o internas.
- Vencimientos previstos.
- Riesgos de retraso.
- Acciones de seguimiento.
- Previsiones operativas de entrada.
- Observaciones internas.

## Salidas previstas

- Clasificación del cobro por estado.
- Priorización de seguimiento preliminar.
- Identificación de riesgos de retraso.
- Lista de acciones siguientes.
- Previsión operativa básica.
- Resultado de revisión humana.

## Documentación V1 disponible

- [Arquitectura](docs/ARQUITECTURA.md)
- [Caso de uso](docs/CASO_USO.md)
- [Roadmap](docs/ROADMAP.md)
- [Modelo de datos](docs/MODELO_DATOS.md)
- [Cartera de cobros ficticia](docs/CARTERA_COBROS_FICTICIA.md)
- [Flujo de validación de cobros](docs/FLUJO_VALIDACION_COBROS.md)

## Datos de ejemplo disponibles

- [cobros_flujo_caja_ficticios.json](datos_ejemplo/cobros_flujo_caja_ficticios.json)

## Criterios de validación

- La documentación debe describir una V1 implementable, no un sistema financiero ya operativo.
- Todas las entidades principales deben quedar definidas con sus campos mínimos.
- La cartera ficticia debe mostrar cobros, riesgos, acciones y previsiones coherentes.
- El flujo de validación debe poder ejecutarse manualmente.
- El JSON debe ser válido y consistente con la documentación.
- Debe quedar explícito que no existe automatización real ni integración viva.

## Próximos pasos

- Revisar la documentación con el resto del catálogo de agentes.
- Decidir más adelante si se construye una implementación mínima V1 o si se continúa con el agente 07.
- Mantener esta base como referencia documental de portfolio.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
