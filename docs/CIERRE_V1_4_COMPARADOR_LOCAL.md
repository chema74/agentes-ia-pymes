# Cierre V1.4 — Comparador Local de Ejecuciones

## Estado de cierre

La fase V1.4 añade comparación local entre el último informe de un agente y un informe histórico anterior.
Se mantiene el alcance de herramienta local temporal con datos ficticios y revisión humana.

## Qué añade V1.4

- comparador local por consola,
- comparación desde la consola local,
- lectura del último informe,
- lectura de informes históricos,
- detección de cambio en la decisión recomendada,
- resumen de diferencias,
- diff textual mediante biblioteca estándar,
- mantenimiento de `salidas/` fuera de Git.

## Flujo operativo local

```powershell
python scripts/preparar_espacio_trabajo.py
python scripts/editor_espacio_trabajo.py
```

Abrir:

`http://127.0.0.1:8765/`

Desde la consola:

- editar datos,
- ejecutar agente,
- consultar histórico,
- seleccionar un informe histórico,
- comparar con el último informe.

También se puede operar por CLI (*Command Line Interface – Interfaz de Línea de Comandos*):

```powershell
python scripts/comparar_informes.py --agente 1 --archivo-historico NOMBRE_ARCHIVO
python scripts/comparar_informes.py --agente 1 --archivo-historico NOMBRE_ARCHIVO --solo-resumen
```

## Qué compara

Compara:

- `salidas/agente-XX/informe.txt`,
- `salidas/agente-XX/historico/NOMBRE_ARCHIVO`.

## Qué detecta

Puede mostrar:

- decisión recomendada actual,
- decisión recomendada histórica,
- si la decisión cambió,
- líneas añadidas,
- líneas eliminadas,
- diferencias textuales relevantes.

## Qué no compara

No compara automáticamente los JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) de trabajo.
No interpreta semánticamente los cambios y no usa IA (*Artificial Intelligence – Inteligencia Artificial*) funcional.
Solo compara texto de informes generados.

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

- no hay IA funcional,
- no hay API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) productiva,
- no hay dashboard productivo,
- no hay web pública,
- no hay Google Workspace,
- no hay integraciones reales,
- no se usan datos reales,
- no sustituye revisión humana,
- el histórico y las comparaciones son locales y están ignorados por Git.

## Valor para portfolio

La V1.4 demuestra:

- trazabilidad local,
- comparación manual asistida,
- madurez operativa,
- revisión de cambios entre ejecuciones,
- separación entre datos, informes, históricos y comparación,
- consola local manipulable,
- validación reproducible.

## Próximas fases posibles

Como evolución futura y fuera de alcance de V1.4:

- comparación automática de JSON de trabajo,
- resumen visual de diferencias,
- métricas agregadas por agente,
- filtros por decisión recomendada,
- exportación de comparaciones,
- API local real,
- dashboard productivo,
- IA funcional,
- integración con Google Workspace,
- web pública de portfolio cuando el sistema esté suficientemente maduro.

## Decisión de cierre

La V1.4 queda cerrada cuando:

- el comparador funciona por consola,
- la consola local permite comparar informes,
- los históricos siguen funcionando,
- el panel local sigue funcionando,
- la validación global devuelve “Resultado final: validacion global correcta.”

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
