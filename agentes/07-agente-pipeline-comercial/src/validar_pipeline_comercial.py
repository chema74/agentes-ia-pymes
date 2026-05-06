from pathlib import Path
import argparse
import json
import sys
from datetime import date


SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "empresa_ficticia",
    "oportunidades_comerciales",
    "acciones_comerciales_siguientes",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "07-agente-pipeline-comercial"
    / "datos_ejemplo"
    / "pipeline_comercial_ficticio.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(
        description="Valida un pipeline comercial ficticio del Agente 07."
    )
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al JSON de pipeline comercial.",
    )
    return parser


def cargar_json(ruta_json):
    try:
        with ruta_json.open("r", encoding="utf-8") as archivo:
            return json.load(archivo), None
    except FileNotFoundError:
        return None, f"Error: archivo no encontrado: {ruta_json}"
    except json.JSONDecodeError as error:
        return None, f"Error: JSON invalido en {ruta_json}: {error.msg}"
    except OSError as error:
        return None, f"Error: no se pudo leer el archivo {ruta_json}: {error}"


def validar_estructura(datos):
    if not isinstance(datos, dict):
        return "Error: estructura incompleta. El JSON principal debe ser un objeto."

    faltantes = [s for s in SECCIONES_OBLIGATORIAS if s not in datos]
    if faltantes:
        return (
            "Error: estructura incompleta. Faltan secciones principales: "
            + ", ".join(faltantes)
        )

    if not isinstance(datos.get("oportunidades_comerciales"), list):
        return (
            "Error: estructura incompleta. La seccion 'oportunidades_comerciales' debe ser una lista."
        )

    for seccion in [
        "bloqueos_comerciales",
        "acciones_comerciales_siguientes",
        "clasificaciones_comerciales",
        "interacciones_comerciales",
    ]:
        if seccion in datos and not isinstance(datos.get(seccion), list):
            return f"Error: estructura incompleta. La seccion '{seccion}' debe ser una lista."

    if "resultado_validacion_manual" not in datos:
        return (
            "Error: estructura incompleta. Falta 'resultado_validacion_manual' en el JSON."
        )

    return None


def texto(registro, campo):
    if not isinstance(registro, dict):
        return ""
    valor = registro.get(campo, "")
    if valor is None:
        return ""
    return str(valor).strip().lower()


def identificador(registro, campo):
    if not isinstance(registro, dict):
        return "sin_identificador"
    return str(registro.get(campo, "sin_identificador"))


def deduplicar_por_id(registros, campo_id):
    vistos = set()
    salida = []
    for registro in registros:
        clave = identificador(registro, campo_id)
        if clave in vistos:
            continue
        vistos.add(clave)
        salida.append(registro)
    return salida


def parsear_fecha(valor):
    valor_texto = str(valor or "").strip().lower()
    if not valor_texto or valor_texto in ["sin fecha", "sin definir", "no aplica", "n/a"]:
        return None
    try:
        return date.fromisoformat(valor_texto)
    except ValueError:
        return None


def analizar(datos):
    oportunidades = datos.get("oportunidades_comerciales", [])
    acciones = datos.get("acciones_comerciales_siguientes", [])
    bloqueos = datos.get("bloqueos_comerciales", [])
    clasificaciones = datos.get("clasificaciones_comerciales", [])
    hoy = date.today()

    abiertas = [
        o
        for o in oportunidades
        if texto(o, "estado_oportunidad") in ["abierta", "pendiente", "en_revision"]
    ]
    ganadas = [o for o in oportunidades if texto(o, "estado_oportunidad") == "ganada"]
    perdidas = [o for o in oportunidades if texto(o, "estado_oportunidad") == "perdida"]
    descartadas = [o for o in oportunidades if texto(o, "estado_oportunidad") == "descartada"]
    bloqueadas = [
        o
        for o in oportunidades
        if texto(o, "estado_oportunidad") == "bloqueada"
        or str(o.get("bloqueo_asociado") or "").strip()
    ]
    prioridades_altas = [
        o for o in oportunidades if texto(o, "prioridad_seguimiento") == "alta"
    ]
    temperatura_alta = [
        o
        for o in oportunidades
        if texto(o, "temperatura_comercial") in ["alta", "caliente", "critica", "crítica"]
    ]
    sin_responsable = [
        o for o in oportunidades if not texto(o, "responsable_interno")
    ]
    sin_proxima_accion = [
        o
        for o in oportunidades
        if not texto(o, "proxima_accion")
        or texto(o, "proxima_accion") in ["sin definir", "pendiente", "n/a", "no aplica"]
    ]
    seguimiento_vencido = []
    for o in oportunidades:
        fecha = parsear_fecha(o.get("fecha_ultima_interaccion"))
        if fecha and fecha < hoy and texto(o, "estado_oportunidad") in [
            "abierta",
            "en_revision",
            "bloqueada",
            "pendiente",
        ]:
            seguimiento_vencido.append(o)

    riesgos_criticos = [
        b
        for b in bloqueos
        if texto(b, "prioridad_bloqueo") in ["alta", "critica", "crítica"]
        and texto(b, "estado_bloqueo") in ["activo", "en_revision", "abierto"]
    ]
    acciones_abiertas = [
        a for a in acciones if texto(a, "estado_accion") in ["pendiente", "en_revision"]
    ]
    acciones_urgentes = [
        a
        for a in acciones_abiertas
        if texto(a, "prioridad_accion") in ["alta", "urgente", "critica", "crítica"]
    ]

    importes_invalidos = []
    for o in oportunidades:
        if "importe_estimado" in o:
            valor = o.get("importe_estimado")
            if not isinstance(valor, (int, float)) or valor < 0:
                importes_invalidos.append(o)

    datos_criticos_ausentes = []
    for o in oportunidades:
        if (
            not texto(o, "nombre_cliente")
            or not texto(o, "fase_comercial")
            or not texto(o, "responsable_interno")
            or not texto(o, "proxima_accion")
        ):
            datos_criticos_ausentes.append(o)
        if "importe_estimado" in o:
            valor = o.get("importe_estimado")
            if not isinstance(valor, (int, float)) or valor < 0:
                datos_criticos_ausentes.append(o)

    temperatura_clasificada = [
        c
        for c in clasificaciones
        if texto(c, "temperatura_comercial") in ["alta", "caliente", "critica", "crítica"]
    ]

    return {
        "total_oportunidades": len(oportunidades),
        "abiertas": deduplicar_por_id(abiertas, "identificador_oportunidad"),
        "ganadas": deduplicar_por_id(ganadas, "identificador_oportunidad"),
        "perdidas": deduplicar_por_id(perdidas, "identificador_oportunidad"),
        "descartadas": deduplicar_por_id(descartadas, "identificador_oportunidad"),
        "bloqueadas": deduplicar_por_id(bloqueadas, "identificador_oportunidad"),
        "prioridades_altas": deduplicar_por_id(
            prioridades_altas, "identificador_oportunidad"
        ),
        "temperatura_alta": deduplicar_por_id(
            temperatura_alta, "identificador_oportunidad"
        ),
        "sin_responsable": deduplicar_por_id(sin_responsable, "identificador_oportunidad"),
        "sin_proxima_accion": deduplicar_por_id(
            sin_proxima_accion, "identificador_oportunidad"
        ),
        "seguimiento_vencido": deduplicar_por_id(
            seguimiento_vencido, "identificador_oportunidad"
        ),
        "riesgos_criticos": deduplicar_por_id(riesgos_criticos, "identificador_bloqueo"),
        "acciones_abiertas": deduplicar_por_id(acciones_abiertas, "identificador_accion"),
        "acciones_urgentes": deduplicar_por_id(acciones_urgentes, "identificador_accion"),
        "importes_invalidos": deduplicar_por_id(
            importes_invalidos, "identificador_oportunidad"
        ),
        "datos_criticos_ausentes": deduplicar_por_id(
            datos_criticos_ausentes, "identificador_oportunidad"
        ),
        "temperatura_clasificada": deduplicar_por_id(
            temperatura_clasificada, "identificador_clasificacion"
        ),
    }


def recomendar_decision(analisis):
    if analisis["bloqueadas"] or analisis["riesgos_criticos"] or analisis["datos_criticos_ausentes"]:
        return "bloquear"

    if (
        analisis["prioridades_altas"]
        or analisis["temperatura_alta"]
        or analisis["seguimiento_vencido"]
        or analisis["acciones_urgentes"]
    ):
        return "priorizar_oportunidad"

    if analisis["sin_responsable"] or analisis["sin_proxima_accion"] or analisis["importes_invalidos"]:
        return "pedir_informacion"

    if (
        not analisis["abiertas"]
        and not analisis["bloqueadas"]
        and not analisis["acciones_abiertas"]
    ):
        return "avanzar"

    return "revisar_de_nuevo"


def nombre_empresa(datos):
    empresa = datos.get("empresa_ficticia", {})
    if isinstance(empresa, dict):
        return empresa.get("nombre", "no disponible")
    return "no disponible"


def imprimir_lista(titulo, registros, campo_id):
    print(f"{titulo}: {len(registros)}")
    for registro in registros:
        print(f"  - {identificador(registro, campo_id)}")


def imprimir_informe(ruta_json, datos, analisis, decision):
    print("Informe de validacion del pipeline comercial del Agente 07")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Empresa ficticia: {nombre_empresa(datos)}")
    print(f"Numero total de oportunidades comerciales: {analisis['total_oportunidades']}")
    print("")
    print("Resumen de fases o estados del pipeline:")
    imprimir_lista("Oportunidades abiertas", analisis["abiertas"], "identificador_oportunidad")
    imprimir_lista("Oportunidades ganadas", analisis["ganadas"], "identificador_oportunidad")
    imprimir_lista("Oportunidades perdidas", analisis["perdidas"], "identificador_oportunidad")
    imprimir_lista(
        "Oportunidades descartadas", analisis["descartadas"], "identificador_oportunidad"
    )
    print("")
    print("Resumen de temperatura comercial:")
    imprimir_lista(
        "Oportunidades con temperatura alta o caliente",
        analisis["temperatura_alta"],
        "identificador_oportunidad",
    )
    print("")
    print("Resumen de prioridades:")
    imprimir_lista(
        "Oportunidades con prioridad alta",
        analisis["prioridades_altas"],
        "identificador_oportunidad",
    )
    print("")
    print("Resumen de bloqueos:")
    imprimir_lista(
        "Oportunidades bloqueadas", analisis["bloqueadas"], "identificador_oportunidad"
    )
    print("")
    print("Resumen de riesgos:")
    imprimir_lista(
        "Riesgos comerciales criticos", analisis["riesgos_criticos"], "identificador_bloqueo"
    )
    print("")
    print("Resumen de datos incompletos:")
    imprimir_lista(
        "Oportunidades sin responsable", analisis["sin_responsable"], "identificador_oportunidad"
    )
    imprimir_lista(
        "Oportunidades sin proxima accion",
        analisis["sin_proxima_accion"],
        "identificador_oportunidad",
    )
    imprimir_lista(
        "Oportunidades con importe ausente o no valido",
        analisis["importes_invalidos"],
        "identificador_oportunidad",
    )
    print("")
    print("Resumen de acciones siguientes:")
    imprimir_lista(
        "Acciones pendientes o en revision",
        analisis["acciones_abiertas"],
        "identificador_accion",
    )
    imprimir_lista("Acciones urgentes", analisis["acciones_urgentes"], "identificador_accion")
    print("")
    print(
        "Aviso: este informe es solo de control operativo ficticio; no garantiza ventas "
        "ni sustituye la revision humana."
    )
    print(f"Decision humana recomendada: {decision}")


def ejecutar(ruta_json):
    datos, error = cargar_json(ruta_json)
    if error:
        print(error)
        return 1

    error = validar_estructura(datos)
    if error:
        print(error)
        return 1

    analisis = analizar(datos)
    decision = recomendar_decision(analisis)
    imprimir_informe(ruta_json, datos, analisis, decision)
    return 0


def main():
    parser = construir_parser()
    argumentos = parser.parse_args()
    return ejecutar(argumentos.ruta_json)


if __name__ == "__main__":
    sys.exit(main())
