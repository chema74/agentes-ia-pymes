import argparse
import json
import sys
from pathlib import Path

# Secciones principales que debe tener el expediente ficticio.
SECCIONES_OBLIGATORIAS = [
    "metadatos_ejemplo",
    "cliente",
    "documentacion_recibida",
    "checklist_onboarding",
    "clasificacion_inicial",
    "acciones_siguientes",
    "resultado_validacion_manual",
]


# Campos minimos necesarios para identificar y revisar el cliente.
CAMPOS_CLIENTE_OBLIGATORIOS = [
    "identificador_cliente",
    "nombre_cliente",
    "nombre_empresa",
    "correo_contacto",
    "telefono_contacto",
    "tipo_servicio_solicitado",
    "necesidad_principal",
    "estado_onboarding",
    "responsable_interno",
]


def obtener_ruta_expediente_por_defecto():
    """Construye la ruta al JSON ficticio desde la ubicacion de este script."""
    carpeta_agente = Path(__file__).resolve().parents[1]
    return carpeta_agente / "datos_ejemplo" / "cliente_onboarding_ficticio.json"


def leer_argumentos():
    """Lee una ruta opcional al expediente JSON desde la consola."""
    parser = argparse.ArgumentParser(
        description="Valida un expediente ficticio de onboarding para PYMES."
    )
    parser.add_argument(
        "ruta_json",
        nargs="?",
        help="Ruta opcional al archivo JSON ficticio que se quiere validar.",
    )
    return parser.parse_args()


def obtener_ruta_expediente(argumentos):
    """Decide si se usa la ruta recibida o el JSON ficticio por defecto."""
    if argumentos.ruta_json:
        return Path(argumentos.ruta_json)

    return obtener_ruta_expediente_por_defecto()


def cargar_expediente(ruta_expediente):
    """Carga el expediente ficticio y controla errores basicos de lectura."""
    try:
        with ruta_expediente.open("r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"ERROR: No se ha encontrado el archivo: {ruta_expediente}")
    except json.JSONDecodeError as error:
        print(f"ERROR: El archivo JSON no es valido: {error}")

    return None


def validar_secciones(expediente):
    """Comprueba que el expediente contiene todas las secciones principales."""
    return [seccion for seccion in SECCIONES_OBLIGATORIAS if seccion not in expediente]


def validar_campos_cliente(cliente):
    """Detecta campos criticos ausentes o vacios dentro de la seccion cliente."""
    campos_faltantes = []

    for campo in CAMPOS_CLIENTE_OBLIGATORIOS:
        valor = cliente.get(campo)
        if valor is None or valor == "":
            campos_faltantes.append(campo)

    return campos_faltantes


def revisar_checklist(checklist):
    """Resume el estado del checklist y localiza pendientes y bloqueos."""
    items_completos = []
    items_pendientes = []
    obligatorios_pendientes = []
    items_bloqueados = []

    for item in checklist:
        estado = item.get("estado_item", "")

        if estado == "completo":
            items_completos.append(item)
        elif estado == "pendiente":
            items_pendientes.append(item)

        if estado == "bloqueado":
            items_bloqueados.append(item)

        if item.get("obligatorio") is True and estado != "completo":
            obligatorios_pendientes.append(item)

    return {
        "completos": len(items_completos),
        "pendientes": len(items_pendientes),
        "obligatorios_pendientes": obligatorios_pendientes,
        "bloqueados": items_bloqueados,
    }


def revisar_documentacion(documentos):
    """Cuenta documentos segun su estado de recepcion."""
    recibidos = 0
    pendientes = 0
    incompletos = 0

    for documento in documentos:
        estado = documento.get("estado_documento", "")

        if estado == "recibido":
            recibidos += 1
        elif estado == "pendiente":
            pendientes += 1
        elif estado == "incompleto":
            incompletos += 1

    return {
        "recibidos": recibidos,
        "pendientes": pendientes,
        "incompletos": incompletos,
    }


def revisar_acciones_siguientes(acciones):
    """Verifica si existe alguna accion que todavia requiera seguimiento."""
    acciones_abiertas = []

    for accion in acciones:
        if accion.get("estado_accion") in ("pendiente", "en_revision"):
            acciones_abiertas.append(accion)

    return acciones_abiertas


def decidir_revision(campos_faltantes, resumen_checklist):
    """Aplica una regla sencilla y transparente para recomendar la decision."""
    if resumen_checklist["bloqueados"] or campos_faltantes:
        return "bloquear"

    if resumen_checklist["obligatorios_pendientes"]:
        return "pedir_informacion"

    if not resumen_checklist["obligatorios_pendientes"]:
        return "avanzar"

    return "revisar_de_nuevo"


def nombres_de_items(items):
    """Devuelve nombres legibles para mostrar pendientes y bloqueos."""
    return [item.get("nombre_item", "Item sin nombre") for item in items]


def imprimir_lista(titulo, elementos):
    """Imprime una lista simple evitando ruido cuando no hay elementos."""
    print(titulo)

    if not elementos:
        print("- Ninguno")
        return

    for elemento in elementos:
        print(f"- {elemento}")


def imprimir_informe(
    expediente,
    campos_faltantes,
    resumen_documentacion,
    resumen_checklist,
    acciones_abiertas,
    decision_recomendada,
):
    """Genera el informe minimo por consola para revision humana."""
    cliente = expediente["cliente"]

    print("INFORME DE VALIDACION DEL EXPEDIENTE")
    print("=" * 40)
    print(f"Cliente ficticio: {cliente.get('nombre_cliente', 'No informado')}")
    print(f"Empresa ficticia: {cliente.get('nombre_empresa', 'No informada')}")
    print(f"Estado del onboarding: {cliente.get('estado_onboarding', 'No informado')}")
    print()

    print("Resumen de documentacion")
    print(f"- Documentos recibidos: {resumen_documentacion['recibidos']}")
    print(f"- Documentos pendientes: {resumen_documentacion['pendientes']}")
    print(f"- Documentos incompletos: {resumen_documentacion['incompletos']}")
    print()

    print("Resumen del checklist")
    print(f"- Items completos: {resumen_checklist['completos']}")
    print(f"- Items pendientes: {resumen_checklist['pendientes']}")
    print(f"- Items obligatorios pendientes: {len(resumen_checklist['obligatorios_pendientes'])}")
    print(f"- Items bloqueados: {len(resumen_checklist['bloqueados'])}")
    print()

    pendientes_detectados = nombres_de_items(resumen_checklist["obligatorios_pendientes"])
    pendientes_detectados.extend(
        accion.get("descripcion_accion", "Accion sin descripcion") for accion in acciones_abiertas
    )

    imprimir_lista("Pendientes detectados", pendientes_detectados)
    print()

    bloqueos_detectados = nombres_de_items(resumen_checklist["bloqueados"])
    imprimir_lista("Bloqueos detectados", bloqueos_detectados)
    print()

    imprimir_lista("Campos criticos faltantes", campos_faltantes)
    print()
    print(f"Decision recomendada de revision manual: {decision_recomendada}")


def main():
    """Orquesta la carga, validacion y generacion del informe."""
    argumentos = leer_argumentos()
    ruta_expediente = obtener_ruta_expediente(argumentos)
    expediente = cargar_expediente(ruta_expediente)

    if expediente is None:
        return 1

    secciones_faltantes = validar_secciones(expediente)
    if secciones_faltantes:
        print("ERROR: La estructura del expediente esta incompleta.")
        imprimir_lista("Secciones faltantes", secciones_faltantes)
        return 1

    campos_faltantes = validar_campos_cliente(expediente["cliente"])
    resumen_checklist = revisar_checklist(expediente["checklist_onboarding"])
    resumen_documentacion = revisar_documentacion(expediente["documentacion_recibida"])
    acciones_abiertas = revisar_acciones_siguientes(expediente["acciones_siguientes"])

    if not acciones_abiertas:
        print("AVISO: No hay acciones pendientes ni en revision.")

    decision_recomendada = decidir_revision(campos_faltantes, resumen_checklist)

    imprimir_informe(
        expediente,
        campos_faltantes,
        resumen_documentacion,
        resumen_checklist,
        acciones_abiertas,
        decision_recomendada,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
