import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SCRIPT = RAIZ / "scripts" / "ejecutar_agente.py"


def ejecutar_comando(*argumentos: str) -> subprocess.CompletedProcess[str]:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, str(SCRIPT), *argumentos],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=entorno,
        check=False,
    )


class TestEjecutarAgente(unittest.TestCase):
    def test_ejecutar_agente_01_por_argumento(self) -> None:
        resultado = ejecutar_comando("--agente", "1")
        self.assertEqual(resultado.returncode, 0)
        self.assertIn("Agente 01", resultado.stdout)

    def test_ejecutar_agente_10_por_argumento(self) -> None:
        resultado = ejecutar_comando("--agente", "10")
        self.assertEqual(resultado.returncode, 0)
        self.assertIn("Agente 10", resultado.stdout)

    def test_error_agente_invalido(self) -> None:
        resultado = ejecutar_comando("--agente", "99")
        self.assertEqual(resultado.returncode, 1)
        salida = resultado.stdout + resultado.stderr
        self.assertIn("Opcion invalida", salida)

    def test_mostrar_ayuda(self) -> None:
        resultado = ejecutar_comando("--help")
        self.assertEqual(resultado.returncode, 0)
        self.assertIn("--agente", resultado.stdout)

    def test_guardar_historico_agente_01(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resultado = ejecutar_comando(
                "--agente",
                "1",
                "--guardar-historico",
                "--directorio-salidas",
                tmp,
            )
            self.assertEqual(resultado.returncode, 0, resultado.stdout + resultado.stderr)
            base = Path(tmp) / "agente-01"
            self.assertTrue((base / "informe.txt").is_file())
            carpeta_historico = base / "historico"
            self.assertTrue(carpeta_historico.is_dir())
            self.assertTrue(any(carpeta_historico.glob("*-informe.txt")))

    def test_guardar_historico_todos(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            resultado = ejecutar_comando(
                "--todos",
                "--guardar-historico",
                "--directorio-salidas",
                tmp,
            )
            self.assertEqual(resultado.returncode, 0, resultado.stdout + resultado.stderr)
            self.assertTrue(any((Path(tmp) / "agente-01" / "historico").glob("*-informe.txt")))
            self.assertTrue(any((Path(tmp) / "agente-10" / "historico").glob("*-informe.txt")))


if __name__ == "__main__":
    unittest.main()
