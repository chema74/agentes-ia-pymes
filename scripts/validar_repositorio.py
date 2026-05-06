from pathlib import Path
import json
import subprocess
import sys


def obtener_raiz_repositorio():
    return Path(__file__).resolve().parents[1]


def obtener_configuracion_agentes():
    return [
        {
            "nombre": "Agente 01",
            "tests": "agentes/01-agente-onboarding-inteligente/tests",
            "json": "agentes/01-agente-onboarding-inteligente/datos_ejemplo/cliente_onboarding_ficticio.json",
        },
        {
            "nombre": "Agente 02",
            "tests": "agentes/02-agente-documental-inteligente/tests",
            "json": "agentes/02-agente-documental-inteligente/datos_ejemplo/inventario_documental_ficticio.json",
        },
        {
            "nombre": "Agente 03",
            "tests": "agentes/03-agente-seguimiento-clientes/tests",
            "json": "agentes/03-agente-seguimiento-clientes/datos_ejemplo/cartera_clientes_ficticia.json",
        },
        {
            "nombre": "Agente 04",
            "tests": "agentes/04-agente-generador-propuestas/tests",
            "json": "agentes/04-agente-generador-propuestas/datos_ejemplo/propuesta_ficticia.json",
        },
        {
            "nombre": "Agente 05",
            "tests": "agentes/05-agente-operaciones-pymes/tests",
            "json": "agentes/05-agente-operaciones-pymes/datos_ejemplo/operaciones_pymes_ficticias.json",
        },
        {
            "nombre": "Agente 06",
            "tests": "agentes/06-agente-control-cobros-flujo-caja/tests",
            "json": "agentes/06-agente-control-cobros-flujo-caja/datos_ejemplo/cobros_flujo_caja_ficticios.json",
        },
        {
            "nombre": "Agente 07",
            "tests": "agentes/07-agente-pipeline-comercial/tests",
            "json": "agentes/07-agente-pipeline-comercial/datos_ejemplo/pipeline_comercial_ficticio.json",
        },
        {
            "nombre": "Agente 08",
            "tests": "agentes/08-agente-formacion-interna/tests",
            "json": "agentes/08-agente-formacion-interna/datos_ejemplo/formacion_interna_ficticia.json",
        },
        {
            "nombre": "Agente 09",
            "tests": "agentes/09-agente-analisis-mercado/tests",
            "json": "agentes/09-agente-analisis-mercado/datos_ejemplo/analisis_mercado_ficticio.json",
        },
        {
            "nombre": "Agente 10",
            "tests": "agentes/10-agente-revision-cumplimiento/tests",
            "json": "agentes/10-agente-revision-cumplimiento/datos_ejemplo/revision_cumplimiento_ficticia.json",
        },
    ]


def validar_ruta_existente(ruta, descripcion):
    if not ruta.exists():
        raise FileNotFoundError(f"Falta {descripcion}: {ruta}")


def validar_json(ruta_json):
    validar_ruta_existente(ruta_json, "archivo JSON")
    with ruta_json.open("r", encoding="utf-8") as archivo:
        json.load(archivo)
    print(f"JSON valido: {ruta_json}")


def ejecutar_tests(ruta_tests, nombre_agente, raiz_repositorio):
    validar_ruta_existente(ruta_tests, "directorio de tests")
    print(f"Ejecutando tests de {nombre_agente}: {ruta_tests}")
    resultado = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(ruta_tests)],
        cwd=raiz_repositorio,
        text=True,
        capture_output=True,
        check=False,
    )
    if resultado.stdout:
        print(resultado.stdout.strip())
    if resultado.stderr:
        print(resultado.stderr.strip())
    if resultado.returncode != 0:
        raise RuntimeError(f"Fallaron los tests de {nombre_agente}.")


def validar_jsons(raiz_repositorio, agentes):
    total = 0
    print("Validando JSON de ejemplo...")
    for agente in agentes:
        ruta_json = raiz_repositorio / agente["json"]
        validar_json(ruta_json)
        total += 1
    return total


def validar_tests(raiz_repositorio, agentes):
    total = 0
    print("Ejecutando tests por agente...")
    for agente in agentes:
        ruta_tests = raiz_repositorio / agente["tests"]
        ejecutar_tests(ruta_tests, agente["nombre"], raiz_repositorio)
        total += 1
    return total


def validar_tests_transversales(raiz_repositorio):
    ruta_tests = raiz_repositorio / "tests"
    if not ruta_tests.exists():
        print("No se encontraron tests transversales en tests/.")
        return 0
    print("Ejecutando tests transversales: tests/")
    ejecutar_tests(ruta_tests, "tests transversales", raiz_repositorio)
    return 1


def main():
    try:
        raiz_repositorio = obtener_raiz_repositorio()
        agentes = obtener_configuracion_agentes()

        json_validados = validar_jsons(raiz_repositorio, agentes)
        tests_ejecutados = validar_tests(raiz_repositorio, agentes)
        tests_transversales = validar_tests_transversales(raiz_repositorio)

        print("")
        print("Resumen final")
        print(f"Tests por agente ejecutados: {tests_ejecutados}")
        print(f"Tests transversales ejecutados: {tests_transversales}")
        print(f"JSON validados: {json_validados}")
        print("Resultado final: validacion global correcta.")
        return 0
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return 1
    except json.JSONDecodeError as error:
        print(f"Error: JSON invalido en {error.doc}")
        return 1
    except RuntimeError as error:
        print(f"Error: {error}")
        return 1
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
