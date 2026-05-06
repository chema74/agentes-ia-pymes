from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import sys
import webbrowser

AGENTES = {i: f"Agente {i:02d}" for i in range(1, 11)}


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Editor local temporal del espacio de trabajo (no es una API productiva)."
    )
    parser.add_argument("--directorio-trabajo", default="espacio_trabajo")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--puerto", type=int, default=8765)
    parser.add_argument("--abrir", action="store_true", help="Abre el navegador al iniciar.")
    return parser


def resolver_directorio_trabajo(valor: str) -> Path:
    raiz = obtener_raiz_repositorio()
    ruta = Path(valor)
    if not ruta.is_absolute():
        ruta = raiz / ruta
    return ruta


def ruta_datos_agente(directorio_trabajo: Path, agente_id: int) -> Path:
    return directorio_trabajo / f"agente-{agente_id:02d}" / "datos.json"


def validar_agente_id(texto: str | None) -> int:
    if texto is None or not texto.isdigit():
        raise ValueError("Debes indicar un id de agente numerico entre 1 y 10.")
    agente_id = int(texto)
    if agente_id not in AGENTES:
        raise ValueError("El id de agente debe estar entre 1 y 10.")
    return agente_id


def leer_json_agente(directorio_trabajo: Path, agente_id: int) -> dict:
    ruta = ruta_datos_agente(directorio_trabajo, agente_id)
    if not ruta.is_file():
        raise FileNotFoundError(
            f"No existe el archivo del agente {agente_id:02d} en el espacio de trabajo: {ruta}"
        )
    with ruta.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_json_agente(directorio_trabajo: Path, agente_id: int, texto_json: str) -> None:
    try:
        datos = json.loads(texto_json)
    except json.JSONDecodeError as error:
        raise ValueError(f"JSON invalido: {error}") from error

    ruta = ruta_datos_agente(directorio_trabajo, agente_id)
    if not ruta.parent.exists():
        raise FileNotFoundError(
            f"No existe carpeta del agente {agente_id:02d} en el espacio de trabajo: {ruta.parent}"
        )

    contenido = json.dumps(datos, ensure_ascii=False, indent=2)
    ruta.write_text(contenido + "\n", encoding="utf-8")


def html_editor() -> str:
    return """<!doctype html>
<html lang=\"es\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Editor local de espacio de trabajo</title>
<style>
body{font-family:Segoe UI,Tahoma,Arial,sans-serif;margin:0;background:#f4f6f8;color:#1f2937}
main{max-width:1080px;margin:0 auto;padding:20px}
.card{background:#fff;border:1px solid #d1d5db;border-radius:10px;padding:16px;margin-bottom:14px}
label,select,button{font-size:14px}
textarea{width:100%;min-height:420px;font-family:Consolas,monospace;font-size:13px}
.msg{margin-top:10px;padding:8px;border-radius:8px;background:#eef2ff}
.err{background:#fee2e2}
</style>
</head>
<body>
<main>
  <div class=\"card\">
    <h1>Editor local temporal del espacio de trabajo</h1>
    <p>Esta interfaz es local, temporal y de apoyo. No es una API productiva ni un dashboard publico.</p>
    <p>Solo edita copias en <code>espacio_trabajo/</code>. No modifica JSON originales.</p>
  </div>
  <div class=\"card\">
    <label for=\"agente\">Agente:</label>
    <select id=\"agente\"></select>
    <button id=\"cargar\">Cargar JSON</button>
    <button id=\"guardar\">Validar y guardar</button>
    <div id=\"mensaje\" class=\"msg\"></div>
  </div>
  <div class=\"card\">
    <textarea id=\"contenido\" spellcheck=\"false\"></textarea>
  </div>
</main>
<script>
const sel=document.getElementById('agente');
const txt=document.getElementById('contenido');
const msg=document.getElementById('mensaje');
function setMsg(t,e=false){msg.textContent=t;msg.className=e?'msg err':'msg';}
async function cargarAgentes(){
  const r=await fetch('/api/agentes');
  const d=await r.json();
  sel.innerHTML='';
  d.agentes.forEach(a=>{
    const o=document.createElement('option');
    o.value=a.id;o.textContent=`${a.id.toString().padStart(2,'0')} - ${a.nombre}`;
    sel.appendChild(o);
  });
}
async function cargar(){
  const id=sel.value;
  const r=await fetch(`/api/agente?id=${id}`);
  const d=await r.json();
  if(!r.ok){setMsg(d.error||'Error al cargar',true);return;}
  txt.value=JSON.stringify(d.datos,null,2);
  setMsg(`Agente ${id} cargado.`);
}
async function guardar(){
  const id=sel.value;
  let obj;
  try{obj=JSON.parse(txt.value);}catch(e){setMsg('JSON invalido en el editor: '+e,true);return;}
  const r=await fetch(`/api/agente?id=${id}`,{method:'POST',headers:{'Content-Type':'application/json; charset=utf-8'},body:JSON.stringify({datos:obj})});
  const d=await r.json();
  if(!r.ok){setMsg(d.error||'Error al guardar',true);return;}
  txt.value=JSON.stringify(d.datos,null,2);
  setMsg(d.mensaje||'Guardado correcto.');
}
document.getElementById('cargar').addEventListener('click',cargar);
document.getElementById('guardar').addEventListener('click',guardar);
cargarAgentes().then(cargar).catch(e=>setMsg('Error al iniciar: '+e,true));
</script>
</body>
</html>
"""


def crear_handler(directorio_trabajo: Path):
    class EditorHandler(BaseHTTPRequestHandler):
        def _enviar_json(self, codigo: int, payload: dict) -> None:
            contenido = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(codigo)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(contenido)))
            self.end_headers()
            self.wfile.write(contenido)

        def _enviar_html(self, codigo: int, contenido: str) -> None:
            data = contenido.encode("utf-8")
            self.send_response(codigo)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self) -> None:
            url = urlparse(self.path)
            if url.path == "/":
                self._enviar_html(200, html_editor())
                return
            if url.path == "/api/agentes":
                agentes = [{"id": i, "nombre": AGENTES[i]} for i in sorted(AGENTES)]
                self._enviar_json(200, {"agentes": agentes, "aviso": "Interfaz local temporal."})
                return
            if url.path == "/api/agente":
                try:
                    agente_id = validar_agente_id(parse_qs(url.query).get("id", [None])[0])
                    datos = leer_json_agente(directorio_trabajo, agente_id)
                    self._enviar_json(200, {"id": agente_id, "datos": datos})
                except ValueError as error:
                    self._enviar_json(400, {"error": str(error)})
                except FileNotFoundError as error:
                    self._enviar_json(404, {"error": str(error)})
                except json.JSONDecodeError as error:
                    self._enviar_json(500, {"error": f"JSON invalido en archivo de trabajo: {error}"})
                return
            self._enviar_json(404, {"error": "Ruta no encontrada."})

        def do_POST(self) -> None:
            url = urlparse(self.path)
            if url.path != "/api/agente":
                self._enviar_json(404, {"error": "Ruta no encontrada."})
                return
            try:
                agente_id = validar_agente_id(parse_qs(url.query).get("id", [None])[0])
                longitud = int(self.headers.get("Content-Length", "0"))
                cuerpo = self.rfile.read(longitud).decode("utf-8")
                payload = json.loads(cuerpo)
                if "datos" not in payload:
                    raise ValueError("Falta la clave 'datos' en el cuerpo de la peticion.")
                guardar_json_agente(directorio_trabajo, agente_id, json.dumps(payload["datos"], ensure_ascii=False))
                datos = leer_json_agente(directorio_trabajo, agente_id)
                self._enviar_json(200, {"mensaje": "Guardado correcto en espacio de trabajo.", "id": agente_id, "datos": datos})
            except ValueError as error:
                self._enviar_json(400, {"error": str(error)})
            except FileNotFoundError as error:
                self._enviar_json(404, {"error": str(error)})
            except json.JSONDecodeError as error:
                self._enviar_json(400, {"error": f"JSON invalido: {error}"})
            except Exception as error:
                self._enviar_json(500, {"error": f"Error inesperado al guardar: {error}"})

        def log_message(self, format: str, *args) -> None:
            return

    return EditorHandler


def iniciar_servidor(directorio_trabajo: Path, host: str, puerto: int, abrir: bool) -> int:
    handler = crear_handler(directorio_trabajo)
    servidor = HTTPServer((host, puerto), handler)

    url = f"http://{host}:{puerto}/"
    print(f"Directorio de trabajo usado: {directorio_trabajo}")
    print(f"Editor local disponible en: {url}")
    print("Aviso: herramienta local temporal; no es una API productiva.")
    print("Aviso: no modifica JSON originales de agentes/*/datos_ejemplo/.")
    print("Para detener el servidor usa Ctrl+C.")

    if abrir:
        webbrowser.open(url)

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("Servidor detenido por usuario.")
        return 0
    finally:
        servidor.server_close()


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)

    try:
        directorio_trabajo = resolver_directorio_trabajo(args.directorio_trabajo)
        if not directorio_trabajo.exists():
            print("Error: no existe el directorio de trabajo.")
            print("Primero ejecuta: python scripts/preparar_espacio_trabajo.py")
            return 1
        return iniciar_servidor(directorio_trabajo, args.host, args.puerto, args.abrir)
    except OSError as error:
        print(f"Error al arrancar el servidor local: {error}")
        return 1
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
