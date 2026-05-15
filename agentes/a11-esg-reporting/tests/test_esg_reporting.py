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
    data_generator = _load_module("a11_data_generator", "data_generator.py")
    esg_calculator = _load_module("a11_esg_calculator", "esg_calculator.py")
    main_module = _load_module("a11_main", "main.py")
    DEPENDENCIES_OK = True
except Exception:
    DEPENDENCIES_OK = False


@unittest.skipUnless(DEPENDENCIES_OK, "Dependencias de a11 no disponibles en este entorno")
class TestESGReporting(unittest.TestCase):
    def test_generate_esg_data_shape(self) -> None:
        with redirect_stdout(io.StringIO()):
            df = data_generator.generate_esg_data(n_companies=5)
        self.assertEqual(len(df), 5)
        self.assertIn("company_id", df.columns)
        self.assertIn("co2_tonnes", df.columns)

    def test_esg_calculator_adds_expected_fields(self) -> None:
        with redirect_stdout(io.StringIO()):
            df = data_generator.generate_esg_data(n_companies=4)
            result = esg_calculator.ESGCalculator().calculate(df)
        self.assertIn("carbon_intensity", result.columns)
        self.assertIn("energy_efficiency", result.columns)
        self.assertIn("social_score", result.columns)
        self.assertIn("esg_grade", result.columns)

    def test_safe_filename_neutralizes_path_segments(self) -> None:
        filename = main_module.safe_filename("../cliente/riesgo")
        self.assertEqual(filename, "cliente_riesgo")
        self.assertNotIn("..", filename)
        self.assertNotIn("/", filename)

    def test_safe_output_path_rejects_escape(self) -> None:
        with self.assertRaises(ValueError):
            main_module.safe_output_path(BASE, "../fuera.md")
