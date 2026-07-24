#  Bootcamp Intensivo de Ingeniería de Datos Senior

> **Ruta para alcanzar nivel Senior en 24 Semanas.**  
> *Metodología militar: Disciplina diaria (1-2 hrs) + Reto Práctico los Domingos.*

![Data Engineering](https://img.shields.io/badge/Stack-Data%20Engineering-blue?style=for-the-badge&logo=python)
![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Containers-blue?style=for-the-badge&logo=docker)
![Spark](https://img.shields.io/badge/Apache_Spark-Big_Data-orange?style=for-the-badge&logo=apachespark)
![Azure](https://img.shields.io/badge/Azure-Cloud-0089D6?style=for-the-badge&logo=microsoftazure)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-FF3621?style=for-the-badge&logo=databricks)

---

##  Roadmap Completo de 24 Semanas

###  FASE 1: Fundamentos de Ingeniería de Software (Semanas 01 - 04)
*Dejar de escribir scripts y empezar a desarrollar software de calidad producción.*

- [ ] **[Semana 1: Python Avanzado (22 Ene - 28 Ene)](phase-1-software-engineering/week-01-python-avanzado/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Crea un Ingestor Genérico. Una clase en Python que acepte una URL de API, haga fetch asíncrono, valide los datos con Pydantic y los guarde en JSON local.
- [ ] **[Semana 2: Testing y Calidad (29 Ene - 4 Feb)](phase-1-software-engineering/week-02-testing-calidad/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Agrega tests unitarios a tu Ingestor de la semana 1. Debe tener 90% de cobertura (coverage). Configura black para que el código se vea profesional.
- [ ] **[Semana 3: Dockerización (5 Feb - 11 Feb)](phase-1-software-engineering/week-03-dockerizacion/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: 'Dockeriza' tu ingestor. Crea un docker-compose.yml que levante tu script de Python y una base de datos Postgres vacía.
- [ ] **[Semana 4: CI/CD - Automatización (12 Feb - 18 Feb)](phase-1-software-engineering/week-04-cicd-automatizacion/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Configura un repo en GitHub. Cada vez que hagas un push, GitHub Actions debe correr tus tests. Si pasan, debe construir la imagen Docker.

###  FASE 2: Bases de Datos y Modelado (Semanas 05 - 08)
*Diseñar el cerebro del sistema y dominar SQL, índices, modelado dimensional y data lakes.*

- [ ] **[Semana 5: SQL Avanzado (19 Feb - 25 Feb)](phase-2-databases-modeling/week-05-sql-avanzado/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Levanta Postgres con Docker. Carga datos crudos (CSV complejos) y usa SQL puro para limpiarlos y generar una vista analítica usando Window Functions.
- [ ] **[Semana 6: Optimización de Bases de Datos (26 Feb - 3 Mar)](phase-2-databases-modeling/week-06-db-optimization/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Genera 1 millón de filas falsas en tu DB. Ejecuta una query lenta. Crea índices y particiones para bajar el tiempo de 5s a 50ms. Documenta el 'Antes y Después'.
- [ ] **[Semana 7: Modelado Dimensional (4 Mar - 10 Mar)](phase-2-databases-modeling/week-07-dimensional-modeling-spotify/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Diseña el esquema para un Clon de Spotify. Dibuja el diagrama ER. Implementa las tablas (DDL) en tu Postgres Dockerizado (fact_streams, dim_cancion, dim_usuario).
- [ ] **[Semana 8: Data Lake & Formatos Modernos (11 Mar - 17 Mar)](phase-2-databases-modeling/week-08-datalake-minio-parquet/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Agrega MinIO a tu docker-compose. Modifica tu script Python para que lea de la API y guarde en formato Parquet particionado por fecha en MinIO (Capa Bronze).

###  FASE 3: Big Data y Transformación (Semanas 09 - 12)
*Escalar el procesamiento masivo de datos con Apache Spark, dbt, DuckDB y Polars.*

- [ ] **[Semana 9: Apache Spark - Arquitectura (18 Mar - 24 Mar)](phase-3-bigdata-transformation/week-09-spark-architecture/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Crea un script en PySpark que lea los Parquets de tu MinIO, haga una agregación simple y lo escriba de vuelta.
- [ ] **[Semana 10: Spark - Optimización (25 Mar - 31 Mar)](phase-3-bigdata-transformation/week-10-spark-optimization/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Toma un dataset público pesado (ej. NYC Taxi Trip Data). Hazlo con Spark optimizando los Joins.
- [ ] **[Semana 11: Modern Stack - dbt (1 Abr - 7 Abr)](phase-3-bigdata-transformation/week-11-dbt-transformation/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Conecta dbt a tu Postgres. Crea la transformación de 'Raw' a 'Modelo Estrella' usando solo SQL y dbt. Genera la documentación automática.
- [ ] **[Semana 12: DuckDB y Polars (8 Abr - 14 Abr)](phase-3-bigdata-transformation/week-12-duckdb-polars/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Reemplaza una parte pequeña de tu pipeline que usaba Pandas por Polars y mide la diferencia de velocidad.

###  FASE 4: Infraestructura y Cloud (Semanas 13 - 16)
*Desplegar infraestructuras como código en la nube (AWS/Azure), Serverless y Contenedores.*

- [ ] **[Semana 13: Cloud (AWS/Azure) - IaaS (15 Abr - 21 Abr)](phase-4-infrastructure-cloud/week-13-cloud-iaas/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Crea una cuenta gratuita en AWS/Azure. Configura manualmente una red segura (VPC) y lanza una instancia pequeña. Conéctate por SSH.
- [ ] **[Semana 14: Infrastructure as Code - Terraform (22 Abr - 28 Abr)](phase-4-infrastructure-cloud/week-14-terraform-iac/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Escribe un script de Terraform que cree el Bucket S3 y la instancia EC2 automáticamente. Destrúyelo (terraform destroy) al final.
- [ ] **[Semana 15: Serverless & Event Driven (29 Abr - 5 May)](phase-4-infrastructure-cloud/week-15-serverless-event-driven/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Crea una Lambda que se active cada vez que subes un archivo a S3. La Lambda debe leer el archivo e imprimir cuántas líneas tiene.
- [ ] **[Semana 16: Contenedores en Nube (6 May - 12 May)](phase-4-infrastructure-cloud/week-16-cloud-containers-ecs/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Sube la imagen Docker de tu ingestor (de la Fase 1) a ECR y ejecútala como una tarea en ECS Fargate programada.

###  FASE 5: Orquestación y Proyecto Final (Semanas 17 - 20)
*Orquestar pipelines de principio a fin con Apache Airflow, calidad de datos y desplegar la plataforma completa.*

- [ ] **[Semana 17: Apache Airflow (13 May - 19 May)](phase-5-orchestration-final-project/week-17-apache-airflow/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Levanta Airflow en Docker. Crea un DAG que orqueste: Ingesta (Python) -> Carga a MinIO -> Transformación (dbt/Spark).
- [ ] **[Semana 18: Observabilidad y Data Quality (20 May - 26 May)](phase-5-orchestration-final-project/week-18-observability-data-quality/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Agrega un paso de 'Great Expectations' a tu DAG de Airflow. Si los datos vienen sucios, el pipeline debe detenerse y mandar una alerta.
- [ ] **[Semana 19: El Proyecto Final - Parte 1 (27 May - 2 Jun)](phase-5-orchestration-final-project/week-19-final-project-part1/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Validar despliegue de infraestructura base e ingesta continua a la capa Bronze.
- [ ] **[Semana 20: El Proyecto Final - Parte 2 (3 Jun - 9 Jun)](phase-5-orchestration-final-project/week-20-final-project-part2/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Presentación final del Gran Proyecto Evolutivo Híbrido funcionando end-to-end.

###  FASE 6: Especialización Enterprise - Azure, Databricks y Fabric (Semanas 21 - 24)
*Escalar el stack hacia soluciones empresariales de Microsoft Azure, Databricks Medallion y Microsoft Fabric.*

- [ ] **[Semana 21: Ecosistema Azure Data (10 Jun - 16 Jun)](phase-6-enterprise-azure-databricks-fabric/week-21-azure-data-ecosystem/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Crea una cuenta Free Tier en Azure. Configura ADLS Gen2 y usa ADF para orquestar una ingesta desde una API pública hacia tu Data Lake en Parquet.
- [ ] **[Semana 22: Databricks y Arquitectura Medallón (17 Jun - 23 Jun)](phase-6-enterprise-azure-databricks-fabric/week-22-databricks-medallion/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Conecta Databricks a tu ADLS Gen2. Lee los datos crudos (Bronze), límpialos usando PySpark, y guárdalos en formato Delta (Silver).
- [ ] **[Semana 23: Microsoft Fabric y el Futuro Unificado (24 Jun - 30 Jun)](phase-6-enterprise-azure-databricks-fabric/week-23-microsoft-fabric/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Crea un Workspace de prueba en Fabric. Configura un Lakehouse, ingesta un CSV local pesado y conéctalo en modo DirectLake a un reporte.
- [ ] **[Semana 24: El Proyecto Final Enterprise (1 Jul - 7 Jul)](phase-6-enterprise-azure-databricks-fabric/week-24-enterprise-final-project/README.md)**
  - *Proyecto:* 🚨 Domingo de Proyecto: Entrega y despliegue del Proyecto Final Enterprise listo para portfolio senior.

---

##  Comandos Rápidos (Makefile)

```bash
make setup      # Instala dependencias y prepara el entorno
make test       # Ejecuta los tests unitarios con pytest y coverage
make lint       # Verifica formateo con black y linter con flake8
make docker-up  # Levanta los servicios locales (Postgres, MinIO, Airflow)
make docker-down # Detiene los servicios locales
```

##  Cómo subir este repositorio a GitHub

1. Inicializa tu repositorio y realiza el primer commit:
```bash
git init
git add .
git commit -m "feat: inicializacion de estructura bootcamp senior DE 24 semanas"
```

2. Vincula tu repositorio remoto en GitHub y sube los cambios:
```bash
git branch -M main
git remote add origin https://github.com/TU_USUARIO/bootcamp-data-engineering-senior.git
git push -u origin main
```
