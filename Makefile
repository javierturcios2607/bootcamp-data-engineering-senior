# Makefile para el Bootcamp Senior de Ingeniería de Datos

.PHONY: setup test lint docker-up docker-down clean

setup:
	pip install --upgrade pip
	pip install -r requirements.txt || true

test:
	pytest --cov=src --cov-report=term-missing phase-1-software-engineering/week-01-python-avanzado/tests/

lint:
	black --check .
	flake8 .

docker-up:
	docker-compose -f phase-1-software-engineering/week-03-dockerizacion/docker-compose.yml up -d

docker-down:
	docker-compose -f phase-1-software-engineering/week-03-dockerizacion/docker-compose.yml down

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
