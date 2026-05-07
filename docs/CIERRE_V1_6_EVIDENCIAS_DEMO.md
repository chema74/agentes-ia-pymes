# Cierre V1.6 — Paquete Local de Evidencias de Demo

## Estado de cierre

La fase V1.6 añade la capacidad de empaquetar localmente evidencias demostrables del sistema para una demo revisable en entorno local.

## Qué añade V1.6

- exportador local de evidencias de demo,
- carpeta `salidas/evidencias_demo/`,
- índice Markdown de evidencias,
- índice HTML (*HyperText Markup Language – Lenguaje de Marcado de Hipertexto*) local de evidencias,
- copia de panel local,
- copia de informe consolidado,
- copia de informes disponibles por agente,
- generación opcional de ZIP (*ZIP archive – Archivo comprimido ZIP*),
- integración con la consola local,
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
- ejecutar agentes,
- revisar informes,
- consultar histórico,
- comparar informes,
- generar informe consolidado,
- exportar evidencias de demo.

También puede ejecutarse por consola:

```powershell
python scripts/exportar_evidencias_demo.py --crear-zip
```

## Qué incluye el paquete de evidencias

Puede incluir:

- `INDICE_EVIDENCIAS.md`,
- `INDICE_EVIDENCIAS.html`,
- `panel_local.html`,
- `informe_consolidado.md`,
- `informe_consolidado.html`,
- informes de agentes disponibles,
- ZIP (*ZIP archive – Archivo comprimido ZIP*) local si se usa `--crear-zip`.

## Qué no incluye

No incluye datos reales, no publica la web, no sube archivos automáticamente, no sustituye revisión humana y no convierte el sistema en una plataforma productiva.

## Validación

La validación global sigue siendo:

```powershell
python scripts/validar_repositorio.py
```

Y valida:

- JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) originales,
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
- el paquete de evidencias es local y queda dentro de `salidas/`, carpeta ignorada por Git.

## Valor para portfolio

La V1.6 demuestra:

- empaquetado local de evidencias,
- capacidad de demo revisable,
- trazabilidad operativa,
- separación entre datos, informes, históricos, comparaciones, consolidado y evidencias,
- madurez de consola local,
- validación reproducible,
- control de alcance y veracidad.

## Próximas fases posibles

Como evolución futura:

- exportación PDF,
- paquete de demo más visual,
- resumen ejecutivo automático local,
- filtros por decisión recomendada,
- métricas agregadas por agente,
- API local real,
- dashboard productivo,
- IA funcional,
- integración con Google Workspace,
- web pública de portfolio cuando el sistema esté suficientemente maduro.

## Decisión de cierre

La V1.6 queda cerrada cuando:

- el paquete de evidencias se genera por consola,
- la consola local permite exportarlo y cargar el índice,
- el ZIP local se puede crear,
- el panel local sigue funcionando,
- la validación global devuelve “Resultado final: validacion global correcta.”

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
