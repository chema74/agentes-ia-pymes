"""Detector de anomalías financieras con Isolation Forest."""

import os
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

TRUSTED_MODEL_DIR = Path(__file__).resolve().parents[1] / "models"


def resolve_trusted_model_path(filepath: str | os.PathLike[str]) -> Path:
    """Limita la carga de joblib a modelos locales controlados por el agente."""
    path = Path(filepath).expanduser().resolve()
    trusted_dir = TRUSTED_MODEL_DIR.resolve()
    if path.suffix != ".pkl":
        raise ValueError("Solo se permite cargar modelos con extension .pkl.")
    if not path.is_relative_to(trusted_dir):
        raise ValueError(f"Modelo no confiable fuera de {trusted_dir}: {path}")
    return path


class FraudDetector:
    """Detector de fraude basado en Isolation Forest."""

    def __init__(self, contamination: float = 0.02):
        self.contamination = contamination
        self.model = IsolationForest(contamination=contamination, random_state=42, n_estimators=100)
        self.scaler = StandardScaler()
        self.feature_columns = ["amount", "user_risk_score", "hour_of_day", "day_of_week"]

    def _extract_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["hour_of_day"] = pd.to_datetime(df["timestamp"]).dt.hour
        df["day_of_week"] = pd.to_datetime(df["timestamp"]).dt.dayofweek
        return df[self.feature_columns]

    def train(self, df: pd.DataFrame):
        print("🔧 Entrenando detector de fraude...")
        features = self._extract_features(df)
        features_scaled = self.scaler.fit_transform(features)
        self.model.fit(features_scaled)
        print("✅ Modelo entrenado correctamente")

    def predict(self, df: pd.DataFrame) -> pd.DataFrame:
        features = self._extract_features(df)
        features_scaled = self.scaler.transform(features)

        predictions = self.model.predict(features_scaled)
        scores = self.model.score_samples(features_scaled)

        df_result = df.copy()
        df_result["prediction"] = (predictions == -1).astype(int)
        df_result["anomaly_score"] = -scores
        df_result["anomaly_score"] = (
            df_result["anomaly_score"] - df_result["anomaly_score"].min()
        ) / (df_result["anomaly_score"].max() - df_result["anomaly_score"].min())
        df_result["confidence"] = df_result["anomaly_score"]
        return df_result

    def save(self, filepath: str):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        joblib.dump(
            {
                "model": self.model,
                "scaler": self.scaler,
                "feature_columns": self.feature_columns,
                "contamination": self.contamination,
            },
            filepath,
        )
        print(f"💾 Modelo guardado en: {filepath}")

    @classmethod
    def load(cls, filepath: str) -> "FraudDetector":
        model_path = resolve_trusted_model_path(filepath)
        data = joblib.load(model_path)
        detector = cls(contamination=data["contamination"])
        detector.model = data["model"]
        detector.scaler = data["scaler"]
        detector.feature_columns = data["feature_columns"]
        print(f" Modelo cargado desde: {model_path}")
        return detector
