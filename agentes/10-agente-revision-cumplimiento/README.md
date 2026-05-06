# Agente de Revisión y Cumplimiento para PYMES

Agente documental para ordenar revisiones internas básicas, evidencias, documentos pendientes, riesgos operativos y acciones de seguimiento relacionadas con controles internos en una PYME (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

## Estado del agente

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Código funcional: no implementado todavía.
- Revisión automática: no implementada todavía.
- Motor normativo: no implementado todavía.
- Dashboard funcional: no implementado todavía.
- Google Workspace: no implementado todavía.
- ERP (*Enterprise Resource Planning – Planificación de Recursos Empresariales*): no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.
- Datos ficticios de ejemplo: disponibles.

## Problema que aborda

Muchas PYMES gestionan revisiones internas con listas dispersas, correos, documentos sueltos y seguimiento manual. Eso dificulta ver qué controles están pendientes, qué evidencias faltan, qué hallazgos requieren revisión y qué acciones de seguimiento conviene priorizar.

## Usuario objetivo

Responsables de operaciones internas, coordinación administrativa y perfiles que necesitan una base documental clara para organizar revisiones básicas de control interno antes de construir un sistema real.

## Objetivo funcional

Definir una base documental V1 implementable que permita describir cómo se ordenarían controles internos, evidencias, hallazgos, documentos pendientes y acciones de seguimiento antes de cualquier desarrollo real.

## Alcance V1 implementable

- Documentar el flujo mínimo de entrada y revisión de controles internos.
- Definir estados, prioridades y tipos de control de forma homogénea.
- Crear un modelo de datos conceptual reutilizable.
- Proporcionar una revisión ficticia para validación manual.
- Aportar datos de ejemplo en formato JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*).
- Mantener la validación humana como control principal.

## Evolución V2 (*Version 2 – Versión 2*) futura

- Incorporar captura estructurada de controles desde procesos internos.
- Añadir reglas de priorización más finas.
- Introducir métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*) de seguimiento.
- Preparar un dashboard funcional.
- Explorar integraciones cuando exista una base técnica estable.

## Fuera de alcance inicial

- Revisión automática real.
- Asesoramiento legal, fiscal, laboral, financiero o regulatorio.
- Motor normativo.
- Dashboard funcional.
- Google Workspace.
- ERP.
- CRM.
- API.
- IA funcional.
- Integración con sistemas externos.
- Garantía de cumplimiento normativo.
- Afirmaciones de que evita sanciones, riesgos legales o incumplimientos.

## Entradas previstas

- Controles internos registrados manualmente.
- Evidencias de revisión.
- Hallazgos internos.
- Documentos pendientes.
- Acciones de seguimiento.
- Observaciones internas.

## Salidas previstas

- Clasificación del control por estado.
- Priorización de revisión preliminar.
- Detección de hallazgos y documentos pendientes.
- Lista de acciones de seguimiento.
- Resultado de validación humana.

## Documentación V1 disponible

- [Arquitectura](docs/ARQUITECTURA.md)
- [Caso de uso](docs/CASO_USO.md)
- [Roadmap](docs/ROADMAP.md)
- [Modelo de datos](docs/MODELO_DATOS.md)
- [Revisión de cumplimiento ficticia](docs/REVISION_CUMPLIMIENTO_FICTICIA.md)
- [Flujo de validación de cumplimiento](docs/FLUJO_VALIDACION_CUMPLIMIENTO.md)

## Datos de ejemplo disponibles

- [revision_cumplimiento_ficticia.json](datos_ejemplo/revision_cumplimiento_ficticia.json)

## Criterios de validación

- La documentación debe describir una V1 implementable, no una herramienta de cumplimiento ya operativa.
- Todas las entidades principales deben quedar definidas con sus campos mínimos.
- La revisión ficticia debe mostrar controles, evidencias, hallazgos, documentos pendientes y acciones coherentes.
- El flujo de validación debe poder ejecutarse manualmente.
- El JSON debe ser válido y consistente con la documentación.
- Debe quedar explícito que no existe automatización real ni integración viva.

## Próximos pasos

- Revisar la documentación con el resto del catálogo de agentes.
- Mantener esta base como referencia documental de portfolio.
- El siguiente paso real es una revisión global del repositorio y la actualización de `README.md` y `CATALOGO.md` raíz cuando corresponda, sin sustituir asesoría profesional.

## Aviso de límites

Este agente no es asesoría legal, fiscal, laboral, financiera ni regulatoria. Tampoco garantiza cumplimiento normativo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
