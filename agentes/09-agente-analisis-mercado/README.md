# Agente de Análisis de Mercado para PYMES

Agente documental para ordenar señales de mercado, competidores, oportunidades, riesgos, observaciones comerciales y posibles acciones de exploración en una PYME (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

## Estado del agente

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Código funcional: no implementado todavía.
- Extracción automática de fuentes: no implementada todavía.
- Scraping: no implementado todavía.
- Dashboard funcional: no implementado todavía.
- Google Workspace: no implementado todavía.
- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*): no implementado todavía.
- API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*): no implementada todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.
- Datos ficticios de ejemplo: disponibles.

## Problema que aborda

Muchas PYMES anotan señales de mercado en notas sueltas, conversaciones internas o correos dispersos. Eso dificulta distinguir competidores, oportunidades, riesgos y acciones de exploración de forma ordenada.

## Usuario objetivo

Responsables de negocio, coordinación comercial y perfiles que necesitan una base documental clara para clasificar información de mercado antes de construir un sistema real.

## Objetivo funcional

Definir una base documental V1 implementable que permita describir cómo se ordenarían señales de mercado, competidores, oportunidades, riesgos y acciones de exploración antes de cualquier desarrollo real.

## Alcance V1 implementable

- Documentar el flujo mínimo de entrada y revisión de señales de mercado.
- Definir tipos de señal, relevancia y estados de forma homogénea.
- Crear un modelo de datos conceptual reutilizable.
- Proporcionar un informe de mercado ficticio para validación manual.
- Aportar datos de ejemplo en formato JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*).
- Mantener la validación humana como control principal.

## Evolución V2 (*Version 2 – Versión 2*) futura

- Incorporar captura estructurada de señales desde procesos internos.
- Añadir reglas de priorización más finas.
- Introducir métricas operativas y KPI (*Key Performance Indicator – Indicador Clave de Rendimiento*) de seguimiento.
- Preparar un dashboard funcional.
- Explorar integraciones cuando exista una base técnica estable.

## Fuera de alcance inicial

- Extracción automática de fuentes.
- Scraping.
- Dashboard funcional.
- Google Workspace.
- CRM.
- API.
- Conexión a datos reales.
- IA funcional.
- Integración con sistemas externos.
- Asesoramiento estratégico garantizado o métricas de mercado no verificadas.

## Entradas previstas

- Señales de mercado registradas manualmente.
- Competidores observados.
- Oportunidades detectadas.
- Riesgos de mercado.
- Observaciones comerciales.
- Acciones de exploración.

## Salidas previstas

- Clasificación de la señal por tipo y estado.
- Priorización de observaciones preliminar.
- Detección de oportunidades y riesgos.
- Lista de acciones de exploración.
- Resultado de validación humana.

## Documentación V1 disponible

- [Arquitectura](docs/ARQUITECTURA.md)
- [Caso de uso](docs/CASO_USO.md)
- [Roadmap](docs/ROADMAP.md)
- [Modelo de datos](docs/MODELO_DATOS.md)
- [Informe de mercado ficticio](docs/INFORME_MERCADO_FICTICIO.md)
- [Flujo de validación de mercado](docs/FLUJO_VALIDACION_MERCADO.md)

## Datos de ejemplo disponibles

- [analisis_mercado_ficticio.json](datos_ejemplo/analisis_mercado_ficticio.json)

## Criterios de validación

- La documentación debe describir una V1 implementable, no una herramienta de análisis ya operativa.
- Todas las entidades principales deben quedar definidas con sus campos mínimos.
- El informe ficticio debe mostrar señales, competidores, oportunidades, riesgos y acciones coherentes.
- El flujo de validación debe poder ejecutarse manualmente.
- El JSON debe ser válido y consistente con la documentación.
- Debe quedar explícito que no existe automatización real ni integración viva.

## Próximos pasos

- Revisar la documentación con el resto del catálogo de agentes.
- Decidir más adelante si se construye una implementación mínima V1 o si se continúa con el agente 10.
- Mantener esta base como referencia documental de portfolio.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
