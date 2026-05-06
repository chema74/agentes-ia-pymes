import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT_PREPARAR = RAIZ / "scripts" / "preparar_espacio_trabajo.py"
SCRIPT_EJECUTAR = RAIZ / "scripts" / "ejecutar_agente.py"
SCRIPT_PANEL = RAIZ / "scripts" / "generar_panel_local.py"


def ejecutar(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=RAIZ,
        text=True,
        capture_output=True,
        encoding="utf-8",
        env=entorno,
        check=False,
    )


def test_preparar_espacio_trabajo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        resultado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(base))
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr

        ruta_01 = base / "agente-01" / "datos.json"
        ruta_10 = base / "agente-10" / "datos.json"
        assert ruta_01.is_file()
        assert ruta_10.is_file()

        with ruta_01.open("r", encoding="utf-8") as archivo:
            json.load(archivo)
        with ruta_10.open("r", encoding="utf-8") as archivo:
            json.load(archivo)


def test_no_sobrescribe_por_defecto() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        primero = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(base))
        assert primero.returncode == 0, primero.stdout + primero.stderr

        ruta_01 = base / "agente-01" / "datos.json"
        datos = json.loads(ruta_01.read_text(encoding="utf-8"))
        datos["campo_prueba_local"] = "conservar"
        ruta_01.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")

        segundo = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(base))
        assert segundo.returncode == 0, segundo.stdout + segundo.stderr

        datos_finales = json.loads(ruta_01.read_text(encoding="utf-8"))
        assert datos_finales.get("campo_prueba_local") == "conservar"


def test_sobrescribe_con_argumento() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        primero = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(base))
        assert primero.returncode == 0, primero.stdout + primero.stderr

        ruta_01 = base / "agente-01" / "datos.json"
        datos = json.loads(ruta_01.read_text(encoding="utf-8"))
        datos["campo_prueba_local"] = "eliminar"
        ruta_01.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")

        segundo = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(base), "--sobrescribir")
        assert segundo.returncode == 0, segundo.stdout + segundo.stderr

        datos_finales = json.loads(ruta_01.read_text(encoding="utf-8"))
        assert "campo_prueba_local" not in datos_finales


def test_ejecutar_agente_con_datos_trabajo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(base))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        resultado = ejecutar(
            SCRIPT_EJECUTAR,
            "--agente",
            "1",
            "--usar-datos-trabajo",
            "--directorio-trabajo",
            str(base),
        )
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        assert "Agente 01" in resultado.stdout


def test_generar_panel_con_datos_trabajo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)

        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        resultado = ejecutar(
            SCRIPT_PANEL,
            "--generar-informes",
            "--usar-datos-trabajo",
            "--directorio-trabajo",
            str(trabajo),
            "--directorio-salidas",
            str(salidas),
        )
        assert resultado.returncode == 0, resultado.stdout + resultado.stderr
        assert (salidas / "panel_local.html").is_file()


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_preparar_espacio_trabajo,
        test_no_sobrescribe_por_defecto,
        test_sobrescribe_con_argumento,
        test_ejecutar_agente_con_datos_trabajo,
        test_generar_panel_con_datos_trabajo,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
