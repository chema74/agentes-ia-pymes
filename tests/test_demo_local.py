import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "ejecutar_demo_local.py"


def ejecutar_comando(*argumentos: str) -> subprocess.CompletedProcess[str]:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, str(SCRIPT), *argumentos],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=entorno,
        check=False,
    )


def test_demo_local_solo_validar() -> None:
    resultado = ejecutar_comando("--solo-validar")
    assert resultado.returncode == 0, resultado.stdout + resultado.stderr
    salida = (resultado.stdout + resultado.stderr).lower()
    assert "entorno preparado" in salida


def test_demo_local_completa_temporal() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        resultado = ejecutar_comando(
            "--directorio-trabajo",
            tmp_trabajo,
            "--directorio-salidas",
            tmp_salidas,
            "--crear-zip",
        )
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        base = Path(tmp_salidas)
        assert (base / "panel_local.html").is_file()
        assert (base / "informe_consolidado.md").is_file()
        assert (base / "informe_consolidado.html").is_file()
        assert (base / "evidencias_demo" / "INDICE_EVIDENCIAS.md").is_file()
        assert (base / "evidencias_demo.zip").is_file()


def test_demo_local_sin_historico() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        resultado = ejecutar_comando(
            "--directorio-trabajo",
            tmp_trabajo,
            "--directorio-salidas",
            tmp_salidas,
            "--sin-historico",
        )
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        assert (Path(tmp_salidas) / "agente-01" / "informe.txt").is_file()


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_demo_local_solo_validar,
        test_demo_local_completa_temporal,
        test_demo_local_sin_historico,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
