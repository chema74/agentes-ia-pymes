from pathlib import Path
import json
import subprocess
import sys


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def listar_agentes(raiz_repositorio: Path) -> list[Path]:
    directorio_agentes = raiz_repositorio / "agentes"
    if not directorio_agentes.exists():
        return []
    return sorted([p for p in directorio_agentes.iterdir() if p.is_dir()])


def validar_ruta_existente(ruta: Path, descripcion: str) -> None:
    if not ruta.exists():
        raise FileNotFoundError(f"Falta {descripcion}: {ruta}")


def validar_json(ruta_json: Path) -> None:
    validar_ruta_existente(ruta_json, "archivo JSON")
    with ruta_json.open("r", encoding="utf-8") as archivo:
        json.load(archivo)
    print(f"JSON valido: {ruta_json}")


def ejecutar_tests(ruta_tests: Path, nombre_objetivo: str, raiz_repositorio: Path) -> None:
    validar_ruta_existente(ruta_tests, "directorio de tests")
    print(f"Ejecutando tests de {nombre_objetivo}: {ruta_tests}")
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
        raise RuntimeError(f"Fallaron los tests de {nombre_objetivo}.")


def validar_jsons_agentes(agentes: list[Path]) -> tuple[int, int]:
    total_json = 0
    agentes_con_json = 0
    print("Validando JSON de ejemplo...")

    for agente in agentes:
        carpeta_datos = agente / "datos_ejemplo"
        if not carpeta_datos.exists():
            continue

        jsons = sorted(carpeta_datos.glob("*.json"))
        if not jsons:
            continue

        agentes_con_json += 1
        for ruta_json in jsons:
            validar_json(ruta_json)
            total_json += 1

    return total_json, agentes_con_json


def validar_tests_agentes(raiz_repositorio: Path, agentes: list[Path]) -> int:
    total = 0
    print("Ejecutando tests por agente...")

    for agente in agentes:
        ruta_tests = agente / "tests"
        if not ruta_tests.exists():
            continue
        ejecutar_tests(ruta_tests, agente.name, raiz_repositorio)
        total += 1

    return total


def validar_tests_transversales(raiz_repositorio: Path) -> int:
    ruta_tests = raiz_repositorio / "tests"
    if not ruta_tests.exists():
        print("No se encontraron tests transversales en tests/.")
        return 0
    print("Ejecutando tests transversales: tests/")
    ejecutar_tests(ruta_tests, "tests transversales", raiz_repositorio)
    return 1


def validar_utf8(raiz_repositorio: Path) -> None:
    script_utf8 = raiz_repositorio / "scripts" / "verificar_utf8.py"
    if not script_utf8.exists():
        raise FileNotFoundError(f"Falta script de verificacion UTF-8: {script_utf8}")

    print("Verificando codificacion UTF-8...")
    resultado = subprocess.run(
        [sys.executable, str(script_utf8)],
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
        raise RuntimeError("Fallaron las comprobaciones de codificacion UTF-8.")


def validar_contrato_agentes(raiz_repositorio: Path) -> None:
    script_contrato = raiz_repositorio / "scripts" / "validar_contrato_agentes.py"
    if not script_contrato.exists():
        raise FileNotFoundError(f"Falta script de contrato de agentes: {script_contrato}")

    print("Verificando contrato tecnico de agentes...")
    resultado = subprocess.run(
        [sys.executable, str(script_contrato)],
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
        raise RuntimeError("Fallaron las comprobaciones del contrato de agentes.")


def main() -> int:
    try:
        raiz_repositorio = obtener_raiz_repositorio()
        agentes = listar_agentes(raiz_repositorio)

        validar_utf8(raiz_repositorio)
        validar_contrato_agentes(raiz_repositorio)
        json_validados, agentes_con_json = validar_jsons_agentes(agentes)
        tests_agentes = validar_tests_agentes(raiz_repositorio, agentes)
        tests_transversales = validar_tests_transversales(raiz_repositorio)

        print("")
        print("Resumen final")
        print(f"Agentes detectados: {len(agentes)}")
        print(f"Agentes con datos JSON: {agentes_con_json}")
        print(f"Agentes con tests ejecutados: {tests_agentes}")
        print(f"Tests transversales ejecutados: {tests_transversales}")
        print(f"JSON validados: {json_validados}")
        print("Resultado final: validacion global correcta.")
        return 0
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return 1
    except json.JSONDecodeError as error:
        print(f"Error: JSON invalido. Detalle: {error}")
        return 1
    except RuntimeError as error:
        print(f"Error: {error}")
        return 1
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
