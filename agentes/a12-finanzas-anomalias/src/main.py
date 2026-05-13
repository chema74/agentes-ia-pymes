"""CLI principal del agente de detección de fraude."""
import sys
import argparse
import pandas as pd
from pathlib import Path

# Asegurar que Python encuentre los módulos en src/
sys.path.append(str(Path(__file__).parent))

from data_generator import generate_synthetic_transactions
from fraud_detector import FraudDetector
from explainer import FraudExplainer

def main():
    parser = argparse.ArgumentParser(description="Agente de Detección de Fraude para PYMES")
    parser.add_argument('--demo', action='store_true', help='Ejecutar demo con datos sintéticos')
    parser.add_argument('--input', type=str, help='Archivo CSV de entrada')
    parser.add_argument('--output', type=str, default='demo/results.json', help='Archivo de salida')
    parser.add_argument('--train', action='store_true', help='Entrenar nuevo modelo')
    parser.add_argument('--model', type=str, default='models/fraud_detector.pkl', help='Ruta del modelo')
    
    args = parser.parse_args()
    
    print("💰 Agente de Detección de Fraude - PYMES")
    print("=" * 50)
    
    # 1. Generar o cargar datos
    if args.demo:
        print("\n📊 Modo DEMO: Generando datos sintéticos...")
        df = generate_synthetic_transactions(n_transactions=100, fraud_rate=0.05)
    elif args.input:
        print(f"\n📂 Cargando datos desde: {args.input}")
        df = pd.read_csv(args.input)
    else:
        print("❌ Error: Especifica --demo o --input <archivo.csv>")
        return
    
    # 2. Entrenar o cargar modelo
    model_path = Path(args.model)
    if args.train:
        print("\n🔧 Entrenando modelo...")
        detector = FraudDetector(contamination=0.02)
        detector.train(df)
        detector.save(args.model)
    elif model_path.exists():
        detector = FraudDetector.load(args.model)
    else:
        print("⚠️ Modelo no encontrado. Entrenando modelo temporal...")
        detector = FraudDetector(contamination=0.02)
        detector.train(df)
    
    # 3. Predecir y explicar
    print("\n🔍 Analizando transacciones...")
    results = detector.predict(df)
    explainer = FraudExplainer()
    
    alerts = results[results['prediction'] == 1]
    
    print(f"\n📈 Resultados:")
    print(f"   - Total analizadas: {len(results)}")
    print(f"   - Alertas generadas: {len(alerts)}")
    print(f"   - Tasa de alerta: {len(alerts)/len(results)*100:.1f}%")
    
    if len(alerts) > 0:
        print(f"\n🚨 Top 3 alertas:")
        for idx, alert in alerts.nlargest(3, 'confidence').iterrows():
            explanation = explainer.explain_transaction(alert)
            print(f"   • {alert['transaction_id']}: €{alert['amount']:.2f} - {explanation['explanation']}")
    
    # 4. Guardar resultados
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    results.to_json(args.output, orient='records', indent=2)
    print(f"\n💾 Resultados guardados en: {args.output}")
    
    if len(alerts) > 0:
        report = explainer.generate_report(alerts)
        report_path = output_path.parent / 'informe.md'
        report_path.write_text(report, encoding='utf-8')
        print(f"📄 Informe generado en: {report_path}")

if __name__ == "__main__":
    main()