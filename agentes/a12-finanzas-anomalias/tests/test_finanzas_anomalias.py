import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
SRC = BASE / "src"


def _load_module(module_name: str, file_name: str):
    spec = importlib.util.spec_from_file_location(module_name, SRC / file_name)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar modulo {module_name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


try:
    data_generator = _load_module("a12_data_generator", "data_generator.py")
    fraud_detector = _load_module("a12_fraud_detector", "fraud_detector.py")
    DEPENDENCIES_OK = True
except Exception:
    DEPENDENCIES_OK = False


@unittest.skipUnless(DEPENDENCIES_OK, "Dependencias de a12 no disponibles en este entorno")
class TestFinanzasAnomalias(unittest.TestCase):
    def test_generate_transactions_shape(self) -> None:
        with redirect_stdout(io.StringIO()):
            df = data_generator.generate_synthetic_transactions(n_transactions=80, fraud_rate=0.1)
        self.assertEqual(len(df), 80)
        self.assertIn("transaction_id", df.columns)
        self.assertIn("is_fraud", df.columns)

    def test_detector_predict_includes_expected_fields(self) -> None:
        with redirect_stdout(io.StringIO()):
            df = data_generator.generate_synthetic_transactions(n_transactions=120, fraud_rate=0.05)
            detector = fraud_detector.FraudDetector(contamination=0.05)
            detector.train(df)
            result = detector.predict(df)
        self.assertIn("prediction", result.columns)
        self.assertIn("anomaly_score", result.columns)
        self.assertIn("confidence", result.columns)

    def test_model_load_rejects_paths_outside_trusted_models_dir(self) -> None:
        with self.assertRaises(ValueError):
            fraud_detector.resolve_trusted_model_path(BASE.parent / "modelo_externo.pkl")

    def test_model_load_rejects_non_pickle_extension(self) -> None:
        with self.assertRaises(ValueError):
            fraud_detector.resolve_trusted_model_path(BASE / "models" / "modelo.json")
