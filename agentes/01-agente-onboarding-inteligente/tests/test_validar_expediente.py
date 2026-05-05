from pathlib import Path
import os
import subprocess
import sys
import unittest


class PruebaValidarExpediente(unittest.TestCase):
    """Comprueba la ejecucion real del script desde consola."""

    def setUp(self):
        """Prepara rutas compartidas para las pruebas."""
        self.raiz_repositorio = Path(__file__).resolve().parents[3]
        self.ruta_agente = self.raiz_repositorio / "agentes" / "01-agente-onboarding-inteligente"
        self.ruta_script = self.ruta_agente / "src" / "validar_expediente.py"
        self.ruta_json = self.ruta_agente / "datos_ejemplo" / "cliente_onboarding_ficticio.json"

    def ejecutar_script(self, argumentos=None):
        """Ejecuta el script como lo haria una persona desde consola."""
        entorno = os.environ.copy()
        # Se fuerza PYTHONIOENCODING para evitar problemas de codificacion al capturar salida en Windows.
        entorno["PYTHONIOENCODING"] = "utf-8"
        comando = [sys.executable, str(self.ruta_script)]

        if argumentos:
            comando.extend(str(argumento) for argumento in argumentos)

        return subprocess.run(
            comando,
            cwd=self.raiz_repositorio,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=entorno,
            check=False,
        )

    def comprobar_salida_basica(self, resultado):
        """Comprueba el resultado minimo esperado del expediente ficticio."""
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
            "Decision recomendada de revision manual: bloquear",
        ]

        for texto in textos_esperados:
            self.assertIn(texto, salida)

    def test_informe_basico_sin_argumentos(self):
        """Valida que el script usa el JSON ficticio por defecto."""
        resultado = self.ejecutar_script()
        self.comprobar_salida_basica(resultado)

    def test_informe_basico_con_ruta_json_explicita(self):
        """Valida que el script acepta una ruta JSON por parametro."""
        resultado = self.ejecutar_script([self.ruta_json])
        self.comprobar_salida_basica(resultado)


if __name__ == "__main__":
    unittest.main()
