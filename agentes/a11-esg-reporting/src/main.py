"""CLI principal del agente ESG."""
import sys
import argparse
import pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from data_generator import generate_esg_data
from esg_calculator import ESGCalculator
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Agente de Reporting ESG para PYMES")
    parser.add_argument('--demo', action='store_true', help='Ejecutar demo con datos sintéticos')
    parser.add_argument('--input', type=str, help='CSV de entrada')
    parser.add_argument('--output-dir', type=str, default='reports', help='Carpeta de salida')
    
    args = parser.parse_args()
    Path(args.output_dir).mkdir(exist_ok=True)
    
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
        filename = f"{args.output_dir}/{row['company_id']}_esg_report.md"
        Path(filename).write_text(report, encoding='utf-8')
    
    # 4. Resumen ejecutivo
    summary = reporter.generate_summary_report(results)
    summary_path = f"{args.output_dir}/esg_executive_summary.md"
    Path(summary_path).write_text(summary, encoding='utf-8')
    
    print(f"\n✅ Informes generados en: {args.output_dir}/")
    print(f"📊 Resumen ejecutivo: {summary_path}")

if __name__ == "__main__":
    main()
