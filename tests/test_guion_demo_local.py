import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "generar_guion_demo_local.py"


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


def test_generar_guion_demo_markdown() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        (base / "panel_local.html").write_text("<html><body>panel</body></html>\n", encoding="utf-8")
        (base / "informe_consolidado.md").write_text("# Informe consolidado local\n", encoding="utf-8")

        resultado = ejecutar_comando("--directorio-salidas", str(base))
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        ruta_md = base / "guion_demo_local.md"
        assert ruta_md.is_file()
        contenido = ruta_md.read_text(encoding="utf-8", errors="replace")
        assert "Guion local de demo guiada" in contenido
        assert "python scripts/ejecutar_demo_local.py --crear-zip" in contenido
        assert "http://127.0.0.1:8765/" in contenido


def test_generar_guion_demo_html() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        (base / "panel_local.html").write_text("<html><body>panel</body></html>\n", encoding="utf-8")
        (base / "informe_consolidado.md").write_text("# Informe consolidado local\n", encoding="utf-8")

        resultado = ejecutar_comando("--directorio-salidas", str(base), "--generar-html")
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        ruta_html = base / "guion_demo_local.html"
        assert ruta_html.is_file()
        contenido = ruta_html.read_text(encoding="utf-8", errors="replace")
        assert "html" in contenido.lower()
        assert "Guion local de demo guiada" in contenido


def test_guion_demo_no_falla_sin_evidencias() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        resultado = ejecutar_comando("--directorio-salidas", str(base))
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        ruta_md = base / "guion_demo_local.md"
        assert ruta_md.is_file()
        contenido = ruta_md.read_text(encoding="utf-8", errors="replace").lower()
        assert "pendiente de generar" in contenido or "no disponible todavia" in contenido


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_generar_guion_demo_markdown,
        test_generar_guion_demo_html,
        test_guion_demo_no_falla_sin_evidencias,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
