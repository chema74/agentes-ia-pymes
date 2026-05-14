import argparse
import json
import sys
from datetime import date
from pathlib import Path

SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "empresa_ficticia",
    "cobros_pendientes",
    "acciones_seguimiento",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "06-agente-control-cobros-flujo-caja"
    / "datos_ejemplo"
    / "cobros_flujo_caja_ficticios.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(
        description="Valida cobros y flujo de caja ficticios del Agente 06."
    )
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al JSON de cobros.",
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
        return "Error: estructura incompleta. Faltan secciones principales: " + ", ".join(faltantes)

    if not isinstance(datos.get("cobros_pendientes"), list):
        return "Error: estructura incompleta. La seccion 'cobros_pendientes' debe ser una lista."

    for seccion_lista in [
        "riesgos_cobro",
        "acciones_seguimiento",
        "previsiones_operativas",
        "referencias_cobro",
    ]:
        if seccion_lista in datos and not isinstance(datos.get(seccion_lista), list):
            return f"Error: estructura incompleta. La seccion '{seccion_lista}' debe ser una lista."

    if "resultado_validacion_manual" not in datos:
        return "Error: estructura incompleta. Falta 'resultado_validacion_manual' en el JSON."

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
    texto_fecha = str(valor or "").strip().lower()
    if not texto_fecha or texto_fecha in ["sin fecha", "sin definir", "no aplica", "n/a"]:
        return None
    try:
        return date.fromisoformat(texto_fecha)
    except ValueError:
        return None


def importe_valido(valor):
    if isinstance(valor, (int, float)):
        return valor >= 0
    return False


def analizar(datos):
    cobros = datos.get("cobros_pendientes", [])
    acciones = datos.get("acciones_seguimiento", [])
    riesgos = datos.get("riesgos_cobro", [])
    previsiones = datos.get("previsiones_operativas", [])
    hoy = date.today()

    cobros_pendientes = [c for c in cobros if texto(c, "estado_cobro") == "pendiente"]
    cobros_vencidos_estado = [c for c in cobros if texto(c, "estado_cobro") == "vencido"]
    cobros_vencidos_fecha = []
    for cobro in cobros:
        fecha_vencimiento = parsear_fecha(cobro.get("fecha_vencimiento"))
        if (
            fecha_vencimiento
            and fecha_vencimiento < hoy
            and texto(cobro, "estado_cobro") not in ["cobrado", "descartado"]
        ):
            cobros_vencidos_fecha.append(cobro)
    cobros_vencidos = deduplicar_por_id(
        cobros_vencidos_estado + cobros_vencidos_fecha, "identificador_cobro"
    )

    cobros_en_riesgo = [
        c
        for c in cobros
        if texto(c, "riesgo_retraso") in ["alto", "critico", "crítico"]
        or texto(c, "estado_cobro") in ["en_revision", "vencido", "bloqueado"]
    ]
    cobros_bloqueados = [c for c in cobros if texto(c, "estado_cobro") == "bloqueado"]
    prioridades_altas = [c for c in cobros if texto(c, "prioridad_seguimiento") == "alta"]
    importes_invalidos = [c for c in cobros if not importe_valido(c.get("importe_previsto"))]
    clientes_ausentes = [c for c in cobros if not texto(c, "nombre_cliente")]
    responsables_ausentes = [c for c in cobros if not texto(c, "responsable_interno")]
    campos_criticos_ausentes = []
    for cobro in cobros:
        if (
            not texto(cobro, "nombre_cliente")
            or not importe_valido(cobro.get("importe_previsto"))
            or not texto(cobro, "estado_cobro")
            or parsear_fecha(cobro.get("fecha_vencimiento")) is None
            or not texto(cobro, "responsable_interno")
        ):
            campos_criticos_ausentes.append(cobro)

    acciones_abiertas = [
        a for a in acciones if texto(a, "estado_accion") in ["pendiente", "en_revision"]
    ]
    acciones_urgentes = [
        a
        for a in acciones_abiertas
        if texto(a, "prioridad_accion") in ["alta", "urgente", "critica", "crítica"]
    ]
    riesgos_criticos = [r for r in riesgos if texto(r, "nivel_riesgo") in ["critico", "crítico"]]
    tension_operativa = [
        p
        for p in previsiones
        if texto(p, "estado_prevision") == "incierta"
        or float(p.get("probabilidad_operativa", 1.0)) < 0.3
    ]

    return {
        "total_cobros": len(cobros),
        "cobros_pendientes": deduplicar_por_id(cobros_pendientes, "identificador_cobro"),
        "cobros_vencidos": cobros_vencidos,
        "cobros_en_riesgo": deduplicar_por_id(cobros_en_riesgo, "identificador_cobro"),
        "cobros_bloqueados": deduplicar_por_id(cobros_bloqueados, "identificador_cobro"),
        "prioridades_altas": deduplicar_por_id(prioridades_altas, "identificador_cobro"),
        "importes_invalidos": deduplicar_por_id(importes_invalidos, "identificador_cobro"),
        "clientes_ausentes": deduplicar_por_id(clientes_ausentes, "identificador_cobro"),
        "responsables_ausentes": deduplicar_por_id(responsables_ausentes, "identificador_cobro"),
        "campos_criticos_ausentes": deduplicar_por_id(
            campos_criticos_ausentes, "identificador_cobro"
        ),
        "acciones_abiertas": deduplicar_por_id(acciones_abiertas, "identificador_accion"),
        "acciones_urgentes": deduplicar_por_id(acciones_urgentes, "identificador_accion"),
        "riesgos_criticos": deduplicar_por_id(riesgos_criticos, "identificador_riesgo"),
        "tension_operativa": deduplicar_por_id(tension_operativa, "identificador_prevision"),
    }


def recomendar_decision(analisis):
    if (
        analisis["cobros_bloqueados"]
        or analisis["riesgos_criticos"]
        or analisis["campos_criticos_ausentes"]
    ):
        return "bloquear"

    if (
        analisis["cobros_vencidos"]
        or analisis["prioridades_altas"]
        or analisis["acciones_urgentes"]
    ):
        return "priorizar_cobro"

    if (
        analisis["clientes_ausentes"]
        or analisis["importes_invalidos"]
        or analisis["responsables_ausentes"]
    ):
        return "pedir_informacion"

    if (
        not analisis["cobros_pendientes"]
        and not analisis["acciones_abiertas"]
        and not analisis["cobros_en_riesgo"]
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
    print("Informe de validacion de cobros y flujo de caja del Agente 06")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Empresa ficticia: {nombre_empresa(datos)}")
    print(f"Numero total de cobros, facturas o registros: {analisis['total_cobros']}")
    print("")
    print("Resumen de estados de cobro:")
    imprimir_lista("Cobros pendientes", analisis["cobros_pendientes"], "identificador_cobro")
    imprimir_lista("Cobros en riesgo", analisis["cobros_en_riesgo"], "identificador_cobro")
    print("")
    print("Resumen de vencimientos:")
    imprimir_lista("Cobros vencidos", analisis["cobros_vencidos"], "identificador_cobro")
    print("")
    print("Resumen de riesgos:")
    imprimir_lista("Riesgos criticos", analisis["riesgos_criticos"], "identificador_riesgo")
    imprimir_lista(
        "Senales operativas de tension de caja",
        analisis["tension_operativa"],
        "identificador_prevision",
    )
    print("")
    print("Resumen de bloqueos:")
    imprimir_lista("Cobros bloqueados", analisis["cobros_bloqueados"], "identificador_cobro")
    print("")
    print("Resumen de datos incompletos:")
    imprimir_lista(
        "Cobros con importe ausente o no valido",
        analisis["importes_invalidos"],
        "identificador_cobro",
    )
    imprimir_lista(
        "Cobros con cliente ausente",
        analisis["clientes_ausentes"],
        "identificador_cobro",
    )
    imprimir_lista(
        "Cobros con responsable ausente",
        analisis["responsables_ausentes"],
        "identificador_cobro",
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
        "Aviso: este informe es solo de control operativo ficticio y apoyo interno; "
        "no es asesoria financiera, fiscal, contable ni legal."
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
