# Cierre V1 - Demo Local Completa

## Estado de cierre

La V1 local completa queda cerrada como demo técnica manipulable, reproducible y validada. El repositorio puede explicarse y revisarse en local sin tocar la web pública y sin depender de servicios externos.

## Capacidades incluidas

- 10 agentes locales.
- scripts por agente.
- tests por agente.
- validación global.
- consola local.
- edición guiada.
- histórico local.
- comparador local.
- informe consolidado.
- paquete de evidencias.
- demo local reproducible.
- guion local de demo.

## Flujo de uso recomendado

El flujo recomendado consiste en validar primero el repositorio, ejecutar después la demo local completa con un solo comando y abrir por último la consola local para recorrer edición, informes, histórico, comparador, evidencias y guion. Ese recorrido deja clara la separación entre datos originales y datos de trabajo.

## Comando principal de demo

```powershell
python scripts/ejecutar_demo_local.py --crear-zip
```

## Consola local

```powershell
python scripts/editor_espacio_trabajo.py
```

Abrir:

`http://127.0.0.1:8765/`

## Evidencias generadas

- `salidas/panel_local.html`
- `salidas/informe_consolidado.md`
- `salidas/informe_consolidado.html`
- `salidas/evidencias_demo/`
- `salidas/evidencias_demo.zip`
- `salidas/guion_demo_local.md`
- `salidas/guion_demo_local.html`

## Validación

```powershell
python scripts/validar_repositorio.py
```

La validación comprueba:

- JSON originales,
- tests por agente,
- tests transversales.

## Límites actuales

- no hay IA funcional,
- no hay API productiva,
- no hay dashboard productivo,
- no hay web pública,
- no hay Google Workspace,
- no hay integraciones reales,
- no se usan datos reales,
- no sustituye revisión humana.

## Valor para portfolio

Esta V1 demuestra arquitectura local, automatización reproducible, trazabilidad, separación entre datos originales y datos de trabajo, evidencias revisables, pruebas, control de alcance y madurez técnica sin ruido comercial.

## Qué queda fuera de alcance

- datos reales,
- IA funcional,
- API productiva,
- dashboard productivo,
- despliegue web,
- Google Workspace,
- integraciones reales.

## Próximas fases posibles

- capturas para portfolio,
- README final de alto impacto,
- panel ejecutivo local más visual,
- exportación PDF,
- API local real,
- dashboard productivo,
- IA funcional,
- Google Workspace,
- publicación web cuando el sistema esté suficientemente maduro.

## Decisión de cierre

La V1 local queda cerrada cuando:

- la demo local se ejecuta con un solo comando,
- genera panel, informe consolidado, evidencias y guion,
- no toca JSON originales,
- la validación global devuelve `Resultado final: validacion global correcta.`

## Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
