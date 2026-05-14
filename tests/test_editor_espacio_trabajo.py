import json
import os
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
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


def iniciar_editor(
    directorio_trabajo: Path, directorio_salidas: Path, puerto: int
) -> subprocess.Popen:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    return subprocess.Popen(
        [
            sys.executable,
            str(SCRIPT_EDITOR),
            "--directorio-trabajo",
            str(directorio_trabajo),
            "--directorio-salidas",
            str(directorio_salidas),
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


def esperar_servidor(puerto: int, segundos: float = 8.0) -> None:
    inicio = time.time()
    url = f"http://127.0.0.1:{puerto}/api/agentes"
    while time.time() - inicio < segundos:
        try:
            with request.urlopen(url, timeout=1) as resp:
                if resp.status == 200:
                    return
        except Exception:
            time.sleep(0.15)
    raise AssertionError("El servidor no arranco a tiempo.")


def obtener_puerto_libre() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def cerrar_proceso(proceso: subprocess.Popen) -> None:
    if proceso.poll() is None:
        proceso.terminate()
    try:
        proceso.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        proceso.kill()
        proceso.communicate(timeout=5)


def post_json(url: str, payload: dict | None = None) -> tuple[int, dict]:
    if payload is None:
        data = b"{}"
    else:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with request.urlopen(req, timeout=20) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as http_error:
        return http_error.code, json.loads(http_error.read().decode("utf-8"))


def test_error_sin_espacio_trabajo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        ruta = Path(tmp) / "no_existe"
        resultado = ejecutar(SCRIPT_EDITOR, "--directorio-trabajo", str(ruta), "--puerto", "8871")
        assert resultado.returncode == 1
        salida = (resultado.stdout or "") + (resultado.stderr or "")
        assert (
            "no existe el directorio de trabajo" in salida.lower()
            or "preparar_espacio_trabajo" in salida
        )


def test_servidor_lista_agentes() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/api/agentes", timeout=3) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert len(datos["agentes"]) == 10
        finally:
            cerrar_proceso(proceso)


def test_servidor_lee_agente() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/api/agente?id=1", timeout=3) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert "datos" in datos
            assert isinstance(datos["datos"], dict)
        finally:
            cerrar_proceso(proceso)


def test_servidor_guarda_agente() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/api/agente?id=1", timeout=3) as resp:
                base = json.loads(resp.read().decode("utf-8"))["datos"]
            base["campo_prueba_editor"] = True

            status, guardado = post_json(
                f"http://127.0.0.1:{puerto}/api/agente?id=1", {"datos": base}
            )
            assert status == 200
            assert "mensaje" in guardado

            ruta_archivo = trabajo / "agente-01" / "datos.json"
            final = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert final.get("campo_prueba_editor") is True
        finally:
            cerrar_proceso(proceso)


def test_servidor_rechaza_json_invalido() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            req = request.Request(
                f"http://127.0.0.1:{puerto}/api/agente?id=1",
                data=b"{no-valido}",
                method="POST",
                headers={"Content-Type": "application/json; charset=utf-8"},
            )
            try:
                request.urlopen(req, timeout=3)
                raise AssertionError("Se esperaba error HTTP por JSON invalido")
            except error.HTTPError as http_error:
                assert http_error.code == 400
            assert proceso.poll() is None
        finally:
            cerrar_proceso(proceso)


def test_servidor_ejecuta_agente() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            status, respuesta = post_json(f"http://127.0.0.1:{puerto}/api/ejecutar?id=1")
            assert status == 200
            assert respuesta.get("ok") is True
            assert (salidas / "agente-01" / "informe.txt").is_file()
        finally:
            cerrar_proceso(proceso)


def test_servidor_genera_panel() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            status, respuesta = post_json(f"http://127.0.0.1:{puerto}/api/generar-panel")
            assert status == 200
            assert respuesta.get("ok") is True
            assert (salidas / "panel_local.html").is_file()
        finally:
            cerrar_proceso(proceso)


def test_servidor_lee_informe() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            status_ejecutar, respuesta_ejecutar = post_json(
                f"http://127.0.0.1:{puerto}/api/ejecutar?id=1"
            )
            assert status_ejecutar == 200
            assert respuesta_ejecutar.get("ok") is True

            with request.urlopen(f"http://127.0.0.1:{puerto}/api/informe?id=1", timeout=10) as resp:
                informe = json.loads(resp.read().decode("utf-8"))
            assert informe.get("ok") is True
            assert bool(informe.get("contenido", "").strip())
        finally:
            cerrar_proceso(proceso)


def test_servidor_lista_historico() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        historico = salidas / "agente-01" / "historico"
        historico.mkdir(parents=True, exist_ok=True)
        (historico / "20260507-120000-informe.txt").write_text(
            "Informe historico 01\n", encoding="utf-8"
        )

        puerto = obtener_puerto_libre()
        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/historico?id=1", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("historico"), list)
            assert len(datos["historico"]) >= 1
        finally:
            cerrar_proceso(proceso)


def test_servidor_lee_informe_historico() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        historico = salidas / "agente-01" / "historico"
        historico.mkdir(parents=True, exist_ok=True)
        nombre = "20260507-120000-informe.txt"
        (historico / nombre).write_text("Contenido historico prueba\n", encoding="utf-8")

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/historico/informe?id=1&archivo={nombre}", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert "Contenido historico prueba" in datos.get("contenido", "")
        finally:
            cerrar_proceso(proceso)


def test_servidor_rechaza_historico_con_ruta_arbitraria() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            try:
                request.urlopen(
                    f"http://127.0.0.1:{puerto}/api/historico/informe?id=1&archivo=../secreto.txt",
                    timeout=5,
                )
                raise AssertionError("Se esperaba error controlado por ruta arbitraria")
            except error.HTTPError as http_error:
                assert http_error.code == 400
            assert proceso.poll() is None
        finally:
            cerrar_proceso(proceso)


def test_servidor_compara_informe_historico() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        base = salidas / "agente-01"
        historico = base / "historico"
        historico.mkdir(parents=True, exist_ok=True)
        (base / "informe.txt").write_text(
            "Decision recomendada: aprobar\nActual\n", encoding="utf-8"
        )
        nombre = "20260507-120000-informe.txt"
        (historico / nombre).write_text(
            "Decision recomendada: bloquear\nHistorico\n", encoding="utf-8"
        )

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/comparar?id=1&archivo={nombre}", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert "decision_actual" in datos
            assert "decision_historica" in datos
            assert "diff" in datos
        finally:
            cerrar_proceso(proceso)


def test_servidor_rechaza_comparacion_ruta_arbitraria() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            try:
                request.urlopen(
                    f"http://127.0.0.1:{puerto}/api/comparar?id=1&archivo=../secreto.txt", timeout=5
                )
                raise AssertionError(
                    "Se esperaba error controlado por ruta arbitraria en comparacion"
                )
            except error.HTTPError as http_error:
                assert http_error.code == 400
            assert proceso.poll() is None
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_acciones() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                content_type = resp.headers.get("Content-Type", "")
                cuerpo = resp.read()
            html = cuerpo.decode("utf-8")
            assert "text/html" in content_type
            assert "charset=utf-8" in content_type.lower()
            assert '<meta charset="utf-8">' in html
            assert "Edición guiada" in html
            assert "Edición JSON" in html
            assert "Histórico local de ejecuciones" in html
            assert "Comparación local" in html
            assert "Comparar con último informe" in html
            assert "Último informe cargado" in html
            assert "Informe consolidado local" in html
            assert "Paquete local de evidencias" in html
            assert "Guion local de demo" in html
            assert "EdiciÃ³n" not in html
            assert "ComparaciÃ³n" not in html
            assert "HistÃ³rico" not in html
            assert "Ã" not in html
            assert "Â" not in html
            assert "�" not in html
            assert "Formatear JSON" in html
            assert "Ejecutar agente seleccionado" in html
            assert "Ejecutar todos los agentes" in html
            assert "Regenerar panel local" in html
            assert "Cargar ultimo informe" in html
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_historico() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8")
            assert "Histórico local de ejecuciones" in html
            assert "Actualizar histórico" in html
            assert "Cargar informe histórico" in html
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_comparador() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8")
            assert "Comparar con último informe" in html
            assert "Comparación local" in html
        finally:
            cerrar_proceso(proceso)


def test_servidor_genera_informe_consolidado() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/generar-informe-consolidado"
            )
            assert status == 200
            assert respuesta.get("ok") is True
            assert (salidas / "informe_consolidado.md").is_file()
        finally:
            cerrar_proceso(proceso)


def test_servidor_lee_informe_consolidado() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr
        (salidas / "informe_consolidado.md").write_text(
            "Informe consolidado local\n", encoding="utf-8"
        )

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/informe-consolidado", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert "Informe consolidado local" in datos.get("contenido", "")
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_informe_consolidado() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Informe consolidado local" in html
            assert "Generar informe consolidado" in html
            assert "Cargar informe consolidado" in html
        finally:
            cerrar_proceso(proceso)


def test_servidor_exporta_evidencias_demo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        (salidas / "panel_local.html").write_text(
            "<html><body>panel</body></html>\n", encoding="utf-8"
        )
        (salidas / "informe_consolidado.md").write_text(
            "# Informe consolidado local\n", encoding="utf-8"
        )
        (salidas / "informe_consolidado.html").write_text(
            "<html><body>consolidado</body></html>\n", encoding="utf-8"
        )
        (salidas / "agente-01").mkdir(parents=True, exist_ok=True)
        (salidas / "agente-01" / "informe.txt").write_text("Informe agente 01\n", encoding="utf-8")

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            status, respuesta = post_json(f"http://127.0.0.1:{puerto}/api/exportar-evidencias-demo")
            assert status == 200
            assert respuesta.get("ok") is True
            assert (salidas / "evidencias_demo" / "INDICE_EVIDENCIAS.md").is_file()
        finally:
            cerrar_proceso(proceso)


def test_servidor_lee_evidencias_demo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        carpeta = salidas / "evidencias_demo"
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "INDICE_EVIDENCIAS.md").write_text(
            "# Paquete local de evidencias de demo\n", encoding="utf-8"
        )

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/evidencias-demo", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert "Paquete local de evidencias de demo" in datos.get("contenido_markdown", "")
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_evidencias_demo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Paquete local de evidencias" in html
            assert "Exportar evidencias de demo" in html
            assert "Cargar indice de evidencias" in html
        finally:
            cerrar_proceso(proceso)


def test_servidor_ejecuta_demo_local() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            status, respuesta = post_json(f"http://127.0.0.1:{puerto}/api/ejecutar-demo-local")
            assert status == 200
            assert respuesta.get("ok") is True
            assert (salidas / "panel_local.html").is_file() or (
                salidas / "evidencias_demo" / "INDICE_EVIDENCIAS.md"
            ).is_file()
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_demo_local() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Demo local reproducible" in html
            assert "Ejecutar demo local completa" in html
        finally:
            cerrar_proceso(proceso)


def test_servidor_genera_guion_demo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            status, respuesta = post_json(f"http://127.0.0.1:{puerto}/api/generar-guion-demo")
            assert status == 200
            assert respuesta.get("ok") is True
            assert (salidas / "guion_demo_local.md").is_file()
            assert (salidas / "guion_demo_local.html").is_file()
        finally:
            cerrar_proceso(proceso)


def test_servidor_lee_guion_demo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        (salidas / "guion_demo_local.md").write_text(
            "# Guion local de demo guiada\n", encoding="utf-8"
        )

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/api/guion-demo", timeout=5) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert "Guion local de demo guiada" in datos.get("contenido_markdown", "")
            assert str(salidas / "guion_demo_local.md") == datos.get("ruta_markdown")
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_guion_demo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Guion local de demo" in html
            assert "Generar guion de demo" in html
            assert "Cargar guion de demo" in html
            assert "rutas, comandos y limites" in html
        finally:
            cerrar_proceso(proceso)


def test_catalogo_muestra_nombres_completos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/api/agentes", timeout=5) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert len(datos["agentes"]) == 10
            nombres = [agente["nombre"] for agente in datos["agentes"]]
            assert any("Onboarding Inteligente" in nombre for nombre in nombres)
            assert any("Revision y Cumplimiento" in nombre for nombre in nombres)
        finally:
            cerrar_proceso(proceso)


def test_servidor_resumen_sin_informes() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/api/resumen", timeout=5) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert len(datos["agentes"]) == 10
            agente_01 = next(a for a in datos["agentes"] if a["id"] == 1)
            assert agente_01["existe_datos_trabajo"] is True
            assert agente_01["existe_informe"] is False
        finally:
            cerrar_proceso(proceso)


def test_servidor_resumen_con_informe() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        carpeta = salidas / "agente-01"
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "informe.txt").write_text(
            "Decision humana recomendada: bloquear\n", encoding="utf-8"
        )

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/api/resumen", timeout=5) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            agente_01 = next(a for a in datos["agentes"] if a["id"] == 1)
            assert agente_01["existe_informe"] is True
            assert "bloquear" in agente_01.get("decision_recomendada", "").lower()
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_resumen() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Resumen local de agentes" in html
            assert "Actualizar resumen" in html
            assert "Seleccionar" in html
            assert "Ver informe" in html
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_boton_panel_local() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Abrir panel local" in html
            assert "salidas" in html
            assert "panel_local.html" in html
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_mantiene_consola_resumen() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8")
            assert "Resumen local de agentes" in html
            assert "Edición JSON" in html
            assert "Acciones operativas" in html
            assert "Último informe cargado" in html
        finally:
            cerrar_proceso(proceso)


def test_api_panel_devuelve_estado() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/api/panel", timeout=5) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert "ok" in datos
            assert "ruta_panel" in datos
            assert "existe" in datos
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_01_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-01", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
            rutas = [campo.get("ruta_json") for campo in datos["campos"]]
            assert "cliente.nombre_cliente" in rutas or "cliente.nombre_empresa" in rutas
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_01_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"cliente.nombre_empresa": "Empresa Piloto Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-01", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-01" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["cliente"]["nombre_empresa"] == "Empresa Piloto Editada"
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_edicion_guiada() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8")
            assert "Edición guiada" in html and "Agente 01" in html
            assert "Cargar edición guiada" in html
            assert "Guardar edición guiada" in html
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_02_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-02", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_02_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"empresa_ficticia.nombre_empresa": "Empresa Documental Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-02", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-02" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["empresa_ficticia"]["nombre_empresa"] == "Empresa Documental Editada"
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_03_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-03", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_03_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"empresa_ficticia.nombre_empresa": "Empresa Seguimiento Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-03", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-03" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["empresa_ficticia"]["nombre_empresa"] == "Empresa Seguimiento Editada"
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_indica_edicion_guiada_ampliada() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8")
            assert "Edición guiada" in html
            assert "Agente 01" in html
            assert "Agente 02" in html
            assert "Agente 03" in html
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_04_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-04", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_04_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"propuesta.plazo_estimado": "tres semanas"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-04", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-04" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["propuesta"]["plazo_estimado"] == "tres semanas"
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_05_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-05", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_05_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Operaciones Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-05", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-05" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["empresa_ficticia"]["nombre"] == "NexoSur Operaciones Editada"
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_06_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-06", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_06_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Cobros Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-06", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-06" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["empresa_ficticia"]["nombre"] == "NexoSur Cobros Editada"
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_indica_edicion_guiada_hasta_agente_06() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8")
            assert "Edición guiada" in html
            assert "Agente 01" in html
            assert "Agente 02" in html
            assert "Agente 03" in html
            assert "Agente 04" in html
            assert "Agente 05" in html
            assert "Agente 06" in html
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_07_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-07", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_07_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Pipeline Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-07", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-07" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["empresa_ficticia"]["nombre"] == "NexoSur Pipeline Editada"
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_08_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-08", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_08_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Formacion Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-08", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-08" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["empresa_ficticia"]["nombre"] == "NexoSur Formacion Editada"
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_09_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-09", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_09_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Mercado Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-09", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-09" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["empresa_ficticia"]["nombre"] == "NexoSur Mercado Editada"
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_10_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-10", timeout=5
            ) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert isinstance(datos.get("campos"), list)
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_10_guarda_cambio() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Revision Editada"}}
            status, respuesta = post_json(
                f"http://127.0.0.1:{puerto}/api/formulario/agente-10", payload
            )
            assert status == 200
            assert respuesta.get("ok") is True

            ruta_archivo = trabajo / "agente-10" / "datos.json"
            datos = json.loads(ruta_archivo.read_text(encoding="utf-8"))
            assert datos["empresa_ficticia"]["nombre"] == "NexoSur Revision Editada"
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_indica_edicion_guiada_para_10_agentes() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            with request.urlopen(f"http://127.0.0.1:{puerto}/", timeout=5) as resp:
                html = resp.read().decode("utf-8")
            assert "Edición guiada" in html
            assert "Agente 01" in html
            assert "Agente 02" in html
            assert "Agente 03" in html
            assert "Agente 04" in html
            assert "Agente 05" in html
            assert "Agente 06" in html
            assert "Agente 07" in html
            assert "Agente 08" in html
            assert "Agente 09" in html
            assert "Agente 10" in html
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_99_no_valido() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        puerto = obtener_puerto_libre()

        proceso = iniciar_editor(trabajo, salidas, puerto)
        try:
            esperar_servidor(puerto)
            try:
                request.urlopen(f"http://127.0.0.1:{puerto}/api/formulario/agente-99", timeout=5)
                raise AssertionError("Se esperaba error controlado para formulario no valido")
            except error.HTTPError as http_error:
                assert http_error.code == 404
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
        test_servidor_ejecuta_agente,
        test_servidor_genera_panel,
        test_servidor_lee_informe,
        test_servidor_lista_historico,
        test_servidor_lee_informe_historico,
        test_servidor_rechaza_historico_con_ruta_arbitraria,
        test_servidor_compara_informe_historico,
        test_servidor_rechaza_comparacion_ruta_arbitraria,
        test_servidor_genera_informe_consolidado,
        test_servidor_lee_informe_consolidado,
        test_servidor_exporta_evidencias_demo,
        test_servidor_lee_evidencias_demo,
        test_servidor_ejecuta_demo_local,
        test_servidor_genera_guion_demo,
        test_servidor_lee_guion_demo,
        test_pagina_principal_contiene_acciones,
        test_pagina_principal_contiene_historico,
        test_pagina_principal_contiene_comparador,
        test_pagina_principal_contiene_informe_consolidado,
        test_pagina_principal_contiene_evidencias_demo,
        test_pagina_principal_contiene_demo_local,
        test_pagina_principal_contiene_guion_demo,
        test_catalogo_muestra_nombres_completos,
        test_servidor_resumen_sin_informes,
        test_servidor_resumen_con_informe,
        test_pagina_principal_contiene_resumen,
        test_pagina_principal_contiene_boton_panel_local,
        test_pagina_principal_mantiene_consola_resumen,
        test_api_panel_devuelve_estado,
        test_formulario_agente_01_devuelve_campos,
        test_formulario_agente_01_guarda_cambio,
        test_pagina_principal_contiene_edicion_guiada,
        test_formulario_agente_02_devuelve_campos,
        test_formulario_agente_02_guarda_cambio,
        test_formulario_agente_03_devuelve_campos,
        test_formulario_agente_03_guarda_cambio,
        test_pagina_principal_indica_edicion_guiada_ampliada,
        test_formulario_agente_04_devuelve_campos,
        test_formulario_agente_04_guarda_cambio,
        test_formulario_agente_05_devuelve_campos,
        test_formulario_agente_05_guarda_cambio,
        test_formulario_agente_06_devuelve_campos,
        test_formulario_agente_06_guarda_cambio,
        test_pagina_principal_indica_edicion_guiada_hasta_agente_06,
        test_formulario_agente_07_devuelve_campos,
        test_formulario_agente_07_guarda_cambio,
        test_formulario_agente_08_devuelve_campos,
        test_formulario_agente_08_guarda_cambio,
        test_formulario_agente_09_devuelve_campos,
        test_formulario_agente_09_guarda_cambio,
        test_formulario_agente_10_devuelve_campos,
        test_formulario_agente_10_guarda_cambio,
        test_pagina_principal_indica_edicion_guiada_para_10_agentes,
        test_formulario_agente_99_no_valido,
    ):
        suite.addTest(unittest.FunctionTestCase(funcion))
    return suite
