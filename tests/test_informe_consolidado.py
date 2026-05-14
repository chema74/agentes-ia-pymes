import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "generar_informe_consolidado.py"


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


def test_generar_informe_consolidado_markdown() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        carpeta = base / "agente-01"
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "informe.txt").write_text("Decision recomendada: aprobar\n", encoding="utf-8")

        resultado = ejecutar_comando("--directorio-salidas", str(base))
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        ruta_md = base / "informe_consolidado.md"
        assert ruta_md.is_file()
        contenido = ruta_md.read_text(encoding="utf-8")
        assert "Informe consolidado local" in contenido
        assert "agente-01" in contenido


def test_generar_informe_consolidado_html() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        carpeta = base / "agente-10"
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "informe.txt").write_text("Decision recomendada: revisar\n", encoding="utf-8")

        resultado = ejecutar_comando("--directorio-salidas", str(base), "--generar-html")
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        ruta_html = base / "informe_consolidado.html"
        assert ruta_html.is_file()
        contenido = ruta_html.read_text(encoding="utf-8")
        assert "<html" in contenido.lower()
        assert "Informe consolidado local" in contenido


def test_informe_consolidado_no_falla_sin_informes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        resultado = ejecutar_comando("--directorio-salidas", str(base), "--generar-html")
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        ruta_md = base / "informe_consolidado.md"
        assert ruta_md.is_file()
        contenido = ruta_md.read_text(encoding="utf-8").lower()
        assert "informe no disponible" in contenido


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_generar_informe_consolidado_markdown,
        test_generar_informe_consolidado_html,
        test_informe_consolidado_no_falla_sin_informes,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
