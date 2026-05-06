from pathlib import Path
import argparse
import json
import sys


ESTADOS_DOCUMENTALES = [
    "recibido",
    "incompleto",
    "pendiente",
    "en_revision",
    "validado",
    "obsoleto",
    "duplicado",
    "descartado",
]

SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "empresa_ficticia",
    "documentos",
    "clasificaciones_documentales",
    "control_versiones",
    "pendientes_documentales",
    "acciones_documentales_siguientes",
    "resultado_validacion_manual",
]

RUTA_JSON_POR_DEFECTO = (
    Path(__file__).resolve().parents[3]
    / "agentes"
    / "02-agente-documental-inteligente"
    / "datos_ejemplo"
    / "inventario_documental_ficticio.json"
)


def construir_parser():
    parser = argparse.ArgumentParser(
        description="Valida un inventario documental ficticio del Agente 02."
    )
    parser.add_argument(
        "ruta_json",
        nargs="?",
        type=Path,
        default=RUTA_JSON_POR_DEFECTO,
        help="Ruta opcional al inventario documental en JSON.",
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

    secciones_faltantes = [
        seccion for seccion in SECCIONES_OBLIGATORIAS if seccion not in datos
    ]
    if secciones_faltantes:
        return (
            "Error: estructura incompleta. Faltan secciones principales: "
            + ", ".join(secciones_faltantes)
        )

    listas_obligatorias = [
        "documentos",
        "pendientes_documentales",
        "acciones_documentales_siguientes",
    ]
    for seccion in listas_obligatorias:
        if not isinstance(datos.get(seccion), list):
            return f"Error: estructura incompleta. La seccion '{seccion}' debe ser una lista."

    return None


def contar_documentos_por_estado(documentos):
    conteo = {estado: 0 for estado in ESTADOS_DOCUMENTALES}
    for documento in documentos:
        estado = obtener_texto(documento, "estado_documental")
        if estado in conteo:
            conteo[estado] += 1
    return conteo


def obtener_texto(registro, campo):
    if not isinstance(registro, dict):
        return ""
    valor = registro.get(campo, "")
    if valor is None:
        return ""
    return str(valor).strip().lower()


def obtener_identificador(registro, campo):
    if not isinstance(registro, dict):
        return "sin_identificador"
    return str(registro.get(campo, "sin_identificador"))


def es_documento_bloqueante(documento):
    # Se admiten campos futuros sin exigirlos al JSON ficticio actual.
    for campo in ["bloqueante", "es_bloqueante", "bloquea"]:
        if isinstance(documento, dict) and documento.get(campo) is True:
            return True

    bloqueo = obtener_texto(documento, "bloqueo")
    return bloqueo in ["bloqueado", "bloqueante", "si", "sí", "true"]


def es_obsoleto_critico(documento, prioridades_por_documento):
    identificador = obtener_identificador(documento, "identificador_documento")
    criticidad = obtener_texto(documento, "criticidad")
    prioridad = prioridades_por_documento.get(identificador, "")
    return obtener_texto(documento, "estado_documental") == "obsoleto" and (
        criticidad in ["alta", "critica", "crítica"]
        or prioridad in ["alta", "critica", "crítica"]
    )


def obtener_prioridades_por_documento(clasificaciones):
    prioridades = {}
    if not isinstance(clasificaciones, list):
        return prioridades
    for clasificacion in clasificaciones:
        identificador = obtener_identificador(clasificacion, "identificador_documento")
        prioridades[identificador] = obtener_texto(clasificacion, "prioridad_revision")
    return prioridades


def filtrar_por_estado(registros, campo_estado, estados):
    encontrados = []
    for registro in registros:
        if obtener_texto(registro, campo_estado) in estados:
            encontrados.append(registro)
    return encontrados


def analizar_inventario(datos):
    documentos = datos["documentos"]
    pendientes = datos["pendientes_documentales"]
    acciones = datos["acciones_documentales_siguientes"]
    prioridades = obtener_prioridades_por_documento(
        datos.get("clasificaciones_documentales", [])
    )

    documentos_pendientes = filtrar_por_estado(documentos, "estado_documental", ["pendiente"])
    documentos_incompletos = filtrar_por_estado(
        documentos, "estado_documental", ["incompleto"]
    )
    documentos_obsoletos = filtrar_por_estado(documentos, "estado_documental", ["obsoleto"])
    documentos_duplicados = filtrar_por_estado(documentos, "estado_documental", ["duplicado"])
    pendientes_activos = filtrar_por_estado(
        pendientes, "estado_pendiente", ["pendiente", "en_revision"]
    )
    pendientes_bloqueados = filtrar_por_estado(
        pendientes, "estado_pendiente", ["bloqueado", "bloqueante"]
    )
    acciones_abiertas = filtrar_por_estado(
        acciones, "estado_accion", ["pendiente", "en_revision"]
    )

    duplicados_sin_resolver = detectar_duplicados_sin_resolver(
        documentos_duplicados, pendientes
    )
    obsoletos_criticos = [
        documento
        for documento in documentos_obsoletos
        if es_obsoleto_critico(documento, prioridades)
    ]
    documentos_bloqueantes = [
        documento for documento in documentos if es_documento_bloqueante(documento)
    ]

    return {
        "conteo_estados": contar_documentos_por_estado(documentos),
        "documentos_pendientes": documentos_pendientes,
        "documentos_incompletos": documentos_incompletos,
        "documentos_obsoletos": documentos_obsoletos,
        "documentos_duplicados": documentos_duplicados,
        "pendientes_activos": pendientes_activos,
        "pendientes_bloqueados": pendientes_bloqueados,
        "acciones_abiertas": acciones_abiertas,
        "documentos_bloqueantes": documentos_bloqueantes,
        "obsoletos_criticos": obsoletos_criticos,
        "duplicados_sin_resolver": duplicados_sin_resolver,
    }


def detectar_duplicados_sin_resolver(documentos_duplicados, pendientes):
    pendientes_por_documento = {}
    for pendiente in pendientes:
        identificador = obtener_identificador(pendiente, "identificador_documento")
        pendientes_por_documento.setdefault(identificador, []).append(pendiente)

    duplicados_sin_resolver = []
    for documento in documentos_duplicados:
        identificador = obtener_identificador(documento, "identificador_documento")
        pendientes_documento = pendientes_por_documento.get(identificador, [])
        esta_resuelto = any(
            obtener_texto(pendiente, "estado_pendiente") in ["resuelto", "descartado"]
            for pendiente in pendientes_documento
        )
        if not esta_resuelto:
            duplicados_sin_resolver.append(documento)
    return duplicados_sin_resolver


def recomendar_decision(analisis):
    hay_bloqueo = (
        analisis["documentos_bloqueantes"]
        or analisis["obsoletos_criticos"]
        or analisis["duplicados_sin_resolver"]
        or analisis["pendientes_bloqueados"]
    )
    if hay_bloqueo:
        return "bloquear"

    if analisis["documentos_pendientes"] or analisis["documentos_incompletos"]:
        return "pedir_informacion"

    if not analisis["pendientes_activos"] and not analisis["acciones_abiertas"]:
        return "avanzar"

    return "revisar_de_nuevo"


def obtener_nombre_empresa(datos):
    empresa = datos.get("empresa_ficticia", {})
    if isinstance(empresa, dict):
        return empresa.get("nombre_empresa", "no disponible")
    return "no disponible"


def imprimir_lista_resumida(titulo, registros, campo_identificador):
    print(f"{titulo}: {len(registros)}")
    for registro in registros:
        identificador = obtener_identificador(registro, campo_identificador)
        print(f"  - {identificador}")


def imprimir_informe(ruta_json, datos, analisis, decision):
    print("Informe de validacion documental del Agente 02")
    print(f"Ruta analizada: {ruta_json}")
    print(f"Empresa ficticia: {obtener_nombre_empresa(datos)}")
    print(f"Numero total de documentos: {len(datos['documentos'])}")
    print("")
    print("Conteo por estados documentales:")
    for estado, total in analisis["conteo_estados"].items():
        print(f"  - {estado}: {total}")

    print("")
    print("Resumen de incidencias documentales:")
    imprimir_lista_resumida(
        "Documentos pendientes",
        analisis["documentos_pendientes"],
        "identificador_documento",
    )
    imprimir_lista_resumida(
        "Documentos incompletos",
        analisis["documentos_incompletos"],
        "identificador_documento",
    )
    imprimir_lista_resumida(
        "Documentos obsoletos",
        analisis["documentos_obsoletos"],
        "identificador_documento",
    )
    imprimir_lista_resumida(
        "Documentos duplicados",
        analisis["documentos_duplicados"],
        "identificador_documento",
    )

    print("")
    print("Resumen de pendientes documentales:")
    imprimir_lista_resumida(
        "Pendientes activos",
        analisis["pendientes_activos"],
        "identificador_pendiente",
    )
    imprimir_lista_resumida(
        "Pendientes bloqueados",
        analisis["pendientes_bloqueados"],
        "identificador_pendiente",
    )

    print("")
    print("Resumen de acciones siguientes:")
    imprimir_lista_resumida(
        "Acciones pendientes o en revision",
        analisis["acciones_abiertas"],
        "identificador_accion",
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

    analisis = analizar_inventario(datos)
    decision = recomendar_decision(analisis)
    imprimir_informe(ruta_json, datos, analisis, decision)
    return 0


def main():
    parser = construir_parser()
    argumentos = parser.parse_args()
    return ejecutar(argumentos.ruta_json)


if __name__ == "__main__":
    sys.exit(main())
