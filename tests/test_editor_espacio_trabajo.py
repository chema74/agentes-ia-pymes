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


def iniciar_editor(directorio_trabajo: Path, directorio_salidas: Path, puerto: int) -> subprocess.Popen:
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
        assert "no existe el directorio de trabajo" in salida.lower() or "preparar_espacio_trabajo" in salida


def test_servidor_lista_agentes() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, salidas, 8872)
        try:
            esperar_servidor(8872)
            with request.urlopen("http://127.0.0.1:8872/api/agentes", timeout=3) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8873)
        try:
            esperar_servidor(8873)
            with request.urlopen("http://127.0.0.1:8873/api/agente?id=1", timeout=3) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8874)
        try:
            esperar_servidor(8874)
            with request.urlopen("http://127.0.0.1:8874/api/agente?id=1", timeout=3) as resp:
                base = json.loads(resp.read().decode("utf-8"))["datos"]
            base["campo_prueba_editor"] = True

            status, guardado = post_json("http://127.0.0.1:8874/api/agente?id=1", {"datos": base})
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

        proceso = iniciar_editor(trabajo, salidas, 8875)
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


def test_servidor_ejecuta_agente() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, salidas, 8876)
        try:
            esperar_servidor(8876)
            status, respuesta = post_json("http://127.0.0.1:8876/api/ejecutar?id=1")
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

        proceso = iniciar_editor(trabajo, salidas, 8877)
        try:
            esperar_servidor(8877)
            status, respuesta = post_json("http://127.0.0.1:8877/api/generar-panel")
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

        proceso = iniciar_editor(trabajo, salidas, 8878)
        try:
            esperar_servidor(8878)
            status_ejecutar, respuesta_ejecutar = post_json("http://127.0.0.1:8878/api/ejecutar?id=1")
            assert status_ejecutar == 200
            assert respuesta_ejecutar.get("ok") is True

            with request.urlopen("http://127.0.0.1:8878/api/informe?id=1", timeout=10) as resp:
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
        (historico / "20260507-120000-informe.txt").write_text("Informe historico 01\n", encoding="utf-8")

        proceso = iniciar_editor(trabajo, salidas, 8912)
        try:
            esperar_servidor(8912)
            with request.urlopen("http://127.0.0.1:8912/api/historico?id=1", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8913)
        try:
            esperar_servidor(8913)
            with request.urlopen(f"http://127.0.0.1:8913/api/historico/informe?id=1&archivo={nombre}", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8914)
        try:
            esperar_servidor(8914)
            try:
                request.urlopen("http://127.0.0.1:8914/api/historico/informe?id=1&archivo=../secreto.txt", timeout=5)
                assert False, "Se esperaba error controlado por ruta arbitraria"
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
        (base / "informe.txt").write_text("Decision recomendada: aprobar\nActual\n", encoding="utf-8")
        nombre = "20260507-120000-informe.txt"
        (historico / nombre).write_text("Decision recomendada: bloquear\nHistorico\n", encoding="utf-8")

        proceso = iniciar_editor(trabajo, salidas, 8916)
        try:
            esperar_servidor(8916)
            with request.urlopen(f"http://127.0.0.1:8916/api/comparar?id=1&archivo={nombre}", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8917)
        try:
            esperar_servidor(8917)
            try:
                request.urlopen("http://127.0.0.1:8917/api/comparar?id=1&archivo=../secreto.txt", timeout=5)
                assert False, "Se esperaba error controlado por ruta arbitraria en comparacion"
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

        proceso = iniciar_editor(trabajo, salidas, 8879)
        try:
            esperar_servidor(8879)
            with request.urlopen("http://127.0.0.1:8879/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
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

        proceso = iniciar_editor(trabajo, salidas, 8915)
        try:
            esperar_servidor(8915)
            with request.urlopen("http://127.0.0.1:8915/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Historico local de ejecuciones" in html
            assert "Actualizar historico" in html
            assert "Cargar informe historico" in html
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_comparador() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, salidas, 8918)
        try:
            esperar_servidor(8918)
            with request.urlopen("http://127.0.0.1:8918/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Comparar con ultimo informe" in html
            assert "Comparaci" in html and "local" in html
        finally:
            cerrar_proceso(proceso)


def test_servidor_genera_informe_consolidado() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, salidas, 8919)
        try:
            esperar_servidor(8919)
            status, respuesta = post_json("http://127.0.0.1:8919/api/generar-informe-consolidado")
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
        (salidas / "informe_consolidado.md").write_text("Informe consolidado local\n", encoding="utf-8")

        proceso = iniciar_editor(trabajo, salidas, 8920)
        try:
            esperar_servidor(8920)
            with request.urlopen("http://127.0.0.1:8920/api/informe-consolidado", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8921)
        try:
            esperar_servidor(8921)
            with request.urlopen("http://127.0.0.1:8921/", timeout=5) as resp:
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

        (salidas / "panel_local.html").write_text("<html><body>panel</body></html>\n", encoding="utf-8")
        (salidas / "informe_consolidado.md").write_text("# Informe consolidado local\n", encoding="utf-8")
        (salidas / "informe_consolidado.html").write_text("<html><body>consolidado</body></html>\n", encoding="utf-8")
        (salidas / "agente-01").mkdir(parents=True, exist_ok=True)
        (salidas / "agente-01" / "informe.txt").write_text("Informe agente 01\n", encoding="utf-8")

        proceso = iniciar_editor(trabajo, salidas, 8922)
        try:
            esperar_servidor(8922)
            status, respuesta = post_json("http://127.0.0.1:8922/api/exportar-evidencias-demo")
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
        (carpeta / "INDICE_EVIDENCIAS.md").write_text("# Paquete local de evidencias de demo\n", encoding="utf-8")

        proceso = iniciar_editor(trabajo, salidas, 8923)
        try:
            esperar_servidor(8923)
            with request.urlopen("http://127.0.0.1:8923/api/evidencias-demo", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8924)
        try:
            esperar_servidor(8924)
            with request.urlopen("http://127.0.0.1:8924/", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8925)
        try:
            esperar_servidor(8925)
            status, respuesta = post_json("http://127.0.0.1:8925/api/ejecutar-demo-local")
            assert status == 200
            assert respuesta.get("ok") is True
            assert (salidas / "panel_local.html").is_file() or (salidas / "evidencias_demo" / "INDICE_EVIDENCIAS.md").is_file()
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_demo_local() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, salidas, 8926)
        try:
            esperar_servidor(8926)
            with request.urlopen("http://127.0.0.1:8926/", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8927)
        try:
            esperar_servidor(8927)
            status, respuesta = post_json("http://127.0.0.1:8927/api/generar-guion-demo")
            assert status == 200
            assert respuesta.get("ok") is True
            assert (salidas / "guion_demo_local.md").is_file()
        finally:
            cerrar_proceso(proceso)


def test_servidor_lee_guion_demo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        (salidas / "guion_demo_local.md").write_text("# Guion local de demo guiada\n", encoding="utf-8")

        proceso = iniciar_editor(trabajo, salidas, 8928)
        try:
            esperar_servidor(8928)
            with request.urlopen("http://127.0.0.1:8928/api/guion-demo", timeout=5) as resp:
                datos = json.loads(resp.read().decode("utf-8"))
            assert datos.get("ok") is True
            assert "Guion local de demo guiada" in datos.get("contenido_markdown", "")
        finally:
            cerrar_proceso(proceso)


def test_pagina_principal_contiene_guion_demo() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, salidas, 8929)
        try:
            esperar_servidor(8929)
            with request.urlopen("http://127.0.0.1:8929/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Guion local de demo" in html
            assert "Generar guion de demo" in html
            assert "Cargar guion de demo" in html
        finally:
            cerrar_proceso(proceso)


def test_catalogo_muestra_nombres_completos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, salidas, 8880)
        try:
            esperar_servidor(8880)
            with request.urlopen("http://127.0.0.1:8880/api/agentes", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8881)
        try:
            esperar_servidor(8881)
            with request.urlopen("http://127.0.0.1:8881/api/resumen", timeout=5) as resp:
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
        (carpeta / "informe.txt").write_text("Decision humana recomendada: bloquear\n", encoding="utf-8")

        proceso = iniciar_editor(trabajo, salidas, 8882)
        try:
            esperar_servidor(8882)
            with request.urlopen("http://127.0.0.1:8882/api/resumen", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8883)
        try:
            esperar_servidor(8883)
            with request.urlopen("http://127.0.0.1:8883/", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8884)
        try:
            esperar_servidor(8884)
            with request.urlopen("http://127.0.0.1:8884/", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8885)
        try:
            esperar_servidor(8885)
            with request.urlopen("http://127.0.0.1:8885/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Resumen local de agentes" in html
            assert "EdiciÃ³n JSON" in html or ("Edici" in html and "JSON" in html)
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

        proceso = iniciar_editor(trabajo, salidas, 8886)
        try:
            esperar_servidor(8886)
            with request.urlopen("http://127.0.0.1:8886/api/panel", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8887)
        try:
            esperar_servidor(8887)
            with request.urlopen("http://127.0.0.1:8887/api/formulario/agente-01", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8888)
        try:
            esperar_servidor(8888)
            payload = {"campos": {"cliente.nombre_empresa": "Empresa Piloto Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8888/api/formulario/agente-01", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8889)
        try:
            esperar_servidor(8889)
            with request.urlopen("http://127.0.0.1:8889/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "Edición guiada del Agente 01" in html or "Edici" in html and "Agente 01" in html
            assert "Cargar edición guiada" in html or "Cargar edici" in html
            assert "Guardar edición guiada" in html or "Guardar edici" in html
        finally:
            cerrar_proceso(proceso)


def test_formulario_agente_02_devuelve_campos() -> None:
    with tempfile.TemporaryDirectory() as tmp_trabajo, tempfile.TemporaryDirectory() as tmp_salidas:
        trabajo = Path(tmp_trabajo)
        salidas = Path(tmp_salidas)
        preparado = ejecutar(SCRIPT_PREPARAR, "--directorio-trabajo", str(trabajo))
        assert preparado.returncode == 0, preparado.stdout + preparado.stderr

        proceso = iniciar_editor(trabajo, salidas, 8890)
        try:
            esperar_servidor(8890)
            with request.urlopen("http://127.0.0.1:8890/api/formulario/agente-02", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8891)
        try:
            esperar_servidor(8891)
            payload = {"campos": {"empresa_ficticia.nombre_empresa": "Empresa Documental Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8891/api/formulario/agente-02", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8892)
        try:
            esperar_servidor(8892)
            with request.urlopen("http://127.0.0.1:8892/api/formulario/agente-03", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8893)
        try:
            esperar_servidor(8893)
            payload = {"campos": {"empresa_ficticia.nombre_empresa": "Empresa Seguimiento Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8893/api/formulario/agente-03", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8894)
        try:
            esperar_servidor(8894)
            with request.urlopen("http://127.0.0.1:8894/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "EdiciÃ³n guiada" in html or ("Edici" in html and "guiada" in html)
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

        proceso = iniciar_editor(trabajo, salidas, 8895)
        try:
            esperar_servidor(8895)
            with request.urlopen("http://127.0.0.1:8895/api/formulario/agente-04", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8896)
        try:
            esperar_servidor(8896)
            payload = {"campos": {"propuesta.plazo_estimado": "tres semanas"}}
            status, respuesta = post_json("http://127.0.0.1:8896/api/formulario/agente-04", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8897)
        try:
            esperar_servidor(8897)
            with request.urlopen("http://127.0.0.1:8897/api/formulario/agente-05", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8898)
        try:
            esperar_servidor(8898)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Operaciones Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8898/api/formulario/agente-05", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8899)
        try:
            esperar_servidor(8899)
            with request.urlopen("http://127.0.0.1:8899/api/formulario/agente-06", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8900)
        try:
            esperar_servidor(8900)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Cobros Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8900/api/formulario/agente-06", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8901)
        try:
            esperar_servidor(8901)
            with request.urlopen("http://127.0.0.1:8901/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "EdiciÃ³n guiada" in html or ("Edici" in html and "guiada" in html)
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

        proceso = iniciar_editor(trabajo, salidas, 8902)
        try:
            esperar_servidor(8902)
            with request.urlopen("http://127.0.0.1:8902/api/formulario/agente-07", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8903)
        try:
            esperar_servidor(8903)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Pipeline Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8903/api/formulario/agente-07", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8904)
        try:
            esperar_servidor(8904)
            with request.urlopen("http://127.0.0.1:8904/api/formulario/agente-08", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8905)
        try:
            esperar_servidor(8905)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Formacion Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8905/api/formulario/agente-08", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8906)
        try:
            esperar_servidor(8906)
            with request.urlopen("http://127.0.0.1:8906/api/formulario/agente-09", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8907)
        try:
            esperar_servidor(8907)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Mercado Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8907/api/formulario/agente-09", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8908)
        try:
            esperar_servidor(8908)
            with request.urlopen("http://127.0.0.1:8908/api/formulario/agente-10", timeout=5) as resp:
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

        proceso = iniciar_editor(trabajo, salidas, 8909)
        try:
            esperar_servidor(8909)
            payload = {"campos": {"empresa_ficticia.nombre": "NexoSur Revision Editada"}}
            status, respuesta = post_json("http://127.0.0.1:8909/api/formulario/agente-10", payload)
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

        proceso = iniciar_editor(trabajo, salidas, 8910)
        try:
            esperar_servidor(8910)
            with request.urlopen("http://127.0.0.1:8910/", timeout=5) as resp:
                html = resp.read().decode("utf-8", errors="replace")
            assert "EdiciÃ³n guiada" in html or ("Edici" in html and "guiada" in html)
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

        proceso = iniciar_editor(trabajo, salidas, 8911)
        try:
            esperar_servidor(8911)
            try:
                request.urlopen("http://127.0.0.1:8911/api/formulario/agente-99", timeout=5)
                assert False, "Se esperaba error controlado para formulario no valido"
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

