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
- `python scripts/generar_panel_local.py --generar-informes --usar-datos-trabajo`

Las copias se guardan en `espacio_trabajo/` y esta carpeta esta ignorada por Git.
Los JSON originales de `agentes/*/datos_ejemplo/` no se modifican.

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
- `docs/INDICE_DOCUMENTAL.md`

El cierre de la capa local interactiva queda documentado en `docs/CIERRE_V1_1_LOCAL_INTERACTIVA.md`.

## Fuera de alcance actual

- Producto SaaS.
- Automatizacion real de procesos de negocio.
- Decisiones automaticas sobre clientes, personas, documentos, cobros o cumplimiento.
- Integracion con sistemas vivos.
- Servicios en red productivos.
- Uso de dependencias externas.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
