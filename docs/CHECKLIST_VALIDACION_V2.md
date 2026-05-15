# CHECKLIST DE VALIDACIÓN V2 — AGENTES IA PARA PYMES

## Control de cierre técnico y documental

---

## 1. Objetivo del checklist

Este documento define las comprobaciones mínimas necesarias para considerar cerrada la V2 de `agentes-ia-pymes`.

IA (*Artificial Intelligence – Inteligencia Artificial*).

PYMES (*Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas*).

La finalidad es evitar un cierre informal o incompleto.

La V2 debe quedar validada con pruebas, documentación, evidencias y estado Git limpio.

---

## 2. Validación de rama

Comprobaciones:

- La rama de trabajo debe ser `v2-agentes-ia-pymes`.
- La rama debe partir de una V1 limpia.
- No debe mezclarse trabajo V2 directamente en `main` sin decisión explícita.
- El repositorio debe mantener trazabilidad entre V1 y V2.

Comando recomendado:

`git branch --show-current`

Resultado esperado:

`v2-agentes-ia-pymes`

---

## 3. Validación de estado Git

Comprobaciones:

- Revisar archivos modificados.
- Revisar archivos nuevos.
- Confirmar que no hay cambios accidentales.
- Confirmar que no se han generado artefactos innecesarios.
- Confirmar que no se han incluido entornos virtuales, cachés o archivos temporales.

Comando recomendado:

`git status`

Resultado esperado al cierre:

Árbol limpio después del commit V2.

---

## 4. Validación de tests

Comando recomendado:

`python -m pytest -q`

Estado base al iniciar V2:

`130 passed`

Resultado esperado:

Todos los tests deben pasar.

Si cambia el número de tests, debe estar justificado por nuevas pruebas añadidas o ajustes controlados.

Pytest (*Python Testing Tool – Herramienta de pruebas para Python*).

---

## 5. Validación global del repositorio

Comando recomendado:

`python .\scripts\validar_repositorio.py`

Comprobaciones:

- Los diez agentes existen.
- Los datos de ejemplo son válidos.
- La estructura mínima se mantiene.
- No se rompe la compatibilidad con la V1.

Resultado esperado:

Validación global correcta.

---

## 6. Validación de documentación V2

Deben existir como mínimo:

- `docs/PLAN_V2_AGENTES_IA_PYMES.md`
- `docs/MAPA_EVIDENCIAS_V2.md`
- `docs/GUIA_EJECUCION_V2.md`
- `docs/LIMITES_ALCANCE_V2.md`
- `docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md`
- `docs/CHECKLIST_VALIDACION_V2.md`

Opcionalmente:

- `docs/CIERRE_TECNICO_V2.md`
- `docs/AUDITORIA_DOCUMENTAL_V2.md`

---

## 7. Validación de ejecución local

Comandos recomendados:

`python .\scripts\preparar_espacio_trabajo.py`

`python .\scripts\ejecutar_demo_local.py`

`python .\scripts\generar_panel_local.py --generar-informes`

`python .\scripts\generar_informe_consolidado.py`

`python .\scripts\exportar_evidencias_demo.py`

Objetivo:

Confirmar que las piezas principales del repositorio siguen siendo ejecutables localmente.

---

## 8. Validación de evidencias

Comprobar que existen evidencias de:

- Tests.
- Validación global.
- Demo local.
- Panel local.
- Informes.
- Exportación de evidencias.
- Documentación de límites.
- Resumen ejecutivo.
- Mapa de evidencias.

Las evidencias no deben exagerar el alcance del repositorio.

---

## 9. Validación de límites

Comprobar que la documentación V2 deja claro que el repositorio no es:

- SaaS terminado.
- Sistema productivo.
- Plataforma multiusuario.
- Solución cloud.
- Implantación empresarial completa.
- Sistema con datos reales.
- Sustituto de una consultoría profesional.

SaaS (*Software as a Service – Software como Servicio*).

Cloud (*Cloud Computing – Computación en la nube*).

---

## 10. Validación de lectura empresarial

Comprobar que una empresa puede entender:

- Qué problema aborda.
- Qué agentes incluye.
- Qué se puede ejecutar.
- Qué evidencias existen.
- Qué límites tiene.
- Cómo podría evolucionar.
- Qué valor aporta como laboratorio local.

---

## 11. Validación de README

Antes de cerrar V2, revisar si `README.md`:

- Menciona la V2.
- Enlaza documentación V2.
- Mantiene claridad.
- No promete producción real.
- No duplica innecesariamente todo el contenido de `docs/`.
- Presenta el proyecto como laboratorio local demostrable.

---

## 12. Validación de cierre

Antes del commit final V2, comprobar:

- Tests correctos.
- Validación global correcta.
- Documentación V2 creada.
- README revisado.
- Sin archivos temporales accidentales.
- Sin carpetas de caché añadidas.
- Sin entorno virtual incluido.
- Sin cambios en la web pública.
- Sin promesas no implementadas.

---

## 13. Comandos finales recomendados

Secuencia final sugerida:

`git status`

`python -m pytest -q`

`python .\scripts\validar_repositorio.py`

`git diff --stat`

`git add README.md docs/PLAN_V2_AGENTES_IA_PYMES.md docs/MAPA_EVIDENCIAS_V2.md docs/GUIA_EJECUCION_V2.md docs/LIMITES_ALCANCE_V2.md docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md docs/CHECKLIST_VALIDACION_V2.md`

`git commit -m "Inicia documentacion V2 de agentes IA para PYMES"`

---

## 14. Resultado esperado

La V2 debe cerrarse solo cuando el repositorio pueda defenderse como:

- Local.
- Reproducible.
- Documentado.
- Validado.
- Comprensible para empresa.
- Honesto en sus límites.
- Preparado para generar evidencias públicas futuras.

---

## Licencia y Autoría

Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.  
© 2025 – Txema Ríos. Todos los derechos compartidos.
