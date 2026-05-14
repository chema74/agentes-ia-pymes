from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def obtener_raiz_repositorio() -> Path:
    return Path(__file__).resolve().parents[1]


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Ejecuta una demo local reproducible (espacio de trabajo, agentes, panel, consolidado y evidencias)."
    )
    parser.add_argument("--directorio-trabajo", default="espacio_trabajo")
    parser.add_argument("--directorio-salidas", default="salidas")
    parser.add_argument("--sobrescribir-trabajo", action="store_true")
    parser.add_argument("--crear-zip", action="store_true")
    parser.add_argument("--sin-historico", action="store_true")
    parser.add_argument("--solo-validar", action="store_true")
    parser.add_argument("--abrir-editor", action="store_true")
    parser.add_argument("--puerto-editor", type=int, default=8765)
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


def validar_entorno(
    raiz: Path, directorio_trabajo: Path, directorio_salidas: Path
) -> tuple[bool, str]:
    requeridos = [
        raiz / "scripts" / "preparar_espacio_trabajo.py",
        raiz / "scripts" / "ejecutar_agente.py",
        raiz / "scripts" / "generar_panel_local.py",
        raiz / "scripts" / "generar_informe_consolidado.py",
        raiz / "scripts" / "exportar_evidencias_demo.py",
        raiz / "scripts" / "generar_guion_demo_local.py",
        raiz / "scripts" / "editor_espacio_trabajo.py",
    ]
    faltantes = [ruta for ruta in requeridos if not ruta.is_file()]
    if faltantes:
        return False, "Faltan scripts requeridos:\n" + "\n".join(str(r) for r in faltantes)
    _ = directorio_trabajo
    _ = directorio_salidas
    return True, "Entorno preparado para demo local reproducible."


def ejecutar_paso(nombre: str, comando: list[str], raiz: Path) -> tuple[bool, str]:
    codigo, salida = ejecutar_comando_local(comando, raiz)
    reporte = [f"[{nombre}] comando: {' '.join(comando)}"]
    if salida:
        reporte.append(salida)
    if codigo != 0:
        reporte.append(f"[{nombre}] error (codigo {codigo}).")
        return False, "\n".join(reporte)
    reporte.append(f"[{nombre}] correcto.")
    return True, "\n".join(reporte)


def construir_resumen(
    directorio_trabajo: Path,
    directorio_salidas: Path,
    crear_zip: bool,
    abrir_editor: bool,
    puerto_editor: int,
) -> str:
    panel = directorio_salidas / "panel_local.html"
    informe_md = directorio_salidas / "informe_consolidado.md"
    informe_html = directorio_salidas / "informe_consolidado.html"
    evidencias = directorio_salidas / "evidencias_demo"
    zip_path = directorio_salidas / "evidencias_demo.zip"
    guion_md = directorio_salidas / "guion_demo_local.md"
    guion_html = directorio_salidas / "guion_demo_local.html"

    lineas = [
        "",
        "Resumen final de demo local reproducible",
        f"- Directorio de trabajo: {directorio_trabajo}",
        f"- Directorio de salidas: {directorio_salidas}",
        f"- Panel local: {panel}",
        f"- Informe consolidado Markdown: {informe_md}",
        f"- Informe consolidado HTML: {informe_html}",
        f"- Carpeta de evidencias: {evidencias}",
        f"- Guion de demo Markdown: {guion_md}",
        f"- Guion de demo HTML: {guion_html}",
    ]
    if crear_zip:
        lineas.append(f"- ZIP de evidencias: {zip_path}")
    if abrir_editor:
        comando_editor = (
            f"python scripts/editor_espacio_trabajo.py --directorio-trabajo {directorio_trabajo} "
            f"--directorio-salidas {directorio_salidas} --puerto {puerto_editor}"
        )
        lineas.append(f"- Comando sugerido para editor: {comando_editor}")
    lineas.append(
        "- Aviso: demo local temporal; no es API productiva, no es dashboard productivo y no es publicacion web."
    )
    return "\n".join(lineas)


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)
    raiz = obtener_raiz_repositorio()
    directorio_trabajo = resolver_ruta(args.directorio_trabajo, raiz)
    directorio_salidas = resolver_ruta(args.directorio_salidas, raiz)

    ok, mensaje = validar_entorno(raiz, directorio_trabajo, directorio_salidas)
    print(mensaje)
    if not ok:
        return 1
    if args.solo_validar:
        return 0

    pasos = []
    comando_preparar = [
        sys.executable,
        str(raiz / "scripts" / "preparar_espacio_trabajo.py"),
        "--directorio-trabajo",
        str(directorio_trabajo),
    ]
    if args.sobrescribir_trabajo:
        comando_preparar.append("--sobrescribir")
    pasos.append(("Preparar espacio de trabajo", comando_preparar))

    comando_ejecutar = [
        sys.executable,
        str(raiz / "scripts" / "ejecutar_agente.py"),
        "--todos",
        "--usar-datos-trabajo",
        "--directorio-trabajo",
        str(directorio_trabajo),
        "--directorio-salidas",
        str(directorio_salidas),
    ]
    if args.sin_historico:
        comando_ejecutar.append("--guardar-salida")
    else:
        comando_ejecutar.append("--guardar-historico")
    pasos.append(("Ejecutar agentes", comando_ejecutar))

    pasos.append(
        (
            "Generar panel local",
            [
                sys.executable,
                str(raiz / "scripts" / "generar_panel_local.py"),
                "--directorio-salidas",
                str(directorio_salidas),
            ],
        )
    )
    pasos.append(
        (
            "Generar informe consolidado",
            [
                sys.executable,
                str(raiz / "scripts" / "generar_informe_consolidado.py"),
                "--directorio-salidas",
                str(directorio_salidas),
                "--generar-html",
            ],
        )
    )

    comando_evidencias = [
        sys.executable,
        str(raiz / "scripts" / "exportar_evidencias_demo.py"),
        "--directorio-salidas",
        str(directorio_salidas),
    ]
    if args.crear_zip:
        comando_evidencias.append("--crear-zip")
    pasos.append(("Exportar evidencias de demo", comando_evidencias))
    pasos.append(
        (
            "Generar guion local de demo",
            [
                sys.executable,
                str(raiz / "scripts" / "generar_guion_demo_local.py"),
                "--directorio-salidas",
                str(directorio_salidas),
                "--generar-html",
            ],
        )
    )

    for nombre, comando in pasos:
        paso_ok, salida = ejecutar_paso(nombre, comando, raiz)
        print(salida)
        if not paso_ok:
            print(f"Error: fallo en paso '{nombre}'.")
            return 1

    print(
        construir_resumen(
            directorio_trabajo,
            directorio_salidas,
            args.crear_zip,
            args.abrir_editor,
            args.puerto_editor,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
