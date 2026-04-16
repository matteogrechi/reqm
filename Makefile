.DEFAULT_GOAL := help

.PHONY: help install-dev test coverage validate export build clean

help:
	@echo "Available targets:"
	@echo "  install-dev  Install package + dev dependencies in editable mode"
	@echo "  test         Run the test suite"
	@echo "  coverage     Run tests with coverage report"
	@echo "  validate     Validate product requirements"
	@echo "  export       Export all Excel reports into exports/"
	@echo "  build        Build wheel and sdist into dist/"
	@echo "  clean        Remove build artefacts"

install-dev:
	uv sync --all-extras

test:
	uv run pytest

coverage:
	uv run pytest --cov=reqm --cov-report=term-missing

validate:
	cd spec && uv --project .. run reqm validate

export:
	uv run python -c "import pathlib; pathlib.Path('exports').mkdir(exist_ok=True)"
	cd spec && uv --project .. run reqm export requirements -o ../exports/requirements.xlsx
	cd spec && uv --project .. run reqm export traceability -o ../exports/traceability.xlsx
	cd spec && uv --project .. run reqm export test-results -o ../exports/test-results.xlsx

build:
	uv build

clean:
	rm -rf dist/ *.egg-info reqm.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
