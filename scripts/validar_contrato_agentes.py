from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

REQUIRED_FILES = ["README.md", "requirements.txt"]
REQUIRED_DIRS = ["src"]
RECOMMENDED_DIRS = ["tests", "datos_ejemplo", "docs"]


@dataclass
class AgentReport:
    name: str
    critical: list[str]
    warnings: list[str]


def inspect_agent(path: Path) -> AgentReport:
    critical: list[str] = []
    warnings: list[str] = []

    for file_name in REQUIRED_FILES:
        if not (path / file_name).is_file():
            critical.append(f"Falta archivo obligatorio: {file_name}")

    for dir_name in REQUIRED_DIRS:
        if not (path / dir_name).is_dir():
            critical.append(f"Falta directorio obligatorio: {dir_name}")

    for dir_name in RECOMMENDED_DIRS:
        if not (path / dir_name).exists():
            warnings.append(f"No existe elemento recomendado: {dir_name}")

    return AgentReport(name=path.name, critical=critical, warnings=warnings)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    agents_dir = root / "agentes"

    if not agents_dir.is_dir():
        print("Error: no existe directorio 'agentes/'.")
        return 1

    reports = [inspect_agent(path) for path in sorted(agents_dir.iterdir()) if path.is_dir()]

    critical_total = 0
    warning_total = 0

    print("Validacion de contrato tecnico de agentes")
    for report in reports:
        print(f"\n- {report.name}")
        if not report.critical and not report.warnings:
            print("  OK")
            continue
        for issue in report.critical:
            critical_total += 1
            print(f"  ERROR: {issue}")
        for warn in report.warnings:
            warning_total += 1
            print(f"  AVISO: {warn}")

    print("\nResumen contrato")
    print(f"Agentes revisados: {len(reports)}")
    print(f"Errores criticos: {critical_total}")
    print(f"Avisos: {warning_total}")

    if critical_total > 0:
        print("Resultado: contrato incumplido.")
        return 1

    print("Resultado: contrato tecnico valido.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
