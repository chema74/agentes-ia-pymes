"""
Validador operativo V2 para el repositorio agentes-ia-pymes.

Este script no sustituye a pytest ni al validador V1 existente.
Su objetivo es añadir una capa específica de control V2:

1. Comprueba documentación obligatoria V2.
2. Comprueba enlaces V2 en README, índice documental y ficha pública.
3. Puede ejecutar pytest y validar_repositorio.py.
4. Genera un informe local en salidas/validacion_v2.md.

El informe generado queda en salidas/, carpeta ignorada por Git.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DOCUMENTOS_V2_OBLIGATORIOS = [
    "docs/PLAN_V2_AGENTES_IA_PYMES.md",
    "docs/MAPA_EVIDENCIAS_V2.md",
    "docs/GUIA_EJECUCION_V2.md",
    "docs/LIMITES_ALCANCE_V2.md",
    "docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md",
    "docs/CHECKLIST_VALIDACION_V2.md",
    "docs/REGISTRO_EJECUCION_V2.md",
    "docs/CIERRE_TECNICO_V2_PROVISIONAL.md",
]

REFERENCIAS_README = [
    "docs/PLAN_V2_AGENTES_IA_PYMES.md",
    "docs/MAPA_EVIDENCIAS_V2.md",
    "docs/GUIA_EJECUCION_V2.md",
    "docs/LIMITES_ALCANCE_V2.md",
    "docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md",
    "docs/CHECKLIST_VALIDACION_V2.md",
    "v2-agentes-ia-pymes",
]

REFERENCIAS_INDICE = [
    "docs/PLAN_V2_AGENTES_IA_PYMES.md",
    "docs/MAPA_EVIDENCIAS_V2.md",
    "docs/GUIA_EJECUCION_V2.md",
    "docs/LIMITES_ALCANCE_V2.md",
    "docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md",
    "docs/CHECKLIST_VALIDACION_V2.md",
    "docs/REGISTRO_EJECUCION_V2.md",
    "docs/CIERRE_TECNICO_V2_PROVISIONAL.md",
]

REFERENCIAS_FICHA_PUBLICA = [
    "Estado V2 en preparación",
    "v2-agentes-ia-pymes",
    "docs/PLAN_V2_AGENTES_IA_PYMES.md",
    "docs/MAPA_EVIDENCIAS_V2.md",
    "docs/GUIA_EJECUCION_V2.md",
    "docs/LIMITES_ALCANCE_V2.md",
    "docs/RESUMEN_EJECUTIVO_EMPRESAS_V2.md",
    "docs/CHECKLIST_VALIDACION_V2.md",
]


@dataclass
class EjecucionComando:
    """Resultado controlado de un comando local."""

    nombre: str
    comando: list[str]
    codigo_salida: int
    salida: str

    @property
    def correcta(self) -> bool:
        return self.codigo_salida == 0


def obtener_raiz_repositorio() -> Path:
    """Devuelve la raíz del repositorio a partir de la ubicación del script."""

    return Path(__file__).resolve().parents[1]


def leer_texto_utf8(ruta: Path) -> str:
    """Lee un archivo como UTF-8 y devuelve su contenido."""

    return ruta.read_text(encoding="utf-8")


def comprobar_documentos_obligatorios(raiz: Path) -> list[str]:
    """Comprueba que todos los documentos V2 obligatorios existen."""

    errores: list[str] = []

    for ruta_relativa in DOCUMENTOS_V2_OBLIGATORIOS:
        ruta = raiz / ruta_relativa
        if not ruta.exists():
            errores.append(f"Falta documento V2 obligatorio: {ruta_relativa}")

    return errores


def comprobar_referencias_en_archivo(
    raiz: Path,
    archivo_relativo: str,
    referencias: list[str],
) -> list[str]:
    """Comprueba que un archivo contiene una lista de referencias esperadas."""

    errores: list[str] = []
    ruta = raiz / archivo_relativo

    if not ruta.exists():
        return [f"No existe el archivo requerido para comprobar referencias: {archivo_relativo}"]

    contenido = leer_texto_utf8(ruta)

    for referencia in referencias:
        if referencia not in contenido:
            errores.append(f"Falta referencia en {archivo_relativo}: {referencia}")

    return errores


def comprobar_referencias_documentales(raiz: Path) -> list[str]:
    """Comprueba enlaces y menciones V2 en documentos principales."""

    errores: list[str] = []

    errores.extend(
        comprobar_referencias_en_archivo(
            raiz=raiz,
            archivo_relativo="README.md",
            referencias=REFERENCIAS_README,
        )
    )

    errores.extend(
        comprobar_referencias_en_archivo(
            raiz=raiz,
            archivo_relativo="docs/INDICE_DOCUMENTAL.md",
            referencias=REFERENCIAS_INDICE,
        )
    )

    errores.extend(
        comprobar_referencias_en_archivo(
            raiz=raiz,
            archivo_relativo="docs/FICHA_PUBLICA_PORTFOLIO.md",
            referencias=REFERENCIAS_FICHA_PUBLICA,
        )
    )

    return errores


def ejecutar_comando(nombre: str, comando: list[str], raiz: Path) -> EjecucionComando:
    """Ejecuta un comando local y captura su salida de forma segura."""

    resultado = subprocess.run(
        comando,
        cwd=raiz,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    salida = "\n".join(
        parte for parte in [resultado.stdout.strip(), resultado.stderr.strip()] if parte
    )

    return EjecucionComando(
        nombre=nombre,
        comando=comando,
        codigo_salida=resultado.returncode,
        salida=salida,
    )


def generar_informe_validacion(
    raiz: Path,
    errores: list[str],
    ejecuciones: list[EjecucionComando],
    modo: str,
) -> Path:
    """Genera un informe Markdown local con el resultado de validación V2."""

    directorio_salidas = raiz / "salidas"
    directorio_salidas.mkdir(exist_ok=True)

    ruta_informe = directorio_salidas / "validacion_v2.md"

    resultado_global = (
        "correcta" if not errores and all(e.correcta for e in ejecuciones) else "con incidencias"
    )

    lineas: list[str] = [
        "# Validación V2 — agentes-ia-pymes",
        "",
        f"Fecha de generación: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"Modo de validación: {modo}",
        "",
        f"Resultado global: {resultado_global}",
        "",
        "## Comprobaciones documentales",
        "",
    ]

    if errores:
        lineas.append("Errores documentales detectados:")
        lineas.append("")
        for error in errores:
            lineas.append(f"- {error}")
    else:
        lineas.append("- Documentación V2 obligatoria localizada.")
        lineas.append("- Referencias V2 localizadas en README, índice documental y ficha pública.")

    lineas.append("")
    lineas.append("## Comandos ejecutados")
    lineas.append("")

    if not ejecuciones:
        lineas.append("- No se ejecutaron comandos externos en este modo.")
    else:
        for ejecucion in ejecuciones:
            estado = "correcto" if ejecucion.correcta else "con error"
            comando_texto = " ".join(ejecucion.comando)
            lineas.append(f"### {ejecucion.nombre}")
            lineas.append("")
            lineas.append(f"- Comando: `{comando_texto}`")
            lineas.append(f"- Código de salida: `{ejecucion.codigo_salida}`")
            lineas.append(f"- Estado: {estado}")
            lineas.append("")
            if ejecucion.salida:
                lineas.append("Salida resumida:")
                lineas.append("")
                lineas.append("```text")
                lineas.append(ejecucion.salida[-4000:])
                lineas.append("```")
                lineas.append("")

    lineas.append("## Alcance")
    lineas.append("")
    lineas.append(
        "Esta validación no convierte el repositorio en SaaS, API productiva, dashboard productivo ni sistema multiusuario."
    )
    lineas.append(
        "Su objetivo es verificar documentación V2, ejecución local y trazabilidad de evidencias."
    )
    lineas.append("")
    lineas.append("## Licencia y Autoría")
    lineas.append("")
    lineas.append("Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.")
    lineas.append("© 2025 – Txema Ríos. Todos los derechos compartidos.")
    lineas.append("")

    ruta_informe.write_text("\n".join(lineas), encoding="utf-8", newline="\n")

    return ruta_informe


def validar_v2(solo_documentacion: bool = False) -> int:
    """Ejecuta la validación V2 y devuelve código de salida."""

    raiz = obtener_raiz_repositorio()

    errores: list[str] = []
    errores.extend(comprobar_documentos_obligatorios(raiz))
    errores.extend(comprobar_referencias_documentales(raiz))

    ejecuciones: list[EjecucionComando] = []

    if not solo_documentacion:
        ejecuciones.append(
            ejecutar_comando(
                nombre="pytest",
                comando=[sys.executable, "-m", "pytest", "-q"],
                raiz=raiz,
            )
        )

        ejecuciones.append(
            ejecutar_comando(
                nombre="validar_repositorio",
                comando=[sys.executable, str(raiz / "scripts" / "validar_repositorio.py")],
                raiz=raiz,
            )
        )

    modo = "solo-documentacion" if solo_documentacion else "completo"
    ruta_informe = generar_informe_validacion(
        raiz=raiz,
        errores=errores,
        ejecuciones=ejecuciones,
        modo=modo,
    )

    print(f"Informe de validación V2 generado: {ruta_informe}")

    if errores:
        print("Errores documentales detectados:")
        for error in errores:
            print(f"- {error}")

    for ejecucion in ejecuciones:
        estado = "correcto" if ejecucion.correcta else "con error"
        print(f"{ejecucion.nombre}: {estado}")

    if errores or any(not ejecucion.correcta for ejecucion in ejecuciones):
        print("Resultado final V2: validación con incidencias.")
        return 1

    print("Resultado final V2: validación correcta.")
    return 0


def construir_parser() -> argparse.ArgumentParser:
    """Construye el parser de argumentos del script."""

    parser = argparse.ArgumentParser(
        description="Valida documentación, referencias y ejecución local V2 del repositorio."
    )

    parser.add_argument(
        "--solo-documentacion",
        action="store_true",
        help="Comprueba solo documentación y enlaces V2, sin ejecutar pytest ni validar_repositorio.py.",
    )

    return parser


def main() -> int:
    """Punto de entrada del validador V2."""

    parser = construir_parser()
    argumentos = parser.parse_args()

    return validar_v2(solo_documentacion=argumentos.solo_documentacion)


if __name__ == "__main__":
    raise SystemExit(main())
