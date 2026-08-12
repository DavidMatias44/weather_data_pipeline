# Weather data pipeline

An end-to-end data pipeline for collecting, transforming, and orchestrating weather data using **Apache Airflow**, **dbt**, and **Docker**.

> **Acknowledgment:** This project was inspired by this [Youtube video](https://www.youtube.com/watch?v=vMgFadPxOLk) by [Calvin Yoon](https://www.youtube.com/@cyprojects)

## Motivation

**Apache Airflow**, **dbt**, and **Docker** are key technologies in the Data Engineering tech stack. The best way to gain proficiency in these tools is through **hands-on practice**. Designing, implementing, and maintaining this project serves as the practical application of these concepts.

## Prerequisites

- **uv**. Python package and project manager.

## Architecture

This project follows the **Medallion Architecture**, and it is **containerized using Docker**.

![Architecture](docs/architecture.png)
