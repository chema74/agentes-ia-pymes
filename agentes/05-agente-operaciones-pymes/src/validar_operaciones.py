import argparse
import json
import sys
from datetime import date
from pathlib import Path

SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "empresa_ficticia",
    "tareas_operativas",
    "acciones_siguientes",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "05-agente-operaciones-pymes"
    / "datos_ejemplo"
    / "operaciones_pymes_ficticias.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(description="Valida operaciones ficticias del Agente 05.")
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al JSON de operaciones.",
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

    if not isinstance(datos.get("tareas_operativas"), list):
        return "Error: estructura incompleta. La seccion 'tareas_operativas' debe ser una lista."

    for seccion in [
        "bloqueos_operativos",
        "acciones_siguientes",
        "procesos_operativos",
        "revisiones_operativas",
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


def parsear_fecha(fecha_texto):
    valor = str(fecha_texto or "").strip().lower()
    if not valor or valor in ["sin fecha prevista", "sin definir", "no aplica", "n/a"]:
        return None
    try:
        return date.fromisoformat(valor)
    except ValueError:
        return None


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
    tareas = datos.get("tareas_operativas", [])
    bloqueos = datos.get("bloqueos_operativos", [])
    acciones = datos.get("acciones_siguientes", [])

    pendientes = [t for t in tareas if texto(t, "estado_tarea") == "pendiente"]
    en_curso_revision = [
        t for t in tareas if texto(t, "estado_tarea") in ["en_progreso", "en_revision"]
    ]
    bloqueadas = [t for t in tareas if texto(t, "estado_tarea") == "bloqueada"]
    prioridades_altas = [t for t in tareas if texto(t, "prioridad") == "alta"]
    responsables_ausentes = [t for t in tareas if not texto(t, "responsable_interno")]
    vencidas = []
    hoy = date.today()
    for tarea in tareas:
        fecha = parsear_fecha(tarea.get("fecha_prevista"))
        if (
            fecha
            and fecha < hoy
            and texto(tarea, "estado_tarea")
            not in [
                "completada",
                "descartada",
            ]
        ):
            vencidas.append(tarea)

    dependencias_no_resueltas = [t for t in tareas if str(t.get("bloqueo_asociado") or "").strip()]
    riesgos_criticos = [
        b
        for b in bloqueos
        if texto(b, "prioridad_bloqueo") in ["alta", "critica", "crítica"]
        and texto(b, "estado_bloqueo") in ["abierto", "en_revision"]
    ]
    acciones_abiertas = [
        a for a in acciones if texto(a, "estado_accion") in ["pendiente", "en_revision"]
    ]
    acciones_urgentes = [
        a
        for a in acciones_abiertas
        if texto(a, "prioridad_accion") in ["alta", "urgente", "critica", "crítica"]
    ]
    bloqueos_abiertos = [
        b for b in bloqueos if texto(b, "estado_bloqueo") in ["abierto", "en_revision"]
    ]

    return {
        "total_tareas": len(tareas),
        "pendientes": pendientes,
        "en_curso_revision": en_curso_revision,
        "bloqueadas": bloqueadas,
        "vencidas": vencidas,
        "prioridades_altas": prioridades_altas,
        "responsables_ausentes": responsables_ausentes,
        "dependencias_no_resueltas": deduplicar_por_id(
            dependencias_no_resueltas, "identificador_tarea"
        ),
        "riesgos_criticos": riesgos_criticos,
        "bloqueos_abiertos": bloqueos_abiertos,
        "acciones_abiertas": acciones_abiertas,
        "acciones_urgentes": acciones_urgentes,
    }


def recomendar_decision(analisis):
    if analisis["bloqueadas"] or analisis["riesgos_criticos"]:
        return "bloquear"

    if analisis["dependencias_no_resueltas"] and analisis["riesgos_criticos"]:
        return "bloquear"

    if analisis["prioridades_altas"] or analisis["vencidas"] or analisis["acciones_urgentes"]:
        return "priorizar"

    if analisis["responsables_ausentes"]:
        return "pedir_informacion"

    if (
        not analisis["pendientes"]
        and not analisis["en_curso_revision"]
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


def imprimir_informe(ruta_json, analisis, datos, decision):
    print("Informe de validacion de operaciones del Agente 05")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Empresa ficticia: {nombre_empresa(datos)}")
    print(f"Numero total de operaciones, tareas o procesos: {analisis['total_tareas']}")
    print("")
    print("Resumen de estados operativos:")
    imprimir_lista("Operaciones pendientes", analisis["pendientes"], "identificador_tarea")
    imprimir_lista(
        "Operaciones en curso o en revision",
        analisis["en_curso_revision"],
        "identificador_tarea",
    )
    print("")
    print("Resumen de prioridades:")
    imprimir_lista(
        "Operaciones con prioridad alta",
        analisis["prioridades_altas"],
        "identificador_tarea",
    )
    imprimir_lista("Operaciones vencidas", analisis["vencidas"], "identificador_tarea")
    print("")
    print("Resumen de bloqueos:")
    imprimir_lista("Operaciones bloqueadas", analisis["bloqueadas"], "identificador_tarea")
    imprimir_lista(
        "Bloqueos abiertos",
        analisis["bloqueos_abiertos"],
        "identificador_bloqueo",
    )
    print("")
    print("Resumen de dependencias:")
    imprimir_lista(
        "Dependencias no resueltas",
        analisis["dependencias_no_resueltas"],
        "identificador_tarea",
    )
    print("")
    print("Resumen de riesgos:")
    imprimir_lista(
        "Riesgos operativos criticos",
        analisis["riesgos_criticos"],
        "identificador_bloqueo",
    )
    print("")
    print("Resumen de acciones siguientes:")
    imprimir_lista(
        "Acciones pendientes o en revision",
        analisis["acciones_abiertas"],
        "identificador_accion",
    )
    imprimir_lista(
        "Acciones urgentes",
        analisis["acciones_urgentes"],
        "identificador_accion",
    )
    imprimir_lista(
        "Operaciones sin responsable",
        analisis["responsables_ausentes"],
        "identificador_tarea",
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

    analisis = analizar(datos)
    decision = recomendar_decision(analisis)
    imprimir_informe(ruta_json, analisis, datos, decision)
    return 0


def main():
    parser = construir_parser()
    argumentos = parser.parse_args()
    return ejecutar(argumentos.ruta_json)


if __name__ == "__main__":
    sys.exit(main())
