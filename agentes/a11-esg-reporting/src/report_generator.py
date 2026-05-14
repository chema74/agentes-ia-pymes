"""Generador de informes ESG con trazabilidad."""

import hashlib
from datetime import datetime

import pandas as pd
from jinja2 import Template

TEMPLATE = """
# 🌱 Informe ESG Sintético - {{ company_name }}

**Fecha generación:** {{ date }}  
**ID Auditoría:** {{ audit_id }}  
**Sector:** {{ sector }} | **Empleados:** {{ employees }}

---

## 📊 Métricas Clave

| Métrica | Valor | Umbral CSRD | Estado |
|---------|-------|-------------|--------|
| Intensidad CO₂ | {{ carbon_intensity }} t/€M | < 0.0005 | {{ '✅' if carbon_intensity < 0.0005 else '⚠️' }} |
| Eficiencia Energética | {{ energy_efficiency }} €/kWh | > 100 | {{ '✅' if energy_efficiency > 100 else '⚠️' }} |
| Diversidad | {{ diversity_pct }}% | > 40% | {{ '✅' if diversity_pct > 40 else '⚠️' }} |
| Formación | {{ training_hours }}h | > 20h | {{ '✅' if training_hours > 20 else '️' }} |
| Proveedores Locales | {{ local_suppliers_pct }}% | > 50% | {{ '✅' if local_suppliers_pct > 50 else '⚠️' }} |

## 🏆 Puntuación ESG: **{{ esg_grade }}**
- Puntuación Social: {{ social_score }}/100
- Cumplimiento CSRD: {{ '✅ Sí' if csrd_compliant else '❌ No' }}

## 🚩 Hallazgos y Recomendaciones
{% for flag in flags %}
- {{ flag }}
{% endfor %}

---
*Informe generado automáticamente por Agente ESG | Trazabilidad: {{ audit_id }}*
"""


class ReportGenerator:
    def __init__(self):
        self.template = Template(TEMPLATE)

    def generate_company_report(self, row: pd.Series) -> str:
        audit_id = hashlib.sha256(
            f"{row['company_id']}-{datetime.now().isoformat()}".encode()
        ).hexdigest()[:8]

        return self.template.render(
            company_name=row["name"],
            date=datetime.now().strftime("%Y-%m-%d"),
            audit_id=audit_id,
            sector=row["sector"],
            employees=row["employees"],
            carbon_intensity=f"{row['carbon_intensity']:.6f}",
            energy_efficiency=f"{row['energy_efficiency']:.2f}",
            diversity_pct=row["diversity_pct"],
            training_hours=row["training_hours"],
            local_suppliers_pct=row["local_suppliers_pct"],
            esg_grade=row["esg_grade"],
            social_score=f"{row['social_score']:.1f}",
            csrd_compliant=row["csrd_compliant"],
            flags=row["flags"],
        )

    def generate_summary_report(self, df: pd.DataFrame) -> str:
        summary = f"# 📈 Resumen Ejecutivo ESG\n\n**Total empresas analizadas:** {len(df)}\n"
        summary += f"**Distribución de notas:** {df['esg_grade'].value_counts().to_dict()}\n"
        summary += f"**Cumplimiento CSRD:** {df['csrd_compliant'].sum()}/{len(df)} ({df['csrd_compliant'].mean() * 100:.1f}%)\n\n"
        summary += "### 🏆 Top 3 Empresas (Nota ESG)\n"
        for _, row in df.nlargest(3, "social_score").iterrows():
            summary += f"- **{row['name']}** ({row['sector']}): Nota {row['esg_grade']} | Social {row['social_score']:.1f}/100\n"
        return summary
