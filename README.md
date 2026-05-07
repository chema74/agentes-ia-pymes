# Repositorio Tecnico agentes-ia-pymes

## Descripcion breve

`agentes-ia-pymes` es un portfolio tecnico con 10 agentes demostrables orientados a problemas habituales de pequenas y medianas empresas. El repositorio prioriza trazabilidad, alcance real y revision humana frente a promesas de automatizacion no implementada.

## Estado actual del repositorio

- Los 10 agentes tienen V1 tecnica local minima disponible.
- Cada agente incluye documentacion base, un archivo JSON (*JavaScript Object Notation - Notacion de Objetos de JavaScript*) ficticio, un script Python de consola y pruebas `unittest`.
- Toda la ejecucion actual funciona con biblioteca estandar de Python.
- La V1 actual valida estructura, estados e incidencias locales con datos ficticios y salida por consola.
- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programacion de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay Google Workspace.
- No hay integraciones reales.

## V1 implementada

La V1 implementada del repositorio consiste en una base tecnica local verificable:

- scripts de consola pequenos y didacticos,
- validacion de JSON ficticios por agente,
- reglas minimas de analisis operativo,
- informes en castellano con decision humana recomendada,
- pruebas `unittest` ejecutables por agente,
- validacion tecnica global del repositorio mediante `python scripts/validar_repositorio.py`,
- workflow de GitHub Actions para ejecutar esa validacion tecnica global,
- lanzador comun por consola en `scripts/ejecutar_agente.py` como punto de entrada unico para los 10 agentes.

Esta V1 no representa una suite productiva ni un sistema automatizado en produccion. Representa una primera base reproducible de portfolio tecnico.

## Validacion tecnica global

El repositorio incluye una capa transversal minima de validacion tecnica:

- `python scripts/validar_repositorio.py`
- comprobacion de los tests `unittest` de los 10 agentes
- validacion de los 10 archivos JSON de ejemplo
- ejecucion automatizable mediante GitHub Actions

## Panel HTML local estatico

Se puede generar un panel HTML local a partir de los informes del lanzador comun:

- `python scripts/generar_panel_local.py --generar-informes`
- `python scripts/generar_panel_local.py --directorio-salidas salidas`

El panel se guarda por defecto en `salidas/panel_local.html`.
La carpeta `salidas/` esta ignorada por Git.
Este panel es local y estatico; no es un dashboard productivo.

## Espacio de trabajo local editable

Se puede preparar una copia editable de los datos ficticios sin tocar los JSON originales del repositorio:

- `python scripts/preparar_espacio_trabajo.py`
- `python scripts/ejecutar_agente.py --agente 1 --usar-datos-trabajo`
- `python scripts/ejecutar_agente.py --todos --usar-datos-trabajo --guardar-salida`
- `python scripts/ejecutar_agente.py --agente 1 --guardar-historico`
- `python scripts/ejecutar_agente.py --todos --usar-datos-trabajo --guardar-historico`
- `python scripts/generar_panel_local.py --generar-informes --usar-datos-trabajo`

Las copias se guardan en `espacio_trabajo/` y esta carpeta esta ignorada por Git.
Los JSON originales de `agentes/*/datos_ejemplo/` no se modifican.

## Historico local de informes

El lanzador comun permite conservar informes anteriores con marca temporal sin perder `informe.txt` como ultimo informe:

- `python scripts/ejecutar_agente.py --agente 1 --guardar-historico`
- `python scripts/ejecutar_agente.py --todos --usar-datos-trabajo --guardar-historico`

Las copias historicas se guardan en `salidas/agente-XX/historico/`.
La carpeta `salidas/` esta ignorada por Git.

## Comparador local de informes

Se puede comparar el ultimo informe de un agente frente a un informe historico:

- `python scripts/comparar_informes.py --agente 1 --archivo-historico NOMBRE_ARCHIVO`

Compara `salidas/agente-XX/informe.txt` contra `salidas/agente-XX/historico/`.
Esta comparacion tambien esta disponible desde la consola local (`scripts/editor_espacio_trabajo.py`).

## Informe consolidado local

Se puede generar un informe consolidado de los 10 agentes a partir de `salidas/agente-XX/informe.txt`:

- `python scripts/generar_informe_consolidado.py`
- `python scripts/generar_informe_consolidado.py --generar-html`

Salidas por defecto:

- `salidas/informe_consolidado.md`
- `salidas/informe_consolidado.html` (si se usa `--generar-html`)

Esta consolidacion tambien esta disponible desde la consola local (`scripts/editor_espacio_trabajo.py`).

## Paquete local de evidencias de demo

Se puede exportar un paquete local de evidencias de demo:

- `python scripts/exportar_evidencias_demo.py --crear-zip`

Genera:

- `salidas/evidencias_demo/`
- `salidas/evidencias_demo.zip`

Tambien puede generarse desde la consola local (`scripts/editor_espacio_trabajo.py`).

## Demo local reproducible

Se puede ejecutar la cadena local completa con un solo comando:

- `python scripts/ejecutar_demo_local.py --crear-zip`

Esta demo local reproducible prepara `espacio_trabajo/`, ejecuta los 10 agentes, genera panel local, informe consolidado y evidencias de demo en `salidas/`.
No modifica JSON originales y no toca la web publica.

## Editor local del espacio de trabajo

Para editar los JSON de trabajo sin tocar los originales:

- `python scripts/preparar_espacio_trabajo.py`
- `python scripts/editor_espacio_trabajo.py`

URL por defecto del editor local: `http://127.0.0.1:8765/`.
Solo edita copias locales en `espacio_trabajo/`.
Los JSON originales en `agentes/*/datos_ejemplo/` no se modifican.
Es una herramienta local temporal; no es una API productiva ni un dashboard publico.

## Acciones desde el editor local

El editor local permite:

- cargar JSON de trabajo,
- usar una edicion guiada para campos clave de los 10 agentes,
- editar datos ficticios,
- formatear JSON,
- validar y guardar,
- ver resumen de los 10 agentes,
- ejecutar agente seleccionado,
- ejecutar todos los agentes,
- cargar informes,
- regenerar panel HTML local.

Puedes definir directorios al arrancar:

`python scripts/editor_espacio_trabajo.py --directorio-trabajo espacio_trabajo --directorio-salidas salidas`

## Documentacion principal

- `docs/EVIDENCIAS_TECNICAS.md`
- `docs/GUIA_DEMO_LOCAL.md`
- `docs/CIERRE_TECNICO_V1.md`
- `docs/CIERRE_V1_1_LOCAL_INTERACTIVA.md`
- `docs/CIERRE_V1_2_EDICION_GUIADA.md`
- `docs/CIERRE_V1_3_HISTORICO_LOCAL.md`
- `docs/CIERRE_V1_4_COMPARADOR_LOCAL.md`
- `docs/CIERRE_V1_5_INFORME_CONSOLIDADO.md`
- `docs/CIERRE_V1_6_EVIDENCIAS_DEMO.md`
- `docs/INDICE_DOCUMENTAL.md`

El cierre de la capa local interactiva queda documentado en `docs/CIERRE_V1_1_LOCAL_INTERACTIVA.md`.
El cierre de la fase de edicion guiada local completa queda documentado en `docs/CIERRE_V1_2_EDICION_GUIADA.md`. 
El cierre de la fase V1.3 de historico local de ejecuciones queda documentado en `docs/CIERRE_V1_3_HISTORICO_LOCAL.md`. 
Los historicos locales de informes se guardan en `salidas/agente-XX/historico/`.
El cierre de la fase V1.4 de comparador local de ejecuciones queda documentado en `docs/CIERRE_V1_4_COMPARADOR_LOCAL.md`.
El comparador local por CLI usa `scripts/comparar_informes.py`.
El cierre de la fase V1.5 de informe consolidado local queda documentado en `docs/CIERRE_V1_5_INFORME_CONSOLIDADO.md`.
La generacion por CLI del informe consolidado local usa `scripts/generar_informe_consolidado.py`.
El cierre de la fase V1.6 de paquete local de evidencias de demo queda documentado en `docs/CIERRE_V1_6_EVIDENCIAS_DEMO.md`.
La exportacion por CLI del paquete local de evidencias usa `scripts/exportar_evidencias_demo.py`.

## Fuera de alcance actual

- Producto SaaS.
- Automatizacion real de procesos de negocio.
- Decisiones automaticas sobre clientes, personas, documentos, cobros o cumplimiento.
- Integracion con sistemas vivos.
- Servicios en red productivos.
- Uso de dependencias externas.

## ðŸªª Licencia y AutorÃ­a

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
Â© 2025 â€“ Txema RÃ­os. Todos los derechos compartidos.



