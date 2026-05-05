from pathlib import Path
import os
import subprocess
import sys
import unittest


class PruebaValidarExpediente(unittest.TestCase):
    """Comprueba la ejecucion real del script desde consola."""

    def test_informe_basico_con_datos_ficticios(self):
        """Valida la salida minima esperada para la V1 local."""
        raiz_repositorio = Path(__file__).resolve().parents[3]
        ruta_script = (
            raiz_repositorio
            / "agentes"
            / "01-agente-onboarding-inteligente"
            / "src"
            / "validar_expediente.py"
        )
        entorno = os.environ.copy()
        # Se fuerza PYTHONIOENCODING para evitar problemas de codificacion al capturar salida en Windows.
        entorno["PYTHONIOENCODING"] = "utf-8"

        resultado = subprocess.run(
            [sys.executable, str(ruta_script)],
            cwd=raiz_repositorio,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=entorno,
            check=False,
        )

        salida = resultado.stdout or ""
        error = resultado.stderr or ""

        self.assertEqual(
            resultado.returncode,
            0,
            msg=f"El script termino con error: {error}",
        )

        textos_esperados = [
            "INFORME DE VALIDACION DEL EXPEDIENTE",
            "Laura Martín",
            "Taller Creativo Bahía, S. L.",
            "Estado del onboarding: en_revision",
            "Documentos recibidos: 1",
            "Documentos pendientes: 1",
            "Documentos incompletos: 1",
            "Items completos: 7",
            "Items obligatorios pendientes: 2",
            "Items bloqueados: 2",
            "Decision recomendada de revision manual: bloquear",
        ]

        for texto in textos_esperados:
            self.assertIn(texto, salida)


if __name__ == "__main__":
    unittest.main()
