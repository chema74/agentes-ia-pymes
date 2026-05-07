# Cierre V1.7 — Demo Local Reproducible

## Estado de cierre

La fase V1.7 añade un orquestador local para reconstruir la demo completa con un solo flujo de ejecucion.

## Qué añade V1.7

- demo local reproducible,
- preparacion del espacio de trabajo,
- ejecucion de los 10 agentes,
- generacion de informes,
- historico local,
- panel HTML (*HyperText Markup Language – Lenguaje de Marcado de Hipertexto*) local,
- informe consolidado,
- paquete de evidencias,
- ZIP (*ZIP archive – Archivo comprimido ZIP*) local opcional.

## Flujo operativo local

```powershell
python scripts/ejecutar_demo_local.py --crear-zip
```

```powershell
python scripts/ejecutar_demo_local.py --solo-validar
```

```powershell
python scripts/ejecutar_demo_local.py --sin-historico
```

## Qué genera

- `espacio_trabajo/`
- `salidas/agente-XX/informe.txt`
- `salidas/agente-XX/historico/`
- `salidas/panel_local.html`
- `salidas/informe_consolidado.md`
- `salidas/informe_consolidado.html`
- `salidas/evidencias_demo/`
- `salidas/evidencias_demo.zip`

Esta cadena opera con JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) originales solo como referencia de copia hacia espacio de trabajo editable.  
No incorpora IA (*Artificial Intelligence – Inteligencia Artificial*) funcional ni API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) productiva.

## Qué no hace

- no publica la web,
- no usa datos reales,
- no usa IA funcional,
- no sube archivos automaticamente,
- no integra Google Workspace,
- no convierte el sistema en plataforma productiva.

## Validación

La validacion global sigue siendo:

```powershell
python scripts/validar_repositorio.py
```

Valida JSON originales, tests por agente y tests transversales.

## Límites actuales

- no hay IA funcional,
- no hay API productiva,
- no hay dashboard productivo,
- no hay web publica,
- no hay Google Workspace,
- no hay integraciones reales,
- no se usan datos reales,
- no sustituye revision humana,
- la demo local es temporal y sus salidas quedan en carpetas ignoradas por Git.

## Valor para portfolio

La V1.7 demuestra reproducibilidad, orquestacion local, demo revisable, trazabilidad operativa y control de alcance sobre una cadena completa local.

## Próximas fases posibles

- modo demo guiado,
- exportacion PDF,
- metricas agregadas,
- panel ejecutivo local,
- API local real,
- dashboard productivo,
- IA funcional,
- integracion con Google Workspace,
- web publica cuando el sistema este suficientemente maduro.

## Decisión de cierre

La V1.7 queda cerrada cuando la demo local puede ejecutarse con un solo comando, genera panel, informe consolidado y evidencias, puede crear ZIP local, no toca JSON originales y la validacion global devuelve “Resultado final: validacion global correcta.”

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
