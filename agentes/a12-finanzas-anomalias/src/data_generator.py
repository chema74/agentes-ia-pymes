"""Generador de transacciones financieras sintéticas para demo."""

import random
from datetime import datetime, timedelta
from typing import Any

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker("es_ES")


def generate_synthetic_transactions(
    n_transactions: int = 1000, fraud_rate: float = 0.02
) -> pd.DataFrame:
    """
    Genera transacciones sintéticas con patrones de fraude inyectados.

    Args:
        n_transactions: Número de transacciones a generar
        fraud_rate: Proporción de transacciones fraudulentas (default 2%)

    Returns:
        DataFrame con transacciones sintéticas
    """
    print(f"📊 Generando {n_transactions} transacciones sintéticas...")

    transactions = []
    base_date = datetime.now() - timedelta(days=90)

    # Usuarios base con comportamiento normal
    n_users = 50
    users: list[dict[str, Any]] = [
        {
            "user_id": i,
            "avg_amount": random.uniform(20, 200),
            "std_amount": random.uniform(10, 50),
            "preferred_categories": random.sample(
                ["supermarket", "restaurant", "gas_station", "online_shopping", "utilities"], k=2
            ),
            "location": fake.city(),
        }
        for i in range(n_users)
    ]

    for i in range(n_transactions):
        user = random.choice(users)
        is_fraud = random.random() < fraud_rate

        if is_fraud:
            # Patrón fraudulento
            amount = user["avg_amount"] * random.uniform(5, 15)  # Monto anómalo
            category = random.choice(["wire_transfer", "cryptocurrency", "gambling", "luxury"])
            location = fake.country()  # Ubicación inusual
            risk_score = round(random.uniform(0.7, 0.95), 2)
        else:
            # Comportamiento normal
            amount = max(5, np.random.normal(user["avg_amount"], user["std_amount"]))
            category = random.choice(user["preferred_categories"])
            location = user["location"]
            risk_score = round(random.uniform(0.05, 0.3), 2)

        transaction = {
            "transaction_id": f"TXN-{i + 1:06d}",
            "user_id": user["user_id"],
            "timestamp": base_date
            + timedelta(
                days=random.randint(0, 90),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59),
            ),
            "amount": round(amount, 2),
            "merchant_category": category,
            "merchant_name": fake.company(),
            "location": location,
            "payment_method": random.choice(["credit_card", "debit_card", "transfer"]),
            "user_risk_score": risk_score,
            "is_fraud": is_fraud,  # Ground truth (solo para evaluación)
        }
        transactions.append(transaction)

    df = pd.DataFrame(transactions)
    print(f"✅ Generadas {len(df)} transacciones")
    print(f"   - Fraudulentas: {df['is_fraud'].sum()} ({df['is_fraud'].mean() * 100:.1f}%)")
    print(f"   - Monto promedio: €{df['amount'].mean():.2f}")
    print(f"   - Rango: €{df['amount'].min():.2f} - €{df['amount'].max():.2f}")

    return df


if __name__ == "__main__":
    # Generar y guardar
    df = generate_synthetic_transactions(n_transactions=1000, fraud_rate=0.02)
    df.to_csv("data/synthetic/transactions_demo.csv", index=False)
    print("💾 Guardado en: data/synthetic/transactions_demo.csv")
