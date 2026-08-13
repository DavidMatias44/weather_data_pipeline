import logging
from os import getenv

from dotenv import load_dotenv

from extract import fetch_data

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

        logger.info("Fetching data from API...")
        raw_data = fetch_data(url=base_url, params=params)
        logger.info("Success!")
        print(raw_data)
    except ValueError as e:
        logger.error("Configuration error: %s", e)


if __name__ == "__main__":
    main()
