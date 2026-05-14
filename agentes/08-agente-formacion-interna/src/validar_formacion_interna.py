import argparse
import json
import sys
from pathlib import Path

SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "empresa_ficticia",
    "modulos_formativos",
    "acciones_formativas_siguientes",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "08-agente-formacion-interna"
    / "datos_ejemplo"
    / "formacion_interna_ficticia.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(description="Valida formacion interna ficticia del Agente 08.")
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al JSON de formacion interna.",
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

    if not isinstance(datos.get("modulos_formativos"), list):
        return "Error: estructura incompleta. La seccion 'modulos_formativos' debe ser una lista."

    for seccion in [
        "rutas_formativas",
        "perfiles_internos",
        "evidencias_formativas",
        "acciones_formativas_siguientes",
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
    rutas = datos.get("rutas_formativas", [])
    modulos = datos.get("modulos_formativos", [])
    perfiles = datos.get("perfiles_internos", [])
    evidencias = datos.get("evidencias_formativas", [])
    acciones = datos.get("acciones_formativas_siguientes", [])

    modulos_pendientes = [m for m in modulos if texto(m, "estado_modulo") == "pendiente"]
    modulos_curso_revision = [
        m for m in modulos if texto(m, "estado_modulo") in ["en_revision", "disponible"]
    ]
    modulos_completados = [m for m in modulos if texto(m, "estado_modulo") == "completado"]
    modulos_bloqueados = [m for m in modulos if texto(m, "estado_modulo") == "bloqueado"]
    prioridades_altas = [m for m in modulos if texto(m, "prioridad_modulo") == "alta"]
    responsables_ausentes = [m for m in modulos if not texto(m, "responsable_contenido")]

    perfiles_sin_ruta = [p for p in perfiles if not texto(p, "ruta_asignada")]

    modulo_ids_con_evidencia = {
        identificador(e, "identificador_modulo")
        for e in evidencias
        if texto(e, "identificador_modulo")
    }
    evidencias_ausentes = [
        m
        for m in modulos
        if identificador(m, "identificador_modulo") not in modulo_ids_con_evidencia
    ]

    riesgos_operativos = [
        r
        for r in rutas
        if texto(r, "estado_ruta") in ["bloqueada", "en_revision"]
        and texto(r, "prioridad_ruta") in ["alta", "critica", "crítica"]
    ]

    acciones_abiertas = [
        a for a in acciones if texto(a, "estado_accion") in ["pendiente", "en_revision"]
    ]
    acciones_urgentes = [
        a
        for a in acciones_abiertas
        if texto(a, "prioridad_accion") in ["alta", "urgente", "critica", "crítica"]
    ]

    datos_criticos_ausentes = []
    for modulo in modulos:
        if (
            not texto(modulo, "identificador_ruta")
            or not texto(modulo, "estado_modulo")
            or not texto(modulo, "responsable_contenido")
        ):
            datos_criticos_ausentes.append(modulo)

    return {
        "total_registros_formativos": len(modulos),
        "modulos_pendientes": deduplicar_por_id(modulos_pendientes, "identificador_modulo"),
        "modulos_curso_revision": deduplicar_por_id(modulos_curso_revision, "identificador_modulo"),
        "modulos_completados": deduplicar_por_id(modulos_completados, "identificador_modulo"),
        "modulos_bloqueados": deduplicar_por_id(modulos_bloqueados, "identificador_modulo"),
        "prioridades_altas": deduplicar_por_id(prioridades_altas, "identificador_modulo"),
        "perfiles_sin_ruta": deduplicar_por_id(perfiles_sin_ruta, "identificador_perfil"),
        "evidencias_ausentes": deduplicar_por_id(evidencias_ausentes, "identificador_modulo"),
        "responsables_ausentes": deduplicar_por_id(responsables_ausentes, "identificador_modulo"),
        "riesgos_operativos": deduplicar_por_id(riesgos_operativos, "identificador_ruta"),
        "acciones_abiertas": deduplicar_por_id(acciones_abiertas, "identificador_accion"),
        "acciones_urgentes": deduplicar_por_id(acciones_urgentes, "identificador_accion"),
        "datos_criticos_ausentes": deduplicar_por_id(
            datos_criticos_ausentes, "identificador_modulo"
        ),
    }


def recomendar_decision(analisis):
    if (
        analisis["modulos_bloqueados"]
        or analisis["riesgos_operativos"]
        or analisis["datos_criticos_ausentes"]
    ):
        return "bloquear"

    if (
        analisis["prioridades_altas"]
        or analisis["acciones_urgentes"]
        or analisis["modulos_pendientes"]
    ):
        return "priorizar_formacion"

    if (
        analisis["perfiles_sin_ruta"]
        or analisis["responsables_ausentes"]
        or analisis["evidencias_ausentes"]
    ):
        return "pedir_informacion"

    if (
        not analisis["modulos_pendientes"]
        and not analisis["modulos_bloqueados"]
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
    print("Informe de validacion de formacion interna del Agente 08")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Empresa ficticia: {nombre_empresa(datos)}")
    print(
        "Numero total de rutas, modulos o registros formativos: "
        f"{analisis['total_registros_formativos']}"
    )
    print("")
    print("Resumen de estados formativos:")
    imprimir_lista("Modulos pendientes", analisis["modulos_pendientes"], "identificador_modulo")
    imprimir_lista(
        "Modulos en curso o en revision",
        analisis["modulos_curso_revision"],
        "identificador_modulo",
    )
    imprimir_lista("Modulos completados", analisis["modulos_completados"], "identificador_modulo")
    print("")
    print("Resumen de prioridades:")
    imprimir_lista(
        "Modulos con prioridad alta",
        analisis["prioridades_altas"],
        "identificador_modulo",
    )
    print("")
    print("Resumen de bloqueos:")
    imprimir_lista("Modulos bloqueados", analisis["modulos_bloqueados"], "identificador_modulo")
    print("")
    print("Resumen de evidencias:")
    imprimir_lista(
        "Modulos sin evidencia registrada",
        analisis["evidencias_ausentes"],
        "identificador_modulo",
    )
    print("")
    print("Resumen de responsables o datos incompletos:")
    imprimir_lista(
        "Modulos sin responsable",
        analisis["responsables_ausentes"],
        "identificador_modulo",
    )
    imprimir_lista(
        "Perfiles sin ruta asignada",
        analisis["perfiles_sin_ruta"],
        "identificador_perfil",
    )
    print("")
    print("Resumen de riesgos:")
    imprimir_lista(
        "Riesgos formativos u operativos", analisis["riesgos_operativos"], "identificador_ruta"
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
        "Aviso: este informe no certifica competencias ni sustituye revision humana; "
        "solo organiza seguimiento formativo ficticio."
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
