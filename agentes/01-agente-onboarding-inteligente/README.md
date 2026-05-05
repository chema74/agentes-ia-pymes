# Agente de Onboarding Inteligente para PYMES

## Descripcion breve
Este agente esta pensado para ordenar el alta inicial de clientes en PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*) mediante recogida estructurada de datos, checklist de onboarding, clasificacion inicial y preparacion de expediente. El enfoque actual es construir una base tecnica demostrable y documentada que permita estandarizar el proceso de entrada de clientes.

Su proposito es reducir ambiguedad operativa y mejorar trazabilidad desde el primer contacto. En esta etapa no se presenta como producto terminado, sino como una primera base de trabajo para evolucion progresiva.

## Estado del agente
- Fase documental inicial: completada para la base V1 (*Version 1 – Versión 1*).
- Diseño V1: preparado.
- Datos ficticios de ejemplo: disponibles.
- Codigo funcional minimo: implementado parcialmente.
- Automatizaciones: no implementadas todavia.
- Integraciones: no implementadas todavia.
- Dashboard: no implementado todavia.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavia.

## Documentacion V1 disponible
- [Modelo conceptual de datos](docs/MODELO_DATOS.md): define los datos minimos necesarios para la V1 y sirve como base conceptual previa a cualquier implementacion.
- [Checklist inicial de onboarding](docs/CHECKLIST_ONBOARDING.md): establece la lista operativa de verificacion para ordenar el alta inicial de clientes.
- [Expediente ficticio de cliente](docs/EXPEDIENTE_CLIENTE_FICTICIO.md): muestra un ejemplo completo y ficticio para validar el modelo, el checklist y la revision manual.
- [Flujo de validacion manual](docs/FLUJO_VALIDACION_MANUAL.md): describe el procedimiento minimo para revisar si un expediente puede avanzar.

## Datos de ejemplo disponibles
- [cliente_onboarding_ficticio.json](datos_ejemplo/cliente_onboarding_ficticio.json): archivo JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) con datos ficticios para validar documentalmente el modelo, el checklist y el flujo manual de la V1.

Este archivo no contiene datos reales, no implica automatizacion implementada y sirve como base para la implementacion minima local.

## Implementacion minima V1 disponible
Existe una primera implementacion local y verificable:

- `src/validar_expediente.py`

El script realiza las siguientes acciones:
- Carga el archivo JSON ficticio.
- Valida secciones principales del expediente.
- Revisa campos minimos del cliente.
- Cuenta documentos recibidos, pendientes e incompletos.
- Revisa items del checklist.
- Detecta pendientes y bloqueos.
- Genera un informe por consola.
- Recomienda una decision de revision humana.

Esta implementacion usa solo la biblioteca estandar de Python. No usa IA, no usa Google Workspace, no usa API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) externa, no crea archivos de salida y no sustituye la revision humana.

## Ejecucion local
El script debe ejecutarse desde la raiz del repositorio con este comando:

```bash
python agentes/01-agente-onboarding-inteligente/src/validar_expediente.py
```

## Resultado de validacion actual
Con el cliente ficticio disponible, la validacion actual produce este resumen:

- Cliente ficticio: Laura Martín.
- Empresa ficticia: Taller Creativo Bahía, S. L.
- Estado del onboarding: en_revision.
- Documentos recibidos: 1.
- Documentos pendientes: 1.
- Documentos incompletos: 1.
- Ítems completos: 7.
- Ítems pendientes: 1.
- Ítems obligatorios pendientes: 2.
- Ítems bloqueados: 2.
- Decisión recomendada de revision manual: bloquear.

Este resultado procede de datos ficticios y sirve solo para validar la V1 minima.

## Problema que aborda
El onboarding en muchas PYMES suele comenzar con informacion inicial dispersa y sin estructura operativa uniforme. Es habitual trabajar con correos y documentos sueltos, sin checklist claro ni trazabilidad minima de que datos faltan para avanzar.

Esto provoca inicios de proyecto sin expediente completo, retrabajo administrativo y dependencia de memoria, llamadas o seguimiento manual para cerrar pendientes criticos.

## Usuario objetivo
Este agente esta orientado a entornos como:
- Consultorias pequeñas.
- Agencias de servicios.
- Despachos profesionales.
- Formadores.
- Empresas de servicios recurrentes.
- Equipos internos de operaciones o administracion.

Esta pensado para organizaciones sin infraestructura tecnica compleja y con necesidad de ordenar su proceso de alta de clientes antes de escalar automatizaciones.

## Objetivo funcional
El objetivo funcional es ayudar a convertir una entrada de cliente desordenada en un expediente inicial mas claro, estructurado y revisable.

Este objetivo incluye:
- Recogida inicial de datos.
- Organizacion de informacion.
- Identificacion de datos pendientes.
- Checklist de onboarding.
- Preparacion de expediente.
- Revision humana antes de avanzar.

## Alcance V1 implementable
La V1 se plantea como una primera version pequeña, realista y verificable.

Incluye actualmente:
- Documentacion funcional y tecnica.
- Definicion del flujo basico.
- Checklist inicial de onboarding.
- Modelo conceptual de datos.
- Ejemplo de expediente de cliente.
- Validacion local minima con datos ficticios.
- Informe por consola para revision humana.

Esta V1 no implica todavia automatizacion completa ni IA generativa funcional.

## Evolucion V2 futura
La V2 (*Version 2 – Versión 2*) define una posible evolucion tecnica posterior.

Puede incluir:
- Formulario de entrada con Google Forms.
- Registro operativo en Google Sheets.
- Generacion documental con Google Docs.
- Carpetas de cliente en Google Drive.
- Dashboard operativo.
- Clasificacion inicial mediante reglas.
- Resumen asistido con IA.
- Alertas o avisos basicos.
- Evolucion hacia integracion con CRM (*Customer Relationship Management - Gestión de Relaciones con Clientes*) y conexion por API, cuando proceda.

Esta seccion describe posibilidades futuras y no funcionalidades implementadas.

## Fuera de alcance inicial
- Agente autonomo completo.
- Toma de decisiones sin revision humana.
- Despliegue productivo.
- Multiempresa real.
- Integraciones activas con clientes reales.
- Sustitucion de criterio profesional.
- Gestion legal, fiscal o contractual avanzada.
- Automatizaciones irreversibles.
- CRM completo.
- Dashboard.
- Google Workspace operativo.
- API externa.

## Entradas previstas
Entradas representadas actualmente en datos ficticios:
- Nombre del cliente.
- Datos de contacto.
- Tipo de servicio solicitado.
- Necesidad principal.
- Documentacion recibida.
- Prioridad inicial.
- Observaciones internas.
- Estado del checklist.

Todavia no existe sistema funcional de captura implementado.

## Salidas previstas
Salidas representadas actualmente por consola:
- Resumen del expediente inicial del cliente.
- Estado de documentacion.
- Estado del checklist de onboarding.
- Lista de datos pendientes.
- Bloqueos detectados.
- Decision recomendada para revision humana.

Todavia no existe generacion automatica de documentos, dashboard ni integracion real con clientes.

## Estructura documental del agente
- README.md
- docs/ARQUITECTURA.md
- docs/CASO_USO.md
- docs/ROADMAP.md
- datos_ejemplo/cliente_onboarding_ficticio.json
- src/validar_expediente.py
- requirements.txt
- .gitignore

## Criterios de validacion
- Se entiende que problema resuelve.
- La V1 puede ejecutarse localmente sin sobreingenieria.
- Esta claro que no esta implementado.
- La evolucion futura esta separada del alcance actual.
- El agente puede demostrarse con datos de ejemplo ficticios.
- Existe revision humana en puntos relevantes.

## Proximos pasos
1. Actualizar el roadmap del agente para reflejar la implementacion minima V1.
2. Crear despues una prueba basica del script con datos ficticios.
3. Hacer commit manual de la primera implementacion minima cuando la documentacion quede alineada.

## ðŸªª Licencia y AutorÃ­a

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
Â© 2025 â€“ Txema RÃ­os. Todos los derechos compartidos.
