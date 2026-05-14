from __future__ import annotations

import argparse
import html
import json
import os
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime
from pathlib import Path

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
        description="Exporta un paquete local de evidencias de demo a partir de salidas/."
    )
    parser.add_argument("--directorio-salidas", default="salidas")
    parser.add_argument("--directorio-evidencias", default="salidas/evidencias_demo")
    parser.add_argument("--crear-zip", action="store_true")
    parser.add_argument("--nombre-zip", default="evidencias_demo.zip")
    parser.add_argument("--regenerar-base", action="store_true")
    return parser


def resolver_ruta(valor: str, raiz: Path) -> Path:
    ruta = Path(valor)
    if not ruta.is_absolute():
        ruta = raiz / ruta
    return ruta


def ejecutar_comando_local(comando: list[str], raiz: Path) -> tuple[int, str]:
    entorno = os.environ.copy()
    entorno["PYTHONIOENCODING"] = "utf-8"
    resultado = subprocess.run(
        comando,
        cwd=raiz,
        text=True,
        capture_output=True,
        check=False,
        encoding="utf-8",
        errors="replace",
        env=entorno,
    )
    salida = ((resultado.stdout or "") + "\n" + (resultado.stderr or "")).strip()
    return resultado.returncode, salida


def regenerar_base(raiz: Path, directorio_salidas: Path) -> tuple[int, str]:
    comandos = [
        [
            sys.executable,
            str(raiz / "scripts" / "generar_panel_local.py"),
            "--generar-informes",
            "--directorio-salidas",
            str(directorio_salidas),
        ],
        [
            sys.executable,
            str(raiz / "scripts" / "generar_informe_consolidado.py"),
            "--directorio-salidas",
            str(directorio_salidas),
            "--generar-html",
        ],
    ]
    salidas = []
    for comando in comandos:
        codigo, salida = ejecutar_comando_local(comando, raiz)
        if salida:
            salidas.append(salida)
        if codigo != 0:
            return 1, "\n\n".join(salidas)
    return 0, "\n\n".join(salidas)


def construir_mapa_evidencias(directorio_salidas: Path) -> list[dict]:
    mapa = [
        {
            "nombre": "Panel HTML local",
            "origen": directorio_salidas / "panel_local.html",
            "destino_relativo": Path("panel_local.html"),
            "descripcion": "Vista local resumida de informes por agente.",
        },
        {
            "nombre": "Informe consolidado Markdown",
            "origen": directorio_salidas / "informe_consolidado.md",
            "destino_relativo": Path("informe_consolidado.md"),
            "descripcion": "Consolidacion local en texto Markdown de los 10 agentes.",
        },
        {
            "nombre": "Informe consolidado HTML",
            "origen": directorio_salidas / "informe_consolidado.html",
            "destino_relativo": Path("informe_consolidado.html"),
            "descripcion": "Consolidacion local en HTML para consulta visual.",
        },
    ]
    for numero, nombre in AGENTES:
        mapa.append(
            {
                "nombre": f"Informe de agente-{numero:02d}",
                "origen": directorio_salidas / f"agente-{numero:02d}" / "informe.txt",
                "destino_relativo": Path("agentes") / f"agente-{numero:02d}-informe.txt",
                "descripcion": f"{nombre}. Ultimo informe local del agente.",
            }
        )
    return mapa


def copiar_evidencias(
    directorio_evidencias: Path, mapa: list[dict]
) -> tuple[list[dict], list[dict]]:
    incluidas = []
    no_disponibles = []
    for item in mapa:
        origen = item["origen"]
        destino = directorio_evidencias / item["destino_relativo"]
        if origen.is_file():
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(origen, destino)
            incluidas.append(
                {
                    "nombre": item["nombre"],
                    "descripcion": item["descripcion"],
                    "origen": origen,
                    "destino_relativo": item["destino_relativo"],
                }
            )
        else:
            no_disponibles.append(
                {
                    "nombre": item["nombre"],
                    "descripcion": item["descripcion"],
                    "origen": origen,
                }
            )
    return incluidas, no_disponibles


def construir_indice_markdown(
    fecha: str, incluidas: list[dict], no_disponibles: list[dict], directorio_evidencias: Path
) -> str:
    lineas = [
        "# Paquete local de evidencias de demo",
        "",
        f"Fecha y hora de generacion: {fecha}",
        "",
        "Aviso de limites: paquete local de demo para revision humana. No es API productiva, no es dashboard productivo, no es publicacion web.",
        "",
        "## Evidencias incluidas",
    ]
    if incluidas:
        for item in incluidas:
            lineas.append(f"- {item['nombre']}: {item['destino_relativo']}")
    else:
        lineas.append("- Ninguna evidencia disponible.")

    lineas.extend(["", "## Evidencias no disponibles"])
    if no_disponibles:
        for item in no_disponibles:
            lineas.append(f"- {item['nombre']}: {item['origen']}")
    else:
        lineas.append("- Ninguna.")

    lineas.extend(["", "## Rutas locales copiadas"])
    if incluidas:
        for item in incluidas:
            lineas.append(
                f"- Origen: {item['origen']} -> Destino: {directorio_evidencias / item['destino_relativo']}"
            )
    else:
        lineas.append("- Sin rutas copiadas.")

    lineas.extend(["", "## Descripcion breve por agente"])
    for numero, nombre in AGENTES:
        lineas.append(
            f"- agente-{numero:02d}: {nombre}. Informe local en `agentes/agente-{numero:02d}-informe.txt` si esta disponible."
        )

    lineas.extend(
        [
            "",
            "Recordatorio: este paquete corresponde a una demo local sobre datos ficticios.",
            "Recordatorio: no hay IA funcional, no hay API productiva, no hay dashboard productivo, no hay Google Workspace y no se usan datos reales.",
        ]
    )
    return "\n".join(lineas) + "\n"


def construir_indice_html(fecha: str, incluidas: list[dict], no_disponibles: list[dict]) -> str:
    tarjetas_incluidas = []
    for item in incluidas:
        ruta_rel = str(item["destino_relativo"]).replace("\\", "/")
        tarjetas_incluidas.append(
            f"""
            <article class="tarjeta ok">
              <h3>{html.escape(item["nombre"])}</h3>
              <p>{html.escape(item["descripcion"])}</p>
              <p><strong>Archivo:</strong> <a href="{html.escape(ruta_rel)}">{html.escape(ruta_rel)}</a></p>
            </article>
            """.strip()
        )

    tarjetas_no_disponibles = []
    for item in no_disponibles:
        tarjetas_no_disponibles.append(
            f"""
            <article class="tarjeta no">
              <h3>{html.escape(item["nombre"])}</h3>
              <p>{html.escape(item["descripcion"])}</p>
              <p><strong>No disponible:</strong> <code>{html.escape(str(item["origen"]))}</code></p>
            </article>
            """.strip()
        )

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Paquete local de evidencias de demo</title>
  <style>
    body{{font-family:Segoe UI,Tahoma,Arial,sans-serif;margin:0;background:#f3f5f8;color:#1f2937}}
    main{{max-width:1100px;margin:0 auto;padding:20px}}
    .card{{background:#fff;border:1px solid #d7dde7;border-radius:10px;padding:14px;margin-bottom:12px}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px}}
    .tarjeta.ok{{border-left:6px solid #0f766e}}
    .tarjeta.no{{border-left:6px solid #b45309}}
    code{{background:#eef2f7;padding:1px 4px;border-radius:4px}}
    a{{color:#1d4ed8;text-decoration:none}}
  </style>
</head>
<body>
  <main>
    <section class="card">
      <h1>Paquete local de evidencias de demo</h1>
      <p><strong>Fecha y hora de generacion:</strong> {html.escape(fecha)}</p>
      <p><strong>Aviso de limites:</strong> paquete local de demo para revision humana. No es API productiva, no es dashboard productivo, no es publicacion web.</p>
      <p><strong>Recordatorio:</strong> demo local sobre datos ficticios. No hay IA funcional, API productiva, dashboard productivo, Google Workspace ni datos reales.</p>
    </section>
    <section class="card">
      <h2>Evidencias incluidas</h2>
      <div class="grid">
        {"".join(tarjetas_incluidas) if tarjetas_incluidas else "<p>No hay evidencias incluidas.</p>"}
      </div>
    </section>
    <section class="card">
      <h2>Evidencias no disponibles</h2>
      <div class="grid">
        {"".join(tarjetas_no_disponibles) if tarjetas_no_disponibles else "<p>No hay evidencias faltantes.</p>"}
      </div>
    </section>
  </main>
</body>
</html>
"""


def crear_zip(directorio_evidencias: Path, ruta_zip: Path) -> None:
    if ruta_zip.exists():
        ruta_zip.unlink()
    with zipfile.ZipFile(ruta_zip, "w", compression=zipfile.ZIP_DEFLATED) as archivo_zip:
        for archivo in directorio_evidencias.rglob("*"):
            if archivo.is_file():
                archivo_zip.write(archivo, archivo.relative_to(directorio_evidencias.parent))


def main(argv: list[str] | None = None) -> int:
    args_lista = list(argv) if argv is not None else sys.argv[1:]
    args = construir_parser().parse_args(args_lista)
    try:
        raiz = obtener_raiz_repositorio()
        directorio_salidas = resolver_ruta(args.directorio_salidas, raiz)

        evidencias_explicitado = any(
            arg == "--directorio-evidencias" or arg.startswith("--directorio-evidencias=")
            for arg in args_lista
        )
        if evidencias_explicitado:
            directorio_evidencias = resolver_ruta(args.directorio_evidencias, raiz)
        else:
            directorio_evidencias = directorio_salidas / "evidencias_demo"

        ruta_zip = directorio_salidas / args.nombre_zip

        if args.regenerar_base:
            codigo, salida = regenerar_base(raiz, directorio_salidas)
            if salida:
                print(salida)
            if codigo != 0:
                print("Error: no se pudo regenerar la base de evidencias.")
                return 1

        directorio_salidas.mkdir(parents=True, exist_ok=True)
        directorio_evidencias.mkdir(parents=True, exist_ok=True)

        mapa = construir_mapa_evidencias(directorio_salidas)
        incluidas, no_disponibles = copiar_evidencias(directorio_evidencias, mapa)

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        indice_md = directorio_evidencias / "INDICE_EVIDENCIAS.md"
        indice_html = directorio_evidencias / "INDICE_EVIDENCIAS.html"
        indice_md.write_text(
            construir_indice_markdown(fecha, incluidas, no_disponibles, directorio_evidencias),
            encoding="utf-8",
        )
        indice_html.write_text(
            construir_indice_html(fecha, incluidas, no_disponibles),
            encoding="utf-8",
        )

        if args.crear_zip:
            crear_zip(directorio_evidencias, ruta_zip)

        print(f"Directorio de salidas usado: {directorio_salidas}")
        print(f"Directorio de evidencias generado: {directorio_evidencias}")
        print(f"Evidencias copiadas: {len(incluidas)}")
        print(f"Evidencias no disponibles: {len(no_disponibles)}")
        print(f"Indice Markdown: {indice_md}")
        print(f"Indice HTML: {indice_html}")
        if args.crear_zip:
            print(f"ZIP generado: {ruta_zip}")
        print(
            "Resumen tecnico: "
            + json.dumps(
                {
                    "evidencias_copiadas": len(incluidas),
                    "evidencias_no_disponibles": len(no_disponibles),
                },
                ensure_ascii=False,
            )
        )
        print("Aviso: paquete local de demo; no es una publicacion web.")
        return 0
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
