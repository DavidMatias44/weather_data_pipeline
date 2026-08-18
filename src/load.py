import logging

from database import create_connection

logger = logging.getLogger(__name__)


def insert_data(params: dict[str, str], records: list[list[float | str | int]]) -> None:
    conn = create_connection(params)
    try:
        with conn:
            schema = params.get("schema")
            raw_data_table = params.get("raw_data_table")
            query = f"""
                INSERT INTO {schema}.{raw_data_table} (
                    time,
                    latitude,
                    longitude,
                    elevation,
                    temperature,
                    precip_prob,
                    updated_at
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP(0)
                )
                ON CONFLICT (time)
                DO UPDATE SET
                    temperature = EXCLUDED.temperature,
                    precip_prob = EXCLUDED.precip_prob,
                    updated_at = CURRENT_TIMESTAMP(0);
                """

            with conn.cursor() as cursor:
                for record in records:
                    cursor.execute(query, record)
    finally:
        conn.close()
