# Guía de Demo Local

## Objetivo de la demo

Esta demo local permite comprobar de forma rápida y honesta la estructura técnica del repositorio, los scripts de consola, los datos ficticios y las pruebas `unittest`. El objetivo es facilitar una revisión humana clara de lo que funciona hoy, sin presentar el repositorio como IA (*Artificial Intelligence – Inteligencia Artificial*) funcional ni como automatización productiva.

## Requisitos previos

- Python instalado.
- Git instalado.
- Terminal PowerShell en Windows.
- No se necesitan dependencias externas.
- No se necesita instalar paquetes.

## Preparar el entorno

```powershell
cd C:\Users\txema\Documents\agentes-ia-pymes
python --version
git status --short
```

## Validación global recomendada

El comando principal de la demo es:

```powershell
python scripts/validar_repositorio.py
```

Este comando valida:

- Los 10 JSON (*JavaScript Object Notation – Notación de Objetos de JavaScript*) de ejemplo.
- Los tests `unittest` de los 10 agentes.
- La coherencia técnica mínima del repositorio.

## Ejecutar un agente individual

Cada agente se puede ejecutar por consola para comprobar su salida local. Ejemplos representativos:

```powershell
python agentes/01-agente-onboarding-inteligente/src/validar_expediente.py
python agentes/06-agente-control-cobros-flujo-caja/src/validar_cobros_flujo_caja.py
python agentes/10-agente-revision-cumplimiento/src/validar_revision_cumplimiento.py
```

## Ejecutar tests de un agente individual

También se puede validar cada agente con `unittest` de forma aislada:

```powershell
python -m unittest discover -s agentes/01-agente-onboarding-inteligente/tests
python -m unittest discover -s agentes/06-agente-control-cobros-flujo-caja/tests
python -m unittest discover -s agentes/10-agente-revision-cumplimiento/tests
```

## Qué debe observar el revisor

El revisor debe ver informes por consola, decisiones humanas recomendadas, avisos de límites cuando aplique, tests `OK`, JSON válidos y una validación global correcta. La lectura esperable es la de una base técnica verificable, no la de un sistema autónomo completo.

## Qué no demuestra esta demo

- No demuestra IA (*Artificial Intelligence – Inteligencia Artificial*) funcional.
- No demuestra API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*) real.
- No demuestra dashboard.
- No demuestra integración con Google Workspace.
- No demuestra automatización productiva.
- No trabaja con datos reales.
- No sustituye revisión humana.

## Relación con GitHub Actions

El repositorio incluye validación mediante GitHub Actions y el workflow ejecuta la validación técnica global en eventos `push` y `pull_request`. Esto aporta CI (*Continuous Integration – Integración Continua*) para la comprobación repetible del estado del repositorio.

## Cierre de la demo

Si el comando global termina con:

`Resultado final: validacion global correcta.`

entonces la demo local está validada.

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
