# Cierre V1.2 — Edición Guiada Local

## Estado de cierre

La fase V1.2 completa la edición guiada para los 10 agentes dentro de la consola local del repositorio `agentes-ia-pymes`. Esta fase consolida una herramienta local manipulable para trabajar con datos ficticios, manteniendo el control de alcance y la revisión humana.

## Qué añade V1.2

- edición guiada para los 10 agentes,
- formularios locales por agente,
- conservación de edición JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) avanzada,
- guardado sobre copias locales en `espacio_trabajo/`,
- ejecución posterior de agentes con datos modificados,
- regeneración de informes y panel local,
- mantenimiento de los JSON originales intactos.

## Flujo operativo local

```powershell
python scripts/preparar_espacio_trabajo.py
python scripts/editor_espacio_trabajo.py
```

Abrir:

`http://127.0.0.1:8765/`

Desde ahí:

- seleccionar agente,
- cargar edición guiada,
- modificar campos,
- guardar,
- ejecutar agente,
- revisar informe,
- regenerar panel local.

## Agentes con edición guiada

- Agente 01 — Onboarding Inteligente.
- Agente 02 — Documental Inteligente.
- Agente 03 — Seguimiento de Clientes.
- Agente 04 — Generador de Propuestas.
- Agente 05 — Operaciones para PYMES.
- Agente 06 — Control de Cobros y Flujo de Caja.
- Agente 07 — Pipeline Comercial.
- Agente 08 — Formación Interna.
- Agente 09 — Análisis de Mercado.
- Agente 10 — Revisión y Cumplimiento.

Referencias de siglas aplicables al contexto documental:

- CRM (*Customer Relationship Management – Gestión de Relaciones con Clientes*),
- LMS (*Learning Management System – Sistema de Gestión del Aprendizaje*),
- RGPD (*General Data Protection Regulation – Reglamento General de Protección de Datos*).

## Qué se puede tocar

La edición guiada modifica copias locales en:

`espacio_trabajo/agente-XX/datos.json`

Los originales en:

`agentes/*/datos_ejemplo/`

no se modifican.

## Qué se puede visualizar

- resumen local de agentes,
- decisiones recomendadas extraídas de informes,
- informes en `salidas/agente-XX/informe.txt`,
- panel local en `salidas/panel_local.html`.

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
- no sustituye revisión humana.

## Valor para portfolio

La V1.2 ya demuestra:

- sistema local manipulable,
- edición guiada,
- separación entre datos originales y datos de trabajo,
- ejecución reproducible,
- validación global,
- visualización local,
- control de alcance y veracidad.

## Próximas fases posibles

Como evolución futura y fuera de alcance de V1.2:

- formularios más específicos por entidad interna,
- edición de listas internas desde interfaz,
- exportación de informes,
- comparación entre ejecuciones,
- histórico de cambios locales,
- API local real,
- dashboard productivo,
- IA funcional,
- integración con Google Workspace,
- web pública de portfolio cuando el sistema esté suficientemente maduro.

## Decisión de cierre

La V1.2 queda cerrada cuando:

- la consola local permite edición guiada de los 10 agentes,
- los agentes pueden ejecutarse con datos editados,
- los informes y panel local se regeneran,
- la validación global devuelve “Resultado final: validacion global correcta.”

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
