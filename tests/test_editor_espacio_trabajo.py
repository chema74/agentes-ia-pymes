import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from urllib import error, request

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT_PREPARAR = RAIZ / "scripts" / "preparar_espacio_trabajo.py"
SCRIPT_EDITOR = RAIZ / "scripts" / "editor_espacio_trabajo.py"


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


def iniciar_editor(directorio_trabajo: Path, puerto: int) -> subprocess.Popen:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    return subprocess.Popen(
        [
            sys.executable,
            str(SCRIPT_EDITOR),
            "--directorio-trabajo",
            str(directorio_trabajo),
            "--host",
            "127.0.0.1",
            "--puerto",
            str(puerto),
        ],
        cwd=RAIZ,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        env=entorno,
    )


def esperar_servidor(puerto: int, segundos: float = 5.0) -> None:
    inicio = time.time()
    url = f"http://127.0.0.1:{puerto}/api/agentes"
    while time.time() - inicio < segundos:
        try:
            with request.urlopen(url, timeout=1) as resp:
                if resp.status == 200:
                    return
        except Exception:
            time.sleep(0.15)
    raise AssertionError("El servidor no arrancó a tiempo.")


def cerrar_proceso(proceso: subprocess.Popen) -> None:
    if proceso.poll() is None:
        proceso.terminate()
        try:
            proceso.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proceso.kill()
            proceso.wait(timeout=3)


def test_error_sin_espacio_trabajo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        ruta = Path(tmp) / "no_existe"
        resultado = ejecutar(SCRIPT_EDITOR, "--directorio-trabajo", str(ruta), "--puerto", "8871")
        assert resultado.returncode == 1
        salida = (resultado.stdout or "") + (resultado.stderr or "")
        assert "no existe el directorio de trabajo" in salida.lower() or "preparar_espacio_trabajo" in salida


def test_servidor_lista_agentes() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        trabajo = Path(tmp)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, 8872)
        try:
            esperar_servidor(8872)
            with request.urlopen("http://127.0.0.1:8872/api/agentes", timeout=3) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert len(datos["agentes"]) == 10
        finally:
            cerrar_proceso(proceso)


def test_servidor_lee_agente() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        trabajo = Path(tmp)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, 8873)
        try:
            esperar_servidor(8873)
            with request.urlopen("http://127.0.0.1:8873/api/agente?id=1", timeout=3) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert "datos" in datos
            assert isinstance(datos["datos"], dict)
        finally:
            cerrar_proceso(proceso)


def test_servidor_guarda_agente() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        trabajo = Path(tmp)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, 8874)
        try:
            esperar_servidor(8874)
            with request.urlopen("http://127.0.0.1:8874/api/agente?id=1", timeout=3) as resp:
                base = json.loads(resp.read().decode("utf-8"))["datos"]
            base["campo_prueba_editor"] = True

            cuerpo = json.dumps({"datos": base}, ensure_ascii=False).encode("utf-8")
            req = request.Request(
                "http://127.0.0.1:8874/api/agente?id=1",
                data=cuerpo,
                method="POST",
                headers={"Content-Type": "application/json; charset=utf-8"},
            )
            with request.urlopen(req, timeout=3) as resp:
                guardado = json.loads(resp.read().decode("utf-8"))
            assert "mensaje" in guardado

            ruta_archivo = trabajo / "agente-01" / "datos.json"
            final = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert final.get("campo_prueba_editor") is True
        finally:
            cerrar_proceso(proceso)


def test_servidor_rechaza_json_invalido() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        trabajo = Path(tmp)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, 8875)
        try:
            esperar_servidor(8875)
            req = request.Request(
                "http://127.0.0.1:8875/api/agente?id=1",
                data=b"{no-valido}",
                method="POST",
                headers={"Content-Type": "application/json; charset=utf-8"},
            )
            try:
                request.urlopen(req, timeout=3)
                assert False, "Se esperaba error HTTP por JSON invalido"
            except error.HTTPError as http_error:
                assert http_error.code == 400
            assert proceso.poll() is None
        finally:
            cerrar_proceso(proceso)


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None):
    suite = unittest.TestSuite()
    for funcion in (
        test_error_sin_espacio_trabajo,
        test_servidor_lista_agentes,
        test_servidor_lee_agente,
        test_servidor_guarda_agente,
        test_servidor_rechaza_json_invalido,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
