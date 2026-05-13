"""Calculadora de métricas y puntuaciones ESG."""
import pandas as pd

class ESGCalculator:
    def __init__(self):
        self.thresholds = {
            'carbon_intensity_max': 0.0005,  # tCO2 / € revenue
            'diversity_min': 40.0,
            'training_min': 20.0,
            'local_suppliers_min': 50.0
        }
    
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        print(" Calculando métricas ESG...")
        result = df.copy()
        
        # Intensidad de carbono
        result['carbon_intensity'] = result['co2_tonnes'] / (result['revenue_eur'] / 1000000)
        
        # Eficiencia energética
        result['energy_efficiency'] = result['revenue_eur'] / result['energy_kwh']
        
        # Puntuación social (0-100)
        result['social_score'] = (
            (result['diversity_pct'] / 100 * 40) +
            (result['training_hours'] / 50 * 30) +
            (result['local_suppliers_pct'] / 100 * 30)
        )
        
        # Flags de cumplimiento
        result['flags'] = result.apply(self._check_flags, axis=1)
        result['esg_grade'] = result.apply(self._assign_grade, axis=1)
        
        print(f"✅ Métricas calculadas")
        print(f"   - Nota media ESG: {result['esg_grade'].map({'A':5,'B':4,'C':3,'D':2,'F':1}).mean():.2f}/5")
        return result
    
    def _check_flags(self, row) -> list:
        flags = []
        if row['carbon_intensity'] > self.thresholds['carbon_intensity_max']:
            flags.append("Alta intensidad de carbono")
        if row['diversity_pct'] < self.thresholds['diversity_min']:
            flags.append("Diversidad por debajo del umbral")
        if row['training_hours'] < self.thresholds['training_min']:
            flags.append("Formación insuficiente")
        if row['local_suppliers_pct'] < self.thresholds['local_suppliers_min']:
            flags.append("Bajo porcentaje de proveedores locales")
        return flags if flags else ["Cumplimiento base OK"]
    
    def _assign_grade(self, row) -> str:
        score = row['social_score']
        if score >= 80 and not row['csrd_compliant']: return 'B'
        if score >= 80 and row['csrd_compliant']: return 'A'
        if score >= 60: return 'C'
        if score >= 40: return 'D'
        return 'F'
