from __future__ import annotations

import argparse
from datetime import datetime
import html
from pathlib import Path
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


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Genera un informe consolidado local desde salidas/agente-XX/informe.txt."
    )
    parser.add_argument("--directorio-salidas", default="salidas")
    parser.add_argument("--generar-html", action="store_true")
    parser.add_argument("--salida-markdown", default="salidas/informe_consolidado.md")
    parser.add_argument("--salida-html", default="salidas/informe_consolidado.html")
    return parser


def resolver_ruta(valor: str, raiz: Path) -> Path:
    ruta = Path(valor)
    if not ruta.is_absolute():
        ruta = raiz / ruta
    return ruta


def extraer_valor_por_prefijo(texto: str, prefijos: list[str]) -> str:
    for linea in texto.splitlines():
        limpia = linea.strip()
        for prefijo in prefijos:
            if limpia.lower().startswith(prefijo.lower()):
                _, _, resto = limpia.partition(":")
                valor = resto.strip()
                if valor:
                    return valor
    return "No identificada"


def leer_informes(directorio_salidas: Path) -> list[dict]:
    resultados = []
    for numero, nombre in AGENTES:
        ruta = directorio_salidas / f"agente-{numero:02d}" / "informe.txt"
        existe = ruta.is_file()
        contenido = ""
        decision = "No identificada"
        estado = "informe no disponible"
        if existe:
            contenido = ruta.read_text(encoding="utf-8", errors="replace")
            decision = extraer_valor_por_prefijo(
                contenido,
                [
                    "Decision humana recomendada",
                    "Decision recomendada",
                    "Decision",
                ],
            )
            estado = "informe disponible"
        resultados.append(
            {
                "id": numero,
                "nombre": nombre,
                "ruta_informe": ruta,
                "existe": existe,
                "estado": estado,
                "decision": decision,
                "contenido": contenido,
            }
        )
    return resultados


def construir_markdown(informes: list[dict], fecha: str) -> str:
    disponibles = [i for i in informes if i["existe"]]
    no_disponibles = [i for i in informes if not i["existe"]]
    lineas = [
        "# Informe consolidado local",
        "",
        f"Fecha y hora de generacion: {fecha}",
        "",
        "Aviso de limites: salida local sobre datos ficticios. No es API productiva, no es dashboard productivo, no es web publica, no usa IA funcional.",
        "",
        "## Resumen general",
        f"- Informes disponibles: {len(disponibles)} de {len(informes)}",
        f"- Informes no disponibles: {len(no_disponibles)} de {len(informes)}",
        "",
        "## Listado de agentes",
    ]
    for info in informes:
        lineas.append(
            f"- agente-{info['id']:02d}: {info['nombre']} | estado: {info['estado']} | decision recomendada: {info['decision']}"
        )
    lineas.extend(
        [
            "",
            "## Informes disponibles",
            *[f"- agente-{i['id']:02d}" for i in disponibles] if disponibles else ["- Ninguno"],
            "",
            "## Informes no disponibles",
            *[f"- agente-{i['id']:02d} (informe no disponible)" for i in no_disponibles] if no_disponibles else ["- Ninguno"],
            "",
            "## Detalle por agente",
        ]
    )
    for info in informes:
        lineas.extend(
            [
                "",
                f"### agente-{info['id']:02d} - {info['nombre']}",
                f"- Estado: {info['estado']}",
                f"- Decision recomendada: {info['decision']}",
                f"- Ruta local del informe: {info['ruta_informe']}",
            ]
        )
        if info["existe"]:
            contenido = info["contenido"].strip() or "(informe vacio)"
            lineas.extend(["", "```text", contenido, "```"])
        else:
            lineas.extend(["", "informe no disponible"])
    lineas.extend(
        [
            "",
            "Recordatorio: este informe consolidado es una salida local sobre datos ficticios.",
        ]
    )
    return "\n".join(lineas) + "\n"


def construir_html(informes: list[dict], fecha: str) -> str:
    disponibles = [i for i in informes if i["existe"]]
    no_disponibles = [i for i in informes if not i["existe"]]
    tarjetas = []
    for info in informes:
        clase = "ok" if info["existe"] else "no"
        detalle = html.escape(info["contenido"].strip() or "(informe vacio)") if info["existe"] else "informe no disponible"
        tarjetas.append(
            f"""
            <article class="tarjeta {clase}">
              <h3>agente-{info['id']:02d} - {html.escape(info['nombre'])}</h3>
              <p><strong>Estado:</strong> {html.escape(info['estado'])}</p>
              <p><strong>Decision recomendada:</strong> {html.escape(info['decision'])}</p>
              <p><strong>Ruta local:</strong> <code>{html.escape(str(info['ruta_informe']))}</code></p>
              <details>
                <summary>Detalle del informe</summary>
                <pre>{detalle}</pre>
              </details>
            </article>
            """.strip()
        )
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Informe consolidado local</title>
  <style>
    body{{font-family:Segoe UI,Tahoma,Arial,sans-serif;margin:0;background:#f3f5f8;color:#1f2937}}
    main{{max-width:1100px;margin:0 auto;padding:20px}}
    .card{{background:#fff;border:1px solid #d7dde7;border-radius:10px;padding:14px;margin-bottom:12px}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:10px}}
    .tarjeta.ok{{border-left:6px solid #0f766e}}
    .tarjeta.no{{border-left:6px solid #b45309}}
    pre{{white-space:pre-wrap;word-break:break-word;background:#f8fafc;border:1px solid #e5e7eb;padding:10px;border-radius:8px}}
    code{{background:#eef2f7;padding:1px 4px;border-radius:4px}}
  </style>
</head>
<body>
  <main>
    <section class="card">
      <h1>Informe consolidado local</h1>
      <p><strong>Fecha y hora de generacion:</strong> {html.escape(fecha)}</p>
      <p><strong>Aviso de limites:</strong> salida local sobre datos ficticios. No es API productiva, no es dashboard productivo, no es web publica, no usa IA funcional.</p>
      <p><strong>Resumen general:</strong> informes disponibles {len(disponibles)} de {len(informes)}; informes no disponibles {len(no_disponibles)} de {len(informes)}.</p>
      <p><strong>Recordatorio:</strong> este informe consolidado es una salida local sobre datos ficticios.</p>
    </section>
    <section class="grid">
      {"".join(tarjetas)}
    </section>
  </main>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)
    try:
        raiz = obtener_raiz_repositorio()
        directorio_salidas = resolver_ruta(args.directorio_salidas, raiz)
        salida_markdown = resolver_ruta(args.salida_markdown, raiz)
        salida_html = resolver_ruta(args.salida_html, raiz)

        directorio_salidas.mkdir(parents=True, exist_ok=True)
        salida_markdown.parent.mkdir(parents=True, exist_ok=True)
        if args.generar_html:
            salida_html.parent.mkdir(parents=True, exist_ok=True)

        informes = leer_informes(directorio_salidas)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        markdown = construir_markdown(informes, fecha)
        salida_markdown.write_text(markdown, encoding="utf-8")

        print(f"Directorio de salidas usado: {directorio_salidas}")
        print(f"Informe consolidado Markdown generado: {salida_markdown}")
        if args.generar_html:
            salida_html.write_text(construir_html(informes, fecha), encoding="utf-8")
            print(f"Informe consolidado HTML generado: {salida_html}")
        print("Aviso: salida local sobre datos ficticios.")
        return 0
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
