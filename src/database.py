import logging

import psycopg2
from psycopg2.extensions import connection

logger = logging.getLogger(__name__)


def create_connection(params: dict[str, str | int]) -> connection:
    logger.debug(
        "Establishing connection to database with host: %s, port: %s",
        params.get("host"),
        params.get("port"),
    )
    conn = psycopg2.connect(
        dbname=params.get("dbname"),
        user=params.get("user"),
        password=params.get("password"),
        host=params.get("host"),
        port=params.get("port"),
    )
    return conn
