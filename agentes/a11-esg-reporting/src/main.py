"""CLI principal del agente ESG."""

import argparse
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).parent))

from data_generator import generate_esg_data
from esg_calculator import ESGCalculator
from report_generator import ReportGenerator


def safe_filename(value: object) -> str:
    """Convierte un identificador externo en un nombre de archivo local seguro."""
    name = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(value)).strip("._")
    return name or "empresa"


def safe_output_path(output_dir: Path, filename: str) -> Path:
    base = output_dir.resolve()
    path = (base / filename).resolve()
    if not path.is_relative_to(base):
        raise ValueError(f"Ruta de salida fuera del directorio permitido: {filename}")
    return path


def main():
    parser = argparse.ArgumentParser(description="Agente de Reporting ESG para PYMES")
    parser.add_argument("--demo", action="store_true", help="Ejecutar demo con datos sintéticos")
    parser.add_argument("--input", type=str, help="CSV de entrada")
    parser.add_argument("--output-dir", type=str, default="reports", help="Carpeta de salida")

    args = parser.parse_args()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("🌱 Agente de Reporting ESG - PYMES")
    print("=" * 50)

    # 1. Datos
    if args.demo:
        df = generate_esg_data()
    elif args.input:
        df = pd.read_csv(args.input)
    else:
        print("❌ Usa --demo o --input <archivo.csv>")
        return

    # 2. Cálculos
    calc = ESGCalculator()
    results = calc.calculate(df)

    # 3. Informes
    reporter = ReportGenerator()
    print("\n📄 Generando informes individuales...")
    for _, row in results.iterrows():
        report = reporter.generate_company_report(row)
        filename = f"{safe_filename(row['company_id'])}_esg_report.md"
        safe_output_path(output_dir, filename).write_text(report, encoding="utf-8")

    # 4. Resumen ejecutivo
    summary = reporter.generate_summary_report(results)
    summary_path = safe_output_path(output_dir, "esg_executive_summary.md")
    summary_path.write_text(summary, encoding="utf-8")

    print(f"\n✅ Informes generados en: {args.output_dir}/")
    print(f"📊 Resumen ejecutivo: {summary_path}")


if __name__ == "__main__":
    main()
