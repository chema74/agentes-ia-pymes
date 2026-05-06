from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


AGENTES = {
    1: ("Agente 01 - Onboarding Inteligente", Path("agentes/01-agente-onboarding-inteligente/src/validar_expediente.py")),
    2: ("Agente 02 - Documental Inteligente", Path("agentes/02-agente-documental-inteligente/src/validar_inventario_documental.py")),
    3: ("Agente 03 - Seguimiento de Clientes", Path("agentes/03-agente-seguimiento-clientes/src/validar_cartera_clientes.py")),
    4: ("Agente 04 - Generador de Propuestas", Path("agentes/04-agente-generador-propuestas/src/validar_propuesta.py")),
    5: ("Agente 05 - Operaciones para PYMES", Path("agentes/05-agente-operaciones-pymes/src/validar_operaciones.py")),
    6: ("Agente 06 - Control de Cobros y Flujo de Caja", Path("agentes/06-agente-control-cobros-flujo-caja/src/validar_cobros_flujo_caja.py")),
    7: ("Agente 07 - Pipeline Comercial", Path("agentes/07-agente-pipeline-comercial/src/validar_pipeline_comercial.py")),
    8: ("Agente 08 - Formacion Interna", Path("agentes/08-agente-formacion-interna/src/validar_formacion_interna.py")),
    9: ("Agente 09 - Analisis de Mercado", Path("agentes/09-agente-analisis-mercado/src/validar_analisis_mercado.py")),
    10: ("Agente 10 - Revision y Cumplimiento", Path("agentes/10-agente-revision-cumplimiento/src/validar_revision_cumplimiento.py")),
}


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lanzador comun por consola para ejecutar uno de los 10 agentes locales."
    )
    parser.add_argument(
        "--agente",
        type=int,
        help="Numero del agente a ejecutar (1-10). Si no se indica, se mostrara un menu interactivo.",
    )
    return parser


def mostrar_menu() -> None:
    print("Agentes disponibles:")
    for numero, (nombre, _) in AGENTES.items():
        print(f"{numero}. {nombre}")


def leer_seleccion_interactiva() -> int | None:
    try:
        texto = input("Selecciona un agente (1-10): ").strip()
    except EOFError:
        print("No se pudo leer una seleccion valida.")
        return None

    if not texto.isdigit():
        print("Opcion invalida.")
        return None

    numero = int(texto)
    if numero not in AGENTES:
        print("Opcion invalida.")
        return None
    return numero


def resolver_agente(numero: int | None) -> int | None:
    if numero is None:
        return leer_seleccion_interactiva()
    if numero not in AGENTES:
        print("Opcion invalida.")
        return None
    return numero


def ejecutar_agente(numero: int) -> int:
    raiz = obtener_raiz_repositorio()
    nombre, ruta_relativa = AGENTES[numero]
    ruta_script = raiz / ruta_relativa

    if not ruta_script.is_file():
        print(f"No se encontro el script del agente: {ruta_script}")
        return 1

    print(f"Agente seleccionado: {nombre}")
    print(f"Script ejecutado: {ruta_script.relative_to(raiz)}")

    resultado = subprocess.run(
        [sys.executable, str(ruta_script)],
        cwd=raiz,
        check=False,
    )

    if resultado.returncode != 0:
        print(f"Resultado del agente: error de ejecucion (codigo {resultado.returncode}).")
        return 1

    print("Resultado del agente: ejecucion correcta.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    argumentos = parser.parse_args(argv)

    mostrar_menu()

    seleccion = resolver_agente(argumentos.agente)
    if seleccion is None:
        return 1

    return ejecutar_agente(seleccion)


if __name__ == "__main__":
    raise SystemExit(main())
