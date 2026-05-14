import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "exportar_evidencias_demo.py"


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


def crear_evidencias_minimas(base: Path) -> None:
    (base / "panel_local.html").write_text("<html><body>panel</body></html>\n", encoding="utf-8")
    (base / "informe_consolidado.md").write_text("# Informe consolidado local\n", encoding="utf-8")
    (base / "informe_consolidado.html").write_text(
        "<html><body>consolidado</body></html>\n", encoding="utf-8"
    )
    (base / "agente-01").mkdir(parents=True, exist_ok=True)
    (base / "agente-10").mkdir(parents=True, exist_ok=True)
    (base / "agente-01" / "informe.txt").write_text("Informe agente 01\n", encoding="utf-8")
    (base / "agente-10" / "informe.txt").write_text("Informe agente 10\n", encoding="utf-8")


def test_exportar_evidencias_basicas() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        crear_evidencias_minimas(base)

        resultado = ejecutar_comando("--directorio-salidas", str(base))

        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        assert (base / "evidencias_demo" / "INDICE_EVIDENCIAS.md").is_file()
        assert (base / "evidencias_demo" / "INDICE_EVIDENCIAS.html").is_file()


def test_exportar_evidencias_con_zip() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        crear_evidencias_minimas(base)

        resultado = ejecutar_comando("--directorio-salidas", str(base), "--crear-zip")

        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        assert (base / "evidencias_demo.zip").is_file()


def test_exportar_evidencias_no_falla_sin_archivos() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        resultado = ejecutar_comando("--directorio-salidas", str(base))

        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        indice = base / "evidencias_demo" / "INDICE_EVIDENCIAS.md"
        assert indice.is_file()
        contenido = indice.read_text(encoding="utf-8", errors="replace").lower()
        assert "evidencias no disponibles" in contenido


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_exportar_evidencias_basicas,
        test_exportar_evidencias_con_zip,
        test_exportar_evidencias_no_falla_sin_archivos,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
