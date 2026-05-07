# Ãndice Documental del Repositorio

## PropÃ³sito del Ã­ndice

Este documento sirve como guia de lectura y navegacion del repositorio. Su objetivo es ayudar a cualquier revisor a localizar rapido la documentacion global, la documentacion por agente, las evidencias tecnicas, la demo local y los documentos de cierre.

## Lectura recomendada para revisiÃ³n rÃ¡pida

1. `README.md`
2. `CATALOGO.md`
3. `docs/EVIDENCIAS_TECNICAS.md`
4. `docs/GUIA_DEMO_LOCAL.md`
5. `docs/CIERRE_TECNICO_V1.md`
6. `docs/CIERRE_V1_1_LOCAL_INTERACTIVA.md`
7. `docs/CIERRE_V1_2_EDICION_GUIADA.md`
8. `docs/CIERRE_V1_3_HISTORICO_LOCAL.md`

## DocumentaciÃ³n global

### `README.md`

Es la puerta de entrada del repositorio. Resume el enfoque general, el alcance actual y las referencias principales para entender la estructura del portfolio.

### `CATALOGO.md`

Recoge el catalogo funcional y documental del repositorio. Sirve para ubicar los agentes y entender la organizacion general antes de entrar en la documentacion especifica.

### `docs/VISION_GENERAL.md`

Expone la vision general del proyecto y su marco tecnico. Aporta contexto de alto nivel para interpretar que pretende mostrar el repositorio y que no.

### `docs/CRITERIOS_PORTFOLIO.md`

Define los criterios de presentacion del portfolio. Ayuda a mantener coherencia entre evidencia tecnica, limites actuales y forma de comunicar el trabajo.

### `docs/EVIDENCIAS_TECNICAS.md`

Resume que puede demostrarse hoy en el repositorio. Sirve para verificar scripts locales, pruebas `unittest`, JSON de ejemplo, validacion global y ausencia de dependencias externas.

### `docs/GUIA_DEMO_LOCAL.md`

Explica como ejecutar la demo local paso a paso. Es la guia practica para un revisor que quiera validar el repositorio desde la terminal.

### `docs/CIERRE_TECNICO_V1.md`

Describe el cierre tecnico de la V1 local. Deja constancia de lo que queda implementado, que limites mantiene el repositorio y como se separa la V1 de una futura evolucion.

### `docs/CIERRE_V1_1_LOCAL_INTERACTIVA.md`

Documenta el cierre de la capa local interactiva aÃ±adida sobre la V1 tecnica local. Resume consola local, espacio de trabajo editable, informes, panel HTML local, flujo operativo y limites actuales de esta fase.

## DocumentaciÃ³n por agente

Cada carpeta dentro de `agentes/` contiene `README`, documentacion V1, JSON ficticio, script local y pruebas `unittest` del agente correspondiente.

## Documentos de evidencia y validaciÃ³n

- `docs/EVIDENCIAS_TECNICAS.md` resume que puede demostrarse hoy y deja constancia de las evidencias tecnicas verificables.
- `docs/GUIA_DEMO_LOCAL.md` explica como ejecutar la demo local y como revisar el comportamiento minimo del repositorio.
- `scripts/validar_repositorio.py` valida los tests y los JSON de ejemplo, ademas de la coherencia tecnica minima del repositorio.
- `.github/workflows/validacion.yml` ejecuta la validacion tecnica en GitHub Actions para `push` y `pull_request`.

## QuÃ© leer segÃºn el objetivo del revisor

- Para entender el proyecto completo: `README.md` y `CATALOGO.md`.
- Para comprobar evidencias tecnicas: `docs/EVIDENCIAS_TECNICAS.md`.
- Para ejecutar la demo local: `docs/GUIA_DEMO_LOCAL.md`.
- Para revisar un agente concreto: la carpeta de ese agente dentro de `agentes/`.
- Para comprobar limites y fuera de alcance: `docs/CIERRE_TECNICO_V1.md`.
- Para revisar la capa local interactiva: `docs/CIERRE_V1_1_LOCAL_INTERACTIVA.md`. 
- Para revisar la fase V1.2: `docs/CIERRE_V1_2_EDICION_GUIADA.md`.
- Para revisar la fase V1.3: `docs/CIERRE_V1_3_HISTORICO_LOCAL.md`.

## LÃ­mites del repositorio actual

- No hay IA (*Artificial Intelligence - Inteligencia Artificial*) funcional.
- No hay API (*Application Programming Interface - Interfaz de ProgramaciÃ³n de Aplicaciones*) productiva.
- No hay dashboard productivo.
- No hay Google Workspace.
- No hay integraciones reales.
- No se trabaja con datos reales.
- No sustituye revision humana.

## Cierre

Este indice debe mantenerse actualizado si se aÃ±aden nuevas fases, scripts, documentacion o capas de interaccion local. Su funcion es ordenar la lectura documental y evitar interpretaciones confusas sobre el alcance actual.

## ðŸªª Licencia y AutorÃ­a

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
Â© 2025 â€“ Txema RÃ­os. Todos los derechos compartidos.




