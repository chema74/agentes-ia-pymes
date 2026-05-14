import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "comparar_informes.py"


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


def test_comparar_informes_ok() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "agente-01"
        historico = base / "historico"
        historico.mkdir(parents=True, exist_ok=True)
        (base / "informe.txt").write_text(
            "Decision recomendada: aprobar\nLinea actual\n", encoding="utf-8"
        )
        nombre = "20260507-120000-informe.txt"
        (historico / nombre).write_text(
            "Decision recomendada: bloquear\nLinea historica\n", encoding="utf-8"
        )

        resultado = ejecutar_comando(
            "--agente",
            "1",
            "--archivo-historico",
            nombre,
            "--directorio-salidas",
            tmp,
        )
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        salida = resultado.stdout.lower()
        assert "comparacion local de informes" in salida
        assert "decision" in salida
        assert "cambio" in salida


def test_comparar_informes_solo_resumen() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "agente-01"
        historico = base / "historico"
        historico.mkdir(parents=True, exist_ok=True)
        (base / "informe.txt").write_text("Decision recomendada: aprobar\nA\n", encoding="utf-8")
        nombre = "20260507-120000-informe.txt"
        (historico / nombre).write_text("Decision recomendada: bloquear\nB\n", encoding="utf-8")

        resultado = ejecutar_comando(
            "--agente",
            "1",
            "--archivo-historico",
            nombre,
            "--directorio-salidas",
            tmp,
            "--solo-resumen",
        )
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        salida = resultado.stdout.lower()
        assert "resumen de diferencias" in salida
        assert "diff textual" not in salida


def test_comparar_rechaza_ruta_arbitraria() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        resultado = ejecutar_comando(
            "--agente",
            "1",
            "--archivo-historico",
            "../secreto.txt",
            "--directorio-salidas",
            tmp,
        )
        assert resultado.returncode == 1
        salida = (resultado.stdout + resultado.stderr).lower()
        assert "no permitida" in salida or "no valido" in salida


def test_comparar_error_sin_ultimo_informe() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        historico = Path(tmp) / "agente-01" / "historico"
        historico.mkdir(parents=True, exist_ok=True)
        nombre = "20260507-120000-informe.txt"
        (historico / nombre).write_text("Decision recomendada: bloquear\n", encoding="utf-8")

        resultado = ejecutar_comando(
            "--agente",
            "1",
            "--archivo-historico",
            nombre,
            "--directorio-salidas",
            tmp,
        )
        assert resultado.returncode == 1
        salida = (resultado.stdout + resultado.stderr).lower()
        assert "no existe el ultimo informe" in salida


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_comparar_informes_ok,
        test_comparar_informes_solo_resumen,
        test_comparar_rechaza_ruta_arbitraria,
        test_comparar_error_sin_ultimo_informe,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
