from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class ConfigAgente:
    numero: int
    nombre: str
    script: Path
    datos: Path


AGENTES: list[ConfigAgente] = [
    ConfigAgente(
        1,
        "Agente 01 - Onboarding Inteligente",
        Path("agentes/01-agente-onboarding-inteligente/src/validar_expediente.py"),
        Path(
            "agentes/01-agente-onboarding-inteligente/datos_ejemplo/cliente_onboarding_ficticio.json"
        ),
    ),
    ConfigAgente(
        2,
        "Agente 02 - Documental Inteligente",
        Path("agentes/02-agente-documental-inteligente/src/validar_inventario_documental.py"),
        Path(
            "agentes/02-agente-documental-inteligente/datos_ejemplo/inventario_documental_ficticio.json"
        ),
    ),
    ConfigAgente(
        3,
        "Agente 03 - Seguimiento de Clientes",
        Path("agentes/03-agente-seguimiento-clientes/src/validar_cartera_clientes.py"),
        Path("agentes/03-agente-seguimiento-clientes/datos_ejemplo/cartera_clientes_ficticia.json"),
    ),
    ConfigAgente(
        4,
        "Agente 04 - Generador de Propuestas",
        Path("agentes/04-agente-generador-propuestas/src/validar_propuesta.py"),
        Path("agentes/04-agente-generador-propuestas/datos_ejemplo/propuesta_ficticia.json"),
    ),
    ConfigAgente(
        5,
        "Agente 05 - Operaciones para PYMES",
        Path("agentes/05-agente-operaciones-pymes/src/validar_operaciones.py"),
        Path("agentes/05-agente-operaciones-pymes/datos_ejemplo/operaciones_pymes_ficticias.json"),
    ),
    ConfigAgente(
        6,
        "Agente 06 - Control de Cobros y Flujo de Caja",
        Path("agentes/06-agente-control-cobros-flujo-caja/src/validar_cobros_flujo_caja.py"),
        Path(
            "agentes/06-agente-control-cobros-flujo-caja/datos_ejemplo/cobros_flujo_caja_ficticios.json"
        ),
    ),
    ConfigAgente(
        7,
        "Agente 07 - Pipeline Comercial",
        Path("agentes/07-agente-pipeline-comercial/src/validar_pipeline_comercial.py"),
        Path("agentes/07-agente-pipeline-comercial/datos_ejemplo/pipeline_comercial_ficticio.json"),
    ),
    ConfigAgente(
        8,
        "Agente 08 - Formacion Interna",
        Path("agentes/08-agente-formacion-interna/src/validar_formacion_interna.py"),
        Path("agentes/08-agente-formacion-interna/datos_ejemplo/formacion_interna_ficticia.json"),
    ),
    ConfigAgente(
        9,
        "Agente 09 - Analisis de Mercado",
        Path("agentes/09-agente-analisis-mercado/src/validar_analisis_mercado.py"),
        Path("agentes/09-agente-analisis-mercado/datos_ejemplo/analisis_mercado_ficticio.json"),
    ),
    ConfigAgente(
        10,
        "Agente 10 - Revision y Cumplimiento",
        Path("agentes/10-agente-revision-cumplimiento/src/validar_revision_cumplimiento.py"),
        Path(
            "agentes/10-agente-revision-cumplimiento/datos_ejemplo/revision_cumplimiento_ficticia.json"
        ),
    ),
]

_AGENTES_POR_NUMERO: dict[int, ConfigAgente] = {a.numero: a for a in AGENTES}


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lanzador comun por consola para ejecutar los 10 agentes locales."
    )
    parser.add_argument("--agente", type=int, help="Numero del agente a ejecutar (1-10).")
    parser.add_argument("--todos", action="store_true", help="Ejecuta los 10 agentes en secuencia.")
    parser.add_argument(
        "--guardar-salida",
        action="store_true",
        help="Guarda cada informe en <directorio-salidas>/agente-XX/informe.txt.",
    )
    parser.add_argument(
        "--guardar-historico",
        action="store_true",
        help="Ademas de informe.txt, guarda una copia historica en <directorio-salidas>/agente-XX/historico/.",
    )
    parser.add_argument(
        "--directorio-salidas",
        default="salidas",
        help="Directorio donde se guardan informes si se usa --guardar-salida (por defecto: salidas).",
    )
    parser.add_argument(
        "--usar-datos-trabajo",
        action="store_true",
        help="Usa JSON del espacio de trabajo en lugar del JSON ficticio original.",
    )
    parser.add_argument(
        "--directorio-trabajo",
        default="espacio_trabajo",
        help="Directorio del espacio de trabajo editable (por defecto: espacio_trabajo).",
    )
    return parser


def obtener_ruta_datos(
    numero: int, raiz: Path, usar_datos_trabajo: bool, directorio_trabajo: Path
) -> tuple[Path, str | None]:
    agente = _AGENTES_POR_NUMERO[numero]
    if not usar_datos_trabajo:
        return raiz / agente.datos, None

    ruta_trabajo = directorio_trabajo / f"agente-{numero:02d}" / "datos.json"
    if not ruta_trabajo.is_file():
        return ruta_trabajo, (
            f"Error: no existe el archivo de trabajo para el agente {numero:02d}: {ruta_trabajo}. "
            "Primero ejecuta: python scripts/preparar_espacio_trabajo.py"
        )
    return ruta_trabajo, None


def ejecutar_agente(
    numero: int, raiz: Path, usar_datos_trabajo: bool, directorio_trabajo: Path
) -> tuple[int, str]:
    agente = _AGENTES_POR_NUMERO[numero]
    ruta_script = raiz / agente.script

    if not ruta_script.is_file():
        return 1, f"No se encontro el script del agente: {ruta_script}"

    ruta_datos, error_datos = obtener_ruta_datos(
        numero, raiz, usar_datos_trabajo, directorio_trabajo
    )
    if error_datos:
        return 1, error_datos

    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"

    comando = [sys.executable, str(ruta_script), str(ruta_datos)]
    resultado = subprocess.run(
        comando,
        cwd=raiz,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        env=entorno,
    )

    salida = []
    salida.append(f"Agente seleccionado: {agente.nombre}")
    salida.append(f"Script ejecutado: {ruta_script.relative_to(raiz)}")
    salida.append(f"Ruta de datos usada: {ruta_datos}")
    if resultado.stdout:
        salida.append(resultado.stdout.strip())
    if resultado.stderr:
        salida.append(resultado.stderr.strip())

    if resultado.returncode != 0:
        salida.append(f"Resultado del agente: error de ejecucion (codigo {resultado.returncode}).")
        return 1, "\n".join(parte for parte in salida if parte)

    salida.append("Resultado del agente: ejecucion correcta.")
    return 0, "\n".join(parte for parte in salida if parte)


def guardar_informe(directorio_salidas: Path, numero: int, informe: str) -> Path:
    carpeta_agente = directorio_salidas / f"agente-{numero:02d}"
    carpeta_agente.mkdir(parents=True, exist_ok=True)
    ruta_informe = carpeta_agente / "informe.txt"
    ruta_informe.write_text(informe + "\n", encoding="utf-8")
    return ruta_informe


def guardar_informe_historico(directorio_salidas: Path, numero: int, informe: str) -> Path:
    carpeta_historico = directorio_salidas / f"agente-{numero:02d}" / "historico"
    carpeta_historico.mkdir(parents=True, exist_ok=True)
    marca = datetime.now().strftime("%Y%m%d-%H%M%S")
    ruta_historico = carpeta_historico / f"{marca}-informe.txt"
    ruta_historico.write_text(informe + "\n", encoding="utf-8")
    return ruta_historico


def ejecutar_seleccion(argumentos: argparse.Namespace, raiz: Path) -> int:
    directorio_trabajo = Path(argumentos.directorio_trabajo)
    if not directorio_trabajo.is_absolute():
        directorio_trabajo = raiz / directorio_trabajo

    directorio_salidas = Path(argumentos.directorio_salidas)
    if not directorio_salidas.is_absolute():
        directorio_salidas = raiz / directorio_salidas

    if argumentos.todos:
        seleccion = [a.numero for a in AGENTES]
    elif argumentos.agente is not None:
        if argumentos.agente not in _AGENTES_POR_NUMERO:
            print("Opcion invalida.")
            return 1
        seleccion = [argumentos.agente]
    else:
        print("Error: debes indicar --agente N o --todos.")
        return 1

    guardar_salida = argumentos.guardar_salida or argumentos.guardar_historico

    hubo_error = False
    for numero in seleccion:
        codigo, informe = ejecutar_agente(
            numero, raiz, argumentos.usar_datos_trabajo, directorio_trabajo
        )
        print(informe)
        if guardar_salida:
            ruta = guardar_informe(directorio_salidas, numero, informe)
            print(f"Informe guardado: {ruta}")
            if argumentos.guardar_historico:
                ruta_historica = guardar_informe_historico(directorio_salidas, numero, informe)
                print(f"Informe historico guardado: {ruta_historica}")
        if codigo != 0:
            hubo_error = True
            if not argumentos.todos:
                return 1

    return 1 if hubo_error else 0


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    argumentos = parser.parse_args(argv)
    raiz = obtener_raiz_repositorio()

    try:
        return ejecutar_seleccion(argumentos, raiz)
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
