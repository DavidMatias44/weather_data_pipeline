import logging

from requests import get as requests_get

from schemas import APIResponse

logger = logging.getLogger(__name__)


def fetch_data(
    url: str, params: dict[str, float | str | int], timeout: tuple[int, int] = (10, 15)
) -> APIResponse:
    res = requests_get(url=url, params=params, timeout=timeout)
    res.raise_for_status()

    return APIResponse.model_validate(res.json())
