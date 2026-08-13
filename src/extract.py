import logging
from typing import Any

from requests import get as requests_get
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)


def fetch_data(
    url: str, params: dict[str, str], timeout: tuple[int, int] = (10, 15)
) -> dict[str, Any]:
    try:
        res = requests_get(url=url, params=params, timeout=timeout)
        res.raise_for_status()
        return res.json()
    except RequestException as e:
        logger.error("Error to fetch data from API: %s", e)
        raise
