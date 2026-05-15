from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def rutas_mypy(root: Path) -> list[list[str]]:
    rutas = [["scripts", "tests"]]
    agentes = root / "agentes"
    for src in sorted(agentes.glob("*/src")):
        rutas.append([str(src.relative_to(root))])
    return rutas


def ejecutar_mypy(root: Path, rutas: list[str]) -> int:
    comando = [sys.executable, "-m", "mypy", *rutas]
    print("$", " ".join(comando))
    resultado = subprocess.run(comando, cwd=root, text=True, check=False)
    return resultado.returncode


def main() -> int:
    root = raiz_repositorio()
    errores = 0
    for grupo in rutas_mypy(root):
        errores += ejecutar_mypy(root, grupo)
    if errores:
        print("Resultado: fallaron comprobaciones de tipos.")
        return 1
    print("Resultado: tipos correctos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
