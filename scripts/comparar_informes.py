from __future__ import annotations

import argparse
import difflib
import os
from pathlib import Path
import sys

AGENTES_VALIDOS = set(range(1, 11))


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Comparador local de informes entre el ultimo informe y un historico."
    )
    parser.add_argument("--agente", type=int, required=True, help="Numero de agente (1-10).")
    parser.add_argument(
        "--archivo-historico",
        required=True,
        help="Nombre de archivo dentro de salidas/agente-XX/historico/.",
    )
    parser.add_argument(
        "--directorio-salidas",
        default="salidas",
        help="Directorio base de salidas (por defecto: salidas).",
    )
    parser.add_argument(
        "--solo-resumen",
        action="store_true",
        help="Muestra solo resumen de comparacion sin diff completo.",
    )
    return parser


def validar_agente(agente: int) -> int:
    if agente not in AGENTES_VALIDOS:
        raise ValueError("El agente debe estar entre 1 y 10.")
    return agente


def resolver_archivo_historico(carpeta_historico: Path, nombre_archivo: str) -> Path:
    if not nombre_archivo:
        raise ValueError("Debes indicar --archivo-historico.")
    if Path(nombre_archivo).name != nombre_archivo:
        raise ValueError("Archivo no valido: ruta no permitida para archivo historico.")
    if ".." in nombre_archivo or "/" in nombre_archivo or "\\" in nombre_archivo:
        raise ValueError("Ruta no permitida para archivo historico.")
    if not nombre_archivo.endswith("-informe.txt"):
        raise ValueError("El archivo historico debe terminar en -informe.txt.")

    ruta = (carpeta_historico / nombre_archivo).resolve()
    base = carpeta_historico.resolve()
    if not str(ruta).startswith(str(base) + os.sep) and ruta != base:
        raise ValueError("Ruta fuera del historico del agente no permitida.")
    return ruta


def extraer_decision(informe: str) -> str:
    prefijos = [
        "decision humana recomendada",
        "decisión humana recomendada",
        "decision recomendada",
        "decisión recomendada",
    ]
    for linea in informe.splitlines():
        limpia = linea.strip()
        for prefijo in prefijos:
            if limpia.lower().startswith(prefijo):
                _, _, resto = limpia.partition(":")
                valor = resto.strip()
                if valor:
                    return valor
    return "No identificada"


def comparar_textos(texto_actual: str, texto_historico: str) -> tuple[str, dict[str, int]]:
    lineas_actual = texto_actual.splitlines()
    lineas_historico = texto_historico.splitlines()

    diff = list(
        difflib.unified_diff(
            lineas_historico,
            lineas_actual,
            fromfile="historico",
            tofile="actual",
            lineterm="",
        )
    )
    diff_texto = "\n".join(diff) if diff else "Sin diferencias textuales."

    agregadas = 0
    eliminadas = 0
    for linea in difflib.ndiff(lineas_historico, lineas_actual):
        if linea.startswith("+ "):
            agregadas += 1
        elif linea.startswith("- "):
            eliminadas += 1
    sin_cambios = max(len(lineas_historico), len(lineas_actual)) - max(agregadas, eliminadas)
    if sin_cambios < 0:
        sin_cambios = 0

    resumen = {
        "lineas_añadidas": agregadas,
        "lineas_eliminadas": eliminadas,
        "lineas_sin_cambios_aprox": sin_cambios,
    }
    return diff_texto, resumen


def ejecutar_comparacion(agente: int, archivo_historico: str, directorio_salidas: Path) -> tuple[dict, int]:
    agente = validar_agente(agente)
    carpeta_agente = directorio_salidas / f"agente-{agente:02d}"
    ruta_actual = carpeta_agente / "informe.txt"
    carpeta_historico = carpeta_agente / "historico"
    ruta_historico = resolver_archivo_historico(carpeta_historico, archivo_historico)

    if not ruta_actual.is_file():
        raise FileNotFoundError(f"No existe el ultimo informe: {ruta_actual}")
    if not ruta_historico.is_file():
        raise FileNotFoundError(f"No existe el informe historico: {ruta_historico}")

    texto_actual = ruta_actual.read_text(encoding="utf-8", errors="replace")
    texto_historico = ruta_historico.read_text(encoding="utf-8", errors="replace")

    decision_actual = extraer_decision(texto_actual)
    decision_historica = extraer_decision(texto_historico)
    decision_cambiada = decision_actual != decision_historica
    diff_texto, resumen = comparar_textos(texto_actual, texto_historico)

    resultado = {
        "agente": f"agente-{agente:02d}",
        "ruta_actual": ruta_actual,
        "ruta_historica": ruta_historico,
        "decision_actual": decision_actual,
        "decision_historica": decision_historica,
        "decision_cambiada": decision_cambiada,
        "resumen": resumen,
        "diff": diff_texto,
    }
    return resultado, 0


def imprimir_resultado(resultado: dict, solo_resumen: bool) -> None:
    print("Comparacion local de informes")
    print(f"Agente: {resultado['agente']}")
    print(f"Ruta ultimo informe: {resultado['ruta_actual']}")
    print(f"Ruta informe historico: {resultado['ruta_historica']}")
    print(f"Decision recomendada actual: {resultado['decision_actual']}")
    print(f"Decision recomendada historica: {resultado['decision_historica']}")
    print(f"Cambio de decision: {'si' if resultado['decision_cambiada'] else 'no'}")
    print("Resumen de diferencias:")
    print(f"- Lineas añadidas: {resultado['resumen']['lineas_añadidas']}")
    print(f"- Lineas eliminadas: {resultado['resumen']['lineas_eliminadas']}")
    print(f"- Lineas sin cambios (aprox): {resultado['resumen']['lineas_sin_cambios_aprox']}")
    if not solo_resumen:
        print("")
        print("Diff textual:")
        print(resultado["diff"])


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)
    raiz = obtener_raiz_repositorio()
    directorio_salidas = Path(args.directorio_salidas)
    if not directorio_salidas.is_absolute():
        directorio_salidas = raiz / directorio_salidas

    try:
        resultado, codigo = ejecutar_comparacion(args.agente, args.archivo_historico, directorio_salidas)
        imprimir_resultado(resultado, args.solo_resumen)
        return codigo
    except (ValueError, FileNotFoundError) as error:
        print(f"Error: {error}")
        return 1
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
