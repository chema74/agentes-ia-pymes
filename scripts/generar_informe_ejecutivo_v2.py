"""
Generador de informe ejecutivo V2 para agentes-ia-pymes.

Este script crea una evidencia local, legible y orientada a portfolio.
No llama a servicios externos.
No requiere claves.
No modifica datos de entrada.
No toca la web pública.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

DOCUMENTOS_CLAVE = [
    "docs/PLAN_V2_AGENTES_IA_PYMES.md",
    "docs/MAPA_EVIDENCIAS_V2.md",
    "docs/GUIA_EJECUCION_V2.md",
    "docs/LIMITES_ALCANCE_V2.md",
    "docs/REGISTRO_EJECUCION_V2.md",
    "docs/CIERRE_TECNICO_V2_PROVISIONAL.md",
    "docs/FICHA_PUBLICA_PORTFOLIO.md",
    "docs/INDICE_DOCUMENTAL.md",
]

SALIDAS_CLAVE = [
    "salidas/validacion_v2.md",
    "salidas/panel_local.html",
    "salidas/informe_consolidado.md",
    "salidas/evidencias_demo.zip",
]

LICENCIA = """---

## 🪪 Licencia y Autoría
Publicado bajo licencia Creative Commons CC BY-SA 4.0 International.
© 2025 – Txema Ríos. Todos los derechos compartidos.
"""


@dataclass(frozen=True)
class RecursoDetectado:
    ruta: str
    existe: bool
    resumen: str


def leer_texto(ruta: Path) -> str:
    """Lee un archivo en UTF-8. Si no existe, devuelve cadena vacía."""
    if not ruta.exists():
        return ""
    return ruta.read_text(encoding="utf-8")


def extraer_titulo(texto: str) -> str:
    """Extrae el primer título Markdown de un documento."""
    for linea in texto.splitlines():
        if linea.startswith("# "):
            return linea.strip()
    return "Sin título detectado"


def resumir_documento(base: Path, ruta_relativa: str) -> RecursoDetectado:
    """Resume un documento clave sin alterar su contenido."""
    ruta = base / ruta_relativa
    if not ruta.exists():
        return RecursoDetectado(ruta_relativa, False, "No encontrado")

    texto = leer_texto(ruta)
    titulo = extraer_titulo(texto)
    lineas = len(texto.splitlines())
    return RecursoDetectado(ruta_relativa, True, f"{titulo} ({lineas} líneas)")


def resumir_salida(base: Path, ruta_relativa: str) -> RecursoDetectado:
    """Resume una salida generada, si existe."""
    ruta = base / ruta_relativa
    if not ruta.exists():
        return RecursoDetectado(ruta_relativa, False, "No encontrada")

    tamano = ruta.stat().st_size
    return RecursoDetectado(ruta_relativa, True, f"Detectada ({tamano} bytes)")


def detectar_tests(texto_validacion: str) -> str:
    """
    Intenta localizar una frase de tests pasados en la validación.

    Es una detección auxiliar, no una fuente de verdad absoluta.
    """
    patrones = [
        r"(\d+\s+passed(?:\s+in\s+[^\n]+)?)",
        r"(\d+\s+tests?\s+pasados?)",
        r"(Resultado final V2:\s*validación correcta)",
        r"(validación correcta)",
    ]

    for patron in patrones:
        coincidencia = re.search(patron, texto_validacion, flags=re.IGNORECASE)
        if coincidencia:
            return coincidencia.group(1)

    return "No detectado en salidas locales"


def construir_informe(base: Path) -> str:
    """Construye el informe ejecutivo V2 en Markdown."""
    documentos = [resumir_documento(base, ruta) for ruta in DOCUMENTOS_CLAVE]
    salidas = [resumir_salida(base, ruta) for ruta in SALIDAS_CLAVE]

    validacion = leer_texto(base / "salidas/validacion_v2.md")
    resumen_tests = detectar_tests(validacion)

    docs_ok = sum(1 for item in documentos if item.existe)
    salidas_ok = sum(1 for item in salidas if item.existe)

    fecha = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")

    lineas = [
        "# 📌 INFORME EJECUTIVO V2 — AGENTES IA PYMES",
        "",
        "## 1. Objetivo",
        "",
        "Este informe resume el estado ejecutivo de la V2 (Version 2 – Versión 2) del repositorio `agentes-ia-pymes` como evidencia local de portfolio.",
        "",
        "El documento se genera de forma local, sin APIs (Application Programming Interfaces – Interfaces de Programación de Aplicaciones), sin claves, sin tarjeta bancaria y sin dependencia cloud obligatoria.",
        "",
        "---",
        "",
        "## 2. Resultado ejecutivo",
        "",
        f"- Fecha de generación: `{fecha}`.",
        f"- Documentos V2 detectados: `{docs_ok}/{len(documentos)}`.",
        f"- Salidas locales detectadas: `{salidas_ok}/{len(salidas)}`.",
        f"- Estado de validación detectado: `{resumen_tests}`.",
        "- Web pública `chema74.github.io`: no modificada.",
        "- Repositorio `main`: no modificado por este informe.",
        "",
        "---",
        "",
        "## 3. Documentación V2 revisada",
        "",
    ]

    for item in documentos:
        estado = "OK" if item.existe else "PENDIENTE"
        lineas.append(f"- `{estado}` — `{item.ruta}` — {item.resumen}")

    lineas.extend(
        [
            "",
            "---",
            "",
            "## 4. Evidencias locales detectadas",
            "",
        ]
    )

    for item in salidas:
        estado = "OK" if item.existe else "PENDIENTE"
        lineas.append(f"- `{estado}` — `{item.ruta}` — {item.resumen}")

    lineas.extend(
        [
            "",
            "---",
            "",
            "## 5. Lectura profesional",
            "",
            "La V2 del repositorio queda orientada a demostrar una arquitectura local, auditable y explicable de agentes para PYMES (Small and Medium-sized Enterprises – Pequeñas y Medianas Empresas).",
            "",
            "El valor principal no está en prometer un producto SaaS (Software as a Service – Software como Servicio), sino en mostrar una base técnica reproducible: documentación, validación, demo local, evidencias y límites explícitos.",
            "",
            "---",
            "",
            "## 6. Límites declarados",
            "",
            "- Este informe no convierte el repositorio en producto comercial final.",
            "- Este informe no modifica la web pública.",
            "- Este informe no ejecuta despliegues.",
            "- Este informe no añade dependencias cloud.",
            "- Este informe no sustituye una auditoría técnica completa.",
            "",
            "---",
            "",
            "## 7. Estado final",
            "",
            "`INFORME_EJECUTIVO_V2_GENERADO: OK`",
            "",
            "`WEB_PUBLICA: NO_MODIFICADA`",
            "",
            "`DEPENDENCIAS_EXTERNAS_OBLIGATORIAS: NINGUNA`",
            "",
            LICENCIA,
        ]
    )

    return "\n".join(lineas)


def escribir_informe(base: Path, salida: Path) -> Path:
    """Escribe el informe en UTF-8."""
    informe = construir_informe(base)
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(informe, encoding="utf-8")
    return salida


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Genera un informe ejecutivo V2 local para agentes-ia-pymes."
    )
    parser.add_argument(
        "--salida",
        default="salidas/informe_ejecutivo_v2.md",
        help="Ruta del informe Markdown de salida.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Muestra una respuesta JSON mínima por consola.",
    )

    args = parser.parse_args()

    base = Path.cwd()
    salida = Path(args.salida)

    ruta_generada = escribir_informe(base, salida)

    if args.json:
        print(
            json.dumps(
                {
                    "resultado": "ok",
                    "archivo": str(ruta_generada),
                    "web_publica": "no_modificada",
                    "dependencias_externas_obligatorias": "ninguna",
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(f"OK_INFORME_EJECUTIVO_V2: {ruta_generada}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
