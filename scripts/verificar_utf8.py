import sys
from pathlib import Path

ALLOWED_EXTENSIONS = {
    ".md",
    ".py",
    ".toml",
    ".ini",
    ".yml",
    ".yaml",
    ".json",
    ".csv",
    ".txt",
}

EXCLUDED_DIRS = {
    ".git",
    ".pytest-tmp",
    "__pycache__",
    "salidas",
    "espacio_trabajo",
    ".venv",
    "venv",
    "node_modules",
}


def should_skip(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    for part in rel.parts:
        if part in EXCLUDED_DIRS:
            return True
    return False


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if should_skip(path, root):
            continue
        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue
        yield path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = []

    for path in iter_files(root):
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path}: {exc}")

    if errors:
        print("Se detectaron archivos no UTF-8:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Comprobacion UTF-8 correcta.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
