# Agente Documental Inteligente para PYMES

## Descripción breve
Este agente está pensado para ayudar a una pequeña o mediana empresa a ordenar documentación interna, clasificar documentos y detectar documentación pendiente. Su propósito es preparar una base documental más trazable, con criterios claros sobre qué existe, qué falta y qué debe revisarse.

La fase documental V1 está preparada y sirve como base para una futura implementación mínima. El agente no se presenta como producto terminado y todavía no incluye código funcional ni automatización productiva.

## Estado del agente
- Estado actual: fase documental V1 preparada.
- Código funcional: no implementado todavía.
- Automatización documental: no implementada todavía.
- Integraciones: no implementadas todavía.
- Dashboard: no implementado todavía.
- Buscador semántico: no implementado todavía.
- OCR: no implementado todavía.
- RAG: no implementado todavía.
- Google Workspace: no implementado todavía.
- IA funcional: no implementada todavía.

## Documentación V1 disponible
- [Arquitectura conceptual](docs/ARQUITECTURA.md): describe la arquitectura prevista y los límites técnicos del agente documental.
- [Caso de uso funcional](docs/CASO_USO.md): define el escenario funcional previsto para una PYME con documentación dispersa.
- [Roadmap de evolución](docs/ROADMAP.md): separa fase documental, V1 implementable, validación interna, V2 futura y fuera de alcance.
- [Modelo conceptual de datos](docs/MODELO_DATOS.md): define entidades, campos mínimos y relaciones documentales para una futura V1.
- [Inventario documental ficticio](docs/INVENTARIO_DOCUMENTAL_FICTICIO.md): muestra un ejemplo documental inventado para validar el modelo.
- [Flujo de validación documental](docs/FLUJO_VALIDACION_DOCUMENTAL.md): describe una revisión manual mínima de documentos, estados, pendientes y acciones.

## Datos de ejemplo disponibles
- [inventario_documental_ficticio.json](datos_ejemplo/inventario_documental_ficticio.json): archivo JSON ficticio con documentos inventados, clasificaciones, versiones, pendientes, acciones y resultado de revisión manual.

Este JSON sirve para una futura validación mínima de V1. No es código funcional, no ejecuta automatizaciones y no implica buscador semántico, OCR, RAG, IA funcional, dashboard ni integración con Google Workspace.

## Problema que aborda
Muchas PYMES trabajan con documentación distribuida en carpetas compartidas, correos, discos locales o herramientas internas sin criterios homogéneos. Esto suele generar pérdida de tiempo, duplicidades y dificultad para saber qué documento es el vigente.

Problemas habituales:
- Documentos dispersos.
- Carpetas mal nombradas.
- Versiones duplicadas.
- Falta de criterios de clasificación.
- Dificultad para localizar información.
- Documentos pendientes sin control.
- Dependencia de una persona que recuerda dónde está cada archivo.
- Riesgo de trabajar con documentos obsoletos.

## Usuario objetivo
Este agente está orientado a perfiles y organizaciones como:
- Consultorías pequeñas.
- Despachos profesionales.
- Agencias de servicios.
- Empresas de formación.
- Gestorías.
- Equipos internos de administración.
- Empresas que trabajan con expedientes, propuestas, contratos, manuales o documentación recurrente.

Está pensado para empresas sin infraestructura técnica compleja, donde el primer valor está en ordenar la documentación antes de automatizarla.

## Objetivo funcional
El objetivo funcional es ayudar a convertir documentación desordenada en una estructura más clara, revisable y preparada para automatización futura.

Debe incluir:
- Inventario básico de documentos.
- Clasificación inicial.
- Identificación de documentos pendientes.
- Detección de duplicados conceptuales o versiones posibles.
- Preparación de una estructura documental.
- Revisión humana antes de cualquier decisión.

## Alcance V1 implementable
La V1 implementable futura debe ser pequeña, realista y verificable. Su objetivo no sería construir un sistema documental completo, sino validar con datos ficticios un flujo documental mínimo.

Puede incluir más adelante:
- Script o lógica mínima para procesar el JSON ficticio.
- Validación de campos obligatorios.
- Revisión de estados documentales.
- Detección simple de pendientes.
- Detección simple de posibles duplicados o versiones ambiguas.
- Informe por consola.

Esta V1 futura no implica todavía OCR funcional, RAG funcional, buscador semántico, dashboard, Google Workspace ni IA funcional.

## Evolución V2 futura
La V2 puede definir una evolución técnica posterior si la V1 mínima queda validada.

Puede incluir en el futuro:
- Registro documental en Google Sheets.
- Organización de carpetas en Google Drive.
- Generación de índice documental.
- Clasificación asistida con IA.
- Extracción futura de texto mediante OCR.
- Búsqueda documental asistida.
- Dashboard de estado documental.
- Integración futura con RAG.
- Alertas sobre documentación pendiente u obsoleta.

Esta sección describe posibilidades futuras, no funcionalidades implementadas.

## Fuera de alcance actual
- Sistema documental completo en producción.
- Buscador semántico funcional.
- RAG implementado.
- OCR implementado.
- Integración real con Google Drive.
- Tratamiento de documentación sensible real.
- Firma digital.
- Gestión legal avanzada.
- Sustitución de revisión humana.
- Control documental normativo completo.
- API pública.
- Multiempresa real.
- Automatización productiva.

## Estructura documental del agente
- README.md
- docs/ARQUITECTURA.md
- docs/CASO_USO.md
- docs/ROADMAP.md
- docs/MODELO_DATOS.md
- docs/INVENTARIO_DOCUMENTAL_FICTICIO.md
- docs/FLUJO_VALIDACION_DOCUMENTAL.md
- datos_ejemplo/inventario_documental_ficticio.json
- requirements.txt
- .gitignore

## Criterios de validación
- ¿Se entiende qué problema documental resuelve?
- ¿La V1 futura puede implementarse sin sobreingeniería?
- ¿Está claro qué no está implementado?
- ¿La evolución futura está separada del alcance actual?
- ¿El agente puede demostrarse con datos documentales ficticios?
- ¿Existe revisión humana en puntos relevantes?
- ¿No se promete IA documental inexistente?

## Próximos pasos
1. Validar el JSON de ejemplo.
2. Hacer commit manual de la fase documental V1 del agente 02.
3. Pasar después al agente 03.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
