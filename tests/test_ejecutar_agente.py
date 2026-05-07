import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "ejecutar_agente.py"


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


def test_ejecutar_agente_01_por_argumento() -> None:
    resultado = ejecutar_comando("--agente", "1")
    assert resultado.returncode == 0
    assert "Agente 01" in resultado.stdout


def test_ejecutar_agente_10_por_argumento() -> None:
    resultado = ejecutar_comando("--agente", "10")
    assert resultado.returncode == 0
    assert "Agente 10" in resultado.stdout


def test_error_agente_invalido() -> None:
    resultado = ejecutar_comando("--agente", "99")
    assert resultado.returncode == 1
    salida = resultado.stdout + resultado.stderr
    assert "Opcion invalida" in salida


def test_mostrar_ayuda() -> None:
    resultado = ejecutar_comando("--help")
    assert resultado.returncode == 0
    assert "--agente" in resultado.stdout


def test_guardar_historico_agente_01() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        resultado = ejecutar_comando(
            "--agente",
            "1",
            "--guardar-historico",
            "--directorio-salidas",
            tmp,
        )
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        base = Path(tmp) / "agente-01"
        assert (base / "informe.txt").is_file()
        carpeta_historico = base / "historico"
        assert carpeta_historico.is_dir()
        assert any(carpeta_historico.glob("*-informe.txt"))


def test_guardar_historico_todos() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        resultado = ejecutar_comando(
            "--todos",
            "--guardar-historico",
            "--directorio-salidas",
            tmp,
        )
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        assert any((Path(tmp) / "agente-01" / "historico").glob("*-informe.txt"))
        assert any((Path(tmp) / "agente-10" / "historico").glob("*-informe.txt"))


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_ejecutar_agente_01_por_argumento,
        test_ejecutar_agente_10_por_argumento,
        test_error_agente_invalido,
        test_mostrar_ayuda,
        test_guardar_historico_agente_01,
        test_guardar_historico_todos,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
