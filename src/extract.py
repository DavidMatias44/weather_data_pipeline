import logging
from typing import Any

from requests import get as requests_get

logger = logging.getLogger(__name__)


def fetch_data(
    url: str, params: dict[str, float | str | int], timeout: tuple[int, int] = (10, 15)
) -> dict[str, Any]:
    res = requests_get(url=url, params=params, timeout=timeout)
    res.raise_for_status()
    return res.json()
