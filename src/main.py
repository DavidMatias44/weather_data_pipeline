import logging
from sys import exit

import psycopg2
from pydantic import ValidationError
from requests.exceptions import RequestException

from config import Settings
from extract import fetch_data
from load import insert_data
from transform import flat_raw_data

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    try:
        settings = Settings()

        base_url = settings.base_url
        params = {
            "latitude": settings.latitude,
            "longitude": settings.longitude,
            "hourly": settings.hourly,
            "timezone": settings.timezone,
            "forecast_days": settings.forecast_days,
        }

        db_params = {
            "dbname": settings.db_name,
            "user": settings.db_user,
            "password": settings.db_password,
            "host": settings.db_host,
            "port": settings.db_port,
            "schema": settings.db_schema,
            "raw_data_table": settings.db_raw_data_table,
        }

        logger.info("Fetching data from API...")
        raw_data = fetch_data(url=base_url, params=params)
        logger.info("Success!")

        logger.info("Flattening raw data...")
        records = flat_raw_data(raw_data=raw_data)
        logger.info("Success!")

        logger.info("Inserting raw data...")
        insert_data(records=records, params=db_params)
        logger.info("Success!")
    except ValidationError as e:
        logger.error("Configuration error: %s", e)
        exit(1)
    except KeyError as e:
        logger.error("Dictionary key does not exists: %s", e)
        exit(1)
    except RequestException:
        logger.exception("Error while fetching data from API")
        exit(1)
    except psycopg2.Error:
        logger.exception("Database error")
        exit(1)
    except Exception:
        logger.exception("Unexpected error")
        exit(1)


if __name__ == "__main__":
    main()
