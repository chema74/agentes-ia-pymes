# Caso de Uso del Agente de Onboarding Inteligente para PYMES

## Propósito del documento
Este documento describe el escenario funcional del agente 01 y cómo la V1 mínima permite validar el caso con datos ficticios. No presenta el agente como producto terminado ni como sistema conectado a clientes reales.

## Estado del caso de uso
- Caso de uso documentado: sí.
- Validación local con datos ficticios: disponible.
- Script de validación: `src/validar_expediente.py`.
- Datos ficticios: `datos_ejemplo/cliente_onboarding_ficticio.json`.
- Pruebas básicas: 4 tests con `unittest`.
- Cliente real: no existe.
- Automatización productiva: no existe.
- IA funcional: no existe.
- Google Workspace: no existe.
- Dashboard: no existe.
- API: no existe.
- Integración real con clientes: no existe.

## Contexto empresarial
El caso de uso parte de una PYME de servicios que recibe nuevos clientes con información inicial dispersa. El problema principal es ordenar los datos antes de empezar a trabajar para evitar retrabajo, vacíos de información y falta de trazabilidad.

## Situación inicial sin agente
- Datos repartidos entre correos, notas y documentos.
- Falta de una lista mínima de información necesaria.
- Inicio del trabajo sin saber qué falta.
- Repetición de preguntas al cliente.
- Retrasos por documentación incompleta.
- Dependencia de seguimiento manual.

## Objetivo del caso de uso
El objetivo es convertir una entrada desordenada en un expediente inicial revisable, con checklist, documentación clasificada por estado y decisión recomendada para revisión humana.

La V1 mínima ya permite validar este caso con datos ficticios mediante el script local.

## Flujo validable en V1
1. Se parte de un expediente ficticio en JSON.
2. El script local carga el expediente.
3. Se validan secciones principales.
4. Se revisan campos mínimos del cliente.
5. Se cuentan documentos recibidos, pendientes e incompletos.
6. Se revisa el checklist.
7. Se detectan pendientes y bloqueos.
8. Se imprime un informe por consola.
9. Se recomienda una decisión de revisión humana.

Este flujo no es una automatización productiva. Es una validación local reproducible con datos inventados.

## Resultado del ejemplo ficticio
El expediente ficticio de Laura Martín, de Taller Creativo Bahía, S. L., produce una decisión recomendada:

- Decisión recomendada de revisión manual: `bloquear`.

La decisión `bloquear` procede de reglas simples:
- Existen ítems bloqueados.
- Existen ítems obligatorios pendientes.
- La revisión humana sigue siendo necesaria antes de avanzar.

No procede de IA y no sustituye criterio profesional.

## Actores implicados
### Cliente ficticio
Aporta información inicial y documentación dentro del ejemplo inventado.

### Responsable interno
Revisa el informe, interpreta los bloqueos y decide qué hacer antes de avanzar.

### Script local
Ordena la validación mínima del expediente ficticio y genera una salida por consola. No actúa sobre sistemas reales.

## Entradas actuales
- Archivo JSON ficticio.
- Ruta opcional al archivo JSON.

No existe captura automática desde formularios, correo, Google Workspace ni sistemas externos.

## Salidas actuales
- Informe por consola.
- Código de salida del proceso.
- Decisión recomendada para revisión humana.

No se crean archivos de salida, documentos, dashboards ni registros en base de datos.

## Pruebas del caso de uso
El caso de uso se valida con `unittest` mediante cuatro pruebas:
- Ejecución sin argumentos.
- Ejecución con ruta explícita al JSON ficticio.
- Error por ruta inexistente.
- Error por JSON válido con estructura incompleta.

Estas pruebas confirman que la V1 mínima es reproducible en local sin dependencias externas.

## Fuera de alcance actual
- Cliente real.
- Datos reales.
- Automatización productiva.
- IA funcional.
- Google Workspace.
- Dashboard.
- API.
- Base de datos.
- Integración real con clientes.
- Decisiones sin revisión humana.
- Producción real.

## Evolución futura
Una V2 podría ampliar la entrada de datos, integrar herramientas externas o mejorar la presentación del estado del onboarding. Antes de implementar esas capacidades debe existir documentación específica, nuevos criterios de validación y pruebas adicionales.

## Próximos pasos
1. Mejorar casos de prueba si aparecen variantes del expediente.
2. Separar reglas si la lógica deja de ser pequeña.
3. Preparar una V2 documental antes de integrar Google Workspace u otros servicios.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
