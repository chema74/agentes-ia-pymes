from pathlib import Path
import argparse
import json
import sys


SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "empresa_ficticia",
    "senales_mercado",
    "acciones_exploracion",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "09-agente-analisis-mercado"
    / "datos_ejemplo"
    / "analisis_mercado_ficticio.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(
        description="Valida un analisis de mercado ficticio del Agente 09."
    )
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al JSON de analisis de mercado.",
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

    if not isinstance(datos.get("senales_mercado"), list):
        return (
            "Error: estructura incompleta. La seccion 'senales_mercado' debe ser una lista."
        )

    for seccion in [
        "competidores_observados",
        "oportunidades_mercado",
        "riesgos_mercado",
        "acciones_exploracion",
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


def analizar(datos):
    senales = datos.get("senales_mercado", [])
    competidores = datos.get("competidores_observados", [])
    oportunidades = datos.get("oportunidades_mercado", [])
    riesgos = datos.get("riesgos_mercado", [])
    acciones = datos.get("acciones_exploracion", [])

    senales_pendientes = [
        s for s in senales if texto(s, "estado_senal") in ["pendiente", "nueva"]
    ]
    senales_revision = [s for s in senales if texto(s, "estado_senal") == "en_revision"]
    senales_descartadas = [s for s in senales if texto(s, "estado_senal") == "descartada"]
    senales_bloqueadas = [s for s in senales if texto(s, "estado_senal") == "bloqueada"]

    oportunidades_alta = [
        o for o in oportunidades if texto(o, "prioridad_exploracion") == "alta"
    ]
    riesgos_criticos_altos = [
        r for r in riesgos if texto(r, "nivel_riesgo") in ["alta", "critica", "crítica"]
    ]
    competidores_relevantes = [
        c for c in competidores if texto(c, "nivel_amenaza") in ["alta", "media"]
    ]
    sin_fuente = [s for s in senales if not texto(s, "fuente_observada")]
    fiabilidad_baja = [
        s for s in senales if texto(s, "nivel_relevancia") in ["baja"]
    ]
    responsables_ausentes = [s for s in senales if not texto(s, "responsable_revision")]
    acciones_abiertas = [
        a for a in acciones if texto(a, "estado_accion") in ["pendiente", "en_revision"]
    ]
    acciones_urgentes = [
        a
        for a in acciones_abiertas
        if texto(a, "prioridad_accion") in ["alta", "urgente", "critica", "crítica"]
    ]
    bloqueos_analisis = [
        a for a in acciones if texto(a, "estado_accion") == "bloqueada"
    ]

    datos_criticos_ausentes = []
    for senal in senales:
        if (
            not texto(senal, "titulo_senal")
            or not texto(senal, "estado_senal")
            or not texto(senal, "fuente_observada")
            or not texto(senal, "responsable_revision")
        ):
            datos_criticos_ausentes.append(senal)

    return {
        "total_registros": len(senales),
        "senales_pendientes": deduplicar_por_id(senales_pendientes, "identificador_senal"),
        "senales_revision": deduplicar_por_id(senales_revision, "identificador_senal"),
        "senales_descartadas": deduplicar_por_id(
            senales_descartadas, "identificador_senal"
        ),
        "senales_bloqueadas": deduplicar_por_id(senales_bloqueadas, "identificador_senal"),
        "oportunidades_alta": deduplicar_por_id(
            oportunidades_alta, "identificador_oportunidad"
        ),
        "riesgos_criticos_altos": deduplicar_por_id(
            riesgos_criticos_altos, "identificador_riesgo"
        ),
        "competidores_relevantes": deduplicar_por_id(
            competidores_relevantes, "identificador_competidor"
        ),
        "sin_fuente": deduplicar_por_id(sin_fuente, "identificador_senal"),
        "fiabilidad_baja": deduplicar_por_id(fiabilidad_baja, "identificador_senal"),
        "responsables_ausentes": deduplicar_por_id(
            responsables_ausentes, "identificador_senal"
        ),
        "acciones_abiertas": deduplicar_por_id(acciones_abiertas, "identificador_accion"),
        "acciones_urgentes": deduplicar_por_id(acciones_urgentes, "identificador_accion"),
        "bloqueos_analisis": deduplicar_por_id(
            bloqueos_analisis, "identificador_accion"
        ),
        "datos_criticos_ausentes": deduplicar_por_id(
            datos_criticos_ausentes, "identificador_senal"
        ),
    }


def recomendar_decision(analisis):
    if (
        analisis["riesgos_criticos_altos"]
        or analisis["bloqueos_analisis"]
        or analisis["sin_fuente"]
        or analisis["datos_criticos_ausentes"]
    ):
        return "bloquear"

    if (
        analisis["oportunidades_alta"]
        or analisis["senales_revision"]
        or analisis["acciones_urgentes"]
    ):
        return "priorizar_exploracion"

    if analisis["responsables_ausentes"] or analisis["fiabilidad_baja"]:
        return "pedir_informacion"

    if (
        not analisis["senales_pendientes"]
        and not analisis["senales_revision"]
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
    print("Informe de validacion de analisis de mercado del Agente 09")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Empresa ficticia: {nombre_empresa(datos)}")
    print(
        "Numero total de senales, oportunidades, riesgos o registros: "
        f"{analisis['total_registros']}"
    )
    print("")
    print("Resumen de senales de mercado:")
    imprimir_lista("Senales pendientes", analisis["senales_pendientes"], "identificador_senal")
    imprimir_lista("Senales en revision", analisis["senales_revision"], "identificador_senal")
    imprimir_lista(
        "Senales descartadas", analisis["senales_descartadas"], "identificador_senal"
    )
    print("")
    print("Resumen de oportunidades:")
    imprimir_lista(
        "Oportunidades de prioridad alta",
        analisis["oportunidades_alta"],
        "identificador_oportunidad",
    )
    print("")
    print("Resumen de competidores:")
    imprimir_lista(
        "Competidores relevantes",
        analisis["competidores_relevantes"],
        "identificador_competidor",
    )
    print("")
    print("Resumen de riesgos:")
    imprimir_lista(
        "Riesgos criticos o altos", analisis["riesgos_criticos_altos"], "identificador_riesgo"
    )
    imprimir_lista(
        "Bloqueos de analisis", analisis["bloqueos_analisis"], "identificador_accion"
    )
    print("")
    print("Resumen de fuentes o fiabilidad:")
    imprimir_lista("Senales sin fuente", analisis["sin_fuente"], "identificador_senal")
    imprimir_lista("Senales con fiabilidad baja", analisis["fiabilidad_baja"], "identificador_senal")
    print("")
    print("Resumen de datos incompletos:")
    imprimir_lista(
        "Senales sin responsable",
        analisis["responsables_ausentes"],
        "identificador_senal",
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
        "Aviso: este informe no es prediccion ni asesoramiento financiero, legal o de "
        "inversion; solo organiza observaciones operativas ficticias."
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
