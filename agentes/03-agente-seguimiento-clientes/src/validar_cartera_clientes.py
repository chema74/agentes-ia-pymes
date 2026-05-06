from pathlib import Path
import argparse
import json
import sys
from datetime import date


SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "empresa_ficticia",
    "clientes",
    "acciones_seguimiento",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "03-agente-seguimiento-clientes"
    / "datos_ejemplo"
    / "cartera_clientes_ficticia.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(
        description="Valida una cartera ficticia de clientes del Agente 03."
    )
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al JSON de cartera de clientes.",
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

    faltantes = [seccion for seccion in SECCIONES_OBLIGATORIAS if seccion not in datos]
    if faltantes:
        return (
            "Error: estructura incompleta. Faltan secciones principales: "
            + ", ".join(faltantes)
        )

    if not isinstance(datos.get("clientes"), list):
        return "Error: estructura incompleta. La seccion 'clientes' debe ser una lista."

    if "acciones_seguimiento" in datos and not isinstance(
        datos.get("acciones_seguimiento"), list
    ):
        return (
            "Error: estructura incompleta. La seccion 'acciones_seguimiento' debe ser "
            "una lista."
        )

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


def es_bloqueado(valor_bloqueo):
    valor = str(valor_bloqueo or "").strip().lower()
    return valor not in ["", "no", "ninguno", "false", "0"]


def parsear_fecha(fecha_texto):
    valor = str(fecha_texto or "").strip().lower()
    if not valor or valor in ["sin fecha prevista", "sin definir", "no aplica", "n/a"]:
        return None
    try:
        return date.fromisoformat(valor)
    except ValueError:
        return None


def detectar_sin_proxima_accion(clientes):
    sin_accion = []
    for cliente in clientes:
        proxima_accion = texto(cliente, "proxima_accion")
        if proxima_accion in ["", "sin definir", "no aplica", "n/a", "pendiente"]:
            sin_accion.append(cliente)
    return sin_accion


def detectar_seguimientos_vencidos(clientes):
    hoy = date.today()
    vencidos = []
    for cliente in clientes:
        fecha = parsear_fecha(cliente.get("fecha_prevista_seguimiento"))
        if fecha and fecha < hoy:
            vencidos.append(cliente)
    return vencidos


def deduplicar_por_identificador(registros, campo_id):
    vistos = set()
    resultado = []
    for registro in registros:
        clave = identificador(registro, campo_id)
        if clave in vistos:
            continue
        vistos.add(clave)
        resultado.append(registro)
    return resultado


def analizar_clientes(datos):
    clientes = datos.get("clientes", [])
    acciones = datos.get("acciones_seguimiento", [])

    activos = [c for c in clientes if texto(c, "estado_cliente") == "activo"]
    en_riesgo_estado = [c for c in clientes if texto(c, "estado_cliente") == "en_riesgo"]
    riesgos_altos = [
        c
        for c in clientes
        if texto(c, "riesgo_operativo") in ["alto", "critico", "crítico"]
    ]
    bloqueados = [
        c
        for c in clientes
        if texto(c, "estado_cliente") == "bloqueado"
        or es_bloqueado(c.get("bloqueo"))
    ]
    prioridades_altas = [c for c in clientes if texto(c, "prioridad") == "alta"]
    responsables_ausentes = [c for c in clientes if not texto(c, "responsable_interno")]
    sin_proxima_accion = detectar_sin_proxima_accion(clientes)
    seguimientos_vencidos = detectar_seguimientos_vencidos(clientes)

    acciones_pendientes = [a for a in acciones if texto(a, "estado_accion") == "pendiente"]
    acciones_revision_curso = [
        a for a in acciones if texto(a, "estado_accion") in ["en_revision", "en_curso"]
    ]
    acciones_bloqueadas = [
        a for a in acciones if texto(a, "estado_accion") == "bloqueada"
    ]

    return {
        "total_clientes": len(clientes),
        "activos": activos,
        "en_riesgo": deduplicar_por_identificador(
            en_riesgo_estado + riesgos_altos, "identificador_cliente"
        ),
        "bloqueados": deduplicar_por_identificador(
            bloqueados, "identificador_cliente"
        ),
        "sin_proxima_accion": sin_proxima_accion,
        "seguimientos_vencidos": seguimientos_vencidos,
        "prioridades_altas": prioridades_altas,
        "responsables_ausentes": responsables_ausentes,
        "acciones_pendientes": acciones_pendientes,
        "acciones_revision_curso": acciones_revision_curso,
        "acciones_bloqueadas": acciones_bloqueadas,
    }


def recomendar_decision(analisis):
    if analisis["bloqueados"] or analisis["acciones_bloqueadas"]:
        return "bloquear"

    if any(texto(c, "riesgo_operativo") in ["critico", "crítico"] for c in analisis["en_riesgo"]):
        return "bloquear"

    if analisis["en_riesgo"] or analisis["seguimientos_vencidos"] or analisis["prioridades_altas"]:
        return "priorizar_seguimiento"

    if analisis["responsables_ausentes"] or analisis["sin_proxima_accion"]:
        return "pedir_informacion"

    if (
        not analisis["bloqueados"]
        and not analisis["en_riesgo"]
        and not analisis["seguimientos_vencidos"]
        and not analisis["sin_proxima_accion"]
    ):
        return "avanzar"

    return "revisar_de_nuevo"


def nombre_empresa(datos):
    empresa = datos.get("empresa_ficticia", {})
    if isinstance(empresa, dict):
        return empresa.get("nombre_empresa", "no disponible")
    return "no disponible"


def imprimir_lista(titulo, registros, campo_id):
    print(f"{titulo}: {len(registros)}")
    for registro in registros:
        print(f"  - {identificador(registro, campo_id)}")


def imprimir_informe(ruta_json, datos, analisis, decision):
    print("Informe de seguimiento de cartera de clientes del Agente 03")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Empresa ficticia: {nombre_empresa(datos)}")
    print(f"Numero total de clientes o registros: {analisis['total_clientes']}")
    print("")
    print("Resumen de estados:")
    imprimir_lista("Clientes activos", analisis["activos"], "identificador_cliente")
    print("")
    print("Resumen de riesgos:")
    imprimir_lista("Clientes en riesgo", analisis["en_riesgo"], "identificador_cliente")
    imprimir_lista(
        "Prioridades altas", analisis["prioridades_altas"], "identificador_cliente"
    )
    print("")
    print("Resumen de bloqueos:")
    imprimir_lista("Clientes bloqueados", analisis["bloqueados"], "identificador_cliente")
    imprimir_lista(
        "Acciones bloqueadas", analisis["acciones_bloqueadas"], "identificador_accion"
    )
    print("")
    print("Resumen de proximas acciones:")
    imprimir_lista(
        "Clientes sin proxima accion", analisis["sin_proxima_accion"], "identificador_cliente"
    )
    imprimir_lista(
        "Clientes con seguimiento vencido",
        analisis["seguimientos_vencidos"],
        "identificador_cliente",
    )
    imprimir_lista(
        "Acciones pendientes", analisis["acciones_pendientes"], "identificador_accion"
    )
    imprimir_lista(
        "Acciones en revision o en curso",
        analisis["acciones_revision_curso"],
        "identificador_accion",
    )
    imprimir_lista(
        "Clientes sin responsable", analisis["responsables_ausentes"], "identificador_cliente"
    )
    print("")
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

    analisis = analizar_clientes(datos)
    decision = recomendar_decision(analisis)
    imprimir_informe(ruta_json, datos, analisis, decision)
    return 0


def main():
    parser = construir_parser()
    argumentos = parser.parse_args()
    return ejecutar(argumentos.ruta_json)


if __name__ == "__main__":
    sys.exit(main())
