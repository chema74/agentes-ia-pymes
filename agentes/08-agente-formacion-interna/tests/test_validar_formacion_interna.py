from pathlib import Path
import os
import subprocess
import sys
import unittest


RAIZ_REPOSITORIO = Path(__file__).resolve().parents[3]
SCRIPT = (
    RAIZ_REPOSITORIO
    / "agentes"
    / "08-agente-formacion-interna"
    / "src"
    / "validar_formacion_interna.py"
)
JSON_FICTICIO = (
    RAIZ_REPOSITORIO
    / "agentes"
    / "08-agente-formacion-interna"
    / "datos_ejemplo"
    / "formacion_interna_ficticia.json"
)
JSON_INCOMPLETO = (
    RAIZ_REPOSITORIO
    / "agentes"
    / "08-agente-formacion-interna"
    / "tests"
    / "datos_prueba"
    / "formacion_incompleta.json"
)


def ejecutar_script(*argumentos):
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [sys.executable, str(SCRIPT), *[str(argumento) for argumento in argumentos]],
        cwd=RAIZ_REPOSITORIO,
        env=entorno,
        text=True,
        capture_output=True,
        check=False,
    )


class ValidarFormacionInternaTests(unittest.TestCase):
    def test_ejecucion_sin_argumentos(self):
        resultado = ejecutar_script()

        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Informe de validacion de formacion interna", resultado.stdout)
        self.assertIn("no certifica competencias", resultado.stdout.lower())
        self.assertIn("Decision humana recomendada", resultado.stdout)

    def test_ejecucion_con_ruta_explicita(self):
        resultado = ejecutar_script(JSON_FICTICIO)

        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Ruta analizada", resultado.stdout)
        self.assertIn("Numero total de rutas, modulos o registros formativos", resultado.stdout)

    def test_error_archivo_inexistente(self):
        resultado = ejecutar_script(RAIZ_REPOSITORIO / "ruta" / "inexistente.json")
        salida = resultado.stdout + resultado.stderr

        self.assertEqual(resultado.returncode, 1)
        self.assertIn("archivo no encontrado", salida.lower())

    def test_error_json_incompleto(self):
        resultado = ejecutar_script(JSON_INCOMPLETO)
        salida = resultado.stdout + resultado.stderr

        self.assertEqual(resultado.returncode, 1)
        self.assertIn("estructura incompleta", salida.lower())


if __name__ == "__main__":
    unittest.main()
