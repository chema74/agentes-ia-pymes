# Repositorio Técnico agentes-ia-pymes

[![CI](https://github.com/chema74/agentes-ia-pymes/actions/workflows/validacion.yml/badge.svg)](https://github.com/chema74/agentes-ia-pymes/actions/workflows/validacion.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

Portfolio técnico con 10 agentes locales para PYMES, construido en castellano y orientado a demostrar arquitectura modular, validación, trazabilidad, edición guiada, generación de evidencias y demo local reproducible.

El proyecto no pretende simular una plataforma productiva ni vender una automatización inexistente. Su objetivo es mostrar una base técnica manipulable, verificable y honesta: agentes locales, datos ficticios, pruebas, consola local, informes y evidencias generadas de forma reproducible.

---

## Qué demuestra

Este repositorio demuestra:

- arquitectura local separada por agentes;
- validación técnica de estructura y coherencia;
- separación entre datos originales y espacio de trabajo editable;
- ejecución reproducible de una demo local completa;
- generación de informes, evidencias y guion de demostración;
- trazabilidad entre agentes, salidas y documentación;
- alcance realista para portfolio técnico, sin promesas de automatización no implementada.

---

## Inicio rápido

Requisito: **Python 3.11 o superior**. No hay dependencias externas — solo biblioteca estándar.

```bash
# 1. Clonar el repositorio
git clone https://github.com/chema74/agentes-ia-pymes.git
cd agentes-ia-pymes

# 2. Validar que todo está en orden
python scripts/validar_repositorio.py

# 3. Ejecutar la demo local completa
python scripts/ejecutar_demo_local.py --crear-zip

# 4. Abrir la consola local de edición
python scripts/editor_espacio_trabajo.py
# → Disponible en http://127.0.0.1:8765/
```

---

## Qué contiene

El repositorio incluye:

- 10 agentes locales funcionales para PYMES;
- scripts por agente;
- tests por agente;
- tests transversales;
- validación global;
- consola local;
- edición guiada para los 10 agentes;
- histórico local de ejecuciones;
- comparador local de informes;
- informe consolidado local;
- paquete local de evidencias;
- demo local reproducible;
- guion local de demo;
- documentación de cierre técnico global.

---

## Cómo usarlo

```bash
# Paso 1 — Validar estructura y tests
python scripts/validar_repositorio.py

# Paso 2 — Demo completa con ZIP de evidencias
python scripts/ejecutar_demo_local.py --crear-zip

# Paso 3 — Consola local de edición guiada
python scripts/editor_espacio_trabajo.py

# Paso 4 — Revisar salidas generadas
# salidas/panel_local.html          → panel visual
# salidas/informe_consolidado.html  → informe unificado
# salidas/evidencias_demo.zip       → paquete de evidencias
# salidas/guion_demo_local.md       → guion de presentación
```

---

## Demo local completa

Recorrido recomendado para explicar el valor técnico del repositorio en menos de dos minutos:

```bash
python scripts/validar_repositorio.py
python scripts/ejecutar_demo_local.py --crear-zip
python scripts/editor_espacio_trabajo.py
# → http://127.0.0.1:8765/
```

---

## Salidas locales

Las salidas locales se generan en:

`salidas/`

El espacio de trabajo editable se genera en:

`espacio_trabajo/`

Ambas carpetas están ignoradas por Git. Esto evita mezclar evidencias locales, informes generados y copias de trabajo con el código fuente del repositorio.

---

## Evidencias generadas

La demo local completa puede generar:

- `salidas/panel_local.html`
- `salidas/informe_consolidado.md`
- `salidas/informe_consolidado.html`
- `salidas/evidencias_demo/`
- `salidas/evidencias_demo.zip`
- `salidas/guion_demo_local.md`
- `salidas/guion_demo_local.html`

Estas evidencias sirven para revisar el funcionamiento local del sistema sin convertirlo en una plataforma productiva.

---

## Límites actuales

El alcance actual está delimitado de forma explícita:

- no hay IA (*Artificial Intelligence – Inteligencia Artificial*) funcional;
- no hay API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) productiva;
- no hay dashboard productivo;
- no hay web pública;
- no hay Google Workspace;
- no hay integraciones reales;
- no se usan datos reales;
- no se persigue una automatización completa de negocio;
- no sustituye revisión humana.

---

## Relevancia para portfolio

Este repositorio es relevante como pieza de portfolio porque muestra:

- criterio de alcance;
- arquitectura modular;
- trazabilidad;
- reproducibilidad;
- separación entre datos originales y datos de trabajo;
- documentación de cierre;
- evidencias locales revisables;
- validación técnica sin dependencias externas;
- capacidad de convertir una idea de agentes en una demo local completa, ejecutable y verificable.

---

## Estado V2 en preparación

Este repositorio ha iniciado una fase V2 orientada a reforzar su valor como laboratorio local, demostrable y comprensible para empresas.

La V2 no convierte el proyecto en un producto SaaS (*Software as a Service – Software como Servicio*) ni en una plataforma productiva. Su objetivo es mejorar documentación, evidencias, ejecución local, límites declarados y lectura empresarial.

Documentación V2 inicial:

- Plan V2: [`docs/PLAN_V2_AGENTES_IA_PYMES.md`](docs/PLAN_V2_AGENTES_IA_PYMES.md)
- Mapa de evidencias V2: [`docs/MAPA_EVIDENCIAS_V2.md`](docs/MAPA_EVIDENCIAS_V2.md)
- Guía de ejecución V2: [`docs/GUIA_EJECUCION_V2.md`](docs/GUIA_EJECUCION_V2.md)
- Límites y alcance V2: [`docs/LIMITES_ALCANCE_V2.md`](docs/LIMITES_ALCANCE_V2.md)
- Resumen ejecutivo para empresas V2: [`docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md`](docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md)
- Checklist de validación V2: [`docs/CHECKLIST_VALIDACION_V2.md`](docs/CHECKLIST_VALIDACION_V2.md)

La rama de trabajo asociada es:

`v2-agentes-ia-pymes`

---

## Enlaces clave

- Cierre V1 local completa: `docs/CIERRE_V1_LOCAL_COMPLETA.md`
- Índice documental: `docs/INDICE_DOCUMENTAL.md`
- Catálogo de agentes: `CATALOGO.md`
- Evidencias técnicas: `docs/EVIDENCIAS_TECNICAS.md`
- Guía de presentación para portfolio: `docs/GUIA_PRESENTACION_PORTFOLIO.md`
- Capturas recomendadas: `docs/CAPTURAS_RECOMENDADAS.md`

---

## Documentación principal

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

---

## Fuera de alcance

Queda fuera del alcance actual:

- producto SaaS (*Software as a Service – Software como Servicio*);
- automatización real de negocio;
- decisiones automáticas sobre clientes, personas, documentos, cobros o cumplimiento;
- integración con sistemas vivos;
- servicios en red productivos;
- uso de dependencias externas;
- tratamiento de datos reales;
- sustitución de revisión humana.

---
## 🖼️ Material de portfolio

Este repositorio incluye una ficha pública y una selección de capturas preparadas para presentar la V1 local completa como proyecto técnico de portfolio.

- Ficha pública del proyecto: [`docs/FICHA_PUBLICA_PORTFOLIO.md`](docs/FICHA_PUBLICA_PORTFOLIO.md)
- Capturas de portfolio: [`docs/assets/capturas_portfolio/`](docs/assets/capturas_portfolio/)

Las capturas muestran la validación global, la consola local, la edición guiada, la ejecución de agentes, el informe consolidado y el paquete local de evidencias.

Este material tiene alcance demostrativo. El proyecto no incluye IA (*Artificial Intelligence – Inteligencia Artificial*) funcional, API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) productiva, dashboard productivo, Google Workspace, integraciones reales ni datos reales.



## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
