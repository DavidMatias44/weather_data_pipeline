import logging
from os import getenv
from sys import exit

import psycopg2
from dotenv import load_dotenv
from requests.exceptions import RequestException

from extract import fetch_data
from load import insert_data
from transform import flat_raw_data

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_env_var(var_name: str) -> str:
    value = getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable {var_name} not found.")
    return value


def main():
    load_dotenv()

    try:
        base_url = get_env_var("BASE_URL")
        params = {
            "latitude": get_env_var("LATITUDE"),
            "longitude": get_env_var("LONGITUDE"),
            "hourly": get_env_var("HOURLY"),
            "timezone": get_env_var("TIMEZONE"),
            "forecast_days": get_env_var("FORECAST_DAYS"),
        }

        db_params = {
            "dbname": get_env_var("DB_NAME"),
            "user": get_env_var("DB_USER"),
            "password": get_env_var("DB_PASSWORD"),
            "host": get_env_var("DB_HOST"),
            "port": get_env_var("DB_PORT"),

            "schema": get_env_var("DB_SCHEMA"),
            "raw_data_table": get_env_var("DB_RAW_DATA_TABLE"),
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
    except ValueError as e:
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


if __name__ == "__main__":
    main()
