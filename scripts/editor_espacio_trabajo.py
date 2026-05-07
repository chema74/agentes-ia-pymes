from __future__ import annotations

import argparse
import difflib
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

FORMULARIOS_GUIADOS = {
    1: [
        {"clave": "nombre_cliente", "etiqueta": "Nombre del cliente", "rutas_json": ["cliente.nombre_cliente"], "multilinea": False},
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["cliente.nombre_empresa"], "multilinea": False},
        {"clave": "correo_contacto", "etiqueta": "Correo de contacto", "rutas_json": ["cliente.correo_contacto"], "multilinea": False},
        {"clave": "telefono_contacto", "etiqueta": "Telefono de contacto", "rutas_json": ["cliente.telefono_contacto"], "multilinea": False},
        {"clave": "tipo_servicio_solicitado", "etiqueta": "Tipo de servicio solicitado", "rutas_json": ["cliente.tipo_servicio_solicitado"], "multilinea": False},
        {"clave": "necesidad_principal", "etiqueta": "Necesidad principal", "rutas_json": ["cliente.necesidad_principal"], "multilinea": True},
        {"clave": "prioridad_inicial", "etiqueta": "Prioridad inicial", "rutas_json": ["cliente.prioridad_inicial"], "multilinea": False},
        {"clave": "estado_onboarding", "etiqueta": "Estado del onboarding", "rutas_json": ["cliente.estado_onboarding"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["cliente.responsable_interno"], "multilinea": False},
        {"clave": "observaciones_internas", "etiqueta": "Observaciones internas", "rutas_json": ["cliente.observaciones_internas"], "multilinea": True},
    ],
    2: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa"], "multilinea": False},
        {"clave": "sector", "etiqueta": "Sector", "rutas_json": ["empresa_ficticia.sector", "empresa_ficticia.tipo_actividad"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["empresa_ficticia.responsable_interno"], "multilinea": False},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_revision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.motivo_decision"], "multilinea": True},
        {"clave": "estado", "etiqueta": "Estado", "rutas_json": ["metadatos_ejemplo.estado"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia"], "multilinea": True},
    ],
    3: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa"], "multilinea": False},
        {"clave": "sector", "etiqueta": "Sector", "rutas_json": ["empresa_ficticia.sector", "empresa_ficticia.tipo_actividad"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["empresa_ficticia.responsable_interno"], "multilinea": False},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_revision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.motivo_decision"], "multilinea": True},
        {"clave": "estado", "etiqueta": "Estado", "rutas_json": ["metadatos_ejemplo.estado"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia"], "multilinea": True},
    ],
    4: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa", "empresa_ficticia.nombre", "propuesta.nombre_empresa"], "multilinea": False},
        {"clave": "nombre_cliente", "etiqueta": "Nombre del cliente", "rutas_json": ["cliente_ficticio.nombre_cliente", "propuesta.nombre_cliente"], "multilinea": False},
        {"clave": "estado_propuesta", "etiqueta": "Estado de la propuesta", "rutas_json": ["propuesta.estado", "propuesta.estado_propuesta"], "multilinea": False},
        {"clave": "objetivo", "etiqueta": "Objetivo", "rutas_json": ["propuesta.objetivo", "propuesta.necesidad_principal"], "multilinea": True},
        {"clave": "alcance", "etiqueta": "Alcance", "rutas_json": ["propuesta.alcance", "propuesta.alcance_preliminar"], "multilinea": True},
        {"clave": "plazo_estimado", "etiqueta": "Plazo estimado", "rutas_json": ["propuesta.plazo_estimado"], "multilinea": False},
        {"clave": "importe_estimado", "etiqueta": "Importe estimado", "rutas_json": ["propuesta.importe_estimado", "propuesta.importe"], "multilinea": False},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_revision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.motivo_decision"], "multilinea": True},
        {"clave": "estado_ejemplo", "etiqueta": "Estado del ejemplo", "rutas_json": ["metadatos_ejemplo.estado", "metadatos_ejemplo.estado_documental"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia", "metadatos_ejemplo.nota"], "multilinea": True},
    ],
    5: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa", "empresa_ficticia.nombre"], "multilinea": False},
        {"clave": "sector", "etiqueta": "Sector", "rutas_json": ["empresa_ficticia.sector"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["empresa_ficticia.responsable_interno"], "multilinea": False},
        {"clave": "estado_general", "etiqueta": "Estado general de operaciones", "rutas_json": ["operaciones.estado_general", "resultado_validacion_manual.estado_general"], "multilinea": False},
        {"clave": "prioridad_general", "etiqueta": "Prioridad general", "rutas_json": ["operaciones.prioridad_general"], "multilinea": False},
        {"clave": "bloqueo_principal", "etiqueta": "Bloqueo principal", "rutas_json": ["operaciones.bloqueo_principal"], "multilinea": True},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.observaciones_finales"], "multilinea": True},
        {"clave": "estado_ejemplo", "etiqueta": "Estado del ejemplo", "rutas_json": ["metadatos_ejemplo.estado", "metadatos_ejemplo.estado_documental"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia", "metadatos_ejemplo.nota"], "multilinea": True},
    ],
    6: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa", "empresa_ficticia.nombre"], "multilinea": False},
        {"clave": "sector", "etiqueta": "Sector", "rutas_json": ["empresa_ficticia.sector"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["empresa_ficticia.responsable_interno"], "multilinea": False},
        {"clave": "estado_general", "etiqueta": "Estado general de control operativo", "rutas_json": ["control_cobros.estado_general", "resultado_validacion_manual.estado_general"], "multilinea": False},
        {"clave": "riesgo_operativo", "etiqueta": "Riesgo operativo", "rutas_json": ["control_cobros.riesgo_operativo"], "multilinea": False},
        {"clave": "prioridad_revision", "etiqueta": "Prioridad de revision", "rutas_json": ["control_cobros.prioridad_revision"], "multilinea": False},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.observaciones_finales"], "multilinea": True},
        {"clave": "estado_ejemplo", "etiqueta": "Estado del ejemplo", "rutas_json": ["metadatos_ejemplo.estado", "metadatos_ejemplo.estado_documental"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia", "metadatos_ejemplo.nota"], "multilinea": True},
    ],
    7: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa", "empresa_ficticia.nombre"], "multilinea": False},
        {"clave": "sector", "etiqueta": "Sector", "rutas_json": ["empresa_ficticia.sector"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["empresa_ficticia.responsable_interno"], "multilinea": False},
        {"clave": "estado_general", "etiqueta": "Estado general del pipeline", "rutas_json": ["pipeline.estado_general", "resultado_validacion_manual.estado_general"], "multilinea": False},
        {"clave": "prioridad_general", "etiqueta": "Prioridad general", "rutas_json": ["pipeline.prioridad_general"], "multilinea": False},
        {"clave": "oportunidad_destacada", "etiqueta": "Oportunidad destacada", "rutas_json": ["pipeline.oportunidad_destacada"], "multilinea": True},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.observaciones_finales"], "multilinea": True},
        {"clave": "estado_ejemplo", "etiqueta": "Estado del ejemplo", "rutas_json": ["metadatos_ejemplo.estado", "metadatos_ejemplo.estado_documental"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia", "metadatos_ejemplo.nota"], "multilinea": True},
    ],
    8: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa", "empresa_ficticia.nombre"], "multilinea": False},
        {"clave": "sector", "etiqueta": "Sector", "rutas_json": ["empresa_ficticia.sector"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["empresa_ficticia.responsable_interno"], "multilinea": False},
        {"clave": "estado_general", "etiqueta": "Estado general de formacion", "rutas_json": ["formacion.estado_general", "resultado_validacion_manual.estado_general"], "multilinea": False},
        {"clave": "prioridad_general", "etiqueta": "Prioridad general", "rutas_json": ["formacion.prioridad_general"], "multilinea": False},
        {"clave": "ruta_destacada", "etiqueta": "Ruta destacada", "rutas_json": ["formacion.ruta_destacada"], "multilinea": True},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.observaciones_finales"], "multilinea": True},
        {"clave": "estado_ejemplo", "etiqueta": "Estado del ejemplo", "rutas_json": ["metadatos_ejemplo.estado", "metadatos_ejemplo.estado_documental"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia", "metadatos_ejemplo.nota"], "multilinea": True},
    ],
    9: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa", "empresa_ficticia.nombre"], "multilinea": False},
        {"clave": "sector", "etiqueta": "Sector", "rutas_json": ["empresa_ficticia.sector"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["empresa_ficticia.responsable_interno"], "multilinea": False},
        {"clave": "estado_general", "etiqueta": "Estado general del analisis", "rutas_json": ["analisis_mercado.estado_general", "resultado_validacion_manual.estado_general"], "multilinea": False},
        {"clave": "prioridad_exploracion", "etiqueta": "Prioridad de exploracion", "rutas_json": ["analisis_mercado.prioridad_exploracion"], "multilinea": False},
        {"clave": "oportunidad_destacada", "etiqueta": "Oportunidad destacada", "rutas_json": ["analisis_mercado.oportunidad_destacada"], "multilinea": True},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.observaciones_finales"], "multilinea": True},
        {"clave": "estado_ejemplo", "etiqueta": "Estado del ejemplo", "rutas_json": ["metadatos_ejemplo.estado", "metadatos_ejemplo.estado_documental"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia", "metadatos_ejemplo.nota"], "multilinea": True},
    ],
    10: [
        {"clave": "nombre_empresa", "etiqueta": "Nombre de la empresa", "rutas_json": ["empresa_ficticia.nombre_empresa", "empresa_ficticia.nombre"], "multilinea": False},
        {"clave": "sector", "etiqueta": "Sector", "rutas_json": ["empresa_ficticia.sector"], "multilinea": False},
        {"clave": "responsable_interno", "etiqueta": "Responsable interno", "rutas_json": ["empresa_ficticia.responsable_interno"], "multilinea": False},
        {"clave": "estado_general", "etiqueta": "Estado general de revision", "rutas_json": ["revision_cumplimiento.estado_general", "resultado_validacion_manual.estado_general"], "multilinea": False},
        {"clave": "prioridad_revision", "etiqueta": "Prioridad de revision", "rutas_json": ["revision_cumplimiento.prioridad_revision"], "multilinea": False},
        {"clave": "riesgo_operativo", "etiqueta": "Riesgo operativo", "rutas_json": ["revision_cumplimiento.riesgo_operativo"], "multilinea": False},
        {"clave": "decision_recomendada", "etiqueta": "Decision recomendada", "rutas_json": ["resultado_validacion_manual.decision_recomendada", "resultado_validacion_manual.decision_humana"], "multilinea": False},
        {"clave": "observaciones", "etiqueta": "Observaciones", "rutas_json": ["resultado_validacion_manual.observaciones", "resultado_validacion_manual.observaciones_finales"], "multilinea": True},
        {"clave": "estado_ejemplo", "etiqueta": "Estado del ejemplo", "rutas_json": ["metadatos_ejemplo.estado", "metadatos_ejemplo.estado_documental"], "multilinea": False},
        {"clave": "advertencia", "etiqueta": "Advertencia", "rutas_json": ["metadatos_ejemplo.advertencia", "metadatos_ejemplo.nota"], "multilinea": True},
    ],
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


def ruta_historico_agente(directorio_salidas: Path, agente_id: int) -> Path:
    return directorio_salidas / f"agente-{agente_id:02d}" / "historico"


def inferir_fecha_historico(nombre_archivo: str) -> str:
    base = nombre_archivo.removesuffix("-informe.txt")
    if len(base) != 15 or "-" not in base:
        return ""
    fecha, hora = base.split("-", 1)
    if len(fecha) == 8 and len(hora) == 6 and fecha.isdigit() and hora.isdigit():
        return f"{fecha[0:4]}-{fecha[4:6]}-{fecha[6:8]} {hora[0:2]}:{hora[2:4]}:{hora[4:6]}"
    return ""


def listar_historico_agente(directorio_salidas: Path, agente_id: int) -> list[dict]:
    carpeta = ruta_historico_agente(directorio_salidas, agente_id)
    if not carpeta.is_dir():
        return []
    historico = []
    for archivo in sorted(carpeta.glob("*-informe.txt"), key=lambda p: p.name, reverse=True):
        try:
            tamano = archivo.stat().st_size
        except OSError:
            tamano = None
        historico.append(
            {
                "nombre_archivo": archivo.name,
                "ruta_informe": str(archivo),
                "fecha_detectada": inferir_fecha_historico(archivo.name),
                "tamaño_bytes": tamano,
            }
        )
    return historico


def resolver_archivo_historico(directorio_salidas: Path, agente_id: int, nombre_archivo: str) -> Path:
    if not nombre_archivo:
        raise ValueError("Debes indicar el nombre del archivo historico.")
    if Path(nombre_archivo).name != nombre_archivo:
        raise ValueError("Archivo no valido: ruta no permitida para historico.")
    if ".." in nombre_archivo or "/" in nombre_archivo or "\\" in nombre_archivo:
        raise ValueError("Ruta no permitida para archivo historico.")
    if not nombre_archivo.endswith("-informe.txt"):
        raise ValueError("El archivo historico debe terminar en -informe.txt.")

    carpeta = ruta_historico_agente(directorio_salidas, agente_id)
    ruta = (carpeta / nombre_archivo).resolve()
    base = carpeta.resolve()
    if not str(ruta).startswith(str(base) + os.sep):
        raise ValueError("Ruta fuera de historico no permitida.")
    return ruta


def extraer_decision_recomendada(texto: str) -> str:
    prefijos = [
        "decision humana recomendada",
        "decisión humana recomendada",
        "decision recomendada",
        "decisión recomendada",
    ]
    for linea in texto.splitlines():
        limpia = linea.strip()
        for prefijo in prefijos:
            if limpia.lower().startswith(prefijo):
                _, _, resto = limpia.partition(":")
                valor = resto.strip()
                if valor:
                    return valor
    return "No identificada"


def construir_comparacion_informes(directorio_salidas: Path, agente_id: int, archivo_historico: str) -> dict:
    ruta_historica = resolver_archivo_historico(directorio_salidas, agente_id, archivo_historico)
    ruta_actual = ruta_informe_agente(directorio_salidas, agente_id)
    if not ruta_actual.is_file():
        raise FileNotFoundError(f"No existe el ultimo informe del agente {agente_id:02d}: {ruta_actual}")
    if not ruta_historica.is_file():
        raise FileNotFoundError(f"No existe el informe historico solicitado: {ruta_historica}")

    texto_actual = ruta_actual.read_text(encoding="utf-8", errors="replace")
    texto_historico = ruta_historica.read_text(encoding="utf-8", errors="replace")

    lineas_actual = texto_actual.splitlines()
    lineas_historico = texto_historico.splitlines()
    diff = list(
        difflib.unified_diff(
            lineas_historico,
            lineas_actual,
            fromfile="historico",
            tofile="actual",
            lineterm="",
        )
    )
    diff_texto = "\n".join(diff) if diff else "Sin diferencias textuales."

    añadidas = 0
    eliminadas = 0
    for linea in difflib.ndiff(lineas_historico, lineas_actual):
        if linea.startswith("+ "):
            añadidas += 1
        elif linea.startswith("- "):
            eliminadas += 1
    sin_cambios = max(len(lineas_historico), len(lineas_actual)) - max(añadidas, eliminadas)
    if sin_cambios < 0:
        sin_cambios = 0

    decision_actual = extraer_decision_recomendada(texto_actual)
    decision_historica = extraer_decision_recomendada(texto_historico)
    decision_cambiada = decision_actual != decision_historica

    return {
        "ok": True,
        "agente": f"agente-{agente_id:02d}",
        "archivo_historico": ruta_historica.name,
        "decision_actual": decision_actual,
        "decision_historica": decision_historica,
        "decision_cambiada": decision_cambiada,
        "resumen": {
            "lineas_añadidas": añadidas,
            "lineas_eliminadas": eliminadas,
            "lineas_sin_cambios_aprox": sin_cambios,
        },
        "diff": diff_texto,
        "mensaje": "Comparacion local completada.",
    }


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


def obtener_valor_por_ruta(datos: dict, ruta_json: str) -> str:
    actual = datos
    for segmento in ruta_json.split("."):
        if not isinstance(actual, dict) or segmento not in actual:
            return ""
        actual = actual[segmento]
    if actual is None:
        return ""
    return str(actual)


def asignar_valor_por_ruta(datos: dict, ruta_json: str, valor: str) -> None:
    segmentos = ruta_json.split(".")
    actual = datos
    for segmento in segmentos[:-1]:
        siguiente = actual.get(segmento)
        if not isinstance(siguiente, dict):
            siguiente = {}
            actual[segmento] = siguiente
        actual = siguiente
    actual[segmentos[-1]] = valor


def agente_con_edicion_guiada(agente_id: int) -> bool:
    return agente_id in FORMULARIOS_GUIADOS


def obtener_id_formulario_desde_ruta(ruta_api: str) -> int | None:
    prefijo = "/api/formulario/agente-"
    if not ruta_api.startswith(prefijo):
        return None
    texto_id = ruta_api.replace(prefijo, "", 1)
    if len(texto_id) != 2 or not texto_id.isdigit():
        return None
    return int(texto_id)


def obtener_definicion_formulario_por_agente(agente_id: int) -> list[dict]:
    if not agente_con_edicion_guiada(agente_id):
        raise ValueError("EdiciÃ³n guiada todavÃ­a no disponible para este agente.")
    return FORMULARIOS_GUIADOS[agente_id]


def resolver_ruta_formulario_disponible(datos: dict, rutas_json: list[str]) -> str:
    for ruta_json in rutas_json:
        if obtener_valor_por_ruta(datos, ruta_json) != "":
            return ruta_json
    return rutas_json[0]


def construir_formulario_por_agente(directorio_trabajo: Path, agente_id: int) -> dict:
    definicion = obtener_definicion_formulario_por_agente(agente_id)
    datos = leer_json_agente(directorio_trabajo, agente_id)
    campos = []
    for campo in definicion:
        ruta_json = resolver_ruta_formulario_disponible(datos, campo["rutas_json"])
        campos.append(
            {
                "clave": campo["clave"],
                "etiqueta": campo["etiqueta"],
                "valor": obtener_valor_por_ruta(datos, ruta_json),
                "ruta_json": ruta_json,
                "multilinea": bool(campo.get("multilinea")),
            }
        )
    return {
        "ok": True,
        "agente": f"agente-{agente_id:02d}",
        "campos": campos,
        "mensaje": f"Formulario guiado del Agente {agente_id:02d} cargado correctamente.",
    }


def guardar_formulario_por_agente(directorio_trabajo: Path, agente_id: int, payload: dict) -> dict:
    definicion = obtener_definicion_formulario_por_agente(agente_id)
    datos = leer_json_agente(directorio_trabajo, agente_id)
    valores = payload.get("campos")
    if not isinstance(valores, dict):
        raise ValueError("La peticion del formulario debe incluir un objeto 'campos'.")

    rutas_permitidas = set()
    for campo in definicion:
        for ruta_json in campo["rutas_json"]:
            rutas_permitidas.add(ruta_json)

    for ruta_json, valor in valores.items():
        if ruta_json in rutas_permitidas:
            asignar_valor_por_ruta(datos, ruta_json, str(valor))

    ruta = ruta_datos_agente(directorio_trabajo, agente_id)
    contenido = json.dumps(datos, ensure_ascii=False, indent=2)
    ruta.write_text(contenido + "\n", encoding="utf-8")

    return {
        "ok": True,
        "mensaje": f"Edicion guiada del Agente {agente_id:02d} guardada correctamente.",
    }


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
        "--guardar-historico",
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
        "--guardar-historico",
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


def generar_informe_consolidado_local(directorio_salidas: Path) -> dict:
    comando = [
        sys.executable,
        str(obtener_raiz_repositorio() / "scripts" / "generar_informe_consolidado.py"),
        "--directorio-salidas",
        str(directorio_salidas),
        "--generar-html",
    ]
    codigo, salida = ejecutar_comando_local(comando)
    ruta_md = directorio_salidas / "informe_consolidado.md"
    ruta_html = directorio_salidas / "informe_consolidado.html"
    return {
        "ok": codigo == 0,
        "codigo_salida": codigo,
        "mensaje": "Informe consolidado local generado." if codigo == 0 else "Error al generar el informe consolidado local.",
        "salida_consola": salida,
        "ruta_markdown": str(ruta_md),
        "ruta_html": str(ruta_html),
        "existe_markdown": ruta_md.is_file(),
        "existe_html": ruta_html.is_file(),
    }


def exportar_evidencias_demo_local(directorio_salidas: Path) -> dict:
    comando = [
        sys.executable,
        str(obtener_raiz_repositorio() / "scripts" / "exportar_evidencias_demo.py"),
        "--directorio-salidas",
        str(directorio_salidas),
        "--crear-zip",
    ]
    codigo, salida = ejecutar_comando_local(comando)
    ruta_directorio = directorio_salidas / "evidencias_demo"
    ruta_indice_html = ruta_directorio / "INDICE_EVIDENCIAS.html"
    ruta_zip = directorio_salidas / "evidencias_demo.zip"
    return {
        "ok": codigo == 0,
        "codigo_salida": codigo,
        "mensaje": "Paquete local de evidencias exportado." if codigo == 0 else "Error al exportar paquete local de evidencias.",
        "salida_consola": salida,
        "ruta_directorio_evidencias": str(ruta_directorio),
        "ruta_indice_html": str(ruta_indice_html),
        "ruta_zip": str(ruta_zip),
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
                        "DecisiÃ³n humana recomendada",
                        "Decision recomendada",
                        "DecisiÃ³n recomendada",
                    ],
                )
                aviso = extraer_valor_por_prefijo(texto, ["Aviso", "Limite", "LÃ­mite", "Riesgo"])
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
:root{--fondo:#f3f5f8;--card:#ffffff;--texto:#1f2937;--borde:#d6dbe3;--ok:#065f46;--okf:#d1fae5;--av:#92400e;--avf:#fef3c7;--er:#991b1b;--erf:#fee2e2;--prim:#1d4ed8}
*{box-sizing:border-box}
body{font-family:Segoe UI,Tahoma,Arial,sans-serif;font-size:16px;margin:0;background:linear-gradient(180deg,#eef2f7,var(--fondo));color:var(--texto)}
main{max-width:1340px;margin:0 auto;padding:24px}
.card{background:var(--card);border:1px solid var(--borde);border-radius:12px;padding:16px;margin-bottom:14px}
.cabecera h1{margin:0 0 8px}
.nota{margin:6px 0;padding:10px;border-radius:8px;background:var(--avf);color:var(--av)}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
label,select,button{font-size:15px}
select,button{padding:9px 12px;border:1px solid #c7d0db;border-radius:8px;background:#fff}
button{cursor:pointer;background:#f9fafb}
button:hover{background:#f3f4f6}
.principal{background:var(--prim);color:#fff;border-color:#1e40af}
.principal:hover{background:#1e40af}
textarea{width:100%;min-height:520px;padding:12px;border:1px solid #c7d0db;border-radius:8px;font-family:Consolas,monospace;font-size:14px;line-height:1.5}
.estado{margin-top:10px;padding:10px;border-radius:8px;background:#eef2ff}
.estado.ok{background:var(--okf);color:var(--ok)}
.estado.warn{background:var(--avf);color:var(--av)}
.estado.err{background:var(--erf);color:var(--er)}
pre{background:#0b1020;color:#d1e7ff;padding:12px;border-radius:8px;white-space:pre-wrap;max-height:340px;overflow:auto}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media (max-width: 980px){.grid{grid-template-columns:1fr}}
.resumen-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}
.tarjeta-agente{border:1px solid #d7dde7;border-radius:10px;padding:12px;background:#fbfcfe}
.tarjeta-agente h4{margin:0 0 6px}
.tag{display:inline-block;padding:2px 6px;border-radius:999px;background:#e5e7eb;font-size:12px}
.ruta-panel{font-size:14px;color:#334155}
.guiada{display:none}
.guiada.activa{display:block}
.form-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px}
.campo{display:flex;flex-direction:column;gap:6px}
.campo input,.campo textarea{padding:9px 10px;border:1px solid #c7d0db;border-radius:8px;font:inherit}
.campo textarea{min-height:90px;resize:vertical}
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
      <button id=\"cargar\" class=\"principal\">Cargar JSON</button>
      <button id=\"formatear\">Formatear JSON</button>
      <button id=\"guardar\" class=\"principal\">Validar y guardar</button>
    </div>
    <div class=\"estado\" id=\"mensaje\"></div>
  </div>

  <div class=\"card guiada\" id=\"bloqueGuiado\">
    <h2>EdiciÃ³n guiada</h2>
    <p>Disponible para Agente 01, Agente 02, Agente 03, Agente 04, Agente 05, Agente 06, Agente 07, Agente 08, Agente 09 y Agente 10. La edicion JSON cruda sigue disponible.</p>
    <!-- Compatibilidad de texto: EdiciÃ³n guiada -->
    <div class=\"row\">
      <button id=\"cargarGuiado\">Cargar ediciÃ³n guiada</button>
      <button id=\"guardarGuiado\" class=\"principal\">Guardar ediciÃ³n guiada</button>
    </div>
    <div id=\"formularioGuiado\" class=\"form-grid\"></div>
  </div>

  <div class=\"grid\">
    <div class=\"card\">
      <h2>EdiciÃ³n JSON</h2>
      <textarea id=\"contenido\" spellcheck=\"false\"></textarea>
      <!-- Compatibilidad de texto: EdiciÃ³n JSON -->
    </div>
    <div class=\"card\">
      <h2>Acciones operativas</h2>
      <div class=\"row\">
        <button id=\"ejecutar\" class=\"principal\">Ejecutar agente seleccionado</button>
        <button id=\"ejecutarTodos\">Ejecutar todos los agentes</button>
        <button id=\"generarPanel\">Regenerar panel local</button>
        <button id=\"cargarInforme\">Cargar ultimo informe</button>
        <button id=\"rutaPanel\">Ver ruta panel local</button>
        <button id=\"abrirPanel\">Abrir panel local</button>
      </div>
      <p class=\"ruta-panel\">Ruta por defecto: salidas/panel_local.html</p>
      <h3>Resultados</h3>
      <p id=\"rutaInfo\"></p>
      <pre id=\"salida\"></pre>
    </div>
  </div>

  <div class=\"card\">
    <h2>Último informe cargado</h2>
    <small>Usa el boton \"Cargar ultimo informe\" para refrescar esta seccion.</small>
    <p id=\"agenteInforme\"></p>
    <pre id=\"informe\"></pre>
  </div>
  <div class=\"card\">
    <h2>Historico local de ejecuciones</h2>
    <small>Informes anteriores guardados por agente en la carpeta historico.</small>
    <div class=\"row\">
      <button id=\"actualizarHistorico\">Actualizar historico</button>
      <select id=\"archivoHistorico\"></select>
      <button id=\"cargarHistorico\">Cargar informe historico</button>
      <button id=\"compararHistorico\">Comparar con ultimo informe</button>
    </div>
    <p id=\"historicoInfo\"></p>
    <pre id=\"informeHistorico\"></pre>
    <h3>ComparaciÃ³n local</h3>
    <p id=\"comparacionDecision\"></p>
    <pre id=\"comparacionDiff\"></pre>
  </div>

  <div class=\"card\">
    <h2>Informe consolidado local</h2>
    <small>Genera y consulta una consolidacion de informes de agente-01 a agente-10.</small>
    <div class=\"row\">
      <button id=\"generarConsolidado\">Generar informe consolidado</button>
      <button id=\"cargarConsolidado\">Cargar informe consolidado</button>
    </div>
    <p id=\"rutaConsolidado\"></p>
    <pre id=\"informeConsolidado\"></pre>
  </div>

  <div class=\"card\">
    <h2>Paquete local de evidencias</h2>
    <small>Exporta un paquete local de demo con indice e informes disponibles.</small>
    <div class=\"row\">
      <button id=\"exportarEvidencias\">Exportar evidencias de demo</button>
      <button id=\"cargarEvidencias\">Cargar indice de evidencias</button>
    </div>
    <p id=\"rutaEvidencias\"></p>
    <pre id=\"evidenciasMarkdown\"></pre>
  </div>
</main>
<script>
const sel=document.getElementById('agente');
const txt=document.getElementById('contenido');
const msg=document.getElementById('mensaje');
const salida=document.getElementById('salida');
const informe=document.getElementById('informe');
const rutaInfo=document.getElementById('rutaInfo');
const agenteInforme=document.getElementById('agenteInforme');
const resumen=document.getElementById('resumen');
const bloqueGuiado=document.getElementById('bloqueGuiado');
const formularioGuiado=document.getElementById('formularioGuiado');
const archivoHistorico=document.getElementById('archivoHistorico');
const historicoInfo=document.getElementById('historicoInfo');
const informeHistorico=document.getElementById('informeHistorico');
const comparacionDecision=document.getElementById('comparacionDecision');
const comparacionDiff=document.getElementById('comparacionDiff');
const rutaConsolidado=document.getElementById('rutaConsolidado');
const informeConsolidado=document.getElementById('informeConsolidado');
const rutaEvidencias=document.getElementById('rutaEvidencias');
const evidenciasMarkdown=document.getElementById('evidenciasMarkdown');

function setMsg(t,tipo='warn'){msg.textContent=t;msg.className='estado '+tipo;}
function setSalida(t){salida.textContent=t||'';}
function setInforme(t){informe.textContent=t||'';}
function setAgenteInforme(t){agenteInforme.textContent=t||'';}
function setHistoricoInfo(t){historicoInfo.textContent=t||'';}
function setInformeHistorico(t){informeHistorico.textContent=t||'';}
function setComparacionDecision(t){comparacionDecision.textContent=t||'';}
function setComparacionDiff(t){comparacionDiff.textContent=t||'';}
function setRutaConsolidado(t){rutaConsolidado.textContent=t||'';}
function setInformeConsolidado(t){informeConsolidado.textContent=t||'';}
function setRutaEvidencias(t){rutaEvidencias.textContent=t||'';}
function setEvidenciasMarkdown(t){evidenciasMarkdown.textContent=t||'';}
function escaparHtml(texto){
  return String(texto ?? '')
    .replaceAll('&','&amp;')
    .replaceAll('<','&lt;')
    .replaceAll('>','&gt;')
    .replaceAll('"','&quot;');
}

function actualizarVisibilidadGuiada(){
  const activo = ['1','2','3','4','5','6','7','8','9','10'].includes(String(sel.value));
  bloqueGuiado.className = activo ? 'card guiada activa' : 'card guiada';
  if(!activo){
    formularioGuiado.innerHTML = '<p>EdiciÃ³n guiada todavÃ­a no disponible para este agente.</p>';
  }
}

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
  actualizarVisibilidadGuiada();
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
  await actualizarHistorico();
}

async function ejecutarTodos(){
  setMsg('Ejecutando todos los agentes...','warn');
  const r=await pedir('/api/ejecutar-todos',{method:'POST'});
  setMsg(r.data.mensaje||'Operacion finalizada',r.data.ok?'ok':'err');
  setSalida(r.data.salida_consola||'');
  await actualizarHistorico();
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
  setAgenteInforme(`Informe cargado para agente ${id}.`);
  rutaInfo.textContent=r.data.ruta_informe?`Informe: ${r.data.ruta_informe}`:'';
}

function renderHistorico(historico, id){
  archivoHistorico.innerHTML='';
  if(!historico || historico.length===0){
    const o=document.createElement('option');
    o.value='';o.textContent='Sin informes historicos';
    archivoHistorico.appendChild(o);
    setHistoricoInfo(`Agente ${id}: no hay historico.`);
    return;
  }
  historico.forEach((item, idx)=>{
    const o=document.createElement('option');
    o.value=item.nombre_archivo;
    const fecha=item.fecha_detectada?` | ${item.fecha_detectada}`:'';
    const tam=(item['tamaño_bytes'] ?? item['tamano_bytes']);
    const size=(tam!==undefined && tam!==null)?` | ${tam} bytes`:'';
    o.textContent=`${idx+1}. ${item.nombre_archivo}${fecha}${size}`;
    archivoHistorico.appendChild(o);
  });
  setHistoricoInfo(`Agente ${id}: ${historico.length} informe(s) historico(s).`);
}

async function actualizarHistorico(){
  const id=sel.value;
  const r=await pedir(`/api/historico?id=${id}`);
  if(!r.ok||!r.data.ok){setMsg(r.data.error||r.data.mensaje||'No se pudo cargar historico','err');return;}
  renderHistorico(r.data.historico||[], id);
}

async function cargarInformeHistorico(){
  const id=sel.value;
  const archivo=archivoHistorico.value;
  if(!archivo){setMsg('No hay archivo historico seleccionado.','warn');return;}
  const r=await pedir(`/api/historico/informe?id=${id}&archivo=${encodeURIComponent(archivo)}`);
  if(!r.ok||!r.data.ok){setMsg(r.data.error||r.data.mensaje||'No se pudo cargar informe historico','err');return;}
  setInformeHistorico(r.data.contenido||'');
  setMsg('Informe historico cargado.','ok');
}

async function compararInformeHistorico(){
  const id=sel.value;
  const archivo=archivoHistorico.value;
  if(!archivo){setMsg('No hay archivo historico seleccionado.','warn');return;}
  const r=await pedir(`/api/comparar?id=${id}&archivo=${encodeURIComponent(archivo)}`);
  if(!r.ok||!r.data.ok){setMsg(r.data.error||r.data.mensaje||'No se pudo comparar informe historico','err');return;}
  const cambio=r.data.decision_cambiada?'si':'no';
  setComparacionDecision(
    `Decision actual: ${r.data.decision_actual} | Decision historica: ${r.data.decision_historica} | Cambio: ${cambio}`
  );
  setComparacionDiff(r.data.diff||'');
  setMsg('Comparacion local completada.','ok');
}

async function verRutaPanel(){
  const r=await pedir('/api/panel');
  if(!r.ok||!r.data.ok){setMsg(r.data.error||'No se pudo obtener la ruta del panel','err');return;}
  const estado=r.data.existe?'(existe)':'(aun no generado)';
  rutaInfo.textContent=`Panel: ${r.data.ruta_panel} ${estado}`;
  setMsg('Ruta de panel local consultada.','ok');
}

async function abrirPanelLocal(){
  const r=await pedir('/api/panel');
  if(!r.ok||!r.data.ok){setMsg(r.data.error||'No se pudo consultar el panel','err');return;}
  const estado=r.data.existe?'existe':'no existe';
  rutaInfo.textContent=`Panel local (${estado}): ${r.data.ruta_panel}`;
  setMsg('El panel local puede abrirse manualmente desde la ruta indicada.','warn');
}

async function generarInformeConsolidado(){
  setMsg('Generando informe consolidado local...','warn');
  const r=await pedir('/api/generar-informe-consolidado',{method:'POST'});
  setMsg(r.data.mensaje||'Operacion finalizada',r.data.ok?'ok':'err');
  setSalida(r.data.salida_consola||'');
  if(r.data.ruta_markdown || r.data.ruta_html){
    const md = r.data.ruta_markdown ? `Markdown: ${r.data.ruta_markdown}` : '';
    const html = r.data.ruta_html ? ` | HTML: ${r.data.ruta_html}` : '';
    setRutaConsolidado(md + html);
  }
}

async function cargarInformeConsolidado(){
  const r=await pedir('/api/informe-consolidado');
  if(!r.ok||!r.data.ok){setMsg(r.data.error||r.data.mensaje||'No se pudo cargar el informe consolidado','err');return;}
  setMsg('Informe consolidado cargado.','ok');
  setInformeConsolidado(r.data.contenido||'');
  const md = r.data.ruta_markdown ? `Markdown: ${r.data.ruta_markdown}` : '';
  const html = r.data.ruta_html ? ` | HTML: ${r.data.ruta_html}` : '';
  setRutaConsolidado(md + html);
}

async function exportarEvidenciasDemo(){
  setMsg('Exportando paquete local de evidencias...','warn');
  const r=await pedir('/api/exportar-evidencias-demo',{method:'POST'});
  setMsg(r.data.mensaje||'Operacion finalizada',r.data.ok?'ok':'err');
  setSalida(r.data.salida_consola||'');
  const dir = r.data.ruta_directorio_evidencias ? `Directorio: ${r.data.ruta_directorio_evidencias}` : '';
  const html = r.data.ruta_indice_html ? ` | Indice HTML: ${r.data.ruta_indice_html}` : '';
  const zip = r.data.ruta_zip ? ` | ZIP: ${r.data.ruta_zip}` : '';
  setRutaEvidencias(dir + html + zip);
}

async function cargarEvidenciasDemo(){
  const r=await pedir('/api/evidencias-demo');
  if(!r.ok||!r.data.ok){setMsg(r.data.error||r.data.mensaje||'No se pudo cargar indice de evidencias','err');return;}
  setMsg('Indice de evidencias cargado.','ok');
  setEvidenciasMarkdown(r.data.contenido_markdown||'');
  const md = r.data.ruta_markdown ? `Markdown: ${r.data.ruta_markdown}` : '';
  const html = r.data.ruta_html ? ` | HTML: ${r.data.ruta_html}` : '';
  const zip = r.data.ruta_zip ? ` | ZIP: ${r.data.ruta_zip}` : '';
  setRutaEvidencias(md + html + zip);
}

function renderFormularioGuiado(campos){
  formularioGuiado.innerHTML = campos.map((campo) => {
    const multilinea = Boolean(campo.multilinea);
    if (multilinea) {
      return `<label class="campo"><span>${escaparHtml(campo.etiqueta)}</span><textarea data-ruta="${escaparHtml(campo.ruta_json)}">${escaparHtml(campo.valor || '')}</textarea></label>`;
    }
    return `<label class="campo"><span>${escaparHtml(campo.etiqueta)}</span><input data-ruta="${escaparHtml(campo.ruta_json)}" value="${escaparHtml(campo.valor || '')}"></label>`;
  }).join('');
}

async function cargarGuiado(){
  const idTexto = String(sel.value);
  if(!['1','2','3','4','5','6','7','8','9','10'].includes(idTexto)){setMsg('EdiciÃ³n guiada todavÃ­a no disponible para este agente.','warn');return;}
  const r=await pedir(`/api/formulario/agente-${idTexto.padStart(2,'0')}`);
  if(!r.ok||!r.data.ok){setMsg(r.data.error||'No se pudo cargar la ediciÃ³n guiada','err');return;}
  renderFormularioGuiado(r.data.campos || []);
  setMsg(r.data.mensaje || 'EdiciÃ³n guiada cargada.','ok');
}

async function guardarGuiado(){
  const idTexto = String(sel.value);
  if(!['1','2','3','4','5','6','7','8','9','10'].includes(idTexto)){setMsg('EdiciÃ³n guiada todavÃ­a no disponible para este agente.','warn');return;}
  const campos = {};
  formularioGuiado.querySelectorAll('[data-ruta]').forEach((nodo) => {
    campos[nodo.getAttribute('data-ruta')] = nodo.value;
  });
  const r=await pedir(`/api/formulario/agente-${idTexto.padStart(2,'0')}`,{method:'POST',headers:{'Content-Type':'application/json; charset=utf-8'},body:JSON.stringify({campos})});
  if(!r.ok||!r.data.ok){setMsg(r.data.error||'No se pudo guardar la ediciÃ³n guiada','err');return;}
  setMsg(r.data.mensaje || 'EdiciÃ³n guiada guardada.','ok');
  await cargar();
}

async function desdeTarjeta(evento){
  const boton = evento.target.closest('button[data-accion]');
  if(!boton){return;}
  const id = boton.getAttribute('data-id');
  const accion = boton.getAttribute('data-accion');
  if(!id || !accion){return;}
  sel.value = id;
  actualizarVisibilidadGuiada();
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
document.getElementById('abrirPanel').addEventListener('click',abrirPanelLocal);
document.getElementById('actualizarResumen').addEventListener('click',actualizarResumen);
document.getElementById('cargarGuiado').addEventListener('click',cargarGuiado);
document.getElementById('guardarGuiado').addEventListener('click',guardarGuiado);
document.getElementById('actualizarHistorico').addEventListener('click',actualizarHistorico);
document.getElementById('cargarHistorico').addEventListener('click',cargarInformeHistorico);
document.getElementById('compararHistorico').addEventListener('click',compararInformeHistorico);
document.getElementById('generarConsolidado').addEventListener('click',generarInformeConsolidado);
document.getElementById('cargarConsolidado').addEventListener('click',cargarInformeConsolidado);
document.getElementById('exportarEvidencias').addEventListener('click',exportarEvidenciasDemo);
document.getElementById('cargarEvidencias').addEventListener('click',cargarEvidenciasDemo);
sel.addEventListener('change',actualizarVisibilidadGuiada);
sel.addEventListener('change',actualizarHistorico);
resumen.addEventListener('click',desdeTarjeta);

cargarAgentes()
  .then(cargar)
  .then(actualizarResumen)
  .then(actualizarHistorico)
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
            if url.path == "/api/historico":
                try:
                    agente_id = validar_agente_id(parse_qs(url.query).get("id", [None])[0])
                    historico = listar_historico_agente(directorio_salidas, agente_id)
                    self._enviar_json(
                        200,
                        {
                            "ok": True,
                            "agente": f"agente-{agente_id:02d}",
                            "historico": historico,
                            "mensaje": "Historico consultado correctamente.",
                        },
                    )
                except ValueError as error:
                    self._enviar_json(400, {"ok": False, "error": str(error)})
                return
            if url.path == "/api/historico/informe":
                try:
                    query = parse_qs(url.query)
                    agente_id = validar_agente_id(query.get("id", [None])[0])
                    archivo = query.get("archivo", [""])[0]
                    ruta = resolver_archivo_historico(directorio_salidas, agente_id, archivo)
                    if not ruta.is_file():
                        self._enviar_json(404, {"ok": False, "mensaje": "Informe historico no encontrado.", "ruta_informe": str(ruta)})
                        return
                    contenido = ruta.read_text(encoding="utf-8", errors="replace")
                    self._enviar_json(200, {"ok": True, "agente": f"agente-{agente_id:02d}", "archivo": ruta.name, "contenido": contenido, "ruta_informe": str(ruta)})
                except ValueError as error:
                    self._enviar_json(400, {"ok": False, "error": str(error)})
                return
            if url.path == "/api/comparar":
                try:
                    query = parse_qs(url.query)
                    agente_id = validar_agente_id(query.get("id", [None])[0])
                    archivo = query.get("archivo", [""])[0]
                    resultado = construir_comparacion_informes(directorio_salidas, agente_id, archivo)
                    self._enviar_json(200, resultado)
                except ValueError as error:
                    self._enviar_json(400, {"ok": False, "error": str(error)})
                except FileNotFoundError as error:
                    self._enviar_json(404, {"ok": False, "error": str(error)})
                return
            if url.path == "/api/panel":
                ruta_panel = directorio_salidas / "panel_local.html"
                self._enviar_json(200, {"ok": True, "ruta_panel": str(ruta_panel), "existe": ruta_panel.is_file()})
                return
            if url.path == "/api/informe-consolidado":
                ruta_md = directorio_salidas / "informe_consolidado.md"
                ruta_html = directorio_salidas / "informe_consolidado.html"
                if not ruta_md.is_file():
                    self._enviar_json(
                        404,
                        {
                            "ok": False,
                            "mensaje": "Informe consolidado no encontrado.",
                            "ruta_markdown": str(ruta_md),
                            "ruta_html": str(ruta_html),
                        },
                    )
                    return
                contenido = ruta_md.read_text(encoding="utf-8", errors="replace")
                self._enviar_json(
                    200,
                    {
                        "ok": True,
                        "contenido": contenido,
                        "ruta_markdown": str(ruta_md),
                        "ruta_html": str(ruta_html),
                        "existe_html": ruta_html.is_file(),
                    },
                )
                return
            if url.path == "/api/evidencias-demo":
                ruta_md = directorio_salidas / "evidencias_demo" / "INDICE_EVIDENCIAS.md"
                ruta_html = directorio_salidas / "evidencias_demo" / "INDICE_EVIDENCIAS.html"
                ruta_zip = directorio_salidas / "evidencias_demo.zip"
                contenido = ""
                if ruta_md.is_file():
                    contenido = ruta_md.read_text(encoding="utf-8", errors="replace")
                self._enviar_json(
                    200,
                    {
                        "ok": True,
                        "contenido_markdown": contenido,
                        "ruta_markdown": str(ruta_md),
                        "ruta_html": str(ruta_html),
                        "ruta_zip": str(ruta_zip),
                        "existe_markdown": ruta_md.is_file(),
                        "existe_html": ruta_html.is_file(),
                        "existe_zip": ruta_zip.is_file(),
                        "mensaje": "Indice de evidencias disponible." if ruta_md.is_file() else "Indice de evidencias no encontrado.",
                    },
                )
                return
            if url.path == "/api/resumen":
                agentes = construir_resumen_agentes(directorio_trabajo, directorio_salidas)
                self._enviar_json(200, {"ok": True, "agentes": agentes})
                return
            if url.path.startswith("/api/formulario/"):
                agente_id = obtener_id_formulario_desde_ruta(url.path)
                if agente_id is None:
                    self._enviar_json(404, {"ok": False, "error": "Formulario no disponible para este agente."})
                    return
                if not agente_con_edicion_guiada(agente_id):
                    self._enviar_json(404, {"ok": False, "agente": f"agente-{agente_id:02d}", "error": "EdiciÃ³n guiada todavÃ­a no disponible para este agente."})
                    return
                try:
                    self._enviar_json(200, construir_formulario_por_agente(directorio_trabajo, agente_id))
                except FileNotFoundError as error:
                    self._enviar_json(404, {"ok": False, "agente": f"agente-{agente_id:02d}", "error": str(error)})
                except Exception as error:
                    self._enviar_json(500, {"ok": False, "agente": f"agente-{agente_id:02d}", "error": f"Error al cargar el formulario: {error}"})
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
                if url.path == "/api/generar-informe-consolidado":
                    self._enviar_json(200, generar_informe_consolidado_local(directorio_salidas))
                    return
                if url.path == "/api/exportar-evidencias-demo":
                    self._enviar_json(200, exportar_evidencias_demo_local(directorio_salidas))
                    return

                if url.path.startswith("/api/formulario/"):
                    agente_id = obtener_id_formulario_desde_ruta(url.path)
                    if agente_id is None:
                        self._enviar_json(404, {"ok": False, "error": "Formulario no disponible para este agente."})
                        return
                    if not agente_con_edicion_guiada(agente_id):
                        self._enviar_json(404, {"ok": False, "agente": f"agente-{agente_id:02d}", "error": "EdiciÃ³n guiada todavÃ­a no disponible para este agente."})
                        return
                    payload = self._leer_json_post()
                    self._enviar_json(200, guardar_formulario_por_agente(directorio_trabajo, agente_id, payload))
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




