from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_step(name: str, command: list[str], cwd: Path) -> int:
    print(f"\n==> {name}")
    print("$", " ".join(command))
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False)
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip())
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Pipeline local de calidad para agentes-ia-pymes")
    parser.add_argument("--sin-mypy", action="store_true", help="Omite comprobacion de mypy")
    parser.add_argument("--sin-cobertura", action="store_true", help="Omite pytest con cobertura")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]

    steps = [
        ("Verificacion UTF-8", [sys.executable, "scripts/verificar_utf8.py"]),
        ("Contrato de agentes", [sys.executable, "scripts/validar_contrato_agentes.py"]),
        ("Validacion global", [sys.executable, "scripts/validar_repositorio.py"]),
    ]

    if not args.sin_mypy:
        steps.append(("Mypy (scripts/tests/agentes)", [sys.executable, "scripts/verificar_tipos.py"]))

    if args.sin_cobertura:
        steps.append(("Pytest", [sys.executable, "-m", "pytest", "-q"]))
    else:
        steps.append(
            (
                "Pytest con cobertura",
                [
                    sys.executable,
                    "-m",
                    "pytest",
                    "-q",
                    "--cov=scripts",
                    "--cov=tests",
                    "--cov=agentes",
                    "--cov-report=term-missing",
                ],
            )
        )

    failed = False
    for name, cmd in steps:
        code = run_step(name, cmd, root)
        if code != 0:
            failed = True
            break

    if failed:
        print("\nResultado: fallaron comprobaciones de calidad.")
        return 1

    print("\nResultado: calidad local correcta.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
