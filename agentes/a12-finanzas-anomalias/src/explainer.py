"""Módulo de explicabilidad (XAI) con lógica de negocio."""
import pandas as pd
from typing import Dict

class FraudExplainer:
    """Genera explicaciones interpretables para predicciones de fraude."""
    
    def __init__(self):
        pass
    
    def explain_transaction(self, transaction: pd.Series) -> Dict:
        """
        Explica por qué una transacción fue marcada como fraudulenta.
        """
        amount = transaction['amount']
        user_risk = transaction['user_risk_score']
        hour = pd.to_datetime(transaction['timestamp']).hour
        category = transaction['merchant_category']
        
        factors = []
        reasons = []
        
        # 1. Análisis de monto
        if amount > 500:
            factors.append(f"Monto elevado: €{amount:.2f}")
            reasons.append("high_amount")
        
        # 2. Análisis de hora
        if hour < 6 or hour > 23:
            factors.append(f"Transacción en horario inusual: {hour:02d}:00")
            reasons.append("unusual_hour")
        
        # 3. Análisis de riesgo de usuario
        if user_risk > 0.6:
            factors.append(f"Usuario con score de riesgo alto: {user_risk:.2f}")
            reasons.append("high_user_risk")
        
        # 4. Análisis de categoría
        high_risk_categories = ['wire_transfer', 'cryptocurrency', 'gambling', 'luxury']
        if category in high_risk_categories:
            factors.append(f"Categoría de alto riesgo: {category}")
            reasons.append("high_risk_category")
        
        # Generar explicación
        if not reasons:
            explanation = "Transacción dentro de parámetros normales."
            reason_code = "NORMAL"
        else:
            explanation = f"Alerta activada por: {', '.join(factors[:2])}"
            reason_code = "_".join(reasons[:3]).upper()
        
        return {
            'reason_code': reason_code,
            'explanation': explanation,
            'contributing_factors': factors,
            'risk_level': 'HIGH' if len(reasons) >= 2 else 'MEDIUM' if len(reasons) == 1 else 'LOW'
        }
    
    def generate_report(self, transactions_flagged: pd.DataFrame) -> str:
        """Genera un informe ejecutivo de transacciones flaggeadas."""
        report = ["# 🚨 Informe de Detección de Fraude\n"]
        report.append(f"**Total de transacciones analizadas:** {len(transactions_flagged)}\n")
        report.append(f"**Transacciones flaggeadas:** {transactions_flagged['prediction'].sum()}\n")
        report.append(f"**Tasa de alerta:** {transactions_flagged['prediction'].mean()*100:.2f}%\n\n")
        
        top_suspicious = transactions_flagged[transactions_flagged['prediction'] == 1].nlargest(5, 'confidence')
        
        report.append("## 🔝 Top 5 Transacciones Sospechosas\n")
        for idx, txn in top_suspicious.iterrows():
            explanation = self.explain_transaction(txn)
            report.append(f"### {txn['transaction_id']}")
            report.append(f"- **Monto:** €{txn['amount']:.2f}")
            report.append(f"- **Categoría:** {txn['merchant_category']}")
            report.append(f"- **Confianza:** {txn['confidence']*100:.1f}%")
            report.append(f"- **Razón:** {explanation['explanation']}")
            report.append("")
        
        return "\n".join(report)