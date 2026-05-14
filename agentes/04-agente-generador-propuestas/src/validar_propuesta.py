import argparse
import json
import sys
from pathlib import Path

SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "propuesta",
    "entregables_propuestos",
    "acciones_comerciales_siguientes",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "04-agente-generador-propuestas"
    / "datos_ejemplo"
    / "propuesta_ficticia.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(description="Valida una propuesta ficticia del Agente 04.")
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al JSON de propuesta.",
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

    if not isinstance(datos.get("propuesta"), dict):
        return "Error: estructura incompleta. La seccion 'propuesta' debe ser un objeto."

    for seccion_lista in [
        "entregables_propuestos",
        "acciones_comerciales_siguientes",
        "condiciones_comerciales",
        "alcance_propuesta",
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


def identificar(registro, campo):
    if not isinstance(registro, dict):
        return "sin_identificador"
    return str(registro.get(campo, "sin_identificador"))


def deduplicar_por_id(registros, campo_id):
    vistos = set()
    salida = []
    for registro in registros:
        clave = identificar(registro, campo_id)
        if clave in vistos:
            continue
        vistos.add(clave)
        salida.append(registro)
    return salida


def detectar_campos_ausentes_propuesta(propuesta):
    ausentes = []
    # Solo validamos campos que existen en la estructura real del ejemplo.
    campos_minimos = [
        "nombre_cliente",
        "nombre_empresa",
        "alcance_preliminar",
        "plazo_estimado",
    ]
    for campo in campos_minimos:
        if campo in propuesta and not texto(propuesta, campo):
            ausentes.append(campo)
    return ausentes


def analizar(datos):
    propuesta = datos.get("propuesta", {})
    entregables = datos.get("entregables_propuestos", [])
    acciones = datos.get("acciones_comerciales_siguientes", [])
    condiciones = datos.get("condiciones_comerciales", [])
    alcance = datos.get("alcance_propuesta", [])

    elementos = entregables + condiciones + alcance
    pendientes = [
        e
        for e in elementos
        if any(
            texto(e, campo_estado) == "pendiente"
            for campo_estado in ["estado_entregable", "estado_condicion", "estado_alcance"]
        )
    ]
    incompletos = [
        e
        for e in elementos
        if any(
            texto(e, campo_estado) in ["incompleto", "pendiente_definir"]
            for campo_estado in ["estado_entregable", "estado_condicion", "tipo_alcance"]
        )
    ]
    en_revision = [
        e
        for e in elementos
        if any(
            texto(e, campo_estado) == "en_revision"
            for campo_estado in ["estado_entregable", "estado_condicion", "estado_alcance"]
        )
    ]
    bloqueados = [a for a in acciones if texto(a, "estado_accion") == "bloqueada"]
    acciones_abiertas = [
        a for a in acciones if texto(a, "estado_accion") in ["pendiente", "en_revision"]
    ]

    riesgos_criticos = [
        c
        for c in condiciones
        if texto(c, "prioridad_condicion") in ["alta", "critica", "crítica"]
        and texto(c, "estado_condicion") in ["pendiente", "en_revision"]
    ]

    advertencias = []
    for campo in ["advertencia", "observaciones_internas"]:
        valor = propuesta.get(campo) if isinstance(propuesta, dict) else ""
        if str(valor or "").strip():
            advertencias.append({"id": campo})

    campos_ausentes = detectar_campos_ausentes_propuesta(propuesta)
    sin_entregables = len(entregables) == 0

    return {
        "estado_propuesta": propuesta.get("estado_propuesta", "no disponible"),
        "cliente_o_empresa": propuesta.get("nombre_empresa")
        or propuesta.get("nombre_cliente")
        or "no disponible",
        "total_servicios_fases_entregables": len(entregables) + len(alcance),
        "pendientes": deduplicar_por_id(pendientes, "identificador_entregable"),
        "incompletos": deduplicar_por_id(incompletos, "identificador_entregable"),
        "en_revision": deduplicar_por_id(en_revision, "identificador_entregable"),
        "bloqueados": bloqueados,
        "acciones_abiertas": acciones_abiertas,
        "riesgos_criticos": riesgos_criticos,
        "advertencias": advertencias,
        "campos_ausentes": campos_ausentes,
        "sin_entregables": sin_entregables,
    }


def recomendar_decision(analisis):
    if analisis["bloqueados"] or analisis["riesgos_criticos"]:
        return "bloquear"

    if analisis["campos_ausentes"] or analisis["sin_entregables"]:
        return "pedir_informacion"

    if analisis["pendientes"] or analisis["incompletos"] or analisis["en_revision"]:
        return "preparar_revision"

    if not analisis["acciones_abiertas"]:
        return "avanzar"

    return "revisar_de_nuevo"


def imprimir_lista(titulo, registros, campo_id):
    print(f"{titulo}: {len(registros)}")
    for registro in registros:
        print(f"  - {identificar(registro, campo_id)}")


def imprimir_informe(ruta_json, analisis, decision):
    print("Informe de validacion de propuesta del Agente 04")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Cliente o empresa ficticia: {analisis['cliente_o_empresa']}")
    print(f"Estado general de la propuesta: {analisis['estado_propuesta']}")
    print(
        "Numero de servicios, fases o entregables detectados: "
        f"{analisis['total_servicios_fases_entregables']}"
    )
    print("")
    imprimir_lista("Resumen de pendientes", analisis["pendientes"], "identificador_entregable")
    imprimir_lista(
        "Resumen de elementos incompletos",
        analisis["incompletos"],
        "identificador_entregable",
    )
    imprimir_lista("Resumen de bloqueos", analisis["bloqueados"], "identificador_accion")
    print(
        f"Resumen de riesgos o advertencias: {len(analisis['riesgos_criticos']) + len(analisis['advertencias'])}"
    )
    imprimir_lista(
        "Resumen de acciones siguientes",
        analisis["acciones_abiertas"],
        "identificador_accion",
    )
    print(f"Campos minimos ausentes en propuesta: {len(analisis['campos_ausentes'])}")
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

    analisis = analizar(datos)
    decision = recomendar_decision(analisis)
    imprimir_informe(ruta_json, analisis, decision)
    return 0


def main():
    parser = construir_parser()
    argumentos = parser.parse_args()
    return ejecutar(argumentos.ruta_json)


if __name__ == "__main__":
    sys.exit(main())
