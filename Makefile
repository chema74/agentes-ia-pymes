.PHONY: qa test test-cov lint type security release-check

qa:
	python scripts/ci_local.py

test:
	python -m pytest -q

test-cov:
	python -m pytest -q --cov=scripts --cov=tests --cov-report=term-missing

lint:
	ruff check .

type:
	mypy scripts tests

security:
	pip-audit --progress-spinner off

release-check:
	python scripts/verificar_utf8.py
	python scripts/validar_contrato_agentes.py
	python scripts/validar_repositorio.py
	python -m pytest -q
