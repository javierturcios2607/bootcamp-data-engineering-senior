# FASE 1: Fundamentos de Ingeniería de Software (Semanas 01 - 04)

**Objetivo:** Dejar de escribir scripts y empezar a desarrollar software de calidad producción.

## Semanas de esta Fase:

- **[Semana 1: Python Avanzado (22 Ene - 28 Ene)](./week-01-python-avanzado/README.md)**: 🚨 Domingo de Proyecto: Crea un Ingestor Genérico. Una clase en Python que acepte una URL de API, haga fetch asíncrono, valide los datos con Pydantic y los guarde en JSON local.
- **[Semana 2: Testing y Calidad (29 Ene - 4 Feb)](./week-02-testing-calidad/README.md)**: 🚨 Domingo de Proyecto: Agrega tests unitarios a tu Ingestor de la semana 1. Debe tener 90% de cobertura (coverage). Configura black para que el código se vea profesional.
- **[Semana 3: Dockerización (5 Feb - 11 Feb)](./week-03-dockerizacion/README.md)**: 🚨 Domingo de Proyecto: 'Dockeriza' tu ingestor. Crea un docker-compose.yml que levante tu script de Python y una base de datos Postgres vacía.
- **[Semana 4: CI/CD - Automatización (12 Feb - 18 Feb)](./week-04-cicd-automatizacion/README.md)**: 🚨 Domingo de Proyecto: Configura un repo en GitHub. Cada vez que hagas un push, GitHub Actions debe correr tus tests. Si pasan, debe construir la imagen Docker.
