from __future__ import annotations

import argparse
from datetime import datetime
from html import escape
from pathlib import Path
import sys

RUTAS_ESPERADAS = [
    "http://127.0.0.1:8765/",
    "salidas/panel_local.html",
    "salidas/informe_consolidado.md",
    "salidas/informe_consolidado.html",
    "salidas/evidencias_demo/INDICE_EVIDENCIAS.html",
    "salidas/evidencias_demo.zip",
]

RUTAS_EVIDENCIAS = [
    ("Panel local", "salidas/panel_local.html", Path("panel_local.html")),
    ("Informe consolidado Markdown", "salidas/informe_consolidado.md", Path("informe_consolidado.md")),
    ("Informe consolidado HTML", "salidas/informe_consolidado.html", Path("informe_consolidado.html")),
    (
        "Indice de evidencias HTML",
        "salidas/evidencias_demo/INDICE_EVIDENCIAS.html",
        Path("evidencias_demo") / "INDICE_EVIDENCIAS.html",
    ),
    ("ZIP de evidencias", "salidas/evidencias_demo.zip", Path("evidencias_demo.zip")),
]


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Genera un guion local de demo guiada en Markdown y, si se solicita, en HTML."
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


def estado_evidencia(directorio_salidas: Path, ruta_relativa: Path) -> str:
    return "disponible" if (directorio_salidas / ruta_relativa).is_file() else "pendiente de generar"


def construir_resumen_evidencias(directorio_salidas: Path) -> list[str]:
    lineas = []
    for nombre, ruta_mostrada, ruta_relativa in RUTAS_EVIDENCIAS:
        estado = estado_evidencia(directorio_salidas, ruta_relativa)
        lineas.append(f"- {nombre}: `{ruta_mostrada}` ({estado})")
    return lineas


def construir_markdown(fecha: str, directorio_salidas: Path) -> str:
    lineas = [
        "# Guion local de demo guiada",
        "",
        f"Fecha y hora de generacion: {fecha}",
        "",
        "Aviso de limites: guion local de demostracion para revision humana. No es IA funcional, no es API productiva, no es dashboard productivo y no es publicacion web.",
        "",
        "## Objetivo de la demo",
        "Mostrar una demo tecnica local, manipulable, reproducible y explicable de los 10 agentes, con edicion controlada, ejecucion local, informes y evidencias revisables.",
        "",
        "## Preparacion previa",
        "- Confirmar que el repositorio esta disponible en local y que Python funciona en la terminal.",
        "- Validar el repositorio antes de la demostracion si se quiere partir de un estado comprobado.",
        "- Recordar que la demo trabaja con datos ficticios y revision humana.",
        "",
        "## Comandos recomendados",
        "- `python scripts/validar_repositorio.py`",
        "- `python scripts/ejecutar_demo_local.py --crear-zip`",
        "- `python scripts/editor_espacio_trabajo.py`",
        "",
        "## Recorrido sugerido por la consola local",
        "- Abrir `http://127.0.0.1:8765/` y revisar el resumen local de agentes.",
        "- Seleccionar un agente, cargar sus datos de trabajo y usar la edicion guiada como prueba.",
        "- Ejecutar el agente seleccionado y cargar el ultimo informe.",
        "- Consultar historico, comparador, informe consolidado, evidencias y guion desde la propia consola local.",
        "",
        "## Que mostrar primero",
        "- La consola local temporal y el resumen de los 10 agentes.",
        "- La separacion entre datos de trabajo editables y JSON originales no modificados.",
        "- La existencia de panel, informe consolidado y paquete de evidencias si ya estan generados.",
        "",
        "## Que editar como prueba",
        "- Un campo de texto simple de `espacio_trabajo/` desde la edicion guiada.",
        "- Un cambio visible y no sensible que permita volver a ejecutar el agente y comparar el resultado.",
        "",
        "## Que ejecutar",
        "- `python scripts/validar_repositorio.py` para validar JSON originales, tests por agente y tests transversales.",
        "- `python scripts/ejecutar_demo_local.py --crear-zip` para regenerar la demo local completa.",
        "- `python scripts/editor_espacio_trabajo.py` para demostrar la capa local interactiva.",
        "",
        "## Que informes revisar",
        "- `salidas/agente-01/informe.txt` como ejemplo inicial.",
        "- `salidas/agente-10/informe.txt` como ejemplo final del catalogo.",
        "- `salidas/informe_consolidado.md` y `salidas/informe_consolidado.html` para la vista global.",
        "",
        "## Que comparar",
        "- El ultimo informe de un agente frente a una entrada de `historico/` usando el comparador local.",
        "- La trazabilidad del cambio entre datos de trabajo editados y salida regenerada.",
        "",
        "## Que evidencias abrir",
        "- `salidas/panel_local.html`",
        "- `salidas/informe_consolidado.html`",
        "- `salidas/evidencias_demo/INDICE_EVIDENCIAS.html`",
        "- `salidas/evidencias_demo.zip`",
        "",
        "## Rutas locales esperadas",
    ]
    for ruta in RUTAS_ESPERADAS:
        lineas.append(f"- `{ruta}`")
    lineas.extend(
        [
            "",
            "Si la demo se ejecuta con otro directorio de salidas, estas rutas siguen siendo la referencia esperada y el prefijo debe sustituirse por el directorio indicado.",
            "",
            "## Estado actual de evidencias",
        ]
    )
    lineas.extend(construir_resumen_evidencias(directorio_salidas))
    lineas.extend(
        [
            "",
            "## Cierre recomendado de la demo",
            "- Confirmar que la demo local es reproducible con un solo comando y que genera panel, informe consolidado, evidencias y guion.",
            "- Recordar que no se tocan JSON originales y que la revision final sigue siendo humana.",
            "- Cerrar la explicacion reforzando alcance real, trazabilidad y limites actuales.",
            "",
            "Recordatorio final: no hay IA funcional, API productiva, dashboard productivo, web publica, Google Workspace, integraciones reales ni datos reales.",
        ]
    )
    return "\n".join(lineas) + "\n"


def construir_bloque_html(titulo: str, elementos: list[str]) -> str:
    items = "".join(f"<li>{escape(elemento)}</li>" for elemento in elementos)
    return (
        f'<section class="bloque">'
        f"<h2>{escape(titulo)}</h2>"
        f"<ul>{items}</ul>"
        f"</section>"
    )


def construir_html(fecha: str, directorio_salidas: Path) -> str:
    bloques = [
        (
            "Fase 1 - Contexto y limites",
            [
                "Explicar que es una demostracion tecnica local, manipulable y reproducible.",
                "Aclarar que no hay IA funcional, API productiva, dashboard productivo, web publica, Google Workspace ni datos reales.",
            ],
        ),
        (
            "Fase 2 - Preparacion previa",
            [
                "Verificar Python y repositorio local.",
                "Ejecutar python scripts/validar_repositorio.py si se quiere partir de una validacion global.",
            ],
        ),
        (
            "Fase 3 - Comandos recomendados",
            [
                "python scripts/validar_repositorio.py",
                "python scripts/ejecutar_demo_local.py --crear-zip",
                "python scripts/editor_espacio_trabajo.py",
            ],
        ),
        (
            "Fase 4 - Recorrido sugerido por consola local",
            [
                "Abrir la consola local y revisar el resumen de agentes.",
                "Editar un campo de prueba en espacio_trabajo/.",
                "Ejecutar un agente, revisar informe, historico y comparador.",
            ],
        ),
        (
            "Fase 5 - Informes, comparacion y evidencias",
            [
                "Revisar salidas/agente-01/informe.txt y salidas/agente-10/informe.txt.",
                "Abrir informe consolidado, panel local e indice de evidencias.",
                "Mostrar el ZIP de evidencias como paquete local exportable.",
            ],
        ),
        (
            "Fase 6 - Cierre recomendado",
            [
                "Confirmar demo reproducible con un solo comando.",
                "Confirmar separacion entre originales y datos de trabajo.",
                "Cerrar reforzando trazabilidad, pruebas y control de alcance.",
            ],
        ),
    ]
    tarjetas_bloques = "".join(construir_bloque_html(titulo, elementos) for titulo, elementos in bloques)

    rutas_html = []
    for ruta in RUTAS_ESPERADAS:
        if ruta.startswith("http://"):
            estado = "disponible"
        else:
            relativa = Path(ruta.replace("salidas/", "", 1))
            estado = "disponible" if (directorio_salidas / relativa).is_file() else "no disponible todavia"
        rutas_html.append(f"<li><code>{escape(ruta)}</code> ({escape(estado)})</li>")

    evidencias_html = []
    for nombre, ruta_mostrada, ruta_relativa in RUTAS_EVIDENCIAS:
        estado = estado_evidencia(directorio_salidas, ruta_relativa)
        evidencias_html.append(
            f"<li><strong>{escape(nombre)}:</strong> <code>{escape(ruta_mostrada)}</code> ({escape(estado)})</li>"
        )

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Guion local de demo guiada</title>
  <style>
    :root {{
      --fondo: #eef3f7;
      --texto: #17212b;
      --card: #ffffff;
      --borde: #c8d4df;
      --acento: #165d57;
      --acento-suave: #dff3ef;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: "Segoe UI", Tahoma, Arial, sans-serif;
      color: var(--texto);
      background: linear-gradient(180deg, #f8fbfd 0%, var(--fondo) 100%);
    }}
    main {{ max-width: 1120px; margin: 0 auto; padding: 24px; }}
    .hero, .panel, .bloque {{
      background: var(--card);
      border: 1px solid var(--borde);
      border-radius: 14px;
      padding: 18px;
      margin-bottom: 14px;
    }}
    .hero {{
      background: linear-gradient(135deg, var(--card) 0%, var(--acento-suave) 100%);
    }}
    .bloques {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
    }}
    .bloque h2 {{ margin-top: 0; font-size: 1.05rem; }}
    ul {{ margin: 0; padding-left: 18px; }}
    li {{ margin: 6px 0; }}
    code {{
      background: #edf2f7;
      padding: 2px 5px;
      border-radius: 5px;
    }}
    .nota {{
      border-left: 6px solid var(--acento);
      padding-left: 12px;
    }}
  </style>
</head>
<body>
  <main>
    <section class="hero">
      <h1>Guion local de demo guiada</h1>
      <p><strong>Fecha y hora de generacion:</strong> {escape(fecha)}</p>
      <p class="nota"><strong>Aviso de limites:</strong> demostracion local para revision humana. No hay IA funcional, API productiva, dashboard productivo, web publica, Google Workspace, integraciones reales ni datos reales.</p>
    </section>
    <section class="panel">
      <h2>Objetivo de la demo</h2>
      <p>Mostrar una V1 local completa como demo tecnica manipulable, reproducible, explicable y validada, sin tocar la web publica.</p>
    </section>
    <section class="bloques">
      {tarjetas_bloques}
    </section>
    <section class="panel">
      <h2>Rutas locales esperadas</h2>
      <ul>
        {"".join(rutas_html)}
      </ul>
    </section>
    <section class="panel">
      <h2>Estado actual de evidencias</h2>
      <ul>
        {"".join(evidencias_html)}
      </ul>
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

        salida_markdown_explicitada = any(
            arg == "--salida-markdown" or arg.startswith("--salida-markdown=") for arg in args_lista
        )
        salida_html_explicitada = any(
            arg == "--salida-html" or arg.startswith("--salida-html=") for arg in args_lista
        )

        if salida_markdown_explicitada:
            salida_markdown = resolver_ruta(args.salida_markdown, raiz)
        else:
            salida_markdown = directorio_salidas / "guion_demo_local.md"

        if salida_html_explicitada:
            salida_html = resolver_ruta(args.salida_html, raiz)
        else:
            salida_html = directorio_salidas / "guion_demo_local.html"

        directorio_salidas.mkdir(parents=True, exist_ok=True)
        salida_markdown.parent.mkdir(parents=True, exist_ok=True)
        if args.generar_html:
            salida_html.parent.mkdir(parents=True, exist_ok=True)

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        salida_markdown.write_text(
            construir_markdown(fecha, directorio_salidas),
            encoding="utf-8",
            errors="replace",
        )

        if args.generar_html:
            salida_html.write_text(
                construir_html(fecha, directorio_salidas),
                encoding="utf-8",
                errors="replace",
            )

        print(f"Directorio de salidas usado: {directorio_salidas}")
        print(f"Guion Markdown generado: {salida_markdown}")
        if args.generar_html:
            print(f"Guion HTML generado: {salida_html}")
        print("Aviso: este guion corresponde a una demostracion local.")
        return 0
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
