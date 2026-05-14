from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

CATALOGO_JSON = {
    1: Path(
        "agentes/01-agente-onboarding-inteligente/datos_ejemplo/cliente_onboarding_ficticio.json"
    ),
    2: Path(
        "agentes/02-agente-documental-inteligente/datos_ejemplo/inventario_documental_ficticio.json"
    ),
    3: Path("agentes/03-agente-seguimiento-clientes/datos_ejemplo/cartera_clientes_ficticia.json"),
    4: Path("agentes/04-agente-generador-propuestas/datos_ejemplo/propuesta_ficticia.json"),
    5: Path("agentes/05-agente-operaciones-pymes/datos_ejemplo/operaciones_pymes_ficticias.json"),
    6: Path(
        "agentes/06-agente-control-cobros-flujo-caja/datos_ejemplo/cobros_flujo_caja_ficticios.json"
    ),
    7: Path("agentes/07-agente-pipeline-comercial/datos_ejemplo/pipeline_comercial_ficticio.json"),
    8: Path("agentes/08-agente-formacion-interna/datos_ejemplo/formacion_interna_ficticia.json"),
    9: Path("agentes/09-agente-analisis-mercado/datos_ejemplo/analisis_mercado_ficticio.json"),
    10: Path(
        "agentes/10-agente-revision-cumplimiento/datos_ejemplo/revision_cumplimiento_ficticia.json"
    ),
}


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepara un espacio local editable con copias de JSON ficticios por agente."
    )
    parser.add_argument(
        "--directorio-trabajo",
        default="espacio_trabajo",
        help="Directorio donde se guardan las copias editables (por defecto: espacio_trabajo).",
    )
    parser.add_argument(
        "--sobrescribir",
        action="store_true",
        help="Si se indica, reemplaza archivos de trabajo que ya existan.",
    )
    return parser


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def validar_json(ruta_json: Path) -> None:
    with ruta_json.open("r", encoding="utf-8") as archivo:
        json.load(archivo)


def copiar_json_agente(
    numero: int, origen: Path, directorio_trabajo: Path, sobrescribir: bool
) -> None:
    if not origen.is_file():
        raise FileNotFoundError(f"Falta JSON original del agente {numero:02d}: {origen}")

    carpeta_destino = directorio_trabajo / f"agente-{numero:02d}"
    carpeta_destino.mkdir(parents=True, exist_ok=True)
    destino = carpeta_destino / "datos.json"

    if destino.exists() and not sobrescribir:
        print(f"Agente {numero:02d}: archivo conservado (ya existe): {destino}")
        return

    shutil.copy2(origen, destino)
    validar_json(destino)
    print(f"Agente {numero:02d}: archivo creado: {destino}")


def preparar_espacio(directorio_trabajo: Path, sobrescribir: bool) -> int:
    raiz = obtener_raiz_repositorio()

    print(f"Directorio de trabajo usado: {directorio_trabajo}")
    if sobrescribir:
        print("Aviso: se ha activado --sobrescribir.")

    for numero, ruta_relativa in CATALOGO_JSON.items():
        origen = raiz / ruta_relativa
        copiar_json_agente(numero, origen, directorio_trabajo, sobrescribir)

    return 0


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)

    try:
        raiz = obtener_raiz_repositorio()
        directorio_trabajo = Path(args.directorio_trabajo)
        if not directorio_trabajo.is_absolute():
            directorio_trabajo = raiz / directorio_trabajo
        directorio_trabajo.mkdir(parents=True, exist_ok=True)
        return preparar_espacio(directorio_trabajo, args.sobrescribir)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return 1
    except json.JSONDecodeError as error:
        print(f"Error: JSON invalido en copia de trabajo: {error}")
        return 1
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
