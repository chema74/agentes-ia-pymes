from __future__ import annotations

import argparse
from datetime import datetime
import html
import os
from pathlib import Path
import subprocess
import sys

AGENTES = [
    (1, "Agente 01 - Onboarding Inteligente"),
    (2, "Agente 02 - Documental Inteligente"),
    (3, "Agente 03 - Seguimiento de Clientes"),
    (4, "Agente 04 - Generador de Propuestas"),
    (5, "Agente 05 - Operaciones para PYMES"),
    (6, "Agente 06 - Control de Cobros y Flujo de Caja"),
    (7, "Agente 07 - Pipeline Comercial"),
    (8, "Agente 08 - Formacion Interna"),
    (9, "Agente 09 - Analisis de Mercado"),
    (10, "Agente 10 - Revision y Cumplimiento"),
]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Genera un panel HTML local y estatico a partir de informes de agentes."
    )
    parser.add_argument(
        "--directorio-salidas",
        default="salidas",
        help="Directorio donde se leen informes y se guarda el panel (por defecto: salidas).",
    )
    parser.add_argument(
        "--generar-informes",
        action="store_true",
        help="Si se indica, genera informes antes de construir el panel.",
    )
    return parser


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def ejecutar_lanzador_todos(directorio_salidas: Path, raiz: Path) -> subprocess.CompletedProcess[str]:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    comando = [
        sys.executable,
        str(raiz / "scripts" / "ejecutar_agente.py"),
        "--todos",
        "--guardar-salida",
        "--directorio-salidas",
        str(directorio_salidas),
    ]
    return subprocess.run(
        comando,
        cwd=raiz,
        text=True,
        capture_output=True,
        check=False,
        encoding="utf-8",
        errors="replace",
        env=entorno,
    )


def ejecutar_lanzador_individual(numero: int, raiz: Path) -> subprocess.CompletedProcess[str]:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    comando = [
        sys.executable,
        str(raiz / "scripts" / "ejecutar_agente.py"),
        "--agente",
        str(numero),
    ]
    return subprocess.run(
        comando,
        cwd=raiz,
        text=True,
        capture_output=True,
        check=False,
        encoding="utf-8",
        errors="replace",
        env=entorno,
    )


def generar_informes_con_lanzador(directorio_salidas: Path, raiz: Path) -> int:
    directorio_salidas.mkdir(parents=True, exist_ok=True)

    resultado_todos = ejecutar_lanzador_todos(directorio_salidas, raiz)
    if resultado_todos.returncode == 0:
        return 0

    # Compatibilidad: si el lanzador aun no soporta --todos/--guardar-salida,
    # generamos informes ejecutando cada agente por separado con el lanzador comun.
    salida_error = (resultado_todos.stdout or "") + (resultado_todos.stderr or "")
    if "--todos" not in salida_error and "argument" not in salida_error.lower():
        return 1

    for numero, _nombre in AGENTES:
        resultado = ejecutar_lanzador_individual(numero, raiz)
        if resultado.returncode != 0:
            print(f"Error al ejecutar el agente {numero:02d}.")
            return 1

        carpeta_agente = directorio_salidas / f"agente-{numero:02d}"
        carpeta_agente.mkdir(parents=True, exist_ok=True)
        informe = carpeta_agente / "informe.txt"
        contenido = (resultado.stdout or "").strip()
        if not contenido:
            contenido = "No se recibio salida del lanzador para este agente."
        informe.write_text(contenido + "\n", encoding="utf-8")

    return 0


def extraer_valor_por_prefijo(texto: str, prefijos: list[str]) -> str:
    for linea in texto.splitlines():
        linea_limpia = linea.strip()
        for prefijo in prefijos:
            if linea_limpia.lower().startswith(prefijo.lower()):
                _, _, resto = linea_limpia.partition(":")
                valor = resto.strip()
                if valor:
                    return valor
    return "No identificado en el informe."


def construir_tarjeta_html(numero: int, nombre: str, informe_ruta: Path, base: Path) -> tuple[str, bool]:
    existe = informe_ruta.is_file()
    ruta_relativa = informe_ruta.relative_to(base) if informe_ruta.is_absolute() else informe_ruta

    if not existe:
        cuerpo = "Informe no encontrado. Pendiente de generar."
        decision = "Pendiente"
        aviso = "No hay informe disponible para este agente."
        clase = "faltante"
    else:
        contenido = informe_ruta.read_text(encoding="utf-8", errors="replace")
        cuerpo = contenido.strip() or "Informe vacio."
        decision = extraer_valor_por_prefijo(
            cuerpo,
            ["decision humana recomendada", "decision recomendada", "decision"],
        )
        aviso = extraer_valor_por_prefijo(cuerpo, ["aviso", "limite", "limitacion", "riesgo"])
        clase = "ok"

    return (
        f"""
        <article class="tarjeta {clase}">
          <h2>{html.escape(nombre)}</h2>
          <p><strong>Estado:</strong> {"Informe encontrado" if existe else "Informe faltante"}</p>
          <p><strong>Ruta informe:</strong> <code>{html.escape(str(ruta_relativa))}</code></p>
          <p><strong>Decision humana recomendada:</strong> {html.escape(decision)}</p>
          <p><strong>Aviso o limite:</strong> {html.escape(aviso)}</p>
          <details>
            <summary>Ver contenido del informe</summary>
            <pre>{html.escape(cuerpo)}</pre>
          </details>
        </article>
        """.strip(),
        existe,
    )


def construir_html(directorio_salidas: Path) -> tuple[str, int]:
    tarjetas = []
    encontrados = 0

    for numero, nombre in AGENTES:
        informe = directorio_salidas / f"agente-{numero:02d}" / "informe.txt"
        tarjeta, existe = construir_tarjeta_html(numero, nombre, informe, directorio_salidas)
        if existe:
            encontrados += 1
        tarjetas.append(tarjeta)

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resumen = f"Informes encontrados: {encontrados} de {len(AGENTES)}"
    tarjetas_html = "\n".join(tarjetas)

    documento = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Panel local de agentes PYME</title>
  <style>
    :root {{
      --fondo: #f4f6f8;
      --texto: #1f2937;
      --tarjeta: #ffffff;
      --borde: #d1d5db;
      --ok: #0f766e;
      --faltante: #b45309;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Segoe UI", Tahoma, Arial, sans-serif;
      color: var(--texto);
      background: linear-gradient(180deg, #eef2f7, var(--fondo));
    }}
    .contenedor {{ max-width: 1100px; margin: 0 auto; padding: 24px; }}
    header {{
      background: var(--tarjeta);
      border: 1px solid var(--borde);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 18px;
    }}
    h1 {{ margin: 0 0 8px; font-size: 1.6rem; }}
    .meta {{ margin: 2px 0; color: #374151; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
    }}
    .tarjeta {{
      background: var(--tarjeta);
      border: 1px solid var(--borde);
      border-radius: 12px;
      padding: 14px;
    }}
    .tarjeta.ok {{ border-left: 6px solid var(--ok); }}
    .tarjeta.faltante {{ border-left: 6px solid var(--faltante); }}
    h2 {{ margin-top: 0; font-size: 1.05rem; }}
    p {{ margin: 8px 0; }}
    pre {{
      margin: 8px 0 0;
      padding: 10px;
      border-radius: 8px;
      background: #f8fafc;
      border: 1px solid #e5e7eb;
      overflow-x: auto;
      white-space: pre-wrap;
      word-break: break-word;
    }}
    code {{ background: #f3f4f6; padding: 1px 4px; border-radius: 4px; }}
  </style>
</head>
<body>
  <main class="contenedor">
    <header>
      <h1>Panel local de informes de agentes</h1>
      <p class="meta"><strong>Generado:</strong> {html.escape(fecha)}</p>
      <p class="meta"><strong>Resumen:</strong> {html.escape(resumen)}</p>
      <p class="meta"><strong>Alcance:</strong> Panel local estatico para revision manual. No es un dashboard productivo.</p>
    </header>
    <section class="grid">
      {tarjetas_html}
    </section>
  </main>
</body>
</html>
"""
    return documento, encontrados


def main(argv: list[str] | None = None) -> int:
    parser = construir_parser()
    args = parser.parse_args(argv)

    try:
        raiz = obtener_raiz_repositorio()
        directorio_salidas = Path(args.directorio_salidas)
        if not directorio_salidas.is_absolute():
            directorio_salidas = raiz / directorio_salidas

        if args.generar_informes:
            resultado = generar_informes_con_lanzador(directorio_salidas, raiz)
            if resultado != 0:
                print("Error: no se pudieron generar los informes con el lanzador comun.")
                return 1

        directorio_salidas.mkdir(parents=True, exist_ok=True)
        html_panel, encontrados = construir_html(directorio_salidas)
        ruta_panel = directorio_salidas / "panel_local.html"
        ruta_panel.write_text(html_panel, encoding="utf-8")

        print(f"Directorio de salidas usado: {directorio_salidas}")
        print(f"Informes encontrados: {encontrados} de {len(AGENTES)}")
        print(f"Panel generado: {ruta_panel}")
        print("Aviso: este panel es local y estatico; no es un dashboard productivo.")
        return 0
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
