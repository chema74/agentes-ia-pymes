# -*- coding: utf-8 -*-
"""
Pruebas del generador de informe ejecutivo V2.

Las pruebas usan un directorio temporal para no depender del estado real
de las salidas locales del repositorio.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


def cargar_modulo():
    """
    Carga el módulo del script de forma explícita.

    Al usar importlib.util.module_from_spec, el módulo debe registrarse
    en sys.modules antes de ejecutar spec.loader.exec_module(modulo).
    Esto evita fallos internos de dataclasses al resolver __module__.
    """
    ruta = Path(__file__).resolve().parents[1] / "scripts" / "generar_informe_ejecutivo_v2.py"
    spec = importlib.util.spec_from_file_location("generar_informe_ejecutivo_v2", ruta)
    modulo = importlib.util.module_from_spec(spec)

    assert spec.loader is not None
    assert spec.name is not None

    sys.modules[spec.name] = modulo
    spec.loader.exec_module(modulo)

    return modulo


def test_construir_informe_detecta_documentos_y_licencia(tmp_path):
    modulo = cargar_modulo()

    docs = tmp_path / "docs"
    salidas = tmp_path / "salidas"
    docs.mkdir()
    salidas.mkdir()

    (docs / "PLAN_V2_AGENTES_IA_PYMES.md").write_text(
        "# Plan V2\n\nContenido de prueba.\n",
        encoding="utf-8",
    )
    (docs / "MAPA_EVIDENCIAS_V2.md").write_text(
        "# Mapa de evidencias\n\nContenido de prueba.\n",
        encoding="utf-8",
    )
    (salidas / "validacion_v2.md").write_text(
        "Resultado final V2: validación correcta\n133 passed in 64.61s\n",
        encoding="utf-8",
    )

    informe = modulo.construir_informe(tmp_path)

    assert "# 📌 INFORME EJECUTIVO V2" in informe
    assert "Documentos V2 detectados" in informe
    assert "133 passed" in informe
    assert "WEB_PUBLICA: NO_MODIFICADA" in informe
    assert "## 🪪 Licencia y Autoría" in informe
    assert "© 2025 – Txema Ríos. Todos los derechos compartidos." in informe


def test_escribir_informe_crea_archivo_markdown(tmp_path):
    modulo = cargar_modulo()

    salida = tmp_path / "salidas" / "informe_ejecutivo_v2.md"
    ruta = modulo.escribir_informe(tmp_path, salida)

    assert ruta.exists()
    texto = ruta.read_text(encoding="utf-8")
    assert "INFORME_EJECUTIVO_V2_GENERADO: OK" in texto
    assert "DEPENDENCIAS_EXTERNAS_OBLIGATORIAS: NINGUNA" in texto