import logging

from src.database import create_connection

logger = logging.getLogger(__name__)


def insert_data(
    params: dict[str, str | int], records: list[list[float | str | int]]
) -> None:
    conn = create_connection(params)
    try:
        with conn:
            schema = params.get("schema")
            raw_data_table = params.get("raw_data_table")

            deduplicated_records = list(
                {record[0]: record for record in records}.values()
            )

            select_query = f"""
                SELECT
                    id,
                    time,
                    temperature,
                    precip_prob
                FROM {schema}.{raw_data_table}
                WHERE time = %s AND valid_to IS NULL;
            """
            update_query = f"""
                UPDATE {schema}.{raw_data_table} SET
                    valid_to = CURRENT_TIMESTAMP(0)
                WHERE id = %s;
            """
            insert_query = f"""
                INSERT INTO {schema}.{raw_data_table} (
                    time, latitude, longitude, elevation, temperature, precip_prob, valid_from
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP(0)
                );
            """

            with conn.cursor() as cursor:
                for record in deduplicated_records:
                    time, latitude, longitude, elevation, temperature, precip_prob = (
                        record
                    )

                    cursor.execute(
                        select_query,
                        (time,),
                    )
                    current_record = cursor.fetchone()

                    if current_record:
                        (
                            current_id,
                            _,
                            current_temperature,
                            current_precip_prob,
                        ) = current_record
                        if (
                            current_temperature == temperature
                            and current_precip_prob == precip_prob
                        ):
                            continue
                        cursor.execute(
                            update_query,
                            (current_id,),
                        )

                    cursor.execute(
                        insert_query,
                        (
                            time,
                            latitude,
                            longitude,
                            elevation,
                            temperature,
                            precip_prob,
                        ),
                    )
    finally:
        conn.close()
