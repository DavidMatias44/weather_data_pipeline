FROM apache/airflow:3.0.0

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

USER airflow

COPY requirements.txt /requirements.txt

RUN uv pip install -r /requirements.txt
