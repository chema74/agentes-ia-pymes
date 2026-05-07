# Repositorio Técnico `agentes-ia-pymes`

## Descripción breve

`agentes-ia-pymes` es un portfolio técnico con 10 agentes locales para PYMES. El repositorio muestra una base reproducible de validación, edición guiada, histórico, comparador, informe consolidado, evidencias y demo local, con revisión humana y datos ficticios.

## Qué demuestra

- Arquitectura local separada por agentes.
- Validación técnica de estructura y coherencia.
- Separación entre datos originales y espacio de trabajo.
- Flujo reproducible para demo y evidencias.
- Alcance realista para portfolio técnico, sin promesas de automatización no implementada.

## Inicio rápido

```powershell
python scripts/validar_repositorio.py
python scripts/ejecutar_demo_local.py --crear-zip
python scripts/editor_espacio_trabajo.py
```

URL local del editor:

`http://127.0.0.1:8765/`

## Qué contiene

- 10 agentes locales funcionales para PYMES.
- Scripts por agente.
- Tests por agente.
- Tests transversales.
- Validación global.
- Consola local.
- Edición guiada para los 10 agentes.
- Histórico local.
- Comparador local.
- Informe consolidado local.
- Paquete local de evidencias.
- Demo local reproducible.
- Guion local de demo.
- Documento de cierre técnico global.

## Cómo usarlo

1. Validar el repositorio con `python scripts/validar_repositorio.py`.
2. Ejecutar la demo local completa con `python scripts/ejecutar_demo_local.py --crear-zip`.
3. Abrir la consola local con `python scripts/editor_espacio_trabajo.py`.
4. Revisar `salidas/` para panel, informes, evidencias y guion.

## Salidas locales

Las salidas locales se generan en:

- `salidas/`
- `espacio_trabajo/`

Ambas carpetas están ignoradas por Git. Eso evita mezclar evidencias locales y copias de trabajo con el código fuente del repositorio.

## Evidencias generadas

La demo local completa genera, según el flujo ejecutado:

- `salidas/panel_local.html`
- `salidas/informe_consolidado.md`
- `salidas/informe_consolidado.html`
- `salidas/evidencias_demo/`
- `salidas/evidencias_demo.zip`
- `salidas/guion_demo_local.md`
- `salidas/guion_demo_local.html`

## Límites actuales

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de Programación de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay web pública.
- No hay Google Workspace.
- No hay integraciones reales.
- No se usan datos reales.
- No se persigue una automatización de negocio completa.

## Relevancia para portfolio

El repositorio es relevante para portfolio porque enseña:

- criterio de alcance,
- trazabilidad,
- reproducibilidad,
- separación entre origen y trabajo,
- documentación de cierre,
- evidencias locales revisables,
- validación técnica sin dependencias externas.

## Enlaces clave

- [Cierre V1 local completa](docs/CIERRE_V1_LOCAL_COMPLETA.md)
- [Índice documental](docs/INDICE_DOCUMENTAL.md)
- [Catálogo de agentes](CATALOGO.md)

## Documentación principal

- `docs/EVIDENCIAS_TECNICAS.md`
- `docs/GUIA_DEMO_LOCAL.md`
- `docs/CIERRE_TECNICO_V1.md`
- `docs/CIERRE_V1_1_LOCAL_INTERACTIVA.md`
- `docs/CIERRE_V1_2_EDICION_GUIADA.md`
- `docs/CIERRE_V1_3_HISTORICO_LOCAL.md`
- `docs/CIERRE_V1_4_COMPARADOR_LOCAL.md`
- `docs/CIERRE_V1_5_INFORME_CONSOLIDADO.md`
- `docs/CIERRE_V1_6_EVIDENCIAS_DEMO.md`
- `docs/CIERRE_V1_7_DEMO_LOCAL_REPRODUCIBLE.md`
- `docs/CIERRE_V1_LOCAL_COMPLETA.md`
- `docs/INDICE_DOCUMENTAL.md`

## Fuera de alcance

- Producto SaaS.
- Automatización real de negocio.
- Decisiones automáticas sobre clientes, personas, documentos, cobros o cumplimiento.
- Integración con sistemas vivos.
- Servicios en red productivos.
- Uso de dependencias externas.

## Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
