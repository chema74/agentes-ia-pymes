import os
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest


RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "generar_panel_local.py"


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


def test_generar_panel_con_informes_existentes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        (base / "agente-01").mkdir(parents=True, exist_ok=True)
        (base / "agente-10").mkdir(parents=True, exist_ok=True)
        (base / "agente-01" / "informe.txt").write_text(
            "Decision humana recomendada: aprobar con seguimiento\n",
            encoding="utf-8",
        )
        (base / "agente-10" / "informe.txt").write_text(
            "Aviso: revisar documentacion pendiente\n",
            encoding="utf-8",
        )

        resultado = ejecutar_comando("--directorio-salidas", str(base))

        assert resultado.returncode == 0
        panel = base / "panel_local.html"
        assert panel.is_file()
        contenido = panel.read_text(encoding="utf-8")
        assert "Agente 01" in contenido
        assert "Agente 10" in contenido


def test_generar_panel_con_generacion_de_informes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        resultado = ejecutar_comando("--generar-informes", "--directorio-salidas", str(base))

        assert resultado.returncode == 0
        assert (base / "panel_local.html").is_file()
        assert (base / "agente-01" / "informe.txt").is_file()
        assert (base / "agente-10" / "informe.txt").is_file()


def test_panel_muestra_informes_faltantes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)

        resultado = ejecutar_comando("--directorio-salidas", str(base))

        assert resultado.returncode == 0
        panel = base / "panel_local.html"
        assert panel.is_file()
        contenido = panel.read_text(encoding="utf-8")
        assert "Informe no encontrado" in contenido or "Pendiente de generar" in contenido


def test_ayuda_panel() -> None:
    resultado = ejecutar_comando("--help")

    assert resultado.returncode == 0
    assert "--directorio-salidas" in resultado.stdout
    assert "--generar-informes" in resultado.stdout


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_generar_panel_con_informes_existentes,
        test_generar_panel_con_generacion_de_informes,
        test_panel_muestra_informes_faltantes,
        test_ayuda_panel,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
