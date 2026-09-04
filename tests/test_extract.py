from unittest.mock import Mock, patch

import pytest
from requests.exceptions import RequestException

from src.extract import fetch_data
from src.schemas import APIResponse


@patch("src.extract.requests_get")
def test_fetch_data_success(mock_get: Mock) -> None:
    mock_res = Mock()
    mock_res.json.return_value = {
        "latitude": 34.0258,
        "longitude": -118.7804,
        "elevation": 1500,
        "hourly": {
            "time": ["2026-09-03T00:00"],
            "temperature_2m": [19.3],
            "precipitation_probability": [5],
        },
    }
    mock_get.return_value = mock_res
    test_url = "https://mock_api.com"
    test_params = {
        "latitude": 34.0258,
        "longitude": -118.7804,
        "hourly": "temperature_2m,precipitation_probability",
        "timezone": "America/Denver",
        "forecast_days": 1,
    }

    res = fetch_data(url=test_url, params=test_params)

    mock_get.assert_called_once_with(url=test_url, params=test_params, timeout=(10, 15))
    mock_res.raise_for_status.assert_called_once()
    assert isinstance(res, APIResponse)
    assert res.latitude == 34.0258
    assert res.longitude == -118.7804


@patch("src.extract.requests_get")
def test_fetch_data_raises_request_exception(mock_get: Mock) -> None:
    mock_res = Mock()
    mock_res.raise_for_status.side_effect = RequestException(
        "Error while fetching data from API"
    )
    mock_get.return_value = mock_res

    with pytest.raises(RequestException):
        fetch_data(url="https://mock_api.com", params={})
