# Cierre V1.3 — Histórico Local de Ejecuciones

## Estado de cierre

La fase V1.3 añade conservación de informes históricos locales por agente dentro del repositorio `agentes-ia-pymes`.
Se mantiene el enfoque de herramienta local con datos ficticios, trazabilidad técnica y revisión humana.

## Qué añade V1.3

- guardado del último informe en `salidas/agente-XX/informe.txt`,
- guardado de informes históricos en `salidas/agente-XX/historico/`,
- ejecución con histórico desde el lanzador común,
- consulta del histórico desde la consola local,
- carga de informes históricos concretos,
- mantenimiento de `espacio_trabajo/` y `salidas/` fuera de Git.

## Flujo operativo local

```powershell
python scripts/preparar_espacio_trabajo.py
python scripts/editor_espacio_trabajo.py
```

Abrir:

`http://127.0.0.1:8765/`

Desde la consola:

- editar datos,
- guardar cambios,
- ejecutar agente,
- consultar último informe,
- consultar histórico,
- regenerar panel local.

También se puede operar por CLI (*Command Line Interface – Interfaz de Línea de Comandos*):

```powershell
python scripts/ejecutar_agente.py --agente 1 --guardar-historico
python scripts/ejecutar_agente.py --todos --usar-datos-trabajo --guardar-historico
```

## Dónde se guardan los resultados

- último informe: `salidas/agente-XX/informe.txt`,
- histórico: `salidas/agente-XX/historico/YYYYMMDD-HHMMSS-informe.txt`,
- panel local: `salidas/panel_local.html`.

## Qué se conserva y qué no

El histórico local conserva informes de ejecuciones locales.
No versiona automáticamente JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) de trabajo ni sustituye Git como control de versiones.

## Validación

La validación global sigue siendo:

```powershell
python scripts/validar_repositorio.py
```

Y valida:

- JSON originales,
- tests por agente,
- tests transversales.

## Límites actuales

- no hay IA (*Artificial Intelligence – Inteligencia Artificial*) funcional,
- no hay API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) productiva,
- no hay dashboard productivo,
- no hay web pública,
- no hay Google Workspace,
- no hay integraciones reales,
- no se usan datos reales,
- no sustituye revisión humana,
- el histórico es local y está ignorado por Git.

## Valor para portfolio

La V1.3 demuestra:

- trazabilidad local,
- comparación manual entre ejecuciones,
- madurez operativa,
- separación entre datos de ejemplo, datos de trabajo e informes,
- consola local manipulable,
- validación reproducible.

## Próximas fases posibles

Como evolución futura y fuera de alcance de V1.3:

- comparación automática entre informes,
- histórico de cambios en JSON de trabajo,
- exportación de informes,
- filtros por agente o decisión recomendada,
- métricas locales agregadas,
- API local real,
- dashboard productivo,
- IA funcional,
- integración con Google Workspace,
- web pública de portfolio cuando el sistema esté suficientemente maduro.

## Decisión de cierre

La V1.3 queda cerrada cuando:

- los agentes pueden ejecutarse con histórico local,
- la consola permite consultar informes históricos,
- el panel local sigue funcionando,
- la validación global devuelve “Resultado final: validacion global correcta.”

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
