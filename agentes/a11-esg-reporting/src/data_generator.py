"""Generador de datos sintéticos ESG para PYMES."""

import random

import pandas as pd
from faker import Faker

fake = Faker("es_ES")


def generate_esg_data(n_companies: int = 10) -> pd.DataFrame:
    print(f"🌱 Generando datos ESG para {n_companies} PYMES sintéticas...")
    companies = []
    sectors = ["manufactura", "tecnologia", "logistica", "retail", "servicios"]

    for i in range(n_companies):
        sector = random.choice(sectors)
        employees = random.randint(20, 250)
        revenue = random.uniform(500000, 5000000)

        # Métricas ambientales
        energy_kwh = random.uniform(employees * 1500, employees * 4000)
        co2_tonnes = energy_kwh * random.uniform(0.0002, 0.0006)

        # Métricas sociales
        diversity_pct = random.uniform(25, 65)
        training_hours = random.uniform(10, 40)
        local_suppliers_pct = random.uniform(30, 90)

        companies.append(
            {
                "company_id": f"PYME-{i + 1:03d}",
                "name": fake.company(),
                "sector": sector,
                "employees": employees,
                "revenue_eur": round(revenue, 2),
                "energy_kwh": round(energy_kwh, 2),
                "co2_tonnes": round(co2_tonnes, 4),
                "diversity_pct": round(diversity_pct, 2),
                "training_hours": round(training_hours, 2),
                "local_suppliers_pct": round(local_suppliers_pct, 2),
                "csrd_compliant": random.choice([True, False]),
            }
        )

    df = pd.DataFrame(companies)
    print(f"✅ Generadas {len(df)} empresas")
    print(f"   - Sector más común: {df['sector'].mode()[0]}")
    print(f"   - CO2 promedio: {df['co2_tonnes'].mean():.4f} t")
    return df


if __name__ == "__main__":
    df = generate_esg_data()
    df.to_csv("data/synthetic/esg_demo.csv", index=False)
    print("💾 Guardado en: data/synthetic/esg_demo.csv")
