import argparse
import json
import sys
from pathlib import Path

SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "empresa_ficticia",
    "controles_internos",
    "acciones_seguimiento",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "10-agente-revision-cumplimiento"
    / "datos_ejemplo"
    / "revision_cumplimiento_ficticia.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(
        description="Valida una revision interna ficticia del Agente 10."
    )
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al JSON de revision y cumplimiento.",
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
        return "Error: estructura incompleta. Faltan secciones principales: " + ", ".join(faltantes)

    if not isinstance(datos.get("controles_internos"), list):
        return "Error: estructura incompleta. La seccion 'controles_internos' debe ser una lista."

    for seccion in [
        "evidencias_revision",
        "hallazgos_internos",
        "documentos_pendientes",
        "acciones_seguimiento",
    ]:
        if seccion in datos and not isinstance(datos.get(seccion), list):
            return f"Error: estructura incompleta. La seccion '{seccion}' debe ser una lista."

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


def analizar(datos):
    controles = datos.get("controles_internos", [])
    evidencias = datos.get("evidencias_revision", [])
    hallazgos = datos.get("hallazgos_internos", [])
    documentos = datos.get("documentos_pendientes", [])
    acciones = datos.get("acciones_seguimiento", [])

    documentos_pendientes = [
        d for d in documentos if texto(d, "estado_documento") in ["pendiente", "en_revision"]
    ]
    hallazgos_abiertos = [
        h
        for h in hallazgos
        if texto(h, "estado_hallazgo") in ["pendiente", "en_revision", "bloqueado"]
    ]
    riesgos_criticos_altos = [
        h for h in hallazgos if texto(h, "nivel_riesgo_operativo") in ["alto", "critico", "crítico"]
    ]
    bloqueados = [c for c in controles if texto(c, "estado_control") == "bloqueado"]
    prioridades_altas = [c for c in controles if texto(c, "prioridad_revision") == "alta"]
    responsables_ausentes = [c for c in controles if not texto(c, "responsable_interno")]

    control_ids_con_evidencia = {
        identificador(e, "identificador_control")
        for e in evidencias
        if texto(e, "identificador_control")
    }
    evidencias_ausentes = [
        c
        for c in controles
        if identificador(c, "identificador_control") not in control_ids_con_evidencia
    ]
    evidencias_criticas_ausentes = [
        c
        for c in evidencias_ausentes
        if texto(c, "prioridad_revision") in ["alta", "critica", "crítica"]
    ]

    acciones_abiertas = [
        a for a in acciones if texto(a, "estado_accion") in ["pendiente", "en_revision"]
    ]
    acciones_urgentes = [
        a
        for a in acciones_abiertas
        if texto(a, "prioridad_accion") in ["alta", "urgente", "critica", "crítica"]
    ]

    categorias_sensibles = [
        c
        for c in controles
        if any(clave in texto(c, "tipo_control") for clave in ["datos_personales", "rgpd"])
    ]

    estados_incompletos = []
    for c in controles:
        if not texto(c, "estado_control") or texto(c, "estado_control") in [
            "sin_definir",
            "ambiguo",
        ]:
            estados_incompletos.append(c)

    datos_criticos_ausentes = []
    for c in controles:
        if (
            not texto(c, "nombre_control")
            or not texto(c, "estado_control")
            or not texto(c, "responsable_interno")
        ):
            datos_criticos_ausentes.append(c)

    return {
        "total_registros": len(controles),
        "documentos_pendientes": deduplicar_por_id(
            documentos_pendientes, "identificador_documento"
        ),
        "evidencias_ausentes": deduplicar_por_id(evidencias_ausentes, "identificador_control"),
        "evidencias_criticas_ausentes": deduplicar_por_id(
            evidencias_criticas_ausentes, "identificador_control"
        ),
        "hallazgos_abiertos": deduplicar_por_id(hallazgos_abiertos, "identificador_hallazgo"),
        "riesgos_criticos_altos": deduplicar_por_id(
            riesgos_criticos_altos, "identificador_hallazgo"
        ),
        "bloqueados": deduplicar_por_id(bloqueados, "identificador_control"),
        "prioridades_altas": deduplicar_por_id(prioridades_altas, "identificador_control"),
        "responsables_ausentes": deduplicar_por_id(responsables_ausentes, "identificador_control"),
        "acciones_abiertas": deduplicar_por_id(acciones_abiertas, "identificador_accion"),
        "acciones_urgentes": deduplicar_por_id(acciones_urgentes, "identificador_accion"),
        "categorias_sensibles": deduplicar_por_id(categorias_sensibles, "identificador_control"),
        "estados_incompletos": deduplicar_por_id(estados_incompletos, "identificador_control"),
        "datos_criticos_ausentes": deduplicar_por_id(
            datos_criticos_ausentes, "identificador_control"
        ),
    }


def recomendar_decision(analisis):
    if (
        analisis["riesgos_criticos_altos"]
        or analisis["evidencias_criticas_ausentes"]
        or analisis["hallazgos_abiertos"]
        or analisis["bloqueados"]
        or analisis["datos_criticos_ausentes"]
    ):
        return "bloquear"

    if (
        analisis["documentos_pendientes"]
        or analisis["acciones_urgentes"]
        or analisis["prioridades_altas"]
    ):
        return "priorizar_revision"

    if (
        analisis["responsables_ausentes"]
        or analisis["evidencias_ausentes"]
        or analisis["estados_incompletos"]
    ):
        return "pedir_informacion"

    if (
        not analisis["documentos_pendientes"]
        and not analisis["hallazgos_abiertos"]
        and not analisis["acciones_abiertas"]
        and not analisis["riesgos_criticos_altos"]
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
    print("Informe de validacion de revision y cumplimiento del Agente 10")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Empresa ficticia: {nombre_empresa(datos)}")
    print(
        "Numero total de revisiones, documentos, hallazgos o registros: "
        f"{analisis['total_registros']}"
    )
    print("")
    print("Resumen de documentos y evidencias:")
    imprimir_lista(
        "Documentos pendientes", analisis["documentos_pendientes"], "identificador_documento"
    )
    imprimir_lista("Evidencias ausentes", analisis["evidencias_ausentes"], "identificador_control")
    print("")
    print("Resumen de hallazgos:")
    imprimir_lista("Hallazgos abiertos", analisis["hallazgos_abiertos"], "identificador_hallazgo")
    print("")
    print("Resumen de riesgos:")
    imprimir_lista(
        "Riesgos criticos o altos",
        analisis["riesgos_criticos_altos"],
        "identificador_hallazgo",
    )
    print("")
    print("Resumen de bloqueos:")
    imprimir_lista("Elementos bloqueados", analisis["bloqueados"], "identificador_control")
    print("")
    print("Resumen de datos incompletos:")
    imprimir_lista(
        "Elementos sin responsable",
        analisis["responsables_ausentes"],
        "identificador_control",
    )
    imprimir_lista(
        "Estados incompletos o ambiguos",
        analisis["estados_incompletos"],
        "identificador_control",
    )
    print("")
    print("Resumen de acciones correctivas o siguientes:")
    imprimir_lista(
        "Acciones pendientes o en revision",
        analisis["acciones_abiertas"],
        "identificador_accion",
    )
    imprimir_lista("Acciones urgentes", analisis["acciones_urgentes"], "identificador_accion")
    print("")
    print("Aviso: este informe no es asesoria legal, fiscal, laboral, financiera ni regulatoria.")
    print(
        "Aviso: este informe no acredita cumplimiento normativo; solo organiza revision "
        "interna ficticia con supervision humana."
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
