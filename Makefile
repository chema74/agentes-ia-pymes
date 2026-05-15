.PHONY: qa test test-cov lint type security release-check

qa:
	python scripts/ci_local.py

test:
	python -m pytest -q

test-cov:
	python -m pytest -q --cov=scripts --cov=tests --cov=agentes --cov-report=term-missing

lint:
	python -m ruff check .

type:
	python scripts/verificar_tipos.py

security:
	python -m pip_audit --progress-spinner off --cache-dir .pytest-tmp/pip-audit-cache

release-check:
	python scripts/verificar_utf8.py
	python scripts/validar_contrato_agentes.py
	python scripts/validar_repositorio.py
	python scripts/verificar_tipos.py
	python -m pytest -q
