# 🧪 MAPA DE EVIDENCIAS V2 — AGENTES IA PARA PYMES

## Documento interno de evidencias para cierre V2

---

## 1. Objetivo del documento

Este documento define qué evidencias debe generar, conservar y mostrar la V2 de `agentes-ia-pymes`.

IA (*Artificial Intelligence – Inteligencia Artificial*).

PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

La finalidad es evitar que el repositorio se valore solo por descripción.

La V2 debe poder demostrar, con pruebas revisables, que el sistema funciona localmente y que sus piezas son comprensibles para una empresa.

---

## 2. Principio general

La evidencia V2 debe ser clara, verificable y útil.

No se trata de acumular capturas o informes sin criterio.

Se trata de demostrar:

- Qué se ejecuta.
- Qué se valida.
- Qué genera resultados.
- Qué puede revisar una empresa.
- Qué límites tiene el repositorio.
- Qué valor aporta frente a una demo superficial.

---

## 3. Evidencias mínimas para considerar cerrada la V2

La V2 deberá conservar evidencias de:

- Estado Git limpio antes del cierre.
- Rama V2.
- Tests ejecutados correctamente.
- Validación global del repositorio.
- Demo local reproducible.
- Panel local generado.
- Informe consolidado generado.
- Comparación histórica disponible.
- Exportación de evidencias.
- Documentación V2 creada.
- Limitaciones declaradas.
- Cierre técnico V2.

---

## 4. Evidencia 1 — Tests automatizados

Comando recomendado:

`python -m pytest -q`

Resultado mínimo esperado:

Los tests deben seguir pasando tras la intervención V2.

Estado base observado al iniciar V2:

`130 passed`

Uso público:

Demostrar que la evolución V2 no rompe la base validada del repositorio.

---

## 5. Evidencia 2 — Validación global del repositorio

Comando recomendado:

`python .\scripts\validar_repositorio.py`

Objetivo:

Comprobar que los agentes, datos de ejemplo y estructura mínima del repositorio siguen siendo válidos.

Uso público:

Demostrar que los diez agentes mantienen coherencia estructural.

---

## 6. Evidencia 3 — Demo local reproducible

Comando recomendado:

`python .\scripts\ejecutar_demo_local.py`

Objetivo:

Ejecutar una demostración local del repositorio sin depender de servicios externos obligatorios.

Uso público:

Demostrar que el repositorio no es solo documentación, sino un sistema local ejecutable.

---

## 7. Evidencia 4 — Espacio de trabajo editable

Comando recomendado:

`python .\scripts\preparar_espacio_trabajo.py`

Objetivo:

Generar un espacio de trabajo local editable a partir de los datos de ejemplo.

Uso público:

Mostrar que el repositorio permite revisar y adaptar información sin modificar directamente los ejemplos originales.

---

## 8. Evidencia 5 — Editor local guiado

Comando recomendado:

`python .\scripts\editor_espacio_trabajo.py`

Objetivo:

Lanzar el editor local para revisar y modificar datos de trabajo de forma guiada.

Uso público:

Demostrar una experiencia más cercana a herramienta operativa que a script aislado.

Nota:

El editor local no debe presentarse como aplicación de producción.

Debe presentarse como herramienta local de demostración.

---

## 9. Evidencia 6 — Panel local

Comando recomendado:

`python .\scripts\generar_panel_local.py --generar-informes`

Objetivo:

Generar un panel HTML local con resumen operativo del repositorio.

HTML (*HyperText Markup Language – Lenguaje de Marcado de Hipertexto*).

Uso público:

Mostrar una vista navegable y entendible de resultados, agentes e informes.

---

## 10. Evidencia 7 — Informe consolidado

Comando recomendado:

`python .\scripts\generar_informe_consolidado.py`

Objetivo:

Crear un informe global del estado o resultados del repositorio.

Uso público:

Demostrar capacidad de síntesis y reporting.

Reporting (*Reporting – Generación de informes*).

---

## 11. Evidencia 8 — Comparador histórico

Comando recomendado:

`python .\scripts\comparar_informes.py`

Objetivo:

Comparar resultados o informes entre ejecuciones.

Uso público:

Demostrar trazabilidad y capacidad de seguimiento histórico.

---

## 12. Evidencia 9 — Exportación de evidencias

Comando recomendado:

`python .\scripts\exportar_evidencias_demo.py`

Objetivo:

Agrupar o preparar evidencias demostrables del repositorio.

Uso público:

Facilitar la revisión del portfolio sin obligar a recorrer manualmente todos los archivos.

---

## 13. Evidencia 10 — Guion de demo local

Comando recomendado:

`python .\scripts\generar_guion_demo_local.py`

Objetivo:

Generar una guía o guion de presentación del repositorio.

Uso público:

Ayudar a explicar el proyecto de forma ordenada ante empresa, reclutador o evaluador técnico.

---

## 14. Capturas recomendadas para V2

Capturas recomendadas:

- Resultado de tests.
- Validación global.
- Demo local.
- Panel local.
- Editor guiado.
- Informe consolidado.
- Exportación de evidencias.
- Estructura documental V2.

Las capturas deben ser limpias, breves y contextualizadas.

No conviene mostrar pantallazos enormes sin lectura.

---

## 15. Evidencias documentales V2

Documentos recomendados para cierre V2:

- `docs/PLAN_V2_AGENTES_IA_PYMES.md`
- `docs/MAPA_EVIDENCIAS_V2.md`
- `docs/GUIA_EJECUCION_V2.md`
- `docs/LIMITES_ALCANCE_V2.md`
- `docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md`
- `docs/CIERRE_TECNICO_V2.md`

Estos documentos deben complementar, no sustituir, la documentación V1 existente.

---

## 16. Criterios de calidad de evidencias

Cada evidencia debe cumplir:

- Ser reproducible.
- Tener contexto.
- Ser entendible.
- No exagerar alcance.
- No depender de pago.
- No requerir datos reales.
- No romper la ejecución local.
- No duplicar documentación innecesaria.

---

## 17. Evidencias que no deben usarse como principales

No deben usarse como evidencias principales:

- Errores antiguos.
- Capturas incompletas.
- Salidas de consola demasiado largas.
- Documentación repetida.
- Funcionalidades futuras no implementadas.
- Mensajes que presenten el repositorio como SaaS terminado.
- Dependencias externas no necesarias.

SaaS (*Software as a Service – Software como Servicio*).

---

## 18. Resultado esperado

Al cerrar V2, este mapa debe permitir demostrar que `agentes-ia-pymes` tiene:

- Código ejecutable.
- Tests.
- Validación.
- Demo local.
- Panel.
- Informes.
- Comparación.
- Exportación de evidencias.
- Documentación de límites.
- Narrativa empresarial clara.

La V2 debe reforzar la idea de que el repositorio es local, práctico, demostrable y útil como base de agentes aplicados a PYMES.

---

## 🪪 Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
