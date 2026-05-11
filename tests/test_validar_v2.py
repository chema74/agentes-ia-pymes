from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def cargar_modulo_validar_v2() -> ModuleType:
    """Carga el script validar_v2.py como módulo importable para pruebas."""

    raiz = Path(__file__).resolve().parents[1]
    ruta_script = raiz / "scripts" / "validar_v2.py"

    especificacion = importlib.util.spec_from_file_location("validar_v2", ruta_script)
    assert especificacion is not None
    assert especificacion.loader is not None

    modulo = importlib.util.module_from_spec(especificacion)
    sys.modules[especificacion.name] = modulo
    especificacion.loader.exec_module(modulo)

    return modulo


def test_documentos_v2_obligatorios_existen() -> None:
    """Comprueba que todos los documentos V2 obligatorios existen."""

    modulo = cargar_modulo_validar_v2()
    raiz = Path(__file__).resolve().parents[1]

    errores = modulo.comprobar_documentos_obligatorios(raiz)

    assert errores == []


def test_referencias_v2_principales_existen() -> None:
    """Comprueba que README, índice y ficha pública contienen referencias V2."""

    modulo = cargar_modulo_validar_v2()
    raiz = Path(__file__).resolve().parents[1]

    errores = modulo.comprobar_referencias_documentales(raiz)

    assert errores == []


def test_generar_informe_validacion_v2() -> None:
    """Comprueba que el informe local de validación V2 se puede generar."""

    modulo = cargar_modulo_validar_v2()
    raiz = Path(__file__).resolve().parents[1]

    ruta_informe = modulo.generar_informe_validacion(
        raiz=raiz,
        errores=[],
        ejecuciones=[],
        modo="solo-documentacion-test",
    )

    assert ruta_informe.exists()

    contenido = ruta_informe.read_text(encoding="utf-8")

    assert "Validación V2" in contenido
    assert "Resultado global: correcta" in contenido
    assert "solo-documentacion-test" in contenido
