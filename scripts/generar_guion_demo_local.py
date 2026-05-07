from __future__ import annotations

import argparse
from datetime import datetime
import html
from pathlib import Path
import sys


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Genera un guion local de demo guiada en Markdown y opcionalmente HTML."
    )
    parser.add_argument("--directorio-salidas", default="salidas")
    parser.add_argument("--generar-html", action="store_true")
    parser.add_argument("--salida-markdown", default="salidas/guion_demo_local.md")
    parser.add_argument("--salida-html", default="salidas/guion_demo_local.html")
    return parser


def resolver_ruta(valor: str, raiz: Path) -> Path:
    ruta = Path(valor)
    if not ruta.is_absolute():
        ruta = raiz / ruta
    return ruta


def estado_evidencia(ruta: Path) -> str:
    return "disponible" if ruta.is_file() else "pendiente de generar"


def construir_markdown(fecha: str, directorio_salidas: Path) -> str:
    rutas = [
        ("Panel local", directorio_salidas / "panel_local.html"),
        ("Informe consolidado Markdown", directorio_salidas / "informe_consolidado.md"),
        ("Informe consolidado HTML", directorio_salidas / "informe_consolidado.html"),
        ("Indice de evidencias HTML", directorio_salidas / "evidencias_demo" / "INDICE_EVIDENCIAS.html"),
        ("ZIP de evidencias", directorio_salidas / "evidencias_demo.zip"),
    ]
    lineas = [
        "# Guion local de demo guiada",
        "",
        f"Fecha y hora de generacion: {fecha}",
        "",
        "Aviso de limites: guion local de apoyo para demostracion tecnica. No es API productiva, no es dashboard productivo y no es publicacion web.",
        "",
        "## Objetivo de la demo",
        "Mostrar un flujo local reproducible de trabajo con 10 agentes tecnicos, salida de informes, consolidacion y evidencias para revision humana.",
        "",
        "## Preparacion previa",
        "- Confirmar entorno local Python y acceso al repositorio.",
        "- Ejecutar validacion global antes de la demo cuando sea necesario.",
        "",
        "## Comandos recomendados",
        "- `python scripts/validar_repositorio.py`",
        "- `python scripts/ejecutar_demo_local.py --crear-zip`",
        "- `python scripts/editor_espacio_trabajo.py`",
        "",
        "## Recorrido sugerido por la consola local",
        "- Abrir la consola local y revisar el resumen de agentes.",
        "- Cargar un agente, revisar datos y guardar un cambio simple de prueba.",
        "- Ejecutar agente seleccionado y revisar salida.",
        "",
        "## Qué mostrar primero",
        "- Estado inicial del resumen local de agentes.",
        "- Ruta de panel local y existencia de informes.",
        "",
        "## Qué editar como prueba",
        "- Un campo de texto no sensible en datos de trabajo de un agente.",
        "- Guardar y volver a cargar para confirmar persistencia local.",
        "",
        "## Qué ejecutar",
        "- Ejecucion de agente seleccionado.",
        "- Ejecucion completa con `python scripts/ejecutar_demo_local.py --crear-zip`.",
        "",
        "## Qué informes revisar",
        "- `salidas/agente-01/informe.txt`",
        "- `salidas/agente-10/informe.txt`",
        "- `salidas/informe_consolidado.md`",
        "",
        "## Qué comparar",
        "- Comparar ultimo informe con historico local usando el comparador disponible.",
        "",
        "## Qué evidencias abrir",
        "- `salidas/panel_local.html`",
        "- `salidas/informe_consolidado.html`",
        "- `salidas/evidencias_demo/INDICE_EVIDENCIAS.html`",
        "- `salidas/evidencias_demo.zip`",
        "",
        "## Rutas locales esperadas",
        "- `http://127.0.0.1:8765/`",
        "- `salidas/panel_local.html`",
        "- `salidas/informe_consolidado.md`",
        "- `salidas/informe_consolidado.html`",
        "- `salidas/evidencias_demo/INDICE_EVIDENCIAS.html`",
        "- `salidas/evidencias_demo.zip`",
        "",
        "## Estado actual de evidencias",
    ]
    for nombre, ruta in rutas:
        lineas.append(f"- {nombre}: `{ruta}` ({estado_evidencia(ruta)})")
    lineas.extend(
        [
            "",
            "## Cierre recomendado de la demo",
            "- Confirmar rutas generadas y archivos principales.",
            "- Recordar limites actuales y fuera de alcance productivo.",
            "",
            "Recordatorio final: no hay IA funcional, no hay API productiva, no hay dashboard productivo, no hay web publica, no hay Google Workspace y no se usan datos reales.",
        ]
    )
    return "\n".join(lineas) + "\n"


def construir_html(fecha: str, directorio_salidas: Path) -> str:
    rutas = [
        "http://127.0.0.1:8765/",
        "salidas/panel_local.html",
        "salidas/informe_consolidado.md",
        "salidas/informe_consolidado.html",
        "salidas/evidencias_demo/INDICE_EVIDENCIAS.html",
        "salidas/evidencias_demo.zip",
    ]
    bloques = [
        ("Objetivo de la demo", "Mostrar un flujo local reproducible con ejecucion, revision y evidencias."),
        ("Preparacion previa", "Validar repositorio y preparar ejecucion local antes de presentar."),
        ("Comandos recomendados", "python scripts/validar_repositorio.py\npython scripts/ejecutar_demo_local.py --crear-zip\npython scripts/editor_espacio_trabajo.py"),
        ("Recorrido sugerido", "Resumen local, edicion de prueba, ejecucion de agentes, revisiones de informes y evidencias."),
    ]
    tarjetas = []
    for titulo, contenido in bloques:
        tarjetas.append(
            f"""
            <article class="tarjeta">
              <h3>{html.escape(titulo)}</h3>
              <pre>{html.escape(contenido)}</pre>
            </article>
            """.strip()
        )
    lista_rutas = []
    for ruta in rutas:
        archivo = directorio_salidas / Path(ruta.replace("salidas/", "")) if ruta.startswith("salidas/") else None
        estado = "no disponible todavia" if archivo is not None and not archivo.is_file() else "disponible"
        lista_rutas.append(f"<li><code>{html.escape(ruta)}</code> ({html.escape(estado)})</li>")

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Guion local de demo guiada</title>
  <style>
    body{{font-family:Segoe UI,Tahoma,Arial,sans-serif;margin:0;background:#f3f5f8;color:#1f2937}}
    main{{max-width:1100px;margin:0 auto;padding:20px}}
    .card{{background:#fff;border:1px solid #d7dde7;border-radius:10px;padding:14px;margin-bottom:12px}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px}}
    .tarjeta{{border-left:6px solid #1d4ed8;background:#fff;border:1px solid #d7dde7;border-radius:10px;padding:12px}}
    pre{{white-space:pre-wrap;word-break:break-word;background:#f8fafc;border:1px solid #e5e7eb;padding:10px;border-radius:8px}}
    code{{background:#eef2f7;padding:1px 4px;border-radius:4px}}
  </style>
</head>
<body>
  <main>
    <section class="card">
      <h1>Guion local de demo guiada</h1>
      <p><strong>Fecha y hora de generacion:</strong> {html.escape(fecha)}</p>
      <p><strong>Aviso de limites:</strong> guion local de demostracion. No es API productiva, no es dashboard productivo y no es publicacion web.</p>
    </section>
    <section class="grid">
      {"".join(tarjetas)}
    </section>
    <section class="card">
      <h2>Rutas locales esperadas</h2>
      <ul>
        {"".join(lista_rutas)}
      </ul>
      <p><strong>Recordatorio:</strong> no hay IA funcional, API productiva, dashboard productivo, web publica, Google Workspace ni datos reales.</p>
    </section>
  </main>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    args_lista = list(argv) if argv is not None else sys.argv[1:]
    args = construir_parser().parse_args(args_lista)
    try:
        raiz = obtener_raiz_repositorio()
        directorio_salidas = resolver_ruta(args.directorio_salidas, raiz)
        salida_md_explicitada = any(
            arg == "--salida-markdown" or arg.startswith("--salida-markdown=") for arg in args_lista
        )
        salida_html_explicitada = any(
            arg == "--salida-html" or arg.startswith("--salida-html=") for arg in args_lista
        )
        salida_md = resolver_ruta(args.salida_markdown, raiz) if salida_md_explicitada else directorio_salidas / "guion_demo_local.md"
        salida_html = resolver_ruta(args.salida_html, raiz) if salida_html_explicitada else directorio_salidas / "guion_demo_local.html"

        directorio_salidas.mkdir(parents=True, exist_ok=True)
        salida_md.parent.mkdir(parents=True, exist_ok=True)
        if args.generar_html:
            salida_html.parent.mkdir(parents=True, exist_ok=True)

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        salida_md.write_text(construir_markdown(fecha, directorio_salidas), encoding="utf-8")
        if args.generar_html:
            salida_html.write_text(construir_html(fecha, directorio_salidas), encoding="utf-8")

        print(f"Directorio de salidas usado: {directorio_salidas}")
        print(f"Guion Markdown generado: {salida_md}")
        if args.generar_html:
            print(f"Guion HTML generado: {salida_html}")
        print("Aviso: este guion es una salida local de demostracion.")
        return 0
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
