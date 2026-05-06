# Caso de Uso

## Propósito del documento

Describir un caso ficticio realista para validar la documentación V1 (*Version 1 – Versión 1*) del Agente de Análisis de Mercado para PYMES.

## Estado del caso de uso

- Fase documental V1 (*Version 1 – Versión 1*): preparada.
- Automatización real: no implementada todavía.
- Dashboard funcional: no implementado todavía.
- IA (*Artificial Intelligence – Inteligencia Artificial*) funcional: no implementada todavía.

## Contexto empresarial

Una PYME de servicios quiere ordenar observaciones sobre competidores, demandas de clientes, cambios de precios, nuevos canales, nichos emergentes y riesgos de mercado, pero lo hace mediante notas sueltas y conversaciones internas.

## Situación inicial sin agente

Antes del agente, las señales de mercado llegan por canales distintos, no se clasifican de forma uniforme y las oportunidades o riesgos se evalúan de forma dispersa.

## Objetivo del caso de uso

Ordenar la observación de mercado mediante una base documental que permita clasificar señales, registrar competidores, detectar riesgos y dejar trazabilidad suficiente para validación humana.

## Actores implicados

- Responsable de negocio.
- Coordinación comercial.
- Persona que registra señales.
- Persona que revisa el análisis.
- Dirección de la PYME como observadora del estado general.

## Flujo funcional previsto

1. Se registra una señal de mercado con datos mínimos.
2. Se vincula la señal a un competidor, oportunidad o riesgo cuando aplique.
3. Se asigna estado y relevancia.
4. Se revisan oportunidades y riesgos derivados.
5. Se propone una acción de exploración.
6. Una persona valida el resultado y decide si avanza, si pide información o si bloquea la señal.

## Datos mínimos del caso

- Identificador de señal.
- Título de la señal.
- Descripción breve.
- Tipo de señal.
- Fuente observada.
- Área de impacto.
- Nivel de relevancia.
- Estado de la señal.
- Responsable de revisión.
- Observaciones internas.

## Tipos de señal de mercado

- demanda_cliente.
- competidor.
- precio.
- canal.
- tendencia.
- riesgo.
- oportunidad.

## Estados de oportunidad o riesgo

- nueva.
- en_revision.
- validada.
- descartada.
- bloqueada.

## Clasificación de mercado prevista

- Señales iniciales para observación general.
- Señales con relevancia media para revisión activa.
- Señales altas o críticas para seguimiento prioritario.
- Oportunidades de mercado asociadas a señales validadas.
- Riesgos de mercado con revisión humana obligatoria.
- Señales descartadas por falta de encaje o duplicidad.

## Resultado esperado en V1

La V1 debe dejar un caso de uso suficientemente claro para demostrar que una PYME puede ordenar su análisis de mercado sin software real, pero con una estructura de datos, estados y revisiones manuales coherente.

## Evolución V2 futura

- Entrada estructurada desde formularios.
- Seguimiento más fino por tipo de señal.
- Métricas de carga operativa.
- Dashboard funcional.
- Integraciones externas cuando exista una base técnica estable.

## Fuera de alcance inicial

- Extracción automática de fuentes.
- Scraping.
- CRM real.
- Google Workspace.
- API.
- IA funcional.
- Decisión autónoma.
- Asesoramiento estratégico garantizado o métricas de mercado no verificadas.

## Criterios de validación funcional

- El caso de uso debe poder explicarse sin ambigüedad.
- La señal debe tener tipo, relevancia y responsable.
- Las oportunidades y riesgos deben ser visibles y revisables.
- La clasificación debe ser comprensible para un equipo no técnico.
- El informe ficticio debe reflejar la misma lógica que este caso de uso.

## Próximos pasos

- Verificar que los datos de ejemplo respetan este caso ficticio.
- Mantener la validación humana como punto de control.
- Decidir más adelante si la V1 pasa a implementación mínima o si se prioriza el siguiente agente del catálogo.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
