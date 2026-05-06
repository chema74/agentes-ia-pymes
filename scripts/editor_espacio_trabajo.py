from __future__ import annotations

import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path
import subprocess
import sys
from urllib.parse import parse_qs, urlparse
import webbrowser

AGENTES = {
    1: "Agente de Onboarding Inteligente",
    2: "Agente Documental Inteligente",
    3: "Agente de Seguimiento de Clientes",
    4: "Agente Generador de Propuestas",
    5: "Agente de Operaciones para PYMES",
    6: "Agente de Control de Cobros y Flujo de Caja",
    7: "Agente de Pipeline Comercial",
    8: "Agente de Formacion Interna",
    9: "Agente de Analisis de Mercado",
    10: "Agente de Revision y Cumplimiento",
}


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Editor local temporal del espacio de trabajo (no es una API productiva)."
    )
    parser.add_argument("--directorio-trabajo", default="espacio_trabajo")
    parser.add_argument("--directorio-salidas", default="salidas")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--puerto", type=int, default=8765)
    parser.add_argument("--abrir", action="store_true", help="Abre el navegador al iniciar.")
    return parser


def resolver_directorio(valor: str) -> Path:
    raiz = obtener_raiz_repositorio()
    ruta = Path(valor)
    if not ruta.is_absolute():
        ruta = raiz / ruta
    return ruta


def ruta_datos_agente(directorio_trabajo: Path, agente_id: int) -> Path:
    return directorio_trabajo / f"agente-{agente_id:02d}" / "datos.json"


def ruta_informe_agente(directorio_salidas: Path, agente_id: int) -> Path:
    return directorio_salidas / f"agente-{agente_id:02d}" / "informe.txt"


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


def ejecutar_comando_local(argumentos: list[str]) -> tuple[int, str]:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    resultado = subprocess.run(
        argumentos,
        cwd=obtener_raiz_repositorio(),
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        env=entorno,
        check=False,
    )
    salida = ((resultado.stdout or "") + "\n" + (resultado.stderr or "")).strip()
    return resultado.returncode, salida


def ejecutar_agente_local(agente_id: int, directorio_trabajo: Path, directorio_salidas: Path) -> dict:
    comando = [
        sys.executable,
        str(obtener_raiz_repositorio() / "scripts" / "ejecutar_agente.py"),
        "--agente",
        str(agente_id),
        "--usar-datos-trabajo",
        "--directorio-trabajo",
        str(directorio_trabajo),
        "--guardar-salida",
        "--directorio-salidas",
        str(directorio_salidas),
    ]
    codigo, salida = ejecutar_comando_local(comando)
    ruta_informe = ruta_informe_agente(directorio_salidas, agente_id)
    return {
        "ok": codigo == 0,
        "codigo_salida": codigo,
        "mensaje": "Agente ejecutado correctamente." if codigo == 0 else "Error al ejecutar el agente.",
        "salida_consola": salida,
        "ruta_informe": str(ruta_informe),
    }


def ejecutar_todos_local(directorio_trabajo: Path, directorio_salidas: Path) -> dict:
    comando = [
        sys.executable,
        str(obtener_raiz_repositorio() / "scripts" / "ejecutar_agente.py"),
        "--todos",
        "--usar-datos-trabajo",
        "--directorio-trabajo",
        str(directorio_trabajo),
        "--guardar-salida",
        "--directorio-salidas",
        str(directorio_salidas),
    ]
    codigo, salida = ejecutar_comando_local(comando)
    return {
        "ok": codigo == 0,
        "codigo_salida": codigo,
        "mensaje": "Ejecucion de todos los agentes completada." if codigo == 0 else "Error al ejecutar todos los agentes.",
        "salida_consola": salida,
    }


def generar_panel_local(directorio_trabajo: Path, directorio_salidas: Path) -> dict:
    comando = [
        sys.executable,
        str(obtener_raiz_repositorio() / "scripts" / "generar_panel_local.py"),
        "--generar-informes",
        "--usar-datos-trabajo",
        "--directorio-trabajo",
        str(directorio_trabajo),
        "--directorio-salidas",
        str(directorio_salidas),
    ]
    codigo, salida = ejecutar_comando_local(comando)
    ruta_panel = directorio_salidas / "panel_local.html"
    return {
        "ok": codigo == 0,
        "codigo_salida": codigo,
        "mensaje": "Panel local regenerado." if codigo == 0 else "Error al generar el panel local.",
        "salida_consola": salida,
        "ruta_panel": str(ruta_panel),
    }


def extraer_valor_por_prefijo(texto: str, prefijos: list[str]) -> str:
    for linea in texto.splitlines():
        linea_limpia = linea.strip()
        for prefijo in prefijos:
            if linea_limpia.lower().startswith(prefijo.lower()):
                _, _, resto = linea_limpia.partition(":")
                valor = resto.strip()
                if valor:
                    return valor
    return ""


def construir_resumen_agentes(directorio_trabajo: Path, directorio_salidas: Path) -> list[dict]:
    resumen = []
    for agente_id, nombre in AGENTES.items():
        codigo = f"agente-{agente_id:02d}"
        ruta_datos = ruta_datos_agente(directorio_trabajo, agente_id)
        ruta_informe = ruta_informe_agente(directorio_salidas, agente_id)
        existe_datos = ruta_datos.is_file()
        existe_informe = ruta_informe.is_file()
        decision = ""
        aviso = ""
        estado = "sin_datos_trabajo" if not existe_datos else "sin_informe"

        if existe_informe:
            try:
                texto = ruta_informe.read_text(encoding="utf-8", errors="replace")
                decision = extraer_valor_por_prefijo(
                    texto,
                    [
                        "Decision humana recomendada",
                        "Decisión humana recomendada",
                        "Decision recomendada",
                        "Decisión recomendada",
                    ],
                )
                aviso = extraer_valor_por_prefijo(texto, ["Aviso", "Limite", "Límite", "Riesgo"])
                estado = "informe_disponible"
                if not aviso:
                    aviso = "Sin avisos identificados en el informe."
            except Exception:
                estado = "error_lectura"
                aviso = "No se pudo leer el informe."
        else:
            aviso = "No hay informe generado."

        resumen.append(
            {
                "id": agente_id,
                "codigo": codigo,
                "nombre": nombre,
                "existe_datos_trabajo": existe_datos,
                "ruta_datos_trabajo": str(ruta_datos),
                "existe_informe": existe_informe,
                "ruta_informe": str(ruta_informe),
                "decision_recomendada": decision,
                "aviso": aviso,
                "estado_resumen": estado,
            }
        )
    return resumen


def html_editor() -> str:
    return """<!doctype html>
<html lang=\"es\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Editor local de espacio de trabajo</title>
<style>
:root{--fondo:#f3f5f8;--card:#ffffff;--texto:#1f2937;--borde:#d6dbe3;--ok:#065f46;--okf:#d1fae5;--av:#92400e;--avf:#fef3c7;--er:#991b1b;--erf:#fee2e2}
*{box-sizing:border-box}
body{font-family:Segoe UI,Tahoma,Arial,sans-serif;margin:0;background:linear-gradient(180deg,#eef2f7,var(--fondo));color:var(--texto)}
main{max-width:1180px;margin:0 auto;padding:22px}
.card{background:var(--card);border:1px solid var(--borde);border-radius:12px;padding:16px;margin-bottom:14px}
.cabecera h1{margin:0 0 8px}
.nota{margin:6px 0;padding:10px;border-radius:8px;background:var(--avf);color:var(--av)}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
label,select,button{font-size:14px}
select,button{padding:8px 10px;border:1px solid #c7d0db;border-radius:8px;background:#fff}
button{cursor:pointer;background:#f9fafb}
button:hover{background:#f3f4f6}
textarea{width:100%;min-height:380px;padding:10px;border:1px solid #c7d0db;border-radius:8px;font-family:Consolas,monospace;font-size:13px;line-height:1.45}
.estado{margin-top:10px;padding:10px;border-radius:8px;background:#eef2ff}
.estado.ok{background:var(--okf);color:var(--ok)}
.estado.warn{background:var(--avf);color:var(--av)}
.estado.err{background:var(--erf);color:var(--er)}
pre{background:#0b1020;color:#d1e7ff;padding:10px;border-radius:8px;white-space:pre-wrap;max-height:280px;overflow:auto}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media (max-width: 900px){.grid{grid-template-columns:1fr}}
.resumen-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:10px}
.tarjeta-agente{border:1px solid #d7dde7;border-radius:10px;padding:10px;background:#fbfcfe}
.tarjeta-agente h4{margin:0 0 6px}
.tag{display:inline-block;padding:2px 6px;border-radius:999px;background:#e5e7eb;font-size:12px}
</style>
</head>
<body>
<main>
  <div class=\"card cabecera\">
    <h1>Editor local temporal del espacio de trabajo</h1>
    <p>Interfaz local de apoyo para editar datos ficticios y lanzar validaciones.</p>
    <p class=\"nota\">Limites: herramienta local temporal, no API productiva, no dashboard publico, no modifica JSON originales.</p>
  </div>

  <div class=\"card\">
    <h2>Resumen local de agentes</h2>
    <div class=\"row\">
      <button id=\"actualizarResumen\">Actualizar resumen</button>
    </div>
    <div id=\"resumen\" class=\"resumen-grid\"></div>
  </div>

  <div class=\"card\">
    <div class=\"row\">
      <label for=\"agente\">Agente:</label>
      <select id=\"agente\"></select>
      <button id=\"cargar\">Cargar JSON</button>
      <button id=\"formatear\">Formatear JSON</button>
      <button id=\"guardar\">Validar y guardar</button>
    </div>
    <div class=\"estado\" id=\"mensaje\"></div>
  </div>

  <div class=\"grid\">
    <div class=\"card\">
      <h2>Edicion JSON</h2>
      <textarea id=\"contenido\" spellcheck=\"false\"></textarea>
    </div>
    <div class=\"card\">
      <h2>Acciones operativas</h2>
      <div class=\"row\">
        <button id=\"ejecutar\">Ejecutar agente seleccionado</button>
        <button id=\"ejecutarTodos\">Ejecutar todos los agentes</button>
        <button id=\"generarPanel\">Regenerar panel local</button>
        <button id=\"cargarInforme\">Cargar ultimo informe</button>
        <button id=\"rutaPanel\">Ver ruta panel local</button>
      </div>
      <h3>Resultados</h3>
      <p id=\"rutaInfo\"></p>
      <pre id=\"salida\"></pre>
    </div>
  </div>

  <div class=\"card\">
    <h2>Ultimo informe cargado</h2>
    <small>Usa el boton \"Cargar ultimo informe\" para refrescar esta seccion.</small>
    <pre id=\"informe\"></pre>
  </div>
</main>
<script>
const sel=document.getElementById('agente');
const txt=document.getElementById('contenido');
const msg=document.getElementById('mensaje');
const salida=document.getElementById('salida');
const informe=document.getElementById('informe');
const rutaInfo=document.getElementById('rutaInfo');
const resumen=document.getElementById('resumen');

function setMsg(t,tipo='warn'){msg.textContent=t;msg.className='estado '+tipo;}
function setSalida(t){salida.textContent=t||'';}
function setInforme(t){informe.textContent=t||'';}

async function pedir(url, opciones={}){
  const r=await fetch(url,opciones);
  const d=await r.json();
  return {ok:r.ok,data:d};
}

async function cargarAgentes(){
  const r=await pedir('/api/agentes');
  if(!r.ok){setMsg(r.data.error||'Error al cargar agentes','err');return;}
  sel.innerHTML='';
  r.data.agentes.forEach(a=>{
    const o=document.createElement('option');
    o.value=a.id;o.textContent=`${a.id.toString().padStart(2,'0')} - ${a.nombre}`;
    sel.appendChild(o);
  });
}

function tarjetaResumen(agente){
  const decision = agente.decision_recomendada || 'No identificada';
  return `<div class="tarjeta-agente">
    <h4>${agente.codigo} - ${agente.nombre}</h4>
    <p><span class="tag">Datos: ${agente.existe_datos_trabajo?'si':'no'}</span>
    <span class="tag">Informe: ${agente.existe_informe?'si':'no'}</span></p>
    <p><strong>Decision:</strong> ${decision}</p>
    <p><strong>Aviso:</strong> ${agente.aviso || 'Sin aviso'}</p>
    <div class="row">
      <button data-accion="seleccionar" data-id="${agente.id}">Seleccionar</button>
      <button data-accion="ejecutar" data-id="${agente.id}">Ejecutar</button>
      <button data-accion="informe" data-id="${agente.id}">Ver informe</button>
    </div>
  </div>`;
}

async function actualizarResumen(){
  const r=await pedir('/api/resumen');
  if(!r.ok){setMsg(r.data.error||'No se pudo actualizar resumen','err');return;}
  resumen.innerHTML = r.data.agentes.map(tarjetaResumen).join('');
}

async function cargar(){
  const id=sel.value;
  const r=await pedir(`/api/agente?id=${id}`);
  if(!r.ok){setMsg(r.data.error||'Error al cargar','err');return;}
  txt.value=JSON.stringify(r.data.datos,null,2);
  setMsg(`Agente ${id} cargado.`,'ok');
}

function formatear(){
  try{
    const obj=JSON.parse(txt.value);
    txt.value=JSON.stringify(obj,null,2);
    setMsg('JSON formateado en pantalla.','ok');
  }catch(e){
    setMsg('JSON invalido para formatear: '+e,'err');
  }
}

async function guardar(){
  const id=sel.value;
  let obj;
  try{obj=JSON.parse(txt.value);}catch(e){setMsg('JSON invalido en el editor: '+e,'err');return;}
  const r=await pedir(`/api/agente?id=${id}`,{method:'POST',headers:{'Content-Type':'application/json; charset=utf-8'},body:JSON.stringify({datos:obj})});
  if(!r.ok){setMsg(r.data.error||'Error al guardar','err');return;}
  txt.value=JSON.stringify(r.data.datos,null,2);
  setMsg(r.data.mensaje||'Guardado correcto.','ok');
}

async function ejecutarAgente(){
  const id=sel.value;
  setMsg('Ejecutando agente...','warn');
  const r=await pedir(`/api/ejecutar?id=${id}`,{method:'POST'});
  setMsg(r.data.mensaje||'Operacion finalizada',r.data.ok?'ok':'err');
  setSalida(r.data.salida_consola||'');
  rutaInfo.textContent=r.data.ruta_informe?`Informe: ${r.data.ruta_informe}`:'';
}

async function ejecutarTodos(){
  setMsg('Ejecutando todos los agentes...','warn');
  const r=await pedir('/api/ejecutar-todos',{method:'POST'});
  setMsg(r.data.mensaje||'Operacion finalizada',r.data.ok?'ok':'err');
  setSalida(r.data.salida_consola||'');
}

async function regenerarPanel(){
  setMsg('Regenerando panel local...','warn');
  const r=await pedir('/api/generar-panel',{method:'POST'});
  setMsg(r.data.mensaje||'Operacion finalizada',r.data.ok?'ok':'err');
  setSalida(r.data.salida_consola||'');
  rutaInfo.textContent=r.data.ruta_panel?`Panel: ${r.data.ruta_panel}`:'';
}

async function cargarInforme(){
  const id=sel.value;
  const r=await pedir(`/api/informe?id=${id}`);
  if(!r.ok||!r.data.ok){setMsg(r.data.error||r.data.mensaje||'No se pudo leer informe','err');return;}
  setMsg('Informe cargado.','ok');
  setSalida(r.data.contenido||'');
  setInforme(r.data.contenido||'');
  rutaInfo.textContent=r.data.ruta_informe?`Informe: ${r.data.ruta_informe}`:'';
}

async function verRutaPanel(){
  const r=await pedir('/api/panel');
  if(!r.ok||!r.data.ok){setMsg(r.data.error||'No se pudo obtener la ruta del panel','err');return;}
  const estado=r.data.existe?'(existe)':'(aun no generado)';
  rutaInfo.textContent=`Panel: ${r.data.ruta_panel} ${estado}`;
  setMsg('Ruta de panel local consultada.','ok');
}

async function desdeTarjeta(evento){
  const boton = evento.target.closest('button[data-accion]');
  if(!boton){return;}
  const id = boton.getAttribute('data-id');
  const accion = boton.getAttribute('data-accion');
  if(!id || !accion){return;}
  sel.value = id;
  if(accion==='seleccionar'){
    await cargar();
    return;
  }
  if(accion==='ejecutar'){
    await ejecutarAgente();
    await actualizarResumen();
    return;
  }
  if(accion==='informe'){
    await cargarInforme();
  }
}

document.getElementById('cargar').addEventListener('click',cargar);
document.getElementById('formatear').addEventListener('click',formatear);
document.getElementById('guardar').addEventListener('click',guardar);
document.getElementById('ejecutar').addEventListener('click',ejecutarAgente);
document.getElementById('ejecutarTodos').addEventListener('click',ejecutarTodos);
document.getElementById('generarPanel').addEventListener('click',regenerarPanel);
document.getElementById('cargarInforme').addEventListener('click',cargarInforme);
document.getElementById('rutaPanel').addEventListener('click',verRutaPanel);
document.getElementById('actualizarResumen').addEventListener('click',actualizarResumen);
resumen.addEventListener('click',desdeTarjeta);

cargarAgentes()
  .then(cargar)
  .then(actualizarResumen)
  .catch(e=>setMsg('Error al iniciar: '+e,'err'));
</script>
</body>
</html>
"""


def crear_handler(directorio_trabajo: Path, directorio_salidas: Path):
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

        def _leer_json_post(self) -> dict:
            longitud = int(self.headers.get("Content-Length", "0"))
            cuerpo = self.rfile.read(longitud).decode("utf-8") if longitud > 0 else "{}"
            return json.loads(cuerpo)

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
            if url.path == "/api/informe":
                try:
                    agente_id = validar_agente_id(parse_qs(url.query).get("id", [None])[0])
                    ruta = ruta_informe_agente(directorio_salidas, agente_id)
                    if not ruta.is_file():
                        self._enviar_json(404, {"ok": False, "mensaje": "Informe no encontrado.", "ruta_informe": str(ruta)})
                        return
                    contenido = ruta.read_text(encoding="utf-8", errors="replace")
                    self._enviar_json(200, {"ok": True, "contenido": contenido, "ruta_informe": str(ruta)})
                except ValueError as error:
                    self._enviar_json(400, {"ok": False, "error": str(error)})
                return
            if url.path == "/api/panel":
                ruta_panel = directorio_salidas / "panel_local.html"
                self._enviar_json(200, {"ok": True, "ruta_panel": str(ruta_panel), "existe": ruta_panel.is_file()})
                return
            if url.path == "/api/resumen":
                agentes = construir_resumen_agentes(directorio_trabajo, directorio_salidas)
                self._enviar_json(200, {"ok": True, "agentes": agentes})
                return
            self._enviar_json(404, {"error": "Ruta no encontrada."})

        def do_POST(self) -> None:
            url = urlparse(self.path)
            try:
                if url.path == "/api/agente":
                    agente_id = validar_agente_id(parse_qs(url.query).get("id", [None])[0])
                    payload = self._leer_json_post()
                    if "datos" not in payload:
                        raise ValueError("Falta la clave 'datos' en el cuerpo de la peticion.")
                    guardar_json_agente(directorio_trabajo, agente_id, json.dumps(payload["datos"], ensure_ascii=False))
                    datos = leer_json_agente(directorio_trabajo, agente_id)
                    self._enviar_json(200, {"mensaje": "Guardado correcto en espacio de trabajo.", "id": agente_id, "datos": datos})
                    return

                if url.path == "/api/ejecutar":
                    agente_id = validar_agente_id(parse_qs(url.query).get("id", [None])[0])
                    self._enviar_json(200, ejecutar_agente_local(agente_id, directorio_trabajo, directorio_salidas))
                    return

                if url.path == "/api/ejecutar-todos":
                    self._enviar_json(200, ejecutar_todos_local(directorio_trabajo, directorio_salidas))
                    return

                if url.path == "/api/generar-panel":
                    self._enviar_json(200, generar_panel_local(directorio_trabajo, directorio_salidas))
                    return

                self._enviar_json(404, {"error": "Ruta no encontrada."})
            except ValueError as error:
                self._enviar_json(400, {"error": str(error), "ok": False})
            except FileNotFoundError as error:
                self._enviar_json(404, {"error": str(error), "ok": False})
            except json.JSONDecodeError as error:
                self._enviar_json(400, {"error": f"JSON invalido: {error}", "ok": False})
            except Exception as error:
                self._enviar_json(500, {"error": f"Error inesperado: {error}", "ok": False})

        def log_message(self, format: str, *args) -> None:
            return

    return EditorHandler


def iniciar_servidor(directorio_trabajo: Path, directorio_salidas: Path, host: str, puerto: int, abrir: bool) -> int:
    handler = crear_handler(directorio_trabajo, directorio_salidas)
    servidor = HTTPServer((host, puerto), handler)

    url = f"http://{host}:{puerto}/"
    print(f"Directorio de trabajo usado: {directorio_trabajo}")
    print(f"Directorio de salidas usado: {directorio_salidas}")
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
        directorio_trabajo = resolver_directorio(args.directorio_trabajo)
        directorio_salidas = resolver_directorio(args.directorio_salidas)
        if not directorio_trabajo.exists():
            print("Error: no existe el directorio de trabajo.")
            print("Primero ejecuta: python scripts/preparar_espacio_trabajo.py")
            return 1
        directorio_salidas.mkdir(parents=True, exist_ok=True)
        return iniciar_servidor(directorio_trabajo, directorio_salidas, args.host, args.puerto, args.abrir)
    except OSError as error:
        print(f"Error al arrancar el servidor local: {error}")
        return 1
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
