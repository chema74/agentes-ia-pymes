# ▶️ GUÍA DE EJECUCIÓN V2 — AGENTES IA PARA PYMES

## Guía local de validación, demo y evidencias

---

## 1. Objetivo de la guía

Esta guía explica cómo ejecutar localmente la V2 de `agentes-ia-pymes`.

IA (*Artificial Intelligence – Inteligencia Artificial*).

PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

El objetivo es que una persona externa pueda validar el repositorio sin depender de servicios de pago, APIs obligatorias ni infraestructura cloud.

API (*Application Programming Interface – Interfaz de Programación de Aplicaciones*).

Cloud (*Cloud Computing – Computación en la nube*).

---

## 2. Principio de ejecución

La ejecución V2 debe seguir tres principios:

- Local-first.
- Free-first.
- Reproducible-first.

Esto significa:

- Debe poder ejecutarse en local.
- No debe exigir servicios de pago.
- Debe generar resultados revisables.
- Debe conservar evidencias.
- Debe declarar sus límites.

---

## 3. Requisitos previos

Requisitos recomendados:

- Python 3.11 o superior.
- PowerShell en Windows.
- Git instalado.
- Entorno virtual opcional.
- Repositorio clonado en local.

Python (*Python – Lenguaje de programación Python*).

Git (*Git – Sistema de control de versiones*).

PowerShell (*PowerShell – Consola y lenguaje de automatización de Microsoft*).

---

## 4. Ubicación local recomendada

Ruta local de trabajo:

`C:\Users\txema\Documents\agentes-ia-pymes`

Comando inicial:

`cd C:\Users\txema\Documents\agentes-ia-pymes`

---

## 5. Validación rápida del repositorio

Comando:

`python .\scripts\validar_repositorio.py`

Objetivo:

Comprobar que los diez agentes, sus datos de ejemplo y la estructura mínima del repositorio están presentes y son válidos.

Resultado esperado:

Validación correcta de la estructura del repositorio.

---

## 6. Ejecución de tests

Comando:

`python -m pytest -q`

Objetivo:

Ejecutar la batería de pruebas automatizadas.

Estado base al iniciar V2:

`130 passed`

Resultado esperado en V2:

Los tests deben seguir pasando después de cualquier intervención.

Pytest (*Python Testing Tool – Herramienta de pruebas para Python*).

---

## 7. Preparación del espacio de trabajo

Comando:

`python .\scripts\preparar_espacio_trabajo.py`

Objetivo:

Crear un espacio editable de trabajo a partir de los datos de ejemplo.

Uso:

Permite modificar datos de prueba sin tocar directamente los datos originales de los agentes.

---

## 8. Ejecución de agente individual

Comando base:

`python .\scripts\ejecutar_agente.py`

Objetivo:

Ejecutar un agente del repositorio sobre datos preparados.

Uso:

Permite revisar el comportamiento de los agentes de forma individual.

---

## 9. Demo local reproducible

Comando:

`python .\scripts\ejecutar_demo_local.py`

Objetivo:

Ejecutar una demostración local del repositorio.

Uso:

Sirve como recorrido rápido para mostrar que el sistema tiene piezas ejecutables y no solo documentación.

---

## 10. Editor local guiado

Comando:

`python .\scripts\editor_espacio_trabajo.py`

Objetivo:

Abrir una herramienta local de edición guiada para revisar y modificar información del espacio de trabajo.

Uso:

Permite una experiencia más visual y operativa.

Importante:

Este editor es una herramienta local de demostración.

No debe presentarse como aplicación de producción, SaaS ni sistema multiusuario.

SaaS (*Software as a Service – Software como Servicio*).

---

## 11. Generación del panel local

Comando recomendado:

`python .\scripts\generar_panel_local.py --generar-informes`

Objetivo:

Generar un panel HTML local con resultados e informes.

HTML (*HyperText Markup Language – Lenguaje de Marcado de Hipertexto*).

Uso:

Permite revisar resultados de manera más clara que una salida de consola aislada.

---

## 12. Informe consolidado

Comando:

`python .\scripts\generar_informe_consolidado.py`

Objetivo:

Generar un informe global del repositorio.

Uso:

Sirve como evidencia documental de resultados y estado operativo.

---

## 13. Comparación de informes

Comando:

`python .\scripts\comparar_informes.py`

Objetivo:

Comparar informes o resultados entre ejecuciones.

Uso:

Permite demostrar trazabilidad histórica.

---

## 14. Exportación de evidencias

Comando:

`python .\scripts\exportar_evidencias_demo.py`

Objetivo:

Agrupar evidencias útiles para revisión externa.

Uso:

Facilita preparar capturas, salidas e informes para portfolio.

---

## 15. Guion de demo local

Comando:

`python .\scripts\generar_guion_demo_local.py`

Objetivo:

Generar un guion de presentación local del repositorio.

Uso:

Ayuda a explicar el proyecto ante una empresa, reclutador o evaluador técnico.

---

## 16. Secuencia recomendada para validar V2

Secuencia recomendada:

1. `git status`
2. `python -m pytest -q`
3. `python .\scripts\validar_repositorio.py`
4. `python .\scripts\preparar_espacio_trabajo.py`
5. `python .\scripts\ejecutar_demo_local.py`
6. `python .\scripts\generar_panel_local.py --generar-informes`
7. `python .\scripts\generar_informe_consolidado.py`
8. `python .\scripts\exportar_evidencias_demo.py`
9. `git status`

---

## 17. Qué debe revisarse después de ejecutar

Después de ejecutar la secuencia V2, revisar:

- Tests superados.
- Validación correcta.
- Informes generados.
- Panel local creado.
- Evidencias exportadas.
- Archivos modificados o generados.
- Estado Git.
- Posibles salidas demasiado ruidosas.
- Coherencia de documentación.

---

## 18. Limitaciones de la ejecución V2

La ejecución V2 no pretende demostrar:

- Producción real.
- Multiusuario.
- Seguridad empresarial completa.
- Despliegue cloud.
- Integración con sistemas reales de empresa.
- Uso de datos reales.
- Producto SaaS terminado.

La ejecución V2 demuestra una base local, modular, revisable y reproducible.

---

## 19. Resultado esperado

Al finalizar la ejecución V2, el repositorio debe poder demostrar:

- Agentes organizados.
- Scripts ejecutables.
- Tests correctos.
- Validación local.
- Panel local.
- Informes.
- Evidencias.
- Documentación de límites.
- Lectura empresarial clara.

---

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
